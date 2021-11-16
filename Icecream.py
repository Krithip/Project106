import plotly.express as px
import csv
import numpy as np
def getDataSource(dataPath):
    temperature = []
    sales = []
    with open(dataPath) as f:
        df = csv.DictReader(f)
        for x in df:
            temperature.append(float(x["Temperature"]))
            sales.append(float(x["Ice-cream Sales"]))
    return {"x":temperature, "y":sales}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(correlation[0,1])
def plot(dataPath):
    with open(dataPath) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales")
        fig.show()
def main():
    dataPath = "C:/Users/Krithi/Desktop/Python/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plot(dataPath)
main()