import math #Bilbioteca de operacoes matematicas

n = 10  #Dimensao do vetor
X = []  #Inciando o vetor vazio
temp = 0    #Variavel auxiliar para o vetor
soma = 0    #Variavel para soma dos elementos do vetor

for i in range(n):
    if(i%2 == 0):
        temp = (3^i) + 7*(math.factorial(i))
    else:
        temp = (2^i) + 4*(math.log(i))
    soma += temp
    X.insert(i, temp)

pos = X.index(max(X))
print('Indice do maior elemento no vetor: ', pos,' Valor: ', X[pos])
print('A media do vetor: ', round(soma/n,2))