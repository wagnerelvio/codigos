#pip install matplotlib numpy
import numpy as np
import matplotlib.pyplot as plt

# Gerando 100 dados aleatórios no intervalo de 1 a 100
dados = np.random.randint(1, 101, 100)

# Calculando as estatísticas
media = np.mean(dados)
mediana = np.median(dados)
desvio_padrao = np.std(dados)

# Exibindo as estatísticas
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Desvio-padrão: {desvio_padrao}")

# Plotando os dados
plt.figure(figsize=(10, 6))
plt.plot(dados, label='Dados aleatórios', marker='o', linestyle='-', color='b')

# Adicionando uma linha para a média, mediana e desvio-padrão
plt.axhline(y=media, color='r', linestyle='--', label=f'Média: {media:.2f}')
plt.axhline(y=mediana, color='g', linestyle='-.', label=f'Mediana: {mediana:.2f}')
plt.axhline(y=media + desvio_padrao, color='purple', linestyle=':', label=f'+1 Desvio-padrão: {media + desvio_padrao:.2f}')
plt.axhline(y=media - desvio_padrao, color='purple', linestyle=':', label=f'-1 Desvio-padrão: {media - desvio_padrao:.2f}')

# Configurações do gráfico
plt.title("Gráfico de Dados Aleatórios com Média, Mediana e Desvio-Padrão")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.show()
