import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("/content/archive (2).zip")
df

df_sample = pd.crosstab(df['room_type_reserved'],df['avg_price_per_room'])
df_sample

observed_values = df_sample.values
observed_values

value=stats.chi2_contingency(df_sample)
value

expected_values=value[3]
expected_values

chi_square = sum([((o-e)**2)/e for o,e in zip(observed_values,expected_values)])
chi_square

chi_square_value=0
for i in chi_square:
    chi_square_value=chi_square_value+i
print(chi_square_value)

critical_value=stats.chi2.ppf(q=0.95,df=106498.76829018457)
critical_value

if chi_square_value>=critical_value:
    print("Null Hypothisis H0 is Rejected,Ha is Accepted, There is some relationship between 2 categorical variables")
else:
    print("Null Hypothisis H0 is Accepted,Ha is Rejected,There is No relationship between 2 categorical variables")
    
    
p_value=1-stats.chi2.cdf(x=chi_square_value,df=107259.03080754353)

if p_value<0.05:
    print("Null Hypothisis H0 is Rejected,Ha is Accepted, There is some relationship between 2 categorical variables")
else:
    print("Null Hypothisis H0 is Accepted,Ha is Rejected,There is No relationship between 2 categorical variables")
