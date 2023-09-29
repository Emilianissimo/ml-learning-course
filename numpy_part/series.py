import pandas as pd

myindex = ['USA', 'CANADA', 'MEXICO']

mydata = [1776, 1867, 1821]

myser = pd.Series(data=mydata)

print(myser)

myser = pd.Series(data=mydata, index=myindex)

print(myser)

ages = {'Sam': 5, 'Frank': 10, 'Spike': 7}

print(pd.Series(ages))

data_set_1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
data_set_2 = {'Brazil': 100, 'China': 500, 'India': 210, 'USA': 260}

sales_q1 = pd.Series(data_set_1)
sales_q2 = pd.Series(data_set_2)

total_q12 = sales_q1.add(sales_q2, fill_value=0)
print(total_q12)
