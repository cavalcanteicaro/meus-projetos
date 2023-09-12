# -*- coding: utf-8 -*-
"""desafio-python

Arquivo Original
    https://colab.research.google.com/drive/1TasrqmS5aZtmYJxRQpf9DjnhNid5Mfny
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Converte os dados para um DataFrame do Pandas para facilitar o manuseio
    df = pd.DataFrame(data)
    print("Dados extraídos com sucesso!")
else:
    print("Erro ao acessar a API.")

# Selecionando colunas relevantes
df = df[['id', 'name', 'email', 'address']]

# Convertendo a coluna 'address' em strings
df['address'] = df['address'].astype(str)

# Contagem de usuários por cidade
city_counts = df['address'].str.split(',').str[-2].str.strip().value_counts()

# Gráfico de barras
plt.figure(figsize=(10, 6))
city_counts.plot(kind='bar', color='skyblue')
plt.title('Contagem de Usuários por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Número de Usuários')
plt.xticks(rotation=45)
plt.show()

