import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


# Configuration class for storing the preprocessor path
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join(
        "artifacts",
        "preprocessor.pkl"
    )


# Handles preprocessing and transformation of data
class DataTransformation:

    def __init__(self):
        # Initialize the data transformation configuration
        self.data_transformation_config = (
            DataTransformationConfig()
        )

    def get_data_transformer_object(self):
        """Creates and returns the complete preprocessing pipeline."""

        try:
            # Define numerical feature columns
            numerical_cols = [
                "writing_score",
                "reading_score"
            ]

            # Define categorical feature columns
            categorical_cols = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            # Create the numerical preprocessing pipeline
            num_pipeline = Pipeline(
                steps=[
                    (
                        "imputer",
                        SimpleImputer(strategy="median")
                    ),
                    (
                        "scaler",
                        StandardScaler()
                    )
                ]
            )

            # Create the categorical preprocessing pipeline
            cat_pipeline = Pipeline(
                steps=[
                    (
                        "imputer",
                        SimpleImputer(
                            strategy="most_frequent"
                        )
                    ),
                    (
                        "ohe",
                        OneHotEncoder(
                            drop = 'first',
                            handle_unknown="ignore",
                            sparse_output=False
                        )
                    )
                ]
            )

            logging.info(
                f"Numerical columns: {numerical_cols}"
            )

            logging.info(
                f"Categorical columns: {categorical_cols}"
            )

            # Apply separate pipelines to numerical and categorical columns
            preprocessor = ColumnTransformer(
                transformers=[
                    (
                        "num_pipeline",
                        num_pipeline,
                        numerical_cols
                    ),
                    (
                        "cat_pipeline",
                        cat_pipeline,
                        categorical_cols
                    )
                ]
            )

            logging.info(
                "Column Transformation completed"
            )

            # Return the complete preprocessing object
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)


    def initiate_data_transformation(
        self,
        train_path,
        test_path
    ):
        """Transforms train and test data and saves the preprocessor."""

        try:
            # Read the training and testing datasets
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info(
                "Read train and test data completed"
            )

            # Get the complete preprocessing object
            preprocessor_obj = (
                self.get_data_transformer_object()
            )

            # Define the target column
            target_column_name = "math_score"

            # Separate training input features and target
            input_feature_train_df = train_df.drop(
                columns=[target_column_name]
            )

            target_feature_train_df = train_df[
                target_column_name
            ]

            # Separate testing input features and target
            input_feature_test_df = test_df.drop(
                columns=[target_column_name]
            )

            target_feature_test_df = test_df[
                target_column_name
            ]

            logging.info(
                "Applying preprocessing on training and testing data"
            )

            # Fit the preprocessor on training data and transform it
            input_feature_train_transform = (
                preprocessor_obj.fit_transform(
                    input_feature_train_df
                )
            )

            # Transform test data using the fitted preprocessor
            input_feature_test_transform = (
                preprocessor_obj.transform(
                    input_feature_test_df
                )
            )

            # Combine transformed training features and target
            train_arr = np.c_[
                input_feature_train_transform,
                np.array(target_feature_train_df)
            ]

            # Combine transformed testing features and target
            test_arr = np.c_[
                input_feature_test_transform,
                np.array(target_feature_test_df)
            ]

            # Save the fitted preprocessing object
            save_object(
                file_path=(
                    self
                    .data_transformation_config
                    .preprocessor_obj_file_path
                ),
                obj=preprocessor_obj
            )

            logging.info(
                "Saved preprocessing object"
            )

            # Return transformed datasets and preprocessor path
            return (
                train_arr,
                test_arr,
                self
                .data_transformation_config
                .preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)


'''
                         DATA INGESTION
                              │
                              ▼
                  ┌─────────────────────┐
                  │     train.csv       │
                  │      test.csv       │
                  └──────────┬──────────┘
                             │
                             ▼
                 initiate_data_transformation()
                             │
                             ▼
               ┌──────────────────────────┐
               │ Read Train & Test Data   │
               │     using Pandas         │
               └────────────┬─────────────┘
                            │
                            ▼
              get_data_transformer_object()
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
     NUMERICAL COLUMNS            CATEGORICAL COLUMNS
     ─────────────────            ───────────────────
     writing_score                gender
     reading_score                race_ethnicity
                                  lunch
                                  test_preparation_course
              │                           │
              ▼                           ▼
     ┌──────────────────┐        ┌───────────────────┐
     │ SimpleImputer    │        │ SimpleImputer     │
     │ strategy=median  │        │ most_frequent     │
     └────────┬─────────┘        └─────────┬─────────┘
              │                            │
              ▼                            ▼
     ┌──────────────────┐        ┌───────────────────┐
     │ StandardScaler   │        │ OneHotEncoder     │
     └────────┬─────────┘        └─────────┬─────────┘
              │                            │
              │                            ▼
              │                  ┌───────────────────┐
              │                  │ StandardScaler    │
              │                  └─────────┬─────────┘
              │                            │
              └──────────────┬─────────────┘
                             │
                             ▼
                   ┌───────────────────┐
                   │ ColumnTransformer │
                   │   preprocessor    │
                   └─────────┬─────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
         TRAINING DATA                TEST DATA
                │                         │
                ▼                         ▼
          fit_transform()              transform()
                │                         │
                ▼                         ▼
       Transformed X_train       Transformed X_test
                │                         │
                ▼                         ▼
         Add y_train                 Add y_test
         math_score                  math_score
                │                         │
                ▼                         ▼
           train_arr                   test_arr
                │                         │
                └────────────┬────────────┘
                             │
                             ▼
                 ┌──────────────────────┐
                 │ Save fitted          │
                 │ preprocessing object │
                 └──────────┬───────────┘
                            │
                            ▼
                artifacts/preprocessor.pkl
                            │
                            ▼
                  ┌───────────────────┐
                  │      RETURN       │
                  ├───────────────────┤
                  │ 1. train_arr      │
                  │ 2. test_arr       │
                  │ 3. preprocessor   │
                  │    file path      │
                  └───────────────────┘
'''