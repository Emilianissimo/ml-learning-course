import numpy as np
import pandas as pd
from datetime import datetime


ser = pd.Series(['Nov3, 1990', '2000-01-01', None])
time_ser = pd.to_datetime(ser)

obvious_euro_date = '31-12-2000'
print(pd.to_datetime(obvious_euro_date))

euro_date = '10-12-2000'

print(
    pd.to_datetime(euro_date, dayfirst=True)
)

american_date = '10-12-2000'

print(
    pd.to_datetime(american_date, dayfirst=False)
)

style_date = '22--Dec--2000'

print(
    pd.to_datetime(style_date, format='%d--%b--%Y')
)

custom_date = '12th of Dec 2000'

print(
    pd.to_datetime(custom_date)
)

sales = pd.read_csv('../csv/datetime.csv')

print(sales)

sales['DATE'] = pd.to_datetime(sales['DATE'])

print(sales['DATE'])

sales = pd.read_csv('../csv/datetime.csv', parse_dates=[0])

sales = sales.set_index('DATE')

print(sales.resample(rule='A').mean())

# Rule list -> pandas docs

sales = pd.read_csv('../csv/datetime.csv', parse_dates=[0])

print(sales['DATE'].dt.year)
