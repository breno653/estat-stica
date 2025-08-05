"""
Histograma:
     Gráfico de barras que representa uma distribuição de frequência.
     - Eixo x (horiz): intervalos (classes) dos dados
     - Eixo y (vertc): frequência (contagem) de itens por intervalo
BoxPlot: 
     Diagrama de caixa que representa os extremos e mais os quartis
     - Min: O menor valor do conjunto de dados
     - Q1: Primeiro quartil dos dados (25%)
     - Q2: Segundo quartil dos dados, a mediana (50%)
     - Q3: Terceiro quartil dos dados (75%)
     - Max: O maior valor do conjunto de dados
Densidade:
     Gráfico que representa uma distribuição suavisada da frequência dos dados
     - Eixo x (horiz): intervalos (classes) dos dados
     - Eixo y (vertc): frequência (contagem) de itens por intervalo
Dispersão:
     Gráfico que representa a relação entre dois conjunto de dados
     - Eixos: Cada eixo representará um dos dois conjunto de dados
     - Pontos: Cada ponto representa a interseção entre as variáveis de ambos os conjuntos.

"""
import matplotlib.pyplot as plt
import pandas as pd
import macaco
print(macaco._doc_)

#importar os dados do csv
df_dados_brutos = pd.read_csv("homicidios_por_populacao/taxa_homicidios.csv")

def histograma():
    bins_do-grafico=[1,5,10,15]
    histograma = (df_dados_brutos['taxa homicidios']).plot.hist(figsize=(6,4),bins=bins_do_grafico)
    histograma.set_xlabel('taxa de homicidios')
    histograma.set_ylabel('frequencia')
