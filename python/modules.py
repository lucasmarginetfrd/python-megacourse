import time
import os
import pandas

while True:
    if os.path.exists("epico/temps_today.csv"):
        data = pandas.read_csv("epico/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist")
    time.sleep(10)

