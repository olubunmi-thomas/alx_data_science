import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.graphics.gofplots import qqplot


def regression_diagnostics(ols, X, feature_names=None):
    """
    Calculate regression assumption diagnostics and create diagnostic plots.

    Parameters
    ----------
    ols : statsmodels regression results
        Fitted OLS regression model.

    X : pandas.DataFrame
        Predictor variables used to fit the model.

    feature_names : list, optional
        Names of predictor variables. If None, X.columns are used.

    Returns
    -------
    dict
        Dictionary containing Durbin-Watson, Breusch-Pagan,
        and VIF results.
    """

    # --------------------------------------------------
    # Prepare feature names
    # --------------------------------------------------
    if feature_names is None:
        feature_names = X.columns.tolist()

    # --------------------------------------------------
    # Residuals and fitted values
    # --------------------------------------------------
    residuals = ols.resid
    fitted_values = ols.fittedvalues

    # ==================================================
    # 1. LINEARITY
    # Residuals vs Fitted
    # ==================================================

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(
        fitted_values,
        residuals,
        alpha=0.5
    )

    ax.axhline(
        0,
        linestyle="--"
    )

    style_plot(
        ax,
        title="Residuals vs Fitted Values",
        xlabel="Fitted Values",
        ylabel="Residuals"
    )

    plt.show()

    # ==================================================
    # 2. INDEPENDENCE
    # Durbin-Watson
    # ==================================================

    dw_stat = durbin_watson(residuals)

    # ==================================================
    # 3. HOMOSCEDASTICITY
    # Breusch-Pagan
    # ==================================================

    bp_test = het_breuschpagan(
        residuals,
        ols.model.exog
    )

    bp_lm_stat = bp_test[0]
    bp_lm_pvalue = bp_test[1]
    bp_f_stat = bp_test[2]
    bp_f_pvalue = bp_test[3]

    # ==================================================
    # 4. NORMALITY
    # Q-Q Plot
    # ==================================================

    fig, ax = plt.subplots(figsize=(8, 5))

    qqplot(
        residuals,
        line="45",
        fit=True,
        ax=ax
    )

    style_plot(
        ax,
        title="Q-Q Plot of Regression Residuals",
        xlabel="Theoretical Quantiles",
        ylabel="Sample Quantiles"
    )

    plt.show()

    # ==================================================
    # 5. MULTICOLLINEARITY
    # VIF
    # ==================================================

    X_vif = X.copy()

    # Add intercept if it isn't already present
    X_vif = X_vif.astype(float)

    vif_data = pd.DataFrame()

    vif_data["Feature"] = X_vif.columns

    vif_data["VIF"] = [
        variance_inflation_factor(
            X_vif.values,
            i
        )
        for i in range(X_vif.shape[1])
    ]

    vif_data = vif_data.sort_values(
        "VIF",
        ascending=False
    ).reset_index(drop=True)

    # ==================================================
    # Summary
    # ==================================================

    diagnostics = {
        "Durbin-Watson": dw_stat,
        "Breusch-Pagan LM Statistic": bp_lm_stat,
        "Breusch-Pagan LM p-value": bp_lm_pvalue,
        "Breusch-Pagan F Statistic": bp_f_stat,
        "Breusch-Pagan F p-value": bp_f_pvalue,
        "VIF": vif_data
    }

    return diagnostics
