import timeit  # profiling


# runs only once
setup = '''
import numpy as np
import pandas as pd
df = pd.read_csv('mock_data.csv')
def quality(total_bill, tip):
    if tip / total_bill > 0.25:
        return "Seks"
    return "Huita"
'''

# first fragment to check
variant_one = '''
df['Tip Quality'] = df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis=1)
'''

# second fragment to check
variant_two = '''
df['Tip Quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
'''

print(timeit.timeit(
    setup=setup,
    stmt=variant_one,
    number=1000
))

print(timeit.timeit(
    setup=setup,
    stmt=variant_two,
    number=1000
))


