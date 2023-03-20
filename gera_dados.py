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
                nota = np.random.randint(5, 11)  # Nota mínima 5 e máxima 10
            elif tipo_aluno == 'bom_em_tudo':
                nota = np.random.randint(8, 11)  # Nota mínima 8 e máxima 10
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

# Gera notas para cada tipo de aluno
notas_matematica = np.concatenate([
    gerar_notas(num_alunos_exatas, 'exatas'),
    gerar_notas(num_alunos_humanas, 'humanas'),
    gerar_notas(num_alunos_bom_em_tudo, 'bom_em_tudo'),
    gerar_notas(num_alunos_ruim_em_tudo, 'ruim_em_tudo')])

notas_linguagens = np.concatenate([
    gerar_notas(num_alunos_humanas, 'humanas'),
    gerar_notas(num_alunos_exatas, 'exatas'),
    gerar_notas(num_alunos_bom_em_tudo, 'bom_em_tudo'),
    gerar_notas(num_alunos_ruim_em_tudo, 'ruim_em_tudo')])

notas_ciencias_natureza = np.concatenate([
    gerar_notas(num_alunos_exatas, 'exatas'),
    gerar_notas(num_alunos_humanas, 'humanas'),
    gerar_notas(num_alunos_bom_em_tudo, 'bom_em_tudo'),
    gerar_notas(num_alunos_ruim_em_tudo, 'ruim_em_tudo')])

notas_ciencias_humanas = np.concatenate([
    gerar_notas(num_alunos_humanas, 'humanas'),
    gerar_notas(num_alunos_exatas, 'exatas'),
    gerar_notas(num_alunos_bom_em_tudo, 'bom_em_tudo'),
    gerar_notas(num_alunos_ruim_em_tudo, 'ruim_em_tudo')])


notas_redacao = np.concatenate([
    gerar_notas(num_alunos_humanas, 'humanas'),
    gerar_notas(num_alunos_exatas, 'exatas'),
    gerar_notas(num_alunos_bom_em_tudo, 'bom_em_tudo'),
    gerar_notas(num_alunos_ruim_em_tudo, 'ruim_em_tudo')])

# Embaralha os dados
embaralhar_indices = np.random.permutation(num_alunos)
notas_matematica = notas_matematica[embaralhar_indices]
notas_linguagens = notas_linguagens[embaralhar_indices]
notas_ciencias_natureza = notas_ciencias_natureza[embaralhar_indices]
notas_ciencias_humanas = notas_ciencias_humanas[embaralhar_indices]
notas_redacao = notas_redacao[embaralhar_indices]

# Cria um DataFrame com os dados gerados
dados = pd.DataFrame({'ID': ids,
                      'Matemática': notas_matematica,
                      'Linguagens': notas_linguagens,
                      'Ciências da Natureza': notas_ciencias_natureza,
                      'Ciências Humanas': notas_ciencias_humanas,
                      'Redação': notas_redacao})

# Salva a base de dados em um arquivo CSV
dados.to_csv('dados_alunos.csv', index=False)
print(dados)