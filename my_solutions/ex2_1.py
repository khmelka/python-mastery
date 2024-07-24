import tracemalloc
import csv

def memory_run():
    f = open('Data/ctabus.csv')
    tracemalloc.start()
    # data = f.read()

    # reading all file into str
    lines = f.readlines()

    print(len(lines))

    current, peak = tracemalloc.get_traced_memory()
    print(current, peak)

# memory_run()

def read_as_tuple():
    records = []
    with open('Data/ctabus.csv') as f:
        tracemalloc.start()
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)

    current, peak = tracemalloc.get_traced_memory()
    print(current, peak)
    # 123842874 123851231

# read_as_tuple()

def read_as_dict():
    records = []
    with open('Data/ctabus.csv') as f:
        tracemalloc.start()
        rows = csv.DictReader(f)
        for row in rows:
            records.append(row)

    print(records[0])

    current, peak = tracemalloc.get_traced_memory()
    print(current, peak)
    # 231395187 231403544

read_as_dict()