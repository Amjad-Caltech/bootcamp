import numpy as np
import fold_change as fc

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

#load in the data settings
wt = np.loadtxt('data/wt_lac.csv', comments="#", delimiter=',', skiprows=3)
q18m = np.loadtxt('data/q18m_lac.csv', comments="#", delimiter=',', skiprows=3)
q18a = np.loadtxt('data/q18a_lac.csv', comments="#", delimiter=',', skiprows=3)

fig, ax = plt.subplots(1,1)
_ = ax.set_xlabel('IPTG concentration')
_ = ax.set_xscale('log')
_ = ax.set_ylabel('Fold Change')
_ = ax.plot(wt[:,0], wt[:,1], label='wt', marker='.', linestyle='none')
_ = ax.plot(q18m[:,0], q18m[:,1], label='q18m', marker='.', linestyle='none')
_ = ax.plot(q18a[:,0], q18a[:,1], label='q18a', marker='.', linestyle='none')

x_theor = np.logspace(-5, 2, num=400)
y_theor_wt = fc.fold_change(x_theor, 141.5)
y_theor_q18m = fc.fold_change(x_theor, 16.56)
y_theor_q18a = fc.fold_change(x_theor, 1332)

_ = ax.plot(x_theor, y_theor_wt, label='Theoretical wt')
_ = ax.plot(x_theor, y_theor_q18m, label='Theoretical q18m')
_ = ax.plot(x_theor, y_theor_q18a, label='Theoretical q18a')

_ = ax.legend()
plt.show()
