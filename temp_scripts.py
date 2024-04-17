import os

import pandas


def temp():
    file_list = os.listdir("C:\\fmsncdata")
    df = pandas.DataFrame(file_list)
    df.to_csv("C:\\tempquotedata\\PartsOff.csv")
    print(df)
