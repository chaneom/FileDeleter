from datetime import datetime
from Engine import Engine
import os

def get_date() -> str:
    while True:
        user_date = input("Type a date in \"YYYY-MM-DD 00:00:00:000\" (year, month, day, hour, minutes, seconds, and milliseconds): ")
        try:
            datetime.fromisoformat(user_date)
            return user_date
        except ValueError:
            print(f"{user_date} is not valid")

def get_path() -> str:
    while True:
        user_path = input("Type a path to file/directories to delete: ")
        if os.path.exists(user_path):
            return user_path
        else:
            print(f"{user_path} is not valid")

def main():
    csv_path = input("Type the name of csv file to read (including .csv at the end of the file) ")
    E = Engine(csv_path)
    path_and_date = {}

    # getting user input
    add_input = input("Do you want to add a file to delete? (type y for yes, hit enter to skip) ")
    while add_input == "y":
        user_path = get_path()
        user_date = get_date()
        path_and_date[user_path] = user_date
        add_input = input("Do you want to add another file to delete? (type y for yes, hit enter to skip) ")

    
    # adding the user input
    for p, d in path_and_date.items():
        E.add_file_to_delete(p, d)

    # deleting files
    E.delete()

if __name__ == "__main__":
    main()