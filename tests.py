>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> salaries = pd.read_csv(r'../Downloads/salaries.csv')
>>> salaries.columns
Index(['Age', 'Gender', 'Location', 'Job Tittle',
       'Years of post-college professional work experience', 'Size of Company',
       'Monthly Gross Salary', 'Other perks'],
      dtype='object')
>>> age_groups = salaries.groupby('Age').Age.count()
>>> age_groups
Age
18-24     41
25-34    272
35-44     92
45-54      8
Name: Age, dtype: int64
>>> genders = salaries.groupby('Gender').Gender.count()
>>> genders
Gender
Female    329
Male       84
Name: Gender, dtype: int64
>>> salaries.groupby('Age').Gender.count()
Age
18-24     41
25-34    272
35-44     92
45-54      8
Name: Gender, dtype: int64
>>> salaries.groupby('Gender').Age.count()
Gender
Female    329
Male       84
Name: Age, dtype: int64
>>> salaries.groupby(['Gender', 'Age']).Age.count()
Gender  Age  
Female  18-24     30
        25-34    225
        35-44     68
        45-54      6
Male    18-24     11
        25-34     47
        35-44     24
        45-54      2
Name: Age, dtype: int64
>>> age_gender = salaries.groupby(['Gender', 'Age']).Age.count()
>>> salaries['Monthly Gross Salary'].unique()
array(['860€', '1,800€', '3,000€', '4,500€', '750€', '1,128€', '2,900€',
       '1,300€', '2,445€', '3,980€', '1,500€', '1,600€', '3,200€',
       '1,850€', '2,500€', '1€', '1,400€', '880€', '2,270€', '2,200€',
       '1,200€',
       '2800€ gross + 1000€ liquido despesas e viatura + 20000€ bruto variavel anual',
       '2,660€', '3,500€', '3,600€', '2,828€', '5,800€', 'BRL 25000,00',
       '2,050€', '5,400€', '2,000€', '1,920€', '1,975€', '1,000€',
       '2,800€', '1,550€', '1,100€', '1,950€', '1,900€', '2,583€',
       '1,970€', '1,130€', '2,150€', '4,000€', '1,650€', '1,875€',
       '2,650€', '2,100€', '2,225€', '3,700€', '5,000€', '10,000€',
       '900€', '1,980€', '980€', '2,720€', '1,700€', '2,400€', '2,600€',
       '1,630€', '4,700€', '10,800€', '1,250€', '2,700€', '957€',
       '8,400€', '450€', '1,808€', '2,300€', '970€', '3,136€', '2,250€',
       '6,000€', '3,250€', '£8750', '1,530€', '€1,080', '972€', '7,000€',
       '18,000€', '1,750€', '1,725€', '4,167€', '7,100€', '1,080€',
       '1,182€', '1,420€', '1,575€', '1,450€', '2,199€', '1,697€',
       '2,190€', '2,850€', '1,125€', '1,290€', '1,221€', '3,570€',
       '1,150€', '1,625€', '1,015€', '719€', '800€', '1168,83€', '700€',
       '1,325€', '1,020€', '1,624€', '919€', '1,571€', '950€',
       '2.000,00€', '4,463€', '2,172€', '1,064€', '2126,83', '3,100€',
       '2,950€', '1,043€', '4,368€', '1,893€', '5,480€', '5,000$',
       '4,150€', '6,833€', '4,286€', '1,857€', '3,800€', '£ 5,500',
       '3,541€', '3,530€', '3,813€', '3,850€', '1,220€', '1,350€',
       '1,517€', '2,370€', '1,640€', '600€', '4,400€', '1,705€', '2,070€',
       '1,790€', '2,450€', '2,875€', '5,500€', '3,300€', '4,445€',
       '9,500€', '2,140€', '8,333€', '2,570€', '2,840€', '3,900€',
       '4,285€', '2,420€', '3,986€', '1,424€', '2,328€', '3,129€',
       '3,192€', '1,636€', '2,330€', '1,583€', '1,320€', '2,333€',
       '4,580€', '3,470€', '1000,00€', '1,867€', '3,550€', '803€',
       '1,060€', '1,173€', '2,425€', '1\xa0690', '7,200€', '1,267€',
       '1,505€', '1,050€', '2,316€', '724€', '2,975€'], dtype=object)
>>> salaries['Monthly Gross Salary'].replace('2800€ gross + 1000€ liquido despesas e viatura + 20000€ bruto variavel anual', '2800')
0        860€
1      1,800€
2      3,000€
3      4,500€
4        750€
        ...  
408    1,500€
409    1,000€
410    2,316€
411      724€
412    2,975€
Name: Monthly Gross Salary, Length: 413, dtype: object
>>> salaries['Monthly Gross Salary'].replace("2800€ gross + 1000€ liquido despesas e viatura + 20000€ bruto variavel anual", "2800")
0        860€
1      1,800€
2      3,000€
3      4,500€
4        750€
        ...  
408    1,500€
409    1,000€
410    2,316€
411      724€
412    2,975€
Name: Monthly Gross Salary, Length: 413, dtype: object
>>> salaries.rename(columns={'Monthly Gross Salary': 'Monthly_Gross_Salary'})
