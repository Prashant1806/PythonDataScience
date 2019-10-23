import pandas as pd
import numpy as np

# create DataFrame
dframe = pd.DataFrame({'Prashant': [23, 24, 22, 22, 23, 24],
						'Data': [10, 12, 13, 14, 15, 16],
						'Science': [122, 142, 112, 122, 114, 112]},
						columns = ['Prashant', 'Data', 'Science'])

# Apply groupby and aggregate function
# max to find max value of column

# &quot;For&quot; and column &quot;Prashant&quot; for every
# different value of column &quot;Prashant&quot;.

print(dframe.groupby(['Prashant']).max())
