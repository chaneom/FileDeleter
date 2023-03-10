from datetime import datetime
from pathlib import Path
import shutil
import os
import csv

class Engine:
    def __init__(self, csv_path: str):
        """Processes Path_and_Condition.csv"""
        self.files = {}
        self.csv_path = csv_path

        with open(csv_path, "r", newline="") as file:
            reader = csv.reader(file)
            reader.__next__()
            for row in reader:
                if len(row) > 0:
                    self.files[row[0]] = row[1]

    @staticmethod
    def condition_met(date: str) -> bool:
        """Checks weather condition is met or not for certain file
        """
        # https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat
        # https://www.iso.org/iso-8601-date-and-time-format.html
        date = datetime.fromisoformat(date)
        if datetime.now() > date:
            return True
        else:
            return False

    @staticmethod
    def path_exists(p: str) -> bool:
        """Checks if the file/dir exists"""
        path = Path(p)
        return path.exists()

    def delete(self):
        """This method will delete files.

        Loops around the extracted data of csv file and
        deletes file if and only if condition_met() and file_exists() returns true.
        """
        deleted_paths = []
        for path, date in self.files.items():
            if Engine.path_exists(path) and Engine.condition_met(date):
                if Path(path).is_dir():
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                deleted_paths.append(path)
        
        for path in deleted_paths:
            del self.files[path]
        
        with open(self.csv_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Path", "Date"])
            for path, date in self.files.items():
                writer.writerow([path, date])


    def __repr__(self) -> str:
        """
        Will return the formatted list of paths and corresponding dates to delete
        
        Ex.
        Path                                              Time to Delete
        ------------------------------------------------------------------------------------------
        C:/Users/name/Desktop/many_files_to_delete             2023-03-10 01:00
        
        """
        representation = f"{'Path ':<50}{'Time to Delete':<30}\n{'-'*90}\n"

        for path, date in self.files.items():
            representation += f"{path:<50}{date:<30}\n"
        
        return representation


    def add_file_to_delete(self, path: str, date: str):
        """Adds filepath and date to Path_and_Condition.csv"""
        with open(self.csv_path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            self.files[path] = date
            writer.writerow([path, date])
        
