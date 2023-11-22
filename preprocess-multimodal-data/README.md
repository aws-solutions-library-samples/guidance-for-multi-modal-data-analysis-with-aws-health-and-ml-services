---
title: Setup Amazon SageMaker Studio
weight: 310
---

Before running the preprocessing notebooks, you will need to create a SageMaker domain and provide the necessary Lake Formation and Athena permissions.

### Create a SageMaker domain

1. Go to the :link[Amazon SageMaker Console]{href="https://us-east-1.console.aws.amazon.com/sagemaker/home?region=us-east-1#/landing" external=true}
2. Select **Admin configurations** on the left and then **Domains**.
3. Click **Create domain**. 
4. Choose **Quick setup**

   ![Set up SageMaker Domain](/static/images/screenshots/sagemaker-domain-setup.png)

5. Click on **Set up**. It takes a couple of minutes for the domain setup to complete. Remain on the same page.

### Provide necessary permissions to the role

1. Once complete, click on the default user profile and note down the execution role on the right hand side of the page. The role will look like `arn:aws:iam::111122223333:role/service-role/AmazonSageMaker-ExecutionRole-XXXX`. Note down the `AmazonSageMaker-ExecutionRole-XXXX` part as it will be used in the next steps.

   ![Get SageMaker Domain Execution Role](/static/images/screenshots/sagemaker-get-domain-execution-role.png)

2. Go to :link[AWS Lake Formation]{href="https://us-east-1.console.aws.amazon.com/lakeformation/home?region=us-east-1#firstRun" external=true} and choose **Administrative roles and tasks**.

   ![Lake Formation Access](/static/images/screenshots/sagemaker-lakeformation.png)

3. Go to the **Data lake administrators** section and click on **Add**. Under **IAM users and roles**, choose the execution role created in the previous step. Click on **Confirm**.

   ![Role Access](/static/images/screenshots/sagemaker-add-role-permissions.png)

4. Go to :link[IAM]{href="https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/home" external=true}. Click on **Roles**. Search for the execution role created in the previous step. Click on the execution role.

5. Click on **Add permissions** and **Attach policies**. Select **AmazonAthenaFullAccess** and **Add permissions**.

6. Go back to the SageMaker domain in your SageMaker console. Under **User profiles**, click on **Launch** and select **Studio**. Wait for the Studio to launch.

   ![Launch SageMaker Studio](/static/images/screenshots/sagemaker-launch-studio.png)

### Clone repository

1. On the SageMaker Studio page, click on the **Git** icon on the left and select **Clone a Repository**. Copy the URL from below and paste under the **Git repository URL**.
```bash
https://github.com/aws-solutions-library-samples/guidance-for-multi-modal-data-analysis-with-aws-health-and-ml-services.git
```
   ![Clone Repository](/static/images/screenshots/sagemaker-clone-repository.png)

2. Click **Clone**. You should now be able to see a set of files loaded on your environment.

   ![Environment with files](/static/images/screenshots/sagemaker-with-files.png)

Congratulations! 

You have successfully setup your SageMaker domain with all the required files for the remaining parts of the lab.