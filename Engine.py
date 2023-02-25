from FileChecker import FileChecker as fc
import datetime

class Engine:
    def __init__(self) -> None:
        self.FilesCheckers= []


    def new_file_delete_schedule(self, file_path: str, latertime: datetime.timedelta) -> None:
        new_fc = fc(file_path, latertime)
        self.FilesCheckers.append(new_fc)
    
    def delete_file(self) -> str:
        num_deleted = 0
        # num_files_in_queue = len(self.FilesCheckers)

        result = ""

        # checks the time and deletes the file
        for fchecker in self.FilesCheckers:
            if fchecker.check() and not fchecker.is_deleted():
                num_deleted += 1
                result += fchecker.delete() + "\n"
        
        return result


