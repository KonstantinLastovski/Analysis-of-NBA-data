import pandas as pd

per_game = pd.read_csv('NBA_players_stats_per_game.csv')
per_100_poss = pd.read_csv('NBA_players_stats_per_100_possessions.csv')
advanced = pd.read_csv('NBA_players_stats_advanced.csv')

print(per_game.head(1), '\n',  per_100_poss.head(1), '\n', advanced.head(1))