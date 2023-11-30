import csv

def read_file(filename):
    isReadFristLine = True
    with open(filename, "rt") as csv_file:
       reader = csv.reader(csv_file)
       
       return reader


# Get file name
def get_file_name(filepath):
    try:
        array_file_path = filepath.split("/")
        size = len(array_file_path)
        file_name = array_file_path[size-1]
        return file_name
    except IndexError as error:
        print(f"{error}")