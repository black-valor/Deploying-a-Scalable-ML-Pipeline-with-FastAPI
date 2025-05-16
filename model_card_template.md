# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model was developed to predict whether a person makes more than $50,000 annually based on Census Data. 
Model Version: 1.0
Model type used: RandomForect Classifier
Model Date: 05/16/2025
Created By: Marcus Hare
## Intended Use
The model is designed and intended to predict whether a person makes more than $50,000 annually using attributes provided by Census Data. This prediction can or will be used for research, academics, or decision making for marketing, planning, or possible eligibility.
## Training Data
The Census Income Dataset was obtained as a .csv from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/census+income)
## Evaluation Data
The Census Income Dataset was also used for the evaluation, though it was between training and testing with 20% of the dataset designated for the testing/evaluation.
## Metrics
Three metrics were used to evaluate performance: Precision, Recall, and F1.
Precision: Accuracy of positive predictions.
Recall: Ability to capture the positive instances.
F1: Balances both Precision and Recall.
Performance based on the model: Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863
## Ethical Considerations
The dataset should only be considered a sample of the overall population and therefore cannot be a guaranteed overall representation. Biases and outliers may exists depending on the data captured and should be assessed for fairness when being used for decision making.
## Caveats and Recommendations
The Dataset used is outdated and may not accurately reflect income levels for populations in present times. Recall metric also reflects an opportunity on identifying individuals with income over $50,000. Monitoring and retraining may be necessary to maintain accuracy.