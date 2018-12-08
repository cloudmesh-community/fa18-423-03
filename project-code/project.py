from parser import *
import os, pandas as pd, numpy as np
import datetime

#Files that already been scanned will be stored inside a text file
#going through the list of file to ensure there is no double reading on the same file
try:
    with open('scanned_file.txt','r') as in_file:
        scanned_files = in_file.readlines()

        scanned_files = [file.strip() for file in scanned_files]
    
except:
    print('This must be an initial run')
    scanned_files = []
    
#detecting all files in the current directory
#files will be uploaded to the same directory in the cloud to be processed
current_files = os.listdir()

#filtering current files to be a file and an xml file
current_files = [file for file in current_files if os.path.isfile(file) and file[-4:]=='.xml' and file not in scanned_files]

##Loading Latest compiled filetered data
for file in current_files:
    new_data = parsing(file)
    
    try:
        old_data = pd.read_csv('compiled_data.csv')
    except:
        print('No old data. New file will be created')
        new_data.to_csv('compiled_data.csv',index = False)
    else:
        df = pd.concat([old_data,new_data])
        df.to_csv('compiled_data.csv',index=False)
    
    with open('scanned_file.txt','a') as out_file:
        out_file.write(file +'\nAdded' +str(datetime.datetime.today())+'\n\n')
    print(file,'has been processed')
print('all data processed')

