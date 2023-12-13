import numpy as np

def lancamento_dados():
    dado1 = np.random.randint(1, 7)
    dado2 = np.random.randint(1, 7)
    return dado1 + dado2



# Array para armazenar os resultados dos jogos
resultados = np.zeros(1000)

# Simula os jogos e armazena os resultados
for i in range(1000):
    resultados[i] = lancamento_dados()

# Média dos resultados
media_resultados = np.mean(resultados)

# Lançamento máximo e mínimo
maximo_resultado = np.max(resultados)
minimo_resultado = np.min(resultados)

# Número de vezes que cada possível lançamento ocorreu
contagem_lancamentos = np.histogram(resultados, bins=np.arange(1.5, 13.5))[0]

# Imprime os resultados
print(f"Média dos resultados: {media_resultados}")
print(f"Lançamento máximo: {maximo_resultado}")
print(f"Lançamento mínimo: {minimo_resultado}")
print("Número de vezes que cada possível lançamento ocorreu:")
for i in range(2, 13):
    print(f"Soma {i}: {contagem_lancamentos[i-2]}")