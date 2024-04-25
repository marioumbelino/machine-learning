import pandas as pd

movies_df = pd.read_csv('atividade02/questao09/movies.csv')

most_popular = movies_df[(movies_df["Popularity"] > 1000) & (movies_df["Vote_average"] > 8)].reset_index()

print(most_popular["Name"])