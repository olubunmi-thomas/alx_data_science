import numpy as np
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

def evaluate_model(y_test, y_pred, model_name="Model"):
    """
    Evaluate a regression model using MAE, RMSE, R², and MAPE.

    Parameters
    ----------
    y_true : array-like
        Actual target values.

    y_pred : array-like
        Predicted target values.

    model_name : str, default="Model"
        Name of the model being evaluated.

    Returns
    -------
    pandas.DataFrame
        Model evaluation metrics.
    """

    y_true = np.asarray(y_test)
    y_pred = np.asarray(y_pred)

    mae = mean_absolute_error(y_test, y_pred)

    rmse = np.sqrt(
        mean_squared_error(y_test, y_pred)
    )

    r2 = r2_score(y_test, y_pred)

    # Avoid division by zero in MAPE
    mask = y_test != 0

    mape = (
        np.mean(
            np.abs(
                (y_test[mask] - y_pred[mask])
                / y_test[mask]
            )
        ) * 100
    )

    results = pd.DataFrame({
        "Model": [model_name],
        "MAE": [mae],
        "RMSE": [rmse],
        "R²": [r2],
        "MAPE (%)": [mape]
    })

    return results
