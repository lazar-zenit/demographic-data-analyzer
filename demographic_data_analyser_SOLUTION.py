import pandas as pd

df=pd.read_csv('adult.data.csv')

number_of_people=len(df.index) #total number of entries

race_count=df.groupby(['race']).size() #group by race and deliver size of that dataframe

average_age_men=df.loc[df['sex']=='Male'][['age']].mean().round(decimals=1) #


percentage_of_bachelors=(df.loc[df['education']=='Bachelors', ['age']] 
                         .count()#hack is to use another column to serve as an index so count will force single series
                         /number_of_people*100).round(decimals=1) #calculate percentadn round it. beware of parentheses

#higher education means 'Bachelors', 'Masters' and 'Doctorate'
number_bachelors=df.loc[df['education']=='Bachelors', ['age']].count() #same hack, easier on syntax if done separately
number_masters=df.loc[df['education']=='Masters', ['age']].count()
number_doctorate=df.loc[df['education']=='Doctorate', ['age']].count()

education=df.value_counts('education')
print(education)
     
higher_education=number_bachelors+number_masters+number_doctorate #sum of higher degrees
lower_education=number_of_people-higher_education #difference between all people and ones with higher degrees


