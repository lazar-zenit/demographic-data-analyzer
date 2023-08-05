import pandas as pd

df=pd.read_csv('adult.data.csv')

number_of_people=len(df.index) #total number of entries

race_count=df.groupby(['race']).size() #group by race and deliver size of that dataframe

average_age_men=df.loc[df['sex']=='Male'][['age']].mean().round(decimals=1) #


'''
number_bachelors=df.loc[df['education']=='Bachelors', ['age']].count() #same hack, easier on syntax if done separately
number_masters=df.loc[df['education']=='Masters', ['age']].count()
number_doctorate=df.loc[df['education']=='Doctorate', ['age']].count()
'''

number_bachelors=(df['education'].value_counts())['Bachelors']
number_masters=(df['education'].value_counts())['Masters']
number_doctorate=(df['education'].value_counts())['Doctorate']

percentage_of_bachelors=(number_bachelors/number_of_people*100).round(decimals=1)

higher_education=number_bachelors+number_masters+number_doctorate #sum of higher degrees
lower_education=number_of_people-higher_education #difference between all people and ones with higher degrees

education_vs_salary=df.loc[:,['education','salary']] #just to make it easier on dislexy

#BEWARE BRACKETS, EDUCATION CONDITION SOULD BE INCASED IN ITS OWN ROUND BRACKETS

higher_education_rich=len(education_vs_salary[
                              ((education_vs_salary['education'] == 'Bachelors') | 
                              (education_vs_salary['education'] == 'Masters') | 
                              (education_vs_salary['education'] == 'Doctorate')
                              )
                              & (education_vs_salary['salary']=='>50K')
                              ]
          )
#for some reason
lower_education_rich = len(education_vs_salary[
                              ((education_vs_salary['education'] == '10th') | 
                              (education_vs_salary['education'] == '11th') | 
                              (education_vs_salary['education'] == '12th') |
                              (education_vs_salary['education'] == '1st-4th') |
                              (education_vs_salary['education'] == '5th-6th') |
                              (education_vs_salary['education'] == '7th-8th') |
                              (education_vs_salary['education'] == '9th') |
                              (education_vs_salary['education'] == 'Assoc-acdm') |
                              (education_vs_salary['education'] == 'Assoc-voc') |
                              (education_vs_salary['education'] == 'HS-grad') |
                              (education_vs_salary['education'] == 'Masters') |
                              (education_vs_salary['education'] == 'Preschool') |
                              (education_vs_salary['education'] == 'Prof-school') |
                              (education_vs_salary['education'] == 'Some-college')
                              )
                              & (education_vs_salary['salary']=='>50K')
                              ]
                          )     


#JUST FOR CHECKS
salary=df.loc[:,['salary']].value_counts()

min_work_hours=df['hours-per-week'].min()

num_min_workers=len(df[
    (df['hours-per-week']==min_work_hours)
    & (df['salary']=='>50K')]
    )
rich_percentage=round(((len(df[df['salary']=='>50K']))/number_of_people*100), 1)#round has to be on the start because of the error "'float' object has no attribute 'round'

