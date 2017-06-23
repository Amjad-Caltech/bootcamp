import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

df_subset1 = df.loc[df['adhesive strength (Pa)'] < -2000, ['impact time (ms)']]

df_subset2 = df.loc[df['ID'] == 'II', ['impact force *','adhesive force (mN)']]

df_subset3 = df.loc[df['ID'].isin(['III', 'IV']),
                    ['adhesive force (mN)',
                    'time the frog pulls on the target (ms)']]

[(frog_id, np.mean(df.loc[df['ID']==frog_id, 'impact force (mN)']))
                                             for frog_id in df['ID'].unique()]
