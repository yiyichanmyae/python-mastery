import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dictionaries(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            record = {}
            record["route"] = row[0]
            record["date"] = row[1]
            record["daytype"] = row[2]
            record["rides"] = int(row[3])
            records.append(record)
    return records

class Ride:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
        
def read_rides_as_class(filename):
    '''
    Read the bus ride data as a list of classes
    '''
    records = []
    with open(filename) as f:

        rows = csv.reader(f) 
        headings = next(rows) # skip headers
        for row in rows:
            record = Ride(row[0], row[1], row[2], row[3])
            records.append(record)
    return records

import typing
class NTRide(typing.NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int
         
def read_rides_as_namedtuples(filename):
    '''
    Read the bus ride data as a list 
    '''
    records = []
    with open(filename) as f:

        rows = csv.reader(f) 
        headings = next(rows) # skip headers
        for row in rows:
            record = NTRide(row[0], row[1], row[2], row[3])
            records.append(record)
    return records

class SlotRide:
    __slots__ = "route", "date", "daytime", "rides"
    def __init__(self, route, date, daytime, rides):
        self.route = route
        self.date = date
        self.daytime = daytime
        self.rides = rides
        
def read_rides_as_slots(filename):
    '''
    Read the bus ride data as a list 
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            record = SlotRide(row[0], row[1], row[2], row[3])
            records.append(record)
    return records

def read_rides(filename):
    '''
    Read the bus ride data with different type of data structure
    '''
    filename = "../../Data/ctabus.csv"
    
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples(filename)
    print("Memory Use Tuples: Current %d, Preadk %d" % tracemalloc.get_traced_memory())
    
    tracemalloc.start()
    rows = read_rides_as_dictionaries(filename)
    print("Memory Use Dictionary: Current %d, Preadk %d" % tracemalloc.get_traced_memory())
    
    tracemalloc.start()
    rows = read_rides_as_tuples(filename)
    print("Memory Use Class: Current %d, Preadk %d" % tracemalloc.get_traced_memory())
    
    tracemalloc.start()
    rows = read_rides_as_namedtuples(filename)
    print("Memory Use NamedTuple: Current %d, Preadk %d" % tracemalloc.get_traced_memory())
    
    tracemalloc.start()
    rows = read_rides_as_slots(filename)
    print("Memory Use Slots: Current %d, Preadk %d" % tracemalloc.get_traced_memory())
    
    
if __name__ == "__main__":
    read_rides("../../Data/ctabus.csv")
    
    