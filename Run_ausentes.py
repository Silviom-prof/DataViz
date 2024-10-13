import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# Carregar o dataset Movimento.csv
df = pd.read_csv('Movimento.csv')

# Visualizar os valores ausentes usando missingno
msno.matrix(df)
plt.title("Visualização de Valores Ausentes - Matrix")
plt.show()

# Heatmap para verificar a correlação de dados ausentes
msno.heatmap(df)
plt.title("Heatmap de Correlação de Valores Ausentes")
plt.show()
