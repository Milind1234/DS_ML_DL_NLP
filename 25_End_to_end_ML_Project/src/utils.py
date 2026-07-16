import os
import sys
import time
import dill

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging


def save_object(file_path, obj):
    """Saves a Python object to a file using dill."""

    try:
        # Get the directory path from the file path
        dir_path = os.path.dirname(file_path)

        # Create the directory if it does not exist
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in binary write mode and save the object
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """Tunes, trains, evaluates, and returns all best fitted models."""

    try:
        # Store test R2 scores of all models
        report = {}

        # Store the best fitted estimator of each model
        trained_models = {}

        # Loop through each model
        for model_name, model in models.items():

            logging.info(f"Training started for: {model_name}")

            # Record the starting time
            start_time = time.time()

            # Get the parameter grid for the current model
            para = param[model_name]

            # Perform hyperparameter tuning using 3-fold cross-validation
            gs = GridSearchCV(
                estimator=model,
                param_grid=para,
                cv=3
            )

            # Find the best parameters and automatically refit the best model
            gs.fit(X_train, y_train)

            # Get the already fitted best estimator
            best_model = gs.best_estimator_

            # Log the best hyperparameters
            logging.info(
                f"Best parameters for {model_name}: {gs.best_params_}"
            )

            # Make predictions using the best fitted model
            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            # Calculate training and testing R2 scores
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # Store the test R2 score
            report[model_name] = test_model_score

            # Store the fitted best model
            trained_models[model_name] = best_model

            # Calculate the total tuning and training time
            total_time = time.time() - start_time

            # Log the model performance
            logging.info(
                f"{model_name} - "
                f"Train R2 Score: {train_model_score:.4f}, "
                f"Test R2 Score: {test_model_score:.4f}"
            )

            # Log the total time required
            logging.info(
                f"Training completed for: {model_name} | "
                f"Time taken: {total_time:.2f} seconds"
            )

        # Return model scores and fitted models
        return report, trained_models

    except Exception as e:
        raise CustomException(e, sys)
    
# def load_object(file_path):
#     try:
#         with open(file_path, "rb") as file_obj:
#             return pickle.load(file_obj)

#     except Exception as e:
#         raise CustomException(e, sys)

"""
save_object("artifacts/preprocessor.pkl", preprocessor_obj)
                    │
                    ▼
        Get directory name
        "artifacts"
                    │
                    ▼
        Create directory if needed
                    │
                    ▼
        Open preprocessor.pkl
        in binary write mode
                    │
                    ▼
        dill.dump(obj, file_obj)
                    │
                    ▼
        Python object is serialized
        and saved to disk
"""

