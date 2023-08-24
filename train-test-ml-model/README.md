## Results from tests conducted on four different outcomes

The train-test-model.ipynb notebook shows the test results for four different outcomes on the entire dataset of clinial, genomic, and imaging features. The four different outcomes tesed are Hypertension, Stroke, Alzheimer's disease, and Coronary heart disease. Tests were conducted for each of the modalities separately and finally by combining all three. In majority of cases it can be seen that using features from all modalities increases the relevant metrics. Please note: As the models were trained on synthetic data, it may not be reflective of real-world examples. 

|         **Hypertension**         | **Accuracy** | **Precision** | **Recall** | **F1** |
|:--------------------------------:|:------------:|:-------------:|:----------:|:------:|
| **Clinical**                     |         0.80 |          0.79 |       0.80 |   0.79 |
| **Genomic**                      |         0.70 |          0.49 |       0.70 |   0.58 |
| **Imaging**                      |         0.70 |          0.49 |       0.70 |   0.58 |
| **Clinical + Genomic + Imaging** |         0.87 |          0.91 |       0.87 |   0.87 |
|                                  |              |               |            |        |
|    **Coronary heart disease**    | **Accuracy** | **Precision** | **Recall** | **F1** |
| **Clinical**                     |         0.63 |          0.76 |       0.63 |   0.68 |
| **Genomic**                      |         0.87 |          0.75 |       0.87 |   0.80 |
| **Imaging**                      |         0.80 |          0.74 |       0.80 |   0.77 |
| **Clinical + Genomic + Imaging** |         0.83 |          0.85 |       0.83 |   0.84 |
|                                  |              |               |            |        |
|            **Stroke**            | **Accuracy** | **Precision** | **Recall** | **F1** |
| **Clinical**                     |         0.53 |          0.54 |       0.53 |   0.53 |
| **Genomic**                      |         0.50 |          0.50 |       0.50 |   0.50 |
| **Imaging**                      |         0.47 |          0.48 |       0.47 |   0.45 |
| **Clinical + Genomic + Imaging** |         0.97 |          0.97 |       0.97 |   0.97 |
|                                  |              |               |            |        |
|      **Alzheimer's disease**     | **Accuracy** | **Precision** | **Recall** | **F1** |
| **Clinical**                     |         0.73 |          0.53 |       0.73 |   0.62 |
| **Genomic**                      |         0.73 |          0.53 |       0.73 |   0.62 |
| **Imaging**                      |         0.97 |          0.93 |       0.97 |   0.95 |
| **Clinical + Genomic + Imaging** |         0.90 |          0.84 |       0.80 |   0.75 |

The hypertension-train-test-deploy.ipynb notebook shows an example of how to deploy the hypertension AutoGluon model on an Amazon SageMaker endpoint and infer from it. A similar approach can be used to deploy models for other outcomes.