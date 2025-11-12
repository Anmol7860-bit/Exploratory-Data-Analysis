#import libraries 
import os 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
from scipy import stats

warnings.filterwarnings("ignore")
diabetes=pd.read_csv('diabetes.csv')
print(diabetes.head())
