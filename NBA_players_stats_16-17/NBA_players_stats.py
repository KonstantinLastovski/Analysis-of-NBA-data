import pandas as pd

# Reading datasets
per_game = pd.read_csv('NBA_players_stats_per_game.csv')
per_100_poss = pd.read_csv('NBA_players_stats_per_100_possessions.csv')
advanced = pd.read_csv('NBA_players_stats_advanced.csv')

# Merging 3 dataframes into one
stats = pd.concat([per_game, per_100_poss, advanced], axis=1)

# Droping empty columns
stats = stats.drop(['Unnamed: 24', 'Unnamed: 29', 'Unnamed: 19'], axis=1)
print(stats.columns)

# Droping duplicated columns with same values
stats = stats.T.drop_duplicates().T
print(stats.columns)