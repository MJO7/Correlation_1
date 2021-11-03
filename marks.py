import numpy as np
import csv

from coffee import getDataSource

def getDataSource(data_path):
   marksPercent = []
   attendance = []
   with open(data_path) as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
         marksPercent.append(float(row["Marks In Percentage"]))
         attendance.append(float(row["Days Present"]))

      return{"x":marksPercent , "y":attendance}

def findCorrelation(datasource):
   correlation = np.corrcoef(datasource["x"] , datasource["y"])
   print("Correlation between percentage of marks of a student and the attendance of the student is \n--->" , correlation[0,1])

def setup():
   data_path = "marks.csv"

   dataSource = getDataSource(data_path)
   findCorrelation(dataSource)
setup()

