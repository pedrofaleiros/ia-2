import pandas as pd

# Leitura dos dados do CSV
data = pd.read_csv("dados_alunos.csv")

# Pesos para os cursos
pesos = {
    "Engenharia": [1.5, 0.8, 1.2, 0.7, 1],
    "Direito": [0.7, 1.2, 0.7, 1.5, 1.2],
    "Medicina": [1.2, 0.8, 1.5, 0.7, 1],
    "TI": [1.5, 0.8, 1.2, 0.7, 1],
    "Artes": [0.6, 1.2, 0.6, 1, 1.5],
    "Línguas": [0.6, 1.5, 0.6, 1, 1.2],
    "Psicologia": [0.8, 1, 0.8, 1.5, 1.2],
}

# Função para calcular o fitness
def calcular_fitness(notas, pesos):
    return round( sum(n * p for n, p in zip(notas, pesos)), 2)

# Criar um novo DataFrame para armazenar os resultados
resultados = pd.DataFrame(columns=["ID"] + list(pesos.keys()))
resultados["ID"] = data["ID"]

# Calcular o fitness para cada aluno e curso
for curso, curso_pesos in pesos.items():
    resultados[curso] = data.iloc[:, 1:].apply(lambda row: calcular_fitness(row, curso_pesos), axis=1)

# Salvar os resultados em um novo CSV
resultados.to_csv("fitness_alunos.csv", index=False)
