import numpy as np
import pandas as pd

df = pd.read_csv("data/titanic.csv")

# (lignes, colonnes)
print(df.shape)
# résumé : colonnes, types, valeurs manquantes
print(df.info())
print(df.head())

#taux de suvie :
print ("Taux de survie global :", df["survived"].mean())
print ("Nombre de survivants :", df["survived"].sum())
print("Répartition :")
print(df["survived"].value_counts())



