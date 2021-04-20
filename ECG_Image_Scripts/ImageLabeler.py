from os import listdir
from os.path import isfile, join
import pandas as pd
path = r"G:\SD 2020\pythonImage 2\data"

# call listdir() method
# path is a directory of which you want to list
directories = listdir(path)
fileName=[]
pottasium=[]
# This would print all the files and directories
for file in directories:
    fileName.append(file)
    pottasium.append(file[:3])
    #Checks the pottasium level and sets it to a value
for i in range(len(pottasium)):
    pottasium[i]=int(float(pottasium[i])*10)
    if(pottasium[i]<=30):
        pottasium[i]=0
    elif(pottasium[i]>=31 and pottasium[i]<=34):
        pottasium[i]=1
    elif(pottasium[i]>=35 and pottasium[i]<=55):
        pottasium[i]=2
    elif(pottasium[i]>=56 and pottasium[i]<=70):
        pottasium[i]=3
    else:
        pottasium[i]=4
d = {'fileName': fileName, 'pottasium': pottasium}

df = pd.DataFrame(data=d)
print(df)
df.to_csv("imageLabels.csv",header=False, index=False)