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


    def condition_met(self, date: str) -> bool:
        """Checks weather condition is met or not for certain file"""
        # https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat
        # https://www.iso.org/iso-8601-date-and-time-format.html
        date = datetime.fromisoformat(date)
        if datetime.now() > date:
            return True
        else:
            return False

    def path_exists(self, p: str) -> bool:
        """Checks if the file/dir exists"""
        path = Path(p)
        return path.exists()

    def delete(self) -> bool:
        """This method will delete files.

        Loops around the extracted data of csv file and
        deletes file if and only if condition_met() and file_exists() returns true.
        """
        deleted_paths = []
        for path, date in self.files.items():
            if self.path_exists(path) and self.condition_met(date):
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
            

    def get_path_and_conditions(self) -> str:
        pass

    def add_file_to_delete(self, path: str, date: str) -> bool:
        """Adds filepath and date to Path_and_Condition.csv"""
        with open(self.csv_path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            self.files[path] = date
            writer.writerow([path, date])
        
