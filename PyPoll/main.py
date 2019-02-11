#import pandas
import pandas as pd

#read the csv file
df = pd.read_csv('election_data.csv')


#print the count of unique voters
print ("Total Votes:" ,df['Voter ID'].count())

#For each candidate,count the number of total votes and create a new dataframe with those corresponding numbers
new_df=df.groupby('Candidate')['Voter ID'].count().reset_index(name='Count').sort_values('Count',ascending=False)

new_df

#create a percentage column and write the percentage of votes for each candidate row
new_df['Percent']=round(new_df.Count/new_df.Count.sum()*100,5)
new_df 

#Summary Table, writes to the outputpoll text file.
#For each candidate, writes the percentages and total votes. Eventually, determines the winner based on the max function.

print("Election Results", file=open("outputpoll.txt", "a"))
print("-------------------------", file=open("outputpoll.txt", "a"))
print ("Total Votes:" ,df['Voter ID'].count(), file=open("outputpoll.txt", "a"))
print("-------------------------", file=open("outputpoll.txt", "a"))
for index, row in new_df.iterrows():
    print (row['Candidate']+": ",str('%.3f'%row['Percent'])+"% ","("+str(row['Count'])+")", file=open("outputpoll.txt", "a"))
print("-------------------------", file=open("outputpoll.txt", "a"))
print("Winner: ", new_df['Candidate'][new_df['Percent'] == new_df['Percent'].max()].iloc[0], file=open("outputpoll.txt", "a"))
print("-------------------------", file=open("outputpoll.txt", "a"))




