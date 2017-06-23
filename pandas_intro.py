import pandas as pd

# Dictionary of top men's World Cup scorers and how many goals
wc_dict = {'Klose': 16,
           'Ronaldo': 15,
           'Müller': 14,
           'Fontaine': 13,
           'Pelé': 12,
           'Kocsis': 11,
           'Klinsmann': 11}

s_goals = pd.Series(wc_dict)

# Dictionary of nations
nation_dict = {'Klose': 'Germany',
               'Ronaldo': 'Brazil',
               'Müller': 'Germany',
               'Fontaine': 'France',
               'Pelé': 'Brazil',
               'Kocsis': 'Hungary',
               'Klinsmann': 'Germany'}

# Series with nations
s_nation = pd.Series(nation_dict)
