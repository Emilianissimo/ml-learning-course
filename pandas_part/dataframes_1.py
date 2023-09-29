import numpy as np
import pandas as pd

df = pd.read_csv('../csv/mock_data.csv')

df = df.set_index('Payment ID')  # set for example ID as index and take data by it


def last_four(num: int) -> str:
    return str(num)[-4:]


df['last_four'] = df['CC Number'].apply(last_four)
print(df)


# Apply data to one column
def yelp(price: float) -> str:
    if price < 10:
        return '$'
    elif 10 <= price < 30:
        return '$$'
    return '$$$'


df['yelp'] = df['total_bill'].apply(yelp)
print(df)


# Apply data to several columns
def quality(total_bill: float, tip: float) -> str:
    if tip / total_bill > 0.25:
        return 'Щедрые'
    return 'Жопные'


# On applying to several, you'll get dataframe as param  for your callback
df['quality'] = df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis=1)  # for column
print(df)

# The same, but faster in case of we're vectorizing simple function into broadcast numpy function
# for series/dataframes/arrays
df['quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
print(df)

print(df.describe())

print(df.sort_values('tip'))
print(df.sort_values('tip', ascending=False))
print(df.sort_values(['tip', 'size']))
# Also works for dates

# max value and index
print(df['total_bill'].max(), df['total_bill'].idxmax())

# correlation, like if total_bill increases if tip increase, than correlation is plus, if not - minus
print(df.corr())

print(df['sex'].value_counts())

print(df['day'].unique(), df['day'].nunique())
# df['sex'].replace(['Female', 'F'])
result = df['sex'].replace(['Female', 'Male'], ['F', 'M'])
print(result)
# Dictionary like
result = df['sex'].map({'Female': 'F', 'Male': 'M'})

print(df.duplicated())
# will return false for first and false for each duplicate of it

simple_df = pd.DataFrame([1, 2, 2, 2], ['a', 'b', 'c', 'd'])
print(simple_df)
print(simple_df.duplicated())
print(simple_df.drop_duplicates())

# should also work for dates, inclusive for 20 included, else will have 19
print(df['total_bill'].between(10, 20, inclusive=True))
# filtering it
print(
    df[df['total_bill'].between(10, 20, inclusive=True)]
)

# 10 first largest tips
print(df.nlargest(10, 'tip'))
# 10 first smallest tips
print(df.nsmallest(10, 'tip'))

# just a random from dataframe sample. Using n returns n count of rows
print(df.sample(n=5))
# using frac, gives a fraction, like 0.1 from all the rows (10%)
print(df.sample(frac=0.1))
