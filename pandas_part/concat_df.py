import numpy as np
import pandas as pd
# we can concat for each axis -> columns and rows
# rows for identical columns and columns for identical rows

df_one = {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
}

df_two = {
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
}

one = pd.DataFrame(df_one)
two = pd.DataFrame(df_two)

print(one, two)

print(pd.concat([one, two], axis=1))  # like left join, rows concat

print(pd.concat([one, two], axis=0))  # columns concat

# can rename columns
two.columns = one.columns
new_df = pd.concat([one, two], axis=0)
print(new_df)  # columns concat

new_df.index = range(len(new_df))
print(new_df)
