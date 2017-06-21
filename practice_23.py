import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

data = np.loadtxt('data/collins_switch.csv', skiprows=2, delimiter=',')

iptg = data[:,0]
gfp = data[:,1]
sem = data[:,2]

fig, ax = plt.subplots(1,1)

_ = ax.set_xlabel('iptg')
_ = ax.set_ylabel('normalized GFP')
_ = ax.set_xscale('log')

#_ = ax.plot(iptg, gfp, marker='.', linestyle='none')
_ = ax.errorbar(iptg, gfp, yerr=sem, linestyle='none',
                marker='.', markersize=10)

plt.show()
