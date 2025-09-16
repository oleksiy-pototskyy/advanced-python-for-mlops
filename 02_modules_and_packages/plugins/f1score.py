#!/usr/bin/python3
"""
F1 Score Metric Plugin
Calculates F1 score (harmonic mean of precision and recall)
"""


def run(y_true, y_pred):
    """
    Calculate F1 score for binary classification
    
    Args:
        y_true: True labels (list or array)
        y_pred: Predicted labels (list or array)
    
    Returns:
        float: F1 score (0.0 to 1.0)
    """
    # Calculate True Positives, False Positives, False Negatives
    tp = sum(1 for true, pred in zip(y_true, y_pred) if true == 1 and pred == 1)
    fp = sum(1 for true, pred in zip(y_true, y_pred) if true == 0 and pred == 1)
    fn = sum(1 for true, pred in zip(y_true, y_pred) if true == 1 and pred == 0)
    
    # Calculate precision and recall
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    
    # Calculate F1 score
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)
