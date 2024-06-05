caminho_arq = 'dados.txt'
# Leitura arquivo
with open(caminho_arq, 'r') as arquivo:
    linhas = arquivo.readlines()

print("Conteudo original do arquivo:")
print(linhas)

# Modificacao da linha
linhas.append('\nEsta e uma nova linha...')

print("Conteudo alterado do arquivo:")
print(linhas)

with open(caminho_arq, 'w') as arquivo:
    arquivo.writelines(linhas)