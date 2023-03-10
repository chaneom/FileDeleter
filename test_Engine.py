import unittest
import datetime
import time
import os
from FileDeleter import Engine


class FileDeletingTest(unittest.TestCase):
    def test_condition_met(self):
        """Tests condition_met() method of Engine class"""
        E = Engine("Path_and_Condition.csv")
        self.assertTrue(E.condition_met("2023-03-09 18:00:00.000"))

    def test_path_exists(self):
        """Tests path_exists() method of Engine class"""
        E = Engine("Path_and_Condition.csv")
        with open("test1.txt", "w") as file:
            file.write("ABC")
        
        self.assertTrue(E.path_exists("test1.txt"))
        os.remove("test1.txt")

    def test_delete(self):
        """Tests delete() method of Engine"""
        with open("testcsv.csv", "w") as file:
            file.write("Path,Condition\n")
            file.write("test2.txt,2023-03-09 18:00:00.000")

        with open("test2.txt", "w") as file2:
            file2.write("This should be deleted")

        E = Engine("testcsv.csv")
        E.delete()
        self.assertFalse(E.path_exists("test2.txt"))
        os.remove("testcsv.csv")




if __name__ == "__main__":
    unittest.main()