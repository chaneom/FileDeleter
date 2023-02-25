import os
import datetime

class FileChecker:
    """ An object that holds path and scheduled time of deletion

    datatypes:
        self.path: it holds a path that will delete a file.
        self.deletion time: it holds the time in which the file will be deleted.
    """
    # Set the path to the file to be deleted
    def __init__(self, file_path: str, latertime: datetime):
        self.path = file_path
        self.deletion_time = datetime.datetime.now() + latertime
        # Set the time interval after which the file should be deleted
        # deletion_time = datetime.datetime.now() + datetime.timedelta(hours=1)

    # Check if it's time to delete the file
    def check_time(self) -> bool:
        if datetime.datetime.now() < self.deletion_time:
            return False
        else:
            return True
    
    """
    exit() is a function that stops program to run.
    """

    def delete_file(self) -> str:
        # Delete the file
        try:
            os.remove(self.path)
            return "File deleted successfully"
        except OSError as error:
            # I should handle a case
            # where I tried to delete file that has been moved
            return str(error)
