import numpy as np
import csv

def getDataSource(data_path):
    CoffeeMl = []
    sleepHours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            CoffeeMl.append(float(row["Coffee in ml"]))
            sleepHours.append(float(row["sleep in hours"]))

    return {"x" : CoffeeMl, "y": sleepHours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between coffee drank(per ml) and hours of sleep is  :-  \n--->",correlation[0,1])

def setup():
    data_path  = "coffee.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()    