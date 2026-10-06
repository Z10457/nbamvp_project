import pandas as pd
#this file is to allow the data to go from scrypt.ipynb to index.qmd
def build_players_df():
    players_df = pd.read_csv("players.csv")
    return players_df