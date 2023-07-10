## Store and analyze clinical data with Amazon HealthLake

To get started with storing clinical data, follow the steps in the guide [here](https://docs.aws.amazon.com/healthlake/latest/devguide/getting-started.html). 

Login to your AWS account, search for Amazon HealthLake, and [create an empty Amazon HealthLake datastore](https://docs.aws.amazon.com/healthlake/latest/devguide/create-data-store.html). This will take 20 minutes to provision.

Once the datastore has been created, navigate to the datastore in the console and click the "Import" button in the top right.
* On the Import page, press the "Browse S3" button, navigate to the sample data bucket, then select the "FHIR" folder. This folder contains various .ndjson files for the patients.
* For an output file location, you can use the "sandbox-data-" folder to store your output job data.
* We have created a HealthLake KMS key you can use throughout the workshop. Select that key for encryption.
* Under the "Access Permissions" section, create an IAM role with a name of your preference.
* Click the "Import data" button.


