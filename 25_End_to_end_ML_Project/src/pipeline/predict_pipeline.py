import os  # Used to create file paths for saved model and preprocessor files
import sys  # Used to provide system-level exception information

import pandas as pd  # Used to convert user input data into a DataFrame

from src.exception import CustomException  # Import custom exception handling class
from src.utils import load_object  # Import utility function to load saved Python objects


# Handles loading the trained model and making predictions
class PredictPipeline:

    # Constructor for the prediction pipeline
    def __init__(self):
        pass


    # Takes input features, preprocesses them, and returns predictions
    def predict(self, features):

        try:
            # Define the path of the saved trained model
            model_path = os.path.join(
                "artifacts",
                "model.pkl"
            )

            # Define the path of the saved preprocessing pipeline
            preprocessor_path = os.path.join(
                "artifacts",
                "preprocessor.pkl"
            )

            # Load the previously trained machine learning model
            model = load_object(
                file_path=model_path
            )

            # Load the previously fitted preprocessing pipeline
            preprocessor = load_object(
                file_path=preprocessor_path
            )

            # Apply the same preprocessing used during model training
            data_scaled = preprocessor.transform(
                features
            )

            # Use the trained model to predict the math score
            preds = model.predict(
                data_scaled
            )

            # Return the predicted result
            return preds

        # Handle any error that occurs during the prediction process
        except Exception as e:
            raise CustomException(e, sys)


# Stores user input and converts it into the format required by the model
class CustomData:

    # Initialize all input features received from the user
    def __init__(
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: float,
        writing_score: float
    ):

        # Store the student's gender
        self.gender = gender

        # Store the student's race or ethnicity group
        self.race_ethnicity = race_ethnicity

        # Store the parent's education level
        self.parental_level_of_education = (
            parental_level_of_education
        )

        # Store the student's lunch type
        self.lunch = lunch

        # Store the student's test preparation course status
        self.test_preparation_course = (
            test_preparation_course
        )

        # Store the student's reading score
        self.reading_score = reading_score

        # Store the student's writing score
        self.writing_score = writing_score


    # Convert the user input data into a Pandas DataFrame
    def get_data_as_data_frame(self):

        try:
            # Create a dictionary containing all user input features
            custom_data_input_dict = {

                # Store gender as a list to create one DataFrame row
                "gender": [
                    self.gender
                ],

                # Store race or ethnicity as a list
                "race_ethnicity": [
                    self.race_ethnicity
                ],

                # Store parental education level as a list
                "parental_level_of_education": [
                    self.parental_level_of_education
                ],

                # Store lunch type as a list
                "lunch": [
                    self.lunch
                ],

                # Store test preparation status as a list
                "test_preparation_course": [
                    self.test_preparation_course
                ],

                # Store reading score as a list
                "reading_score": [
                    self.reading_score
                ],

                # Store writing score as a list
                "writing_score": [
                    self.writing_score
                ]
            }

            # Convert the input dictionary into a one-row Pandas DataFrame
            return pd.DataFrame(
                custom_data_input_dict
            )

        # Handle any error that occurs while creating the DataFrame
        except Exception as e:
            raise CustomException(e, sys)