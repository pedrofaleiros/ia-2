import pandas as pd

# Leitura dos dados do CSV
data = pd.read_csv("dados_alunos_materias.csv")

# Pesos para os cursos
# 1 - Matemática       2 - Física   3 - Biologia    4 - Química   5 - Língua Portuguesa
# 6 - Língua Inglesa   7 - Artes    8 - Filosofia   9 - Redação   10 - História    11 - Geografia
pesos = {
    "exatas": [1.5, 1.5, 1.5, 1.5, 1, 0.5, 0.5, 0.5, 1, 0.5, 0.5],
    "humanas": [0.5, 0.5, 0.5, 0.5, 1.5, 0.5, 1, 1.5, 1.5, 2, 2],
    'TI': [2, 2, 0.5, 1, 1, 1, 0.5, 0.5, 1, 0.5, 0.5],
    'saude': [1, 0.5, 2, 1.5, 1, 0.5, 0.5, 1, 1, 0.5, 0.5]
}

# Função para calcular o fitness


def calcular_fitness(notas, pesos):
    return round(sum(n * p for n, p in zip(notas, pesos)), 2)


# Criar um novo DataFrame para armazenar os resultados
resultados = pd.DataFrame(columns=["ID"] + list(pesos.keys()))
resultados["ID"] = data["ID"]

# Calcular o fitness para cada aluno e curso
for curso, curso_pesos in pesos.items():
    resultados[curso] = data.iloc[:, 1:].apply(
        lambda row: calcular_fitness(row, curso_pesos), axis=1)

# Salvar os resultados em um novo CSV
resultados.to_csv("fitness_alunos.csv", index=False, sep=',')
