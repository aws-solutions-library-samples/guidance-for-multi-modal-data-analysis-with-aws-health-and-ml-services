## Results from tests conducted on four different outcomes

The train-test-model.ipynb notebook shows the test results for four different outcomes on the entire dataset of clinial, genomic, and imaging features. The four different outcomes tesed are Hypertension, Stroke, Alzheimer's disease, and Coronary heart disease. Tests were conducted for each of the modalities separately and finally by combining all three. In majority of cases it can be seen that using features from all modalities increases the relevant metrics. Please note: As the models were trained on synthetic data, it may not be reflective of real-world examples. 

|         **Hypertension**         | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1** |
|:--------------------------------:|:------------:|:---------------------:|:-------------:|:----------:|:------:|
|           **Clinical**           |          0.8 |                  0.73 |         0.792 |        0.8 |  0.792 |
|           **Genomic**            |          0.7 |                   0.5 |          0.49 |        0.7 |  0.576 |
|           **Imaging**            |          0.7 |                   0.5 |          0.49 |        0.7 |  0.576 |
|      **Clinical + Genomic**      |        0.866 |                 0.841 |         0.866 |      0.866 |  0.866 |
| **Clinical + Genomic + Imaging** |        0.866 |                 0.904 |         0.907 |      0.866 |  0.871 |
|                                  |              |                       |               |            |        |
|            **Stroke**            | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1** |
|           **Clinical**           |        0.533 |                 0.535 |         0.538 |      0.533 |  0.533 |
|           **Genomic**            |          0.5 |                 0.495 |         0.497 |        0.5 |  0.498 |
|           **Imaging**            |        0.466 |                 0.477 |         0.476 |      0.466 |  0.452 |
|      **Clinical + Genomic**      |          0.6 |                 0.616 |         0.654 |        0.6 |  0.577 |
| **Clinical + Genomic + Imaging** |        0.966 |                 0.964 |         0.968 |      0.966 |  0.966 |
|                                  |              |                       |               |            |        |
|       **Alzheimer's disease**    | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1** |
|           **Clinical**           |        0.733 |                   0.5 |         0.533 |      0.733 |   0.62 |
|           **Genomic**            |        0.733 |                   0.5 |         0.533 |      0.733 |   0.62 |
|           **Imaging**            |        0.966 |                   0.5 |         0.934 |      0.966 |   0.95 |
|      **Clinical + Genomic**      |        0.733 |                   0.5 |         0.533 |      0.733 |   0.62 |
| **Clinical + Genomic + Imaging** |          0.9 |                 0.625 |         0.842 |        0.8 |  0.752 |
|                                  |              |                       |               |            |        |
|      **Coronary heart disease**  | **Accuracy** | **Balanced Accuracy** | **Precision** | **Recall** | **F1** |
|           **Clinical**           |        0.633 |                 0.471 |         0.757 |      0.633 |  0.684 |
|           **Genomic**            |        0.866 |                   0.5 |         0.751 |      0.866 |  0.804 |
|           **Imaging**            |          0.8 |                 0.461 |         0.742 |        0.8 |   0.77 |
|      **Clinical + Genomic**      |        0.766 |                 0.548 |         0.789 |      0.766 |  0.777 |
| **Clinical + Genomic + Imaging** |        0.833 |                 0.692 |          0.85 |      0.833 |   0.84 |

The hypertension-train-test-deploy.ipynb notebook shows an example of how to deploy the binary classification hypertension AutoGluon model on an Amazon SageMaker endpoint and infer from it. A similar approach can be used to deploy models for other outcomes.