import numpy as np
import pandas as pd

df = pd.read_csv('../csv/mpg.csv')

print(
    df.groupby('model_year').mean()
)

print(
    df.groupby(['model_year', 'cylinders']).mean()  # returns multiindex
)

# Indexes are not columns
print(
    df.groupby(['model_year']).describe().transpose()
)

year_cul = df.groupby(['model_year', 'cylinders']).mean()
print(year_cul)

# loc needed to call by index
print(year_cul.loc[70])
print(year_cul.loc[[70, 82]])
print(year_cul.loc[(70, 4)])

# cross-section in case of loc do not work for multiindex
print(
    year_cul.xs(key=70, level='model_year')
)

# It won't show cylinders' count
print(
    year_cul.xs(key=4, level='cylinders')
)

# prepare data to filter by multiindex
print(
    df[df['cylinders'].isin([6, 8])].groupby(['model_year', 'cylinders']).mean()
)
# don't try to use xs on multiple child indexes, prepare data first -> Better

# switch levels
print(year_cul.swaplevel())

# sorting by index level
print(
    year_cul.sort_index(level='model_year', ascending=False)
)

'''
DIFFERENT AGGREGATIONS FOR DIFFERENT COLUMNS
'''

print(
    df.agg(['std', 'mean'])['mpg']
)

print(
    df.agg(
        {
            'mpg': ['max', 'mean'],
            'weight': ['mean', 'std']
        }
    )
)
