import os       # Provides functions for working with file and directory paths
import sys      # Provides system-related information, used here for exception handling
import dill     # Used to serialize (save) Python objects into files

# Import our custom exception class for handling errors
from src.exception import CustomException


def save_object(file_path, obj):
    """
    Saves a Python object to a file using dill serialization.

    Parameters:
    ----------
    file_path : str
        The path where the serialized object should be saved.

    obj : object
        The Python object that needs to be saved.
        Example: trained model, preprocessor, encoder, scaler, etc.
    """

    try:
        # Extract the directory path from the complete file path.
        #
        # Example:
        # file_path = "artifacts/preprocessor.pkl"
        #
        # os.path.dirname(file_path)
        # Output:
        # "artifacts"
        dir_path = os.path.dirname(file_path)


        # Create the directory if it does not already exist.
        #
        # exist_ok=True means:
        # If the directory already exists, Python will NOT raise an error.
        #
        # Example:
        # If "artifacts" does not exist -> it will be created.
        # If "artifacts" already exists -> nothing happens.
        os.makedirs(dir_path, exist_ok=True)


        # Open the file in binary write mode ("wb").
        #
        # "w" = write mode
        # "b" = binary mode
        #
        # Serialization libraries like dill store objects as binary data,
        # so we need to use "wb".
        #
        # The "with" statement automatically closes the file
        # after the operation is completed.
        with open(file_path, "wb") as file_obj:


            # Serialize the Python object and save it into the opened file.
            #
            # Example:
            # obj = trained ML model
            #
            # dill.dump() converts the Python object into a binary format
            # and writes it into the .pkl file.
            dill.dump(obj, file_obj)


    except Exception as e:

        # If any error occurs during:
        # 1. Directory creation
        # 2. File opening
        # 3. Object serialization
        #
        # The error is passed to our custom exception handler.
        #
        # 'e'   -> contains the actual error
        # 'sys' -> provides traceback information such as
        #          file name and line number
        raise CustomException(e, sys)
    

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