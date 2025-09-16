#!/usr/bin/python3
"""
Accuracy Metric Plugin
Calculates classification accuracy as the ratio of correct predictions
"""


def run(y_true, y_pred):
    """
    Calculate accuracy metric
    
    Args:
        y_true: True labels (list or array)
        y_pred: Predicted labels (list or array)
    
    Returns:
        float: Accuracy score (0.0 to 1.0)
    """
    # Convert to lists for element-wise comparison
    if hasattr(y_true, '__iter__') and hasattr(y_pred, '__iter__'):
        correct = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
        return correct / len(y_true)
    else:
        raise ValueError("y_true and y_pred must be iterable")

