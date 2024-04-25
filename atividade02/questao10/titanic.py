import pandas as pd

titanic_df = pd.read_csv('atividade02/questao10/titanic_dataset.csv')

missing_values = titanic_df.isna().sum()

titanic_df = titanic_df.dropna(subset=["age"])

underage_df = titanic_df[(titanic_df["age"] < 18)]

print(underage_df)
