import pandas as pd

def converter_binario(valor, n_bits):
    return format(int(valor), f'0{n_bits}b')

def codificar_binario(df, n_bits):
    df_codificado = df.copy()
    
    for col in df_codificado.columns:
        # Convertendo os valores em inteiros entre 0 e 1023
        min_val = df_codificado[col].min()
        max_val = df_codificado[col].max()
        df_codificado[col] = ((df_codificado[col] - min_val) / (max_val - min_val) * 1023).astype(int)

        # Convertendo os valores inteiros em binário
        df_codificado[col] = df_codificado[col].apply(lambda x: converter_binario(x, n_bits))
    
    return df_codificado

# Lendo o arquivo CSV
dados_alunos = pd.read_csv('dados_alunos.csv', delimiter=',')

# Removendo a coluna ID, pois ela não precisa ser convertida para binário
id_alunos = dados_alunos.pop('ID')

# Codificando os dados em binário com 10 bits
n_bits = 10
dados_binarios = codificar_binario(dados_alunos, n_bits)

# Adicionando a coluna ID novamente
dados_binarios.insert(0, 'ID', id_alunos)

# Salvando o DataFrame codificado em um novo arquivo CSV
dados_binarios.to_csv('dados_alunos_binarios.csv', index=False)
