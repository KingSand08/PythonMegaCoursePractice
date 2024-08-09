import pandas
import os

if(os.path.exists("files/temps_today.csv")):
    data = pandas.read_csv("files/temps_today.csv")
    print(data.mean())
    print(data["st1"])
    print(data["st2"])
else:
    print("The file does not exist at this location.")