import sweetviz as sv
import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('Movimento.csv')

# Gerar um relatório de EDA interativo
report = sv.analyze(df)
report.show_html("sweetviz_report.html")
