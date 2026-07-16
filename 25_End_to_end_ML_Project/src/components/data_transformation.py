# ============================================================
# IMPORT REQUIRED LIBRARIES
# ============================================================

import sys # Used to access system-level information.
import os # Used for working with file and directory paths.
from dataclasses import dataclass # @dataclass helps create configuration classes with less boilerplate code.
import numpy as np # NumPy is used for array operations.
import pandas as pd # Pandas is used to read CSV files and work with DataFrames.


# ============================================================
# IMPORT SCIKIT-LEARN PREPROCESSING TOOLS
# ============================================================

from sklearn.compose import ColumnTransformer  # ColumnTransformer allows us to apply different preprocessing
from sklearn.impute import SimpleImputer # SimpleImputer is used to handle missing values.
from sklearn.pipeline import Pipeline # Pipeline allows us to execute multiple preprocessing steps
from sklearn.preprocessing import OneHotEncoder, StandardScaler # OneHotEncoder:Converts categorical values into numerical binary columns.
# ============================================================
# IMPORT PROJECT-SPECIFIC MODULES
# ============================================================

from src.exception import CustomException
# Custom exception class used to provide detailed error messages.

from src.logger import logging
# Custom logging configuration used to track the execution flow.

from src.utils import save_object
# Utility function used to save Python objects such as the
# fitted preprocessing pipeline into a .pkl file.


# ============================================================
# DATA TRANSFORMATION CONFIGURATION
# ============================================================

@dataclass
class DataTransformatiionConfig:

    # Define the location where the fitted preprocessing object
    # will be saved.
    #
    # Final path:
    # artifacts/preprocessor.pkl
    preprocessor_obj_file_path = os.path.join(
        'artifacts',
        'preprocessor.pkl'
    )


# ============================================================
# DATA TRANSFORMATION CLASS
# ============================================================

class DataTransformation:

    def __init__(self):

        # Create an object of DataTransformatiionConfig.
        #
        # This gives us access to:
        # self.data_transformation_config.preprocessor_obj_file_path
        self.data_transformation_config = DataTransformatiionConfig()


    # ========================================================
    # CREATE THE PREPROCESSING OBJECT
    # ========================================================

    def get_data_transformer_object(self):
        """
        This function is responsible for creating the complete
        data preprocessing pipeline.

        It creates:
        1. Numerical preprocessing pipeline
        2. Categorical preprocessing pipeline
        3. ColumnTransformer combining both pipelines

        Returns:
            preprocessor:
                A ColumnTransformer object containing all
                preprocessing operations.
        """

        try:

            # ------------------------------------------------
            # DEFINE NUMERICAL COLUMNS
            # ------------------------------------------------

            numerical_cols = [
                'writing_score',
                'reading_score'
            ]

            # These columns contain numerical values.
            # They will go through:
            #
            # Median Imputation
            #        ↓
            # Standard Scaling


            # ------------------------------------------------
            # DEFINE CATEGORICAL COLUMNS
            # ------------------------------------------------

            categorical_cols = [
                'gender',
                'race_ethnicity',
                'lunch',
                'test_preparation_course'
            ]

            # These columns contain categorical/string values.
            # They will go through:
            #
            # Most Frequent Imputation
            #        ↓
            # One-Hot Encoding
            #        ↓
            # Standard Scaling


            # =================================================
            # CREATE NUMERICAL PIPELINE
            # =================================================

            num_pipeline = Pipeline(

                steps=[

                    # STEP 1:
                    # Replace missing numerical values
                    # with the median value of each column.
                    (
                        'imputer',
                        SimpleImputer(strategy='median')
                    ),

                    # STEP 2:
                    # Standardize the numerical columns.
                    #
                    # Formula:
                    #
                    # z = (x - mean) / standard deviation
                    (
                        'scaler',
                        StandardScaler()
                    )
                ]
            )

            # Log the numerical columns for debugging
            # and execution tracking.
            logging.info(
                f"Numerical columns: {numerical_cols}"
            )


            # =================================================
            # CREATE CATEGORICAL PIPELINE
            # =================================================

            cat_pipeline = Pipeline(

                steps=[

                    # STEP 1:
                    # Replace missing categorical values
                    # with the most frequently occurring value
                    # in each column.
                    (
                        'imputer',
                        SimpleImputer(
                            strategy='most_frequent'
                        )
                    ),


                    # STEP 2:
                    # Convert categorical values into numerical
                    # values using One-Hot Encoding.
                    #
                    # Example:
                    #
                    # gender
                    # ------
                    # male
                    # female
                    #
                    # becomes:
                    #
                    # gender_male   gender_female
                    #      1              0
                    #      0              1
                    #
                    # handle_unknown='ignore':
                    # Prevents errors if an unseen category
                    # appears in the test or prediction data.
                    #
                    # sparse_output=False:
                    # Returns a normal dense NumPy array instead
                    # of a sparse matrix.
                    (
                        'ohe',
                        OneHotEncoder(
                            handle_unknown='ignore',
                            sparse_output=False
                        )
                    ),


                    # STEP 3:
                    # Scale the one-hot encoded categorical
                    # features.
                    #
                    # Because sparse_output=False above,
                    # StandardScaler can work with the dense
                    # output without the sparse-matrix error.
                    (
                        'scaler',
                        StandardScaler()
                    )
                ]
            )

            # Log categorical column information.
            logging.info(
                f"Categorical columns: {categorical_cols}"
            )


            # =================================================
            # CREATE COLUMN TRANSFORMER
            # =================================================

            preprocessor = ColumnTransformer(

                transformers=[

                    # Apply num_pipeline only to
                    # numerical_cols.
                    (
                        'num_pipeline',
                        num_pipeline,
                        numerical_cols
                    ),

                    # Apply cat_pipeline only to
                    # categorical_cols.
                    (
                        'cat_pipeline',
                        cat_pipeline,
                        categorical_cols
                    )
                ]
            )

            # At this point, our complete preprocessing
            # architecture has been created.
            logging.info(
                "Column Transformation completed"
            )


            # Return the complete preprocessing object.
            return preprocessor


        except Exception as e:

            # If any error occurs while creating the preprocessing
            # pipeline, convert it into our custom exception.
            raise CustomException(e, sys)


    # ========================================================
    # PERFORM DATA TRANSFORMATION
    # ========================================================

    def initiate_data_transformation(
        self,
        train_path,
        test_path
    ):

        """
        This function performs the actual data transformation.

        Steps:

        1. Read train.csv and test.csv
        2. Create the preprocessing object
        3. Separate input features and target feature
        4. Fit preprocessing on training data
        5. Transform training data
        6. Transform testing data
        7. Combine transformed features with target
        8. Save the fitted preprocessing object
        9. Return transformed arrays
        """

        try:

            # =================================================
            # READ TRAINING AND TESTING DATA
            # =================================================

            # Read the training CSV file and convert it
            # into a Pandas DataFrame.
            train_df = pd.read_csv(train_path)

            # Read the testing CSV file and convert it
            # into a Pandas DataFrame.
            test_df = pd.read_csv(test_path)


            logging.info(
                'Read train and test data completed'
            )


            # =================================================
            # GET PREPROCESSING OBJECT
            # =================================================

            logging.info(
                'Obtaining preprocessing object'
            )

            # Call the method that creates the complete
            # ColumnTransformer.
            preprocessor_obj = (
                self.get_data_transformer_object()
            )


            # =================================================
            # DEFINE TARGET COLUMN
            # =================================================

            # math_score is the value our ML model
            # will eventually try to predict.
            target_column_name = 'math_score'


            # =================================================
            # SEPARATE TRAINING INPUT AND TARGET
            # =================================================

            # Remove the target column from training data.
            #
            # X_train
            input_feature_train_df = train_df.drop(
                columns=[target_column_name]
            )


            # Extract only the target column.
            #
            # y_train
            target_feature_train_df = train_df[
                target_column_name
            ]


            # =================================================
            # SEPARATE TESTING INPUT AND TARGET
            # =================================================

            # Remove target column from testing data.
            #
            # X_test
            input_feature_test_df = test_df.drop(
                columns=[target_column_name]
            )


            # Extract target column from testing data.
            #
            # y_test
            target_feature_test_df = test_df[
                target_column_name
            ]


            logging.info(
                'Applying the preprocessing object on '
                'training dataframe and testing dataframe.'
            )


            # =================================================
            # FIT AND TRANSFORM TRAINING DATA
            # =================================================

            # fit_transform() performs TWO operations:
            #
            # 1. FIT
            #    Learn preprocessing information from
            #    training data.
            #
            #    Examples:
            #    - Median values
            #    - Most frequent categories
            #    - OneHotEncoder categories
            #    - Mean and standard deviation
            #
            # 2. TRANSFORM
            #    Apply those learned transformations.
            #
            # IMPORTANT:
            # We fit preprocessing ONLY on training data.
            input_feature_train_transform = (
                preprocessor_obj.fit_transform(
                    input_feature_train_df
                )
            )


            # =================================================
            # TRANSFORM TEST DATA
            # =================================================

            # Notice that we use:
            #
            # transform()
            #
            # NOT:
            #
            # fit_transform()
            #
            # The preprocessing rules learned from training
            # data must also be used on test data.
            #
            # This prevents DATA LEAKAGE.
            input_feature_test_transform = (
                preprocessor_obj.transform(
                    input_feature_test_df
                )
            )


            # =================================================
            # COMBINE X_TRAIN WITH Y_TRAIN
            # =================================================

            # np.c_ combines arrays column-wise.
            #
            # Before:
            #
            # X_train transformed:
            #
            # feature1  feature2  feature3 ...
            #
            # y_train:
            #
            # math_score
            #
            # After:
            #
            # feature1  feature2 ... math_score
            train_arr = np.c_[

                input_feature_train_transform,

                np.array(
                    target_feature_train_df
                )
            ]


            # =================================================
            # COMBINE X_TEST WITH Y_TEST
            # =================================================

            test_arr = np.c_[

                input_feature_test_transform,

                np.array(
                    target_feature_test_df
                )
            ]


            # =================================================
            # SAVE PREPROCESSING OBJECT
            # =================================================

            # Save the fitted ColumnTransformer so that the
            # exact same preprocessing steps can later be used
            # for:
            #
            # - New prediction data
            # - Deployment
            # - Prediction pipeline
            #
            # Saved as:
            #
            # artifacts/preprocessor.pkl
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


            # =================================================
            # RETURN TRANSFORMED DATA
            # =================================================

            return (

                # Complete transformed training dataset
                train_arr,

                # Complete transformed testing dataset
                test_arr,

                # Location of saved preprocessor.pkl
                self
                .data_transformation_config
                .preprocessor_obj_file_path
            )


        except Exception as e:

            # Convert any error into our custom exception
            # containing detailed debugging information.
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