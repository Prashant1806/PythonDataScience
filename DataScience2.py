import numpy as np
import pandas as pd

# Create a DataFrame
dframe = pd.DataFrame({'Prashant': [23, 24, 22],
						'Data': [10, 12, np.nan],
						'Science': [0, np.nan, np.nan]},
						columns = ['Prashant', 'Data', 'Science'])

# Use fillna of complete Dataframe

# value function will be applied on every column
dframe.fillna(value = dframe.mean(), inplace = True)
print(dframe)

# filling value of one column
dframe['Data'].fillna(value = dframe['Data'].mean(),
									inplace = True)
print(dframe)
