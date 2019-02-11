#import pandas 
import pandas as pd

#read csv file
df = pd.read_csv('budget_data.csv')

#import dateconversion libraries
from datetime import datetime
from dateutil.parser import parse

#convert string date to datetime
df['FullDate'] = pd.to_datetime(df['Date'])

#extract year and month from datetime column
df['Year'] = pd.DatetimeIndex(df['FullDate']).year

df['Month'] = pd.DatetimeIndex(df['FullDate']).month

#create month-year pairs
df['MonthYear'] = pd.to_datetime(df['FullDate']).dt.to_period('M')

#print number of unique months
print ("Total Months:" ,df['Date'].nunique())

#print profit/loss total
print("Total: $"+str(df['Profit/Losses'].sum()))

#In order to calculate  the change from one month to the next, create a new column and record the value by shifting the current month 1 row down.
df['Profit/Loss_Shifted']=df['Profit/Losses'].shift(1)

#create a column to record the chnage between shifted value(previous month) and the current month
df['Change']=df['Profit/Losses']-df['Profit/Loss_Shifted']
print("Average Change: $"+str(round(df['Change'].mean(),2)))

#print the maximum positive change 
print("Greatest Increase in Profits: " +df['Date'][df['Change'] == df['Change'].max()].iloc[0]+ " ($"+str(int(df['Change'].max()))+")")

#print the maximum negative change  
print("Greatest Increase in Profits: " +df['Date'][df['Change'] == df['Change'].min()].iloc[0]+ " ($"+str(int(df['Change'].min()))+")")


#Summary Table

print("Financial Analysis", file=open("outputbank.txt", "a"))
print("----------------------------", file=open("outputbank.txt", "a"))
print ("Total Months:" ,df['Date'].nunique(), file=open("outputbank.txt", "a"))
print("Total: $"+str(df['Profit/Losses'].sum()), file=open("outputbank.txt", "a"))
print("Average Change: $"+str(round(df['Change'].mean(),2)), file=open("outputbank.txt", "a"))
print("Greatest Increase in Profits: " +df['Date'][df['Change'] == df['Change'].max()].iloc[0]+ " ($"+str(int(df['Change'].max()))+")", file=open("outputbank.txt", "a"))
print("Greatest Increase in Profits: " +df['Date'][df['Change'] == df['Change'].min()].iloc[0]+ " ($"+str(int(df['Change'].min()))+")", file=open("outputbank.txt", "a"))

