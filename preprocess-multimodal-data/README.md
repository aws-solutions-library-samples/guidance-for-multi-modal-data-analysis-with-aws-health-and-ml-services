Before running the preprocessing notebooks, you will need to create a SageMaker domain if you haven't already and provide the necessary Lake Formation and Athena permissions.

### Create a SageMaker domain

You can skip this step and if you already have a SageMaker domain setup.

1. Go to the **Amazon SageMaker Console**
2. Select **Admin configurations** on the left and then **Domains**.
3. Click **Create domain**. 
4. Choose **Quick setup**
5. Click on **Set up**. It takes a couple of minutes for the domain setup to complete. Remain on the same page.

### Provide necessary permissions to the role

1. Get the execution role of your SageMaker domain. Click on the default user profile and note down the execution role on the right hand side of the page. The role will look like `arn:aws:iam::111122223333:role/service-role/AmazonSageMaker-ExecutionRole-XXXX`. Note down the `AmazonSageMaker-ExecutionRole-XXXX` part as it will be used in the next steps.
2. Go to **Lake Formation** service page and choose **Administrative roles and tasks**.
3. Go to the **Data lake administrators** section and click on **Add**. Under **IAM users and roles**, choose the execution role created in the previous step. Click on **Confirm**.
4. Go to **IAM** service page. Click on **Roles**. Search for the execution role created in the previous step. Click on the execution role.
5. Click on **Add permissions** and **Attach policies**. Select **AmazonAthenaFullAccess** and **Add permissions**.
6. Go back to the SageMaker domain in your SageMaker console. Under **User profiles**, click on **Launch** and select **Studio**. Wait for the Studio to launch.
