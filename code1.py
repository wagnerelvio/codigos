#pip install matplotlib


import matplotlib.pyplot as plt

# Dados para plotar
x = [1, 2, 3, 4, 5]  # Eixo X
y = [2, 4, 6, 8, 10]  # Eixo Y

# Criando o gráfico
plt.plot(x, y, label="Crescimento linear", color='b', marker='o')

# Adicionando título e rótulos aos eixos
plt.title("Gráfico Simples")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Adicionando legenda
plt.legend()

# Mostrando o gráfico
plt.show()





