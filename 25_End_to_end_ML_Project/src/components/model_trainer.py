import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


# Configuration class for storing the trained model path
@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join(
        "artifacts",
        "model.pkl"
    )


# Handles model training, tuning, evaluation, and selection
class ModelTrainer:

    def __init__(self):
        # Initialize the model trainer configuration
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self, train_array, test_array):
        """Trains multiple models and saves the best performing model."""

        try:
            logging.info("Splitting training and test input data")

            # Separate training and testing features and targets
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            # Define all regression models
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "KNN Regressor": KNeighborsRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(
                    verbose=False
                ),
                "AdaBoost Regressor": AdaBoostRegressor()
            }

            # Define hyperparameter grids for all models
            params={
                    "Decision Tree": {
                        'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                        'splitter':['best','random'],
                        'max_features':['sqrt','log2'],
                    },
                    "Random Forest":{
                        'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                        'max_features':['sqrt','log2',None],
                        'n_estimators': [8,16,32,64,128,256]
                    },
                    "Gradient Boosting":{
                        'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                        'learning_rate':[.1,.01,.05,.001],
                        'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                        'criterion':['squared_error', 'friedman_mse'],
                        'max_features': ['sqrt', 'log2', None],
                        'n_estimators': [8,16,32,64,128,256]
                    },
                    "Linear Regression":{},
                    "XGBRegressor":{
                        'learning_rate':[.1,.01,.05,.001],
                        'n_estimators': [8,16,32,64,128,256]
                    },
                    "CatBoosting Regressor":{
                        'depth': [6,8,10],
                        'learning_rate': [0.01, 0.05, 0.1],
                        'iterations': [30, 50, 100]
                    },
                    "AdaBoost Regressor":{
                        'learning_rate':[.1,.01,0.5,.001],
                        'loss':['linear','square','exponential'],
                        'n_estimators': [8,16,32,64,128,256]
                    },
                    "KNN Regressor": {
                        "n_neighbors": [3, 5, 7, 9, 11, 15],
                        "weights": ["uniform", "distance"],
                        "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
                        "leaf_size": [20, 30, 40],
                        "p": [1, 2]
                        }
                    }

            # Tune, train, and evaluate all models
            model_report, trained_models = evaluate_models(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models,
                param=params
            )

            # Log the test scores of all models
            logging.info(
                f"Model evaluation report: {model_report}"
            )

            # Get the name of the model with the highest test R2 score
            best_model_name = max(
                model_report,
                key=model_report.get
            )

            # Get the best test R2 score
            best_model_score = model_report[
                best_model_name
            ]

            # Get the fitted and tuned best model
            best_model = trained_models[
                best_model_name
            ]

            # Ensure the best model meets the minimum performance requirement
            if best_model_score < 0.6:
                raise Exception(
                    "No model achieved the minimum required R2 score."
                )

            # Log the best model and its score
            logging.info(
                f"Best model: {best_model_name} | "
                f"R2 Score: {best_model_score:.4f}"
            )

            # Save the fitted best model
            save_object(
                file_path=(
                    self
                    .model_trainer_config
                    .trained_model_file_path
                ),
                obj=best_model
            )

            logging.info(
                f"Best model saved successfully: {best_model_name}"
            )

            # Return the already calculated R2 score of the best model
            return best_model_score

        except Exception as e:
            raise CustomException(e, sys)