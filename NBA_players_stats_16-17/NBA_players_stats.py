import pandas as pd

per_game = pd.read_csv('NBA_players_stats_per_game.csv')
per_100_poss = pd.read_csv('NBA_players_stats_per_100_possessions.csv')
advanced = pd.read_csv('NBA_players_stats_advanced.csv')

#two = pd.merge(per_game, per_100_poss, on='Rk')
stats = pd.concat([per_game, per_100_poss, advanced], axis=1)
print(stats.head())