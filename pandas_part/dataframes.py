import numpy as np
import pandas as pd

np.random.seed(101)

mydata = np.random.randint(0, 101, (4, 3))

print(mydata)

myindex = ['CA', 'NY', 'AZ', "TX"]

mycolumns = ['JAN', 'FEB', 'MAR']

df = pd.DataFrame(data=mydata, index=myindex, columns=mycolumns)

print(df)

print(df.info())

# File parsing

df = pd.read_csv('../csv/mock_data.csv')

print(df)

# first 5 or else rows
print(df.head(5))
print(df.head(10))
# last 5 or else rows
print(df.tail(5))
print(df.tail(10))

print('---------------------------------------------------------------------------')
print(df.describe())
print(df.describe().transpose())
print('---------------------------------------------------------------------------')

# DataFrame column is Series
print(df['total_bill'])
print('---------------------------------------------------------------------------')
# Already DataFrame with two and more columns
print(df[
          ['total_bill', 'tip']
      ])
print('---------------------------------------------------------------------------')
df['tip_percentage'] = np.round(100 * df['tip'] / df['total_bill'], 2)
print(df)
# Tip percent amount from total_bill
# Works as dictionary btw

print('---------------------------------------------------------------------------')

df_dropped = df.drop('tip_percentage', axis=1)
# inplace -> will rewrite df itself, but maybe deprecated in the future, no need to pay attention
print(df_dropped)

print('---------------------------------------------------------------------------')

df = df.set_index('Payment ID')  # set for example ID as index and take data by it
print(df)
print('---------------------------------------------------------------------------')
df = df.reset_index()
print(df)
df = df.set_index('Payment ID')  # set for example ID as index and take data by it
print('---------------------------------------------------------------------------')
# TODO: we had append, but now is concat
# Pandas do not checking index as unique by default
print('---------------------------------------------------------------------------')
# Pandas broadcasts whole column
more_than_40 = df['total_bill'] > 40
print(more_than_40)
print(df[more_than_40])
print(df[df['sex'] == 'Male'])
# and
print(
    df[
        (df['total_bill'] > 30) & (df['sex'] == 'Male')
    ]
)
# or
print(
    df[
        (df['total_bill'] > 30) | (df['sex'] == 'Male')
    ]
)
# in
print(
    df[
        df['day'].isin(['Sun', 'Sat'])
    ]
)


