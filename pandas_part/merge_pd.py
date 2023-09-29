import numpy as np
import pandas as pd


registrations = pd.DataFrame({'reg_id': [1, 2, 3, 4], 'name': ['Andrew' ,'Bobo', 'Claire', 'David']})
logins = pd.DataFrame({'log_id': [1, 2, 3, 4], 'name': ['Xavier', 'Andrew', 'Yolanda', 'Bobo']})

# INNER MERGE
print(
    pd.merge(registrations, logins, how='inner', on='name')
)

# LEFT MERGE

print(
    pd.merge(left=registrations, right=logins, how='left', on='name')
)

# RIGHT MERGE

print(
    pd.merge(left=registrations, right=logins, how='right', on='name')
)

# OUTER MERGE

print(
    pd.merge(left=registrations, right=logins, how='outer', on='name')
)

# SETTING INDEX BY NAME AND MERGING BY IT

registrations = registrations.set_index('name')
# logins stay the same

# Index + column name
print(
    pd.merge(registrations, logins, left_index=True, right_on='name', how='inner')
)

registrations = registrations.reset_index()  # drop index
registrations.columns = ['reg_name', 'reg_id']
print(registrations)

# merging via different named columns

result = pd.merge(registrations, logins, how='inner', left_on='reg_name', right_on='name')
print(
    result
)

# drop reg name
print(result.drop('reg_name', axis=1))

# duplicates
registrations.columns = ['name', 'id']
logins.columns = ['id', 'name']

print(
    pd.merge(registrations, logins, how='inner', on='name')
)

print(
    pd.merge(registrations, logins, how='inner', on='name', suffixes=('_reg', '_log'))
)
