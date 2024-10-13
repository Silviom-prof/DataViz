import pandas as pd
import pandas_profiling

# Carregar o arquivo CSV
df = pd.read_csv('Movimento.csv')

# Gerar o relatório de perfil
profile = df.profile_report(title="Relatório de Análise Exploratória de Movimento")
profile.to_file("movimento_report.html")