import numpy as np
import pandas as pd

df = pd.read_csv("data/titanic.csv")

# (lignes, colonnes)
print(df.shape)
# résumé : colonnes, types, valeurs manquantes
print(df.info())
print(df.head())




