import os  # Import os module to work with file paths and directories
import sys # Import sys module to get system-level exception information
from src.exception import CustomException # Import our custom exception class for better error handling
from src.logger import logging # Import our custom logging configuration
import pandas as pd # Import pandas for reading and working with datasets
from sklearn.model_selection import train_test_split # Import train_test_split to divide the dataset into training and testing data
from dataclasses import dataclass # Import dataclass to easily create a configuration class

# @dataclass automatically creates useful methods like __init__
# for the variables defined inside this class
@dataclass
class DataIngestionConfig:

    # Path where the training dataset will be saved
    # Result: artifacts/train.csv
    train_data_path: str = os.path.join("artifacts", "train.csv")

    # Path where the testing dataset will be saved
    # Result: artifacts/test.csv
    test_data_path: str = os.path.join("artifacts", "test.csv")

    # Path where the complete/raw dataset will be saved
    # Result: artifacts/data.csv
    raw_data_path: str = os.path.join("artifacts", "data.csv")


# This class is responsible for the complete data ingestion process
class DataIngestion:

    # Constructor - automatically runs when a DataIngestion object is created
    def __init__(self):

        # Create an object of DataIngestionConfig
        # This gives us access to all configured file paths
        self.ingestion_config = DataIngestionConfig()


    # Main method responsible for reading, splitting, and saving the data
    def initiate_data_ingestion(self):

        # Log that the data ingestion process has started
        logging.info("Entered the data ingestion method or component")

        try:

            # Read the original CSV dataset using pandas
            # os.path.join creates the path:
            # notebook/data/stud.csv
            df = pd.read_csv(
                os.path.join("notebook", "data", "stud.csv")
            )

            # Log that the dataset was successfully loaded
            logging.info("Read the dataset as dataframe")


            # Get the directory name from the training data path
            #
            # self.ingestion_config.train_data_path
            # = artifacts/train.csv
            #
            # os.path.dirname(...)
            # = artifacts
            #
            # os.makedirs() creates the artifacts directory
            # if it does not already exist
            #
            # exist_ok=True prevents an error if the directory
            # already exists
            os.makedirs(
                os.path.dirname(
                    self.ingestion_config.train_data_path
                ),
                exist_ok=True
            )


            # Save the complete original dataset inside
            # the artifacts directory
            #
            # Output:
            # artifacts/data.csv
            #
            # index=False prevents pandas from saving
            # the DataFrame index as an extra column
            #
            # header=True saves the column names
            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )


            # Log that the train-test splitting process is starting
            logging.info("Train test split initiated")


            # Split the complete dataset into:
            #
            # 80% training data
            # 20% testing data
            #
            # test_size=0.2 means 20% is used for testing
            #
            # random_state=42 makes the split reproducible,
            # meaning we get the same split every time
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )


            # Save the training dataset
            #
            # Output:
            # artifacts/train.csv
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )


            # Save the testing dataset
            #
            # Output:
            # artifacts/test.csv
            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )


            # Log that the complete ingestion process
            # has finished successfully
            logging.info("Ingestion of the data is completed")


            # Return the paths of the generated
            # training and testing datasets
            #
            # This allows the next component, such as
            # data transformation, to use these files
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        # Catch any error that occurs inside the try block
        except Exception as e:

            # Convert the normal exception into our custom exception
            # sys is passed so that the custom exception can provide
            # information such as the filename and line number
            raise CustomException(e, sys)


# This block runs only when this Python file is executed directly
#
# Example:
# python src/components/data_ingestion.py
#
# It will NOT run automatically when this file is imported
# into another Python file
if __name__ == "__main__":

    # Create an object of the DataIngestion class
    #
    # This automatically calls the __init__ method
    obj = DataIngestion()

    # Start the complete data ingestion process
    obj.initiate_data_ingestion()