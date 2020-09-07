import pandas as pd
import numpy as np
import regex as re
import matplotlib.pyplot as plt
import seaborn as sns

apps = pd.read_csv("/Users/Carlos/Desktop/Ironhack/REPOS/proyecto/storytelling-project/Data/msft.csv")



def ratingsearch(r):
    """"
    This function returns the apps table sorted by the rating you specified.
    Input: r = Rating you want to search by.
    Output : Apps dataframe only with the rating you specified.
    """
    for n in apps_clean["Rating"]:
        return apps_clean.where(apps_clean['Rating'] == r).dropna()

def priceapp (name):
    """
    This function returns the price of an app with the index number of the same.
    Input = Name of the app, you have to refer to it with "".
    Output = Index number and price of the app
    """
    
    return apps_clean["Price"].where(apps_clean["Name"] == f"{name}").dropna().reset_index()

def currency(x):
    """
    This function converts Indian rupees to euros.
    Input: The column with the rupees prices.
    Ouput: The same column expressed in euros.
    """
    res = re.findall(r"\d+.\d+",x)
    if x == "Free":
        return 0.0
    elif res:
        return float(res[0])*0.012
    
# apps.Price.apply(lambda x: x.replace(",",""))
# La función lambda para reemplazar comas con . en el precio