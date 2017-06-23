import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import bootcamp_utils as bcu

import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')

x = np.linspace(1600, 2500, 400)
cdf_theor = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))

data_x, data_y = bcu.ecdf(xa_low)

fig, ax = plt.subplots(1,1)

_ = ax.set_xlabel('cross sectional diameter')
_ = ax.set_ylabel('ECDF')

_ = ax.plot(x, cdf_theor, color='gray')
_ = ax.plot(data_x, data_y, label='low food')

_ = ax.legend()

plt.show()
