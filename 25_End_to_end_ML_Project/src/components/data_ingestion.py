import os
import sys
from dataclasses import dataclass

import pandas as pd

from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging

from src.components.data_transformation import (
    DataTransformation
)

from src.components.model_trainer import (
    ModelTrainer
)


# Configuration class for storing dataset paths
@dataclass
class DataIngestionConfig:

    train_data_path: str = os.path.join(
        "artifacts",
        "train.csv"
    )

    test_data_path: str = os.path.join(
        "artifacts",
        "test.csv"
    )

    raw_data_path: str = os.path.join(
        "artifacts",
        "data.csv"
    )


# Handles reading, splitting, and saving the dataset
class DataIngestion:

    def __init__(self):
        # Initialize the data ingestion configuration
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        """Reads, splits, and saves the dataset."""

        logging.info(
            "Entered the data ingestion method or component"
        )

        try:
            # Read the original dataset
            df = pd.read_csv(
                os.path.join(
                    "notebook",
                    "data",
                    "stud.csv"
                )
            )

            logging.info(
                "Read the dataset as dataframe"
            )

            # Create the artifacts directory if it does not exist
            os.makedirs(
                os.path.dirname(
                    self.ingestion_config.train_data_path
                ),
                exist_ok=True
            )

            # Save the complete raw dataset
            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )

            logging.info(
                "Train test split initiated"
            )

            # Split the dataset into 80% training and 20% testing
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # Save the training dataset
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            # Save the testing dataset
            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logging.info(
                "Ingestion of the data is completed"
            )

            # Return the generated train and test paths
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


# Execute the complete ML training pipeline
if __name__ == "__main__":

    # Perform data ingestion
    data_ingestion = DataIngestion()

    train_data_path, test_data_path = (
        data_ingestion.initiate_data_ingestion()
    )

    # Perform data transformation
    data_transformation = DataTransformation()

    train_arr, test_arr, _ = (
        data_transformation.initiate_data_transformation(
            train_data_path,
            test_data_path
        )
    )

    # Train and select the best model
    model_trainer = ModelTrainer()

    final_r2_score = (
        model_trainer.initiate_model_trainer(
            train_arr,
            test_arr
        )
    )

    # Display the final R2 score
    print(
        f"Best Model R2 Score: {final_r2_score:.4f}"
    )