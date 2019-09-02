# Reading CSV Files
# CSV files are a common file format for tabular data
# We can read CSV files just like other text files
# Python has built-in CSV modules to read/write CSVs more easily
#   reader - lets you iterate over rows of the CSV as lists
#   DictReader - lets you iterate over rows of the CSV as OrderedDicts
#   Keys are determined by the header row

from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file) # this gives you a loopable iterator, NOT A LIST
    next(csv_reader) # skips the 1st line (the header in this case)
    for row in csv_reader:
        # each row is a list
        print(row)
        print(f"{row[0]} is from {row[1]}")


from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row['Name'])


# Can have a different delimiter other than a comma:
from csv import reader
with open("fighters_pipe.csv") as file:
    csv_reader = reader(file, delimiter="|") # specifies the pipe as the delimiter for this instance
    for row in csv_reader:
        # each row is a list
        print(row)