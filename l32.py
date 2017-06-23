import numpy as np
import pandas as pd

import bootcamp_utils

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

def sem(data):
    return np.std(data) / np.sqrt(len(data))

gb = df.groupby('ID')
df_mean_sem = gb.agg([np.mean, sem])
#print(df_mean_sem['impact force (mN)'])

# fig, ax = plt.subplots(1,1)
# _ = ax.set_ylabel('impact force (mN)')
# _ = ax.grid(False, axis='x')
# _ = ax.bar(np.arange(4), df_mean_sem[('impact force (mN)', 'mean')],
#         yerr=df_mean_sem[('impact force (mN)', 'sem')],
#         tick_label=['I', 'II', 'III', 'IV'])

#ax = sns.barplot(data=df, x='ID', y='impact force (mN)')
# ax.set_xlabel('')
# ax.set_ylabel('impact force (mN)');

_ = sns.swarmplot(data=df, x='ID', y='impact force (mN)')

plt.show()
