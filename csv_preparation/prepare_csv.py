# import librairie pandas
import pandas as pd

# lecture
df = pd.read_csv('netflix_titles.csv')

df.columns = ["SHOW_ID", "TYPE", "TITLE", "DIRECTOR", "CAST", "COUNTRY", "DATE_ADDED", "RELEASE_YEAR", "RATING", "DURATION", "LISTED_IN", "DESCRIPTION"]

#print(df.head(5))

# Enregistrement au format CSV
df.to_csv("titles.csv",sep=';',index=False)

