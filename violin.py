
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ukrulgbt.csv')
ax = sns.violinplot(data=df, palette="pastel")
plt.show()

fig = ax.get_figure()
fig.savefig('negativeDeltaPlot.png', dpi=300)



