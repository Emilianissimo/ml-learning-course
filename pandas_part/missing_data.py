import numpy as np
import pandas as pd


# np.nan == np.nan -> False
# np.nan is np.nan -> True

df = pd.read_csv('../csv/movie_scores.csv')

print(df.head())
print(df.isnull())
print(df.notnull())

condition = df['pre_movie_score'].notnull()
print(df[condition])

condition = df['pre_movie_score'].isnull() & df['first_name'].notnull()
print(df[condition])

'''
DELETE RECORD IF NAN
'''

print(df.dropna())  # delete if any has nan
print(df.dropna(thresh=1))
# delete only if it hasn't any value and all are nan | For example thresh=5 will require that all 5 columns should
# be not a nan
print(df.dropna(axis=1))
# columns, will delete all columns that have nan. One row has all columns that nan, so we have empty table
print(df.dropna(subset=['last_name']))  # check only this column for nan

'''
FILL THE RECORD IF NAN
'''

print(df.fillna('HUY'))

print(df['pre_movie_score'].fillna(0))

# Fill with mean (medium) value

print(df['pre_movie_score'].fillna(df['pre_movie_score'].mean()))

# will work for all NUMERIC type values in case of mean() works only for them and ignores others
print(df.fillna(df.mean()))

# Linear interpolation, we have here ordered dict, so we can interpolate data
airline_tix = {
    'first': 100,
    'business': np.nan,
    'economy_plus': 50,
    'economy': 30
}

ser = pd.Series(airline_tix)

print(ser.interpolate())  # ONLY FOR ORDERED DATA
