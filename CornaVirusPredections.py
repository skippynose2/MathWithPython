import csv
import quandl, math
import numpy as np
import pandas as pd
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("USA.csv")
print(df.loc[49, "Day"])
print(df.loc[49, "new_cases"])
#iterate from row 14074 and iterate to 14154 create X and Y, total cases and X will be number of days
#14074 will be day 1 and 14154 will the most recent day
#create numpy array for X and Y


#we want our label to be total cases
#we want to replace date with day
#b = df.loc[14074, "new_cases"]
#print(b)


#changing date to 1, 2, 3 etc and creating the x values

#Created file with only USA data all of these are our x
'''
with open('USA.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Day", "new_cases", "new_deaths"])
    x = 14074
    day = 1
    while x in range(14154):
        d = df.loc[x, "date"] = day
        dfday = df.loc[x, "date"]
        dfnew = df.loc[x, "new_cases"]
        dfdeaths = df.loc[x, "new_deaths"]
        writer.writerow([dfday, dfnew, dfdeaths])
        x += 1
        day += 1
'''




'''numCasesArray = np.array([])
x = 14074
while x in range(14154):
    numCasesArray = np.append(numCasesArray, [df.loc[x, "total_cases"]])
    x+=1
'''
