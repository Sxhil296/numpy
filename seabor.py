# seaborn is a library that uses matplotlib underneath to plot graphs, it will be used to visualise random distributions


import matplotlib.pyplot as plt
import seaborn as sns

# sns.histplot([0, 1, 2, 3, 4, 5])
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

