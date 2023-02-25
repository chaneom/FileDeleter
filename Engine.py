from FileChecker import FileChecker as fc
import datetime

class Engine:
    """Engine class holds list of FileCheckers and does operations on them
    
    datatypes:
        self.FileCheckers: holds list of FileCheckers
    """
    def __init__(self) -> None:
        self.FileCheckers= []


    def new_file_delete_schedule(self, file_path: str, latertime: datetime.timedelta) -> None:
        """appends new FileChecker to list. returns none

        parameters:
            file_path: path of the file
            latertime: datetime.timedelta object. It specifies time waiting time for delete
        """
        new_fc = fc(file_path, latertime)
        self.FileCheckers.append(new_fc)
    
    def delete_file(self) -> str:
        """deletes the FilChecker in the list, if the condition is met.
        """
        num_deleted = 0
        # num_files_in_queue = len(self.FilesCheckers)

        result = ""

        # checks the time and deletes the file
        for fchecker in self.FileCheckers:
            if fchecker.check() and not fchecker.is_deleted():
                num_deleted += 1
                result += fchecker.delete() + "\n"
        
        return result


