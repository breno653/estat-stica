import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

data = 'data/sp500_data.csv.gz'
df = pd.read_csv(data)
print(df.head(5))

df= df.drop(columns=['ADS'])

df= df.rename(columns={'Unnamed: 0': 'Data'})
print(df.head(5))

df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index('Data')
print(df.head(5))

# encontrar a maio r e maior data
data_inicio = df.index.min()
data_fim =df.index.max()
print(f"Quantidades de variações coletadas: {len(df)}")
print(f"Periodo de coleta:{data_inicio.strftime('%d/%m/%Y')} á {data_fim.strftime('%d/%m/%Y')}")

ativo = 'IBM'
maior_valor = df[ativo].max()
data_maior = df[ativo].idxmax()
menor_valor = df[ativo].min()
data_menor = df[ativo].idxmin()
print("-" * 30)
print(f"Maior variação diaria: {maior_valor:.4f}")
print(f"Ocorreu no dia: {data_maior.strftime('%d/%m/%Y')}")

media = df[ativo].mean()
mediana = df[ativo].median()
moda= df[ativo].mode()
print(f"Medidas de tendências central para {ativo}:")
print(f"Média: {media:4f}")
print(f"Mediana: {mediana:.4f}")
if (len(moda) > 0):
    print(f"Modas: {moda}")
else:
    print(f"O ativo {ativo} é amodal")