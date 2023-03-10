from datetime import datetime
from pathlib import Path
import shutil
import os
import csv

class Engine:
    def __init__(self, csv_path: str):
        """Processes Path_and_Condition.csv"""
        self.files = {}

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
        for path, date in self.files.items():
            if self.path_exists(path) and self.condition_met(date):
                if Path(path).is_dir():
                    shutil.rmtree(path)
                else:
                    os.remove(path)


    def add_file_to_delete(self) -> None:
        """Adds filepath and date to Path_and_Condition.csv"""
        pass