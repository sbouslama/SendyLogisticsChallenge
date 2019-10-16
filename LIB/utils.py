import warnings
warnings.filterwarnings("ignore")
import pandas as  pd 
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime

def data_characterization(data):
    print("shape of data : "+str(data.shape))
    data_characterization=pd.DataFrame()
    columns=data.columns
    Type=[]
    Count=[]
    unique_values=[]
    Max=[]
    Min=[]
    Mean=[]
    Nan_counts=data.isnull().sum().tolist()
    Nan_ratio=(data.isnull().sum()/len(data)).values

    Type=data.dtypes.tolist()
    J=0
    for  i  in columns : 
        unique=list(data[i].unique())
        unique_values.append(unique)
        Count.append(len(unique))
        
        
        if (data[i].dtypes.name == 'object') :
            Max.append(0)
            Min.append(0)
            Mean.append(0)
        elif ( (data[i].dtypes == '<M8[ns]') ) : 
            Max.append(0)
            Min.append(0)
            Mean.append(0)
        elif ( (data[i].dtype.name=="category") ) : 
            Max.append(0)
            Min.append(0)
            Mean.append(0)

        else : 
            Max.append(data[i].max())
            Min.append(data[i].min())
            Mean.append(data[i].mean())
   
    data_characterization["Columns name"]=columns
    data_characterization["Type "]=data.dtypes.tolist()
    data_characterization["Count unique values"]=Count
    data_characterization["Count Nan values"]=Nan_counts
    data_characterization["Ratio Nan values"]=Nan_ratio

    data_characterization["Unique   values"]=unique_values
    data_characterization["Max"]=Max
    data_characterization["Min"]=Min
    data_characterization["Mean"]=Mean
    
    display(data_characterization)    
    return None 