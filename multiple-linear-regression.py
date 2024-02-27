# importing packages
import pandas as pd
import numpy as np

# reading data(our data is fuelconsumption)
df = pd.read_csv("yourdata.csv")

# take a look at the dataset
df.head()

# selecting features
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.head(9)

# spliting data
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]


# multiple regression model
from sklearn import linear_model
regr = linear_model.LinearRegression()
x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (x, y)
# The coefficients
print ('Coefficients: ', regr.coef_)