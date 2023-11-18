import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames= ["name","home"],lineterminator="\r\n") # hint for showing DictWriter order of columns
    writer.writerow({"home":home, "name":name})                # when writing it out