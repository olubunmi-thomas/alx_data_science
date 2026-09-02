from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def train_models(X_train, y_train, X_test):

    models = {
        "Linear Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LinearRegression())
        ]),

        "Ridge": Pipeline([
            ("scaler", StandardScaler()),
            ("model", Ridge(alpha=1.0))
        ]),

        "Lasso": Pipeline([
            ("scaler", StandardScaler()),
            ("model", Lasso(
                alpha=0.1,
                max_iter=10000
            ))
        ]),

        "Random Forest": RandomForestRegressor(
            n_estimators=300,
            random_state=42,
            n_jobs=-1
        ),

        "Gradient Boosting": GradientBoostingRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=3,
            random_state=42
        )
    }

    predictions = {}

    for name, model in models.items():

        model.fit(
            X_train,
            y_train
        )

        predictions[name] = model.predict(
            X_test
        )

    return models, predictions