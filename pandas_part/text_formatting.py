import numpy as np
import pandas as pd


names = pd.Series([
    'andrew',
    'bobo',
    'claire',
    'david',
    '5'
])

print(names.str.upper())
print(names.str.isdigit())

tech_finance = ['GOOG,APPL,AMZN', 'JPN,BAC,GS']
tickers = pd.Series(tech_finance)

print(tickers.str.split(',', expand=True))

messy_names = pd.Series(['andrew  ', 'bo:bo', '  claire  '])
print(
    messy_names
      .str.replace(':', '')
      .str.strip()
      .str.capitalize()
    )


def cleanup(name: str) -> str:
    name = name.replace(':', '')
    name = name.strip()
    name = name.capitalize()
    return name


print(messy_names.apply(cleanup))

# built-in functions are slower than apply. Apply need to be vectorized, and it will be faster. But if it is not so much
# big data, built-in functions are faster for developer.
