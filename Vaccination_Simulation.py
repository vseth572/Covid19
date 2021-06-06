import pandas as pd
import numpy as np
from sklearn import linear_model
from scipy.stats import expon
from math import exp
import matplotlib.pyplot as plt
#Intial data set that will be used to train the model
initial_set = { "rate": [12,9,18,7,17,8,23,20,6,14,38,2],
                "personnel":[12,5,20,6,20,5,25,21,5,15,18,5],
                "purchase_power":[13,10,25,8,20,15,15,10,12,12,20,6],
                "distance":[4,10,2,8,3,20,12,2,13,22,5,23]}
d1 = pd.DataFrame(data = initial_set)
d1["supplies"]=d1["personnel"]*25+d1["purchase_power"]*5

#Training Data Set
d2 = pd.DataFrame(dict(
    personnel = np.random.randint(5,25,50),
    purchase_power = np.random.randint(0.5,50,50),
    distance = np.random.randint(2,30,50),))
d2["supplies"] =d2["personnel"]*25+d2["purchase_power"]*5

# d1 = d1.append(d2, ignore_index = True)

X = d1[["personnel","purchase_power","distance","supplies"]]
Y = d1[["rate"]]
regr = linear_model.LinearRegression()
regr.fit(X,Y)
predicted_rate = regr.predict(d2)

#Appending the predicted value of rate to the training data frame
d2["rate"]=predicted_rate
print(d2.corr())

#Calculating the mean rate and lambda
mean_rate = d2["rate"].mean()
lmbda = (1/mean_rate)
print("The value of lambda: ",lmbda)



## Function to
def populate(p):
    x = pd.DataFrame(columns =["day","cumulative_population_covered"])
    i = 1
    while((1-exp(-i*lmbda))<=0.999):
        x.loc[i-1] = [i,p*(1-exp(-i*lmbda))]
        i+=1
    return x

Delhi = populate(2000)
Mumbai = populate(1500)

plt.plot(Delhi["day"], Delhi["cumulative_population_covered"],'r')
plt.plot(Mumbai["day"], Mumbai["cumulative_population_covered"],'b')
plt.show()


