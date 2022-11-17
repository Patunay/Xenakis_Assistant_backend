import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_array = np.array(([0,0,1,2,3,4,1,3,2,1,4,5,1,0,0,0],[0,1,2,3,4,5,6,1,3,16,1,7,1,7,1,0]),dtype="int8")



df = pd.DataFrame(data_array)   # columns=["a","b","c","d","e"])

p1 = sns.heatmap(df, annot=True,fmt='d', cmap="BuPu")

# print(p1)
plt.show()