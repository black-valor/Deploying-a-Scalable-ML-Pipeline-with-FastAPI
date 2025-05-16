import pytest
# TODO: add necessary import
import numpy as np
import pandas as pd
from ml.data import process_data
from ml.model import (
    compute_model_metrics,
    train_model, inference
)
from train_model import X_train, y_train
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
# TODO: implement the first test. Change the function name and input as needed

def test_one():
    """
    Verifying that the Model Type returns as expected.
    """
   # Create a control dataset
    data = pd.DataFrame(
        {
            "feature1": [1, 2, 3, 4, 5],
            "feature2": [0, 1, 0, 1, 0],
            "label": [0, 1, 0, 1, 0],
        }
    )
    # Process the data
    X_train, y_train, _, _ = process_data(
        data,
        categorical_features=["feature2"],
        label="label",
        training=True,
    )
    # Train model
    model = train_model(X_train, y_train)
    # Verify model returned is expected.
    expected_model_type = RandomForestClassifier
    assert isinstance(model, expected_model_type)

# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Verifying that metrics return and are between 0 and 1.
    """
    model = train_model(X_train, y_train)
    preds = inference(model, X_train)
    metrics = compute_model_metrics(y_train, preds)
    assert len(metrics) == 3
    assert type(metrics) == tuple
    for metric in metrics:
        assert metric >= 0 and metric <= 1


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    Verifying that data loads and has the correct shape.
    """
    X, y = make_classification(n_samples=50, n_features=5, random_state=42)
    assert X.shape == (50, 5)
    assert y.shape == (50,)
