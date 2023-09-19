import json


import boto3
import botocore.exceptions


def create_omics_role(rolename, policy, trust_policy, iam=None):
    # Create the IAM client
    if not iam:
        iam = boto3.resource('iam')

    # Check if the role already exist. If not, create it
    try:
        role = iam.Role(rolename)
        role.load()

    except botocore.exceptions.ClientError as ex:
        if ex.response["Error"]["Code"] == "NoSuchEntity":
            #Create the role with the corresponding trust policy
            role = iam.create_role(
                RoleName=rolename, 
                AssumeRolePolicyDocument=json.dumps(trust_policy))

            #Create policy
            policy = iam.create_policy(
                PolicyName='{}-policy'.format(rolename), 
                Description="Policy for Amazon Omics",
                PolicyDocument=json.dumps(policy))

            #Attach the policy to the role
            policy.attach_role(RoleName=rolename)
        else:
            print (ex)
            print('Somthing went wrong, please retry and check your account settings and permissions')


def get_role_arn(rolename, client=None):
    """retrieves the arn for an iam role name"""
    if not client:
        client = boto3.client('iam')
    
    role = client.get_role(RoleName=rolename)['Role']
    return role['Arn']


def get_ref_store_id(client=None):
    if not client:
        client = boto3.client('omics')
    
    resp = client.list_reference_stores(maxResults=10)
    list_of_stores = resp.get('referenceStores')
    store_id = None
    
    if list_of_stores != None:
        # Since there can only be one store per region, if there is a store present use the first one
        store_id = list_of_stores[0].get('id')
    
    return store_id


def get_reference_arn(ref_name, client=None):
    if not client:
        client = boto3.client('omics')
    
    resp = client.list_reference_stores(maxResults=10)
    ref_stores = resp.get('referenceStores')
    
    # There can only be one reference store per account per region
    # if there is a store present, it is the first one
    ref_store = ref_stores[0] if ref_stores else None
    
    if not ref_store:
        raise RuntimeError("You have not created a reference store, please got to the Amazon Omics Storage tutorial to learn how to create one. Do not continue with this notebook")
        
    ref_arn = None
    resp = client.list_references(referenceStoreId=ref_store['id'])
    ref_list = resp.get('references')
    
    for ref in resp.get('references'):
        if ref['name'] == ref_name:
            ref_arn = ref['arn']
    
    if ref_arn == None:
        raise RuntimeError(f"Could not find {ref_name}.")
    
    return ref_arn


def create_resource_link(database_name, store, store_type='variant'):
    ram = boto3.client('ram')
    glue = boto3.client('glue')

    caller_identity = boto3.client('sts').get_caller_identity()
    AWS_ACCOUNT_ID = caller_identity['Account']
    AWS_IDENITY_ARN = caller_identity['Arn']

    response = ram.list_resources(resourceOwner='OTHER-ACCOUNTS', resourceType='glue:Database')

    if not response.get('resources'):
        print('no shared resources found. verify that you have successfully created an Omics Analytics store')
    else:
        store_resources = [resource for resource in response['resources'] if store['id'] in resource['arn']]
        if not store_resources:
            print(f"no shared resources matching {store_type} store id {store['id']} found")
        else:
            store_resource = store_resources[0]

    resource_share = ram.get_resource_shares(
        resourceOwner='OTHER-ACCOUNTS', 
        resourceShareArns=[store_resource['resourceShareArn']])['resourceShares'][0]
    
    # this creates a resource link to the table for the variant store and adds it to the `omicsdb` database
    response = glue.create_table(
        DatabaseName=database_name,
        TableInput = {
            "Name": store['name'],
            "TargetTable": {
                "CatalogId": resource_share['owningAccountId'],
                "DatabaseName": f"{store_type}_{AWS_ACCOUNT_ID}_{store['id']}",
                "Name": store['name'],
            }
        }
    )
    
    return store_resource, resource_share, response