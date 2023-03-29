import pandas as pd
import numpy as np

# Define o número de alunos na base de dados
num_alunos = 5000

# Gera notas aleatórias, considerando 4 bimestres e 3 anos do ensino médio
np.random.seed(42)
ids = range(1, num_alunos + 1)

def gerar_notas(num_alunos, tipo_aluno):
    notas = []
    for _ in range(num_alunos):
        bimestres = 4
        anos = 3
        soma = 0
        for _ in range(bimestres * anos):
            if tipo_aluno == 'exatas':
                nota = np.random.randint(7, 11)  # Nota mínima 7 e máxima 10
            elif tipo_aluno == 'humanas':
                nota = np.random.randint(5, 9)  # Nota mínima 5 e máxima 10
            elif tipo_aluno == 'bom_em_tudo':
                nota = np.random.randint(7, 11)  # Nota mínima 8 e máxima 10
            else:  # tipo_aluno == 'ruim_em_tudo'
                nota = np.random.randint(5, 8)   # Nota mínima 5 e máxima 7
            soma += nota
        media = soma / (bimestres * anos)
        media_arredondada = round(media, 2)
        notas.append(media_arredondada)
    return np.array(notas)

# Define a distribuição dos alunos
num_alunos_bom_em_tudo = num_alunos_ruim_em_tudo = num_alunos // 10
num_alunos_restantes = num_alunos - num_alunos_bom_em_tudo - num_alunos_ruim_em_tudo
num_alunos_exatas = num_alunos_humanas = num_alunos_restantes // 2

# Gera notas para cada matéria e tipo de aluno
notas_matematica = gerar_notas(num_alunos, 'exatas')
notas_fisica = gerar_notas(num_alunos, 'exatas')
notas_biologia = gerar_notas(num_alunos, 'exatas')
notas_quimica = gerar_notas(num_alunos, 'exatas')
notas_lingua_portuguesa = gerar_notas(num_alunos, 'humanas')
notas_lingua_inglesa = gerar_notas(num_alunos, 'humanas')
notas_artes = gerar_notas(num_alunos, 'humanas')
notas_filosofia = gerar_notas(num_alunos, 'humanas')
notas_redacao = gerar_notas(num_alunos, 'humanas')
notas_historia = gerar_notas(num_alunos, 'humanas')
notas_geografia = gerar_notas(num_alunos, 'humanas')

# Embaralha os dados
embaralhar_indices = np.random.permutation(num_alunos)
# Embaralha os dados
notas_matematica = notas_matematica[embaralhar_indices]
notas_fisica = notas_fisica[embaralhar_indices]
notas_biologia = notas_biologia[embaralhar_indices]
notas_quimica = notas_quimica[embaralhar_indices]
notas_lingua_portuguesa = notas_lingua_portuguesa[embaralhar_indices]
notas_lingua_inglesa = notas_lingua_inglesa[embaralhar_indices]
notas_artes = notas_artes[embaralhar_indices]
notas_filosofia = notas_filosofia[embaralhar_indices]
notas_redacao = notas_redacao[embaralhar_indices]
notas_historia = notas_historia[embaralhar_indices]
notas_geografia = notas_geografia[embaralhar_indices]

# Cria um DataFrame com os dados gerados
dados = pd.DataFrame({'ID': ids,
                      'Matemática': notas_matematica,
                      'Física': notas_fisica,
                      'Biologia': notas_biologia,
                      'Química': notas_quimica,
                      'Língua Portuguesa': notas_lingua_portuguesa,
                      'Língua Inglesa': notas_lingua_inglesa,
                      'Artes': notas_artes,
                      'Filosofia': notas_filosofia,
                      'Redação': notas_redacao,
                      'História': notas_historia,
                      'Geografia': notas_geografia})

# Salva a base de dados em um arquivo CSV
dados.to_csv('dados_alunos_materias.csv', index=False)
print(dados)
