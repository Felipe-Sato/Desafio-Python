aluno1 = input('Entre com a nota do aluno 1: ')
aluno2 = input('Entre com a nota do aluno 2: ')
aluno3 = input('Entre com a nota do aluno 3: ')
aluno4 = input('Entre com a nota do aluno 4: ')
aluno5 = input('Entre com a nota do aluno 5: ')

dicionario = {"alunoA" : aluno1, "alunoB" : aluno2, "alunoC" : aluno3, "alunoD" : aluno4, "alunoE" : aluno5}
for chave,valor in dicionario.items():
    if valor == dicionario[max(dicionario, key=dicionario.get)]:
        break

print('Maior nota: ', valor, ' que e do aluno: ', chave)