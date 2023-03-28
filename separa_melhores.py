import pandas as pd
import numpy as np

# Ler os dados do arquivo fitness_alunos.csv
resultados = pd.read_csv("fitness_alunos.csv")

# Encontrar o curso com melhor fitness para cada aluno
melhor_curso = resultados.iloc[:, 1:].apply(lambda row: row.index[np.argmax(row.values)], axis=1)

# Criar um novo DataFrame com os resultados
melhores_cursos = pd.DataFrame({"ID": resultados["ID"], "Melhor Curso": melhor_curso})

# Salvar os resultados em um novo CSV
melhores_cursos.to_csv("melhores_cursos_alunos.csv", index=False)
