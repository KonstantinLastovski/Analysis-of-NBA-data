import pandas as pd

# Reading datasets
per_game = pd.read_csv('NBA_players_stats_per_game.csv')
per_100_poss = pd.read_csv('NBA_players_stats_per_100_possessions.csv')
advanced = pd.read_csv('NBA_players_stats_advanced.csv')

# Merging 3 dataframes into one
stats = pd.concat([per_game, per_100_poss, advanced], axis=1)

# Droping empty columns
stats = stats.drop(['Unnamed: 24', 'Unnamed: 29', 'Unnamed: 19'], axis=1)

# Droping duplicated columns with same values
stats = stats.T.drop_duplicates().T

# Droping raws with stats of players which was traded this season (Dataframe had raws with stats in old team,
# in new team and total. We keep only total stats of these players)
stats = stats.drop_duplicates(['Rk']).reset_index()

#Finding indexes of raws and columns with NaN values
#x = list(pd.isnull(stats).any(1).nonzero()[0])
#y = list(pd.isnull(stats).any(0).nonzero()[0])
#print(x, y)
#xy = stats.loc[x]

# Replace all of the NaN values with 0
stats = stats.fillna(0)

#Convert columns to numeric formats
stats.apply(pd.to_numeric, errors='ignore')

#Rename players to normal view
list_player = []
for i in stats.Player:
    i = i.split("\\")[0]
    list_player.append(i)
stats.Player = list_player

print(stats.dtypes)


