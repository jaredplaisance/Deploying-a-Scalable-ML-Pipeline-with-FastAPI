from ml.model import train_model, compute_model_metrics
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


# Test if train_model returns an instance of the RandomForestClassifier
def test_model_instance():
    X_train = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    y_train = pd.Series([0, 1, 0])
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)


# Test if compute_model_metrics returns the expected value
def test_compute_model_metrics_value():
    y_true = np.array([0, 1, 0, 1, 0])
    y_pred = np.array([0, 1, 1, 1, 0])
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)
    assert precision == 0.6666666666666666
    assert recall == 1.0
    assert f1 == 0.8


# Test if the trained model type is RandomForestClassifier
def test_model_type():
    X_train = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    y_train = pd.Series([0, 1, 0])
    model = train_model(X_train, y_train)
    assert type(model).__name__ == 'RandomForestClassifier'
