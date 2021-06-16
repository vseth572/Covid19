import pandas as pd
import numpy as np
from sklearn import linear_model
from scipy.stats import expon
from math import exp
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Intial data set that will be used to train the model
initial_set = {"rate": [12, 9, 18, 7, 17, 8, 23, 20, 6, 14, 38, 2],
               "personnel": [12, 5, 20, 6, 20, 5, 25, 21, 5, 15, 18, 5],
               "purchase_power": [13, 10, 25, 8, 20, 15, 15, 10, 12, 12, 20, 6],
               "distance": [4, 10, 2, 8, 3, 20, 12, 2, 13, 22, 5, 23]}
d1 = pd.DataFrame(data=initial_set)
d1["supplies"] = d1["personnel"] * 25 + d1["purchase_power"] * 5

#intialize function that takes no of observations as input
def initialize_dataframe(n):
    x = pd.DataFrame(dict(
        personnel=np.random.randint(5, 25, n),
        purchase_power=np.random.randint(0.5, 50, n),
        distance=np.random.randint(2, 20, n), ))
    x["supplies"] = x["personnel"] * 15 + x["purchase_power"] * 5
    return x
#d2 = initialize_dataframe(50)
# d1 = d1.append(d2, ignore_index = True)

X = d1[["personnel", "purchase_power", "distance", "supplies"]]
Y = d1[["rate"]]
regr = linear_model.LinearRegression()
regr.fit(X, Y)

def populate(p,lmbda):
    x = pd.DataFrame(columns=["day", "cumulative_population_covered"])
    i = 1
    while (1 - exp(-i * lmbda)) <= 0.999:
        x.loc[i - 1] = [i, p * (1 - exp(-i * lmbda))]
        i += 1
    return x


lmbda = [0.015,0.02,0.03,0.04,0.05]
list_of_dfs = []
for i in range(5):
    d2 = initialize_dataframe(50)
    predicted_rate = regr.predict(d2)
    mean_rate = predicted_rate.mean()
    # lmbda.append(1/mean_rate)
    list_of_dfs.append(populate(2000,lmbda[i]))
    #r_sq[i] = regr.score(X,Y)
#print("R square: ", r_sq)
# Appending the predicted value of rate to the training data frame
#d2["rate"] = predicted_rate
#print(d2.corr())

# Calculating the mean rate and lambda
# mean_rate = d2["rate"].mean()
# lmbda = (1 / mean_rate)
print("The value of lambda: ", lmbda)

""" Function that takes population in thosands as an argument and populates
a dataframe of day and cumulative population vaccinated"""




"""The Population for a city/region can be passed as a list or 
it can also be loaded from a csv file"""
# Delhi = populate(2000)
# Mumbai = populate(1500)

"""Plotting the Exponential Curve for Delhi and Mumbai"""
jet= plt.get_cmap('jet')
colors = iter(jet(np.linspace(0,1,10)))
for i in range(5):
    plt.plot(list_of_dfs[i]["day"], list_of_dfs[i]["cumulative_population_covered"], 'r',color = next(colors))
plt.xlabel("Days")
plt.axis([0,300,0,2000])
plt.ylabel("Population Vaccinated")
# plt.plot(Mumbai["day"], Mumbai["cumulative_population_covered"], 'b',label="Mumbai")
plt.legend(loc=2)
plt.show()
