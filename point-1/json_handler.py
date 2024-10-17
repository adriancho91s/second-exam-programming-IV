import json


class JsonHandler:
    """
    A class to handle JSON file operations.
    """

    @staticmethod
    def write(file_path, data):
        """
        Writes data to a JSON file.

        Args:
            file_path (str): The path where the JSON file will be saved.
            data (dict): The data to be written to the JSON file.

        Raises:
            Exception: If an error occurs during the file writing process.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print("The file has been successfully generated.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def read(file_path):
        """
        Reads data from a JSON file.

        Args:
            file_path (str): The path of the JSON file to be read.

        Returns:
            dict: The data read from the JSON file.

        Raises:
            Exception: If an error occurs during the file reading process.
        """
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
