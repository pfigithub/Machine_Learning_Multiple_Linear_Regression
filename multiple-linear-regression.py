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