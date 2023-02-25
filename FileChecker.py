import os
import datetime

class FileChecker:
    """ An object that holds path and scheduled time of deletion

    datatypes:
        self.path: it holds a path that will delete a file.
        self.deletion_time: it holds the time in which the file will be deleted.
        self.status: it tells you if this object de
    """

    # Set the path to the file to be deleted
    def __init__(self, file_path: str, latertime: datetime.timedelta):
        self.path = file_path
        self.deletion_time = datetime.datetime.now() + latertime
        self.status = False
        # Set the time interval after which the file should be deleted
        # deletion_time = datetime.datetime.now() + datetime.timedelta(hours=1)

    # Check if it's time to delete the file
    def check(self) -> bool:
        if datetime.datetime.now() < self.deletion_time:
            return False
        else:
            return True
    
    """
    exit() is a function that stops program to run.
    """

    def delete(self) -> str:
        # Delete the file
        try:
            os.remove(self.path)
            self.status = True
            return f"File at \"{self.path}\" deleted successfully"
        except OSError as error:
            # I should handle a case
            # where I tried to delete file that has been moved
            return str(error)
        
    def is_deleted(self) -> bool:
        return self.status
