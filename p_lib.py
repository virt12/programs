import pandas as pd #importing pandas library working with dataframes
import os # importing os library working with file system in os

file_path=input("Please enter the full file path") #providing user input in order to get data file path
if (len(file_path) ==0 or (not os.path.isfile(file_path))):# if file path not presented or that file not exists then error message
    print("Path can't be null, please insert a new path or you typed wrong file path")
else:
    df = pd.read_csv(file_path)# in success case we storing data file in df variable
    df1=df.groupby(['Darbuotojas']).sum()# implementing grouping by darbuotojas and doing sum salary (alga)
    mokesciai=df1["Alga"]*0.4# in order to taxes we need to count it by multiply 0.4
    df1['Mokesciai']=mokesciai # adding new column with taxes (mokesciai)
    df1.rename(columns = {'Alga':'Suma'}, inplace = True)# changing column name
    result1_file_path=input("Please provide result file path for first task part")#asking the user input referencing for result file path
    df1.to_csv (result1_file_path, index = True, header=True)#writing first task condition result to the new csv file
    df4=df#assign primary data into new variable for the second task condition
    df4= df.groupby(['Darbuotojas', 'Tipas']).sum()#implementing grouping by employees(darbuotojas) and type(tipas) and counting it's sum
    df4 = df4.reset_index()#reseting index of dataframe in order to fulfill empty row places by adding same names for different types
    df4=df4.rename(columns = {'Alga':'Suma'}, inplace = False)# rename the column name
    result2_file_path=input("Please provide result file path for second task part")#asking the user input referencing for result file path
    df4.to_csv (result2_file_path, index = True, header=True)#writing second condition results to the new csv file
   
