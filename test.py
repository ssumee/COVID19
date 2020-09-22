#importing module to store and process data
import pandas as pd 
#importing module for numerical analysis		
import numpy as np
#importing module for plotting
import seaborn as sns
#importing module for data visualisation
import matplotlib.pyplot as pyplot

print('Modules are imported.')

#importing dataset
corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head(10) 	
 
#checking the shape of dataframe
corona_dataset_csv.shape

#Deleting the useless columns
corona_dataset_csv.drop(["Lat", "Long"], axis = 1, inplace = True)
corona_dataset_csv.head(10)

#Aggregating the rows by the country
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregated.head()

#Visualising data related to a country
corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()

#Calculating a good measure



