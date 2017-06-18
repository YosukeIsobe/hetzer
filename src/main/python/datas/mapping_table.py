import csv

def read():
    retval = {}
    with open("./src/main/resources/mapping.csv", "r") as f:
        reader = csv.reader(f)
        for r in reader:
            retval[int(r[1])] = r[0]
    return retval
