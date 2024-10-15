import pandas as pd

# Lendo o arquivo txt separado por ";"
file_path = '/mnt/data/exemplo.txt'  # Substitua pelo caminho do arquivo
df = pd.read_csv(file_path, sep=';')

# Exportando para Excel
output_file = '/mnt/data/output.xlsx'
df.to_excel(output_file, index=False)

# Retornando o caminho do arquivo gerado
output_file