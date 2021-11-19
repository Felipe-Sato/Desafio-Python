A = 2           #1a Condicao
B = 49          #2a Condicao
C = 37          #3a Condicao
Contador = 0    #Variavel de Resposta

#Vetor com os valores pares, i.e. multiplos de 2
X = range(2,5000000,2)

#Loop para verificar o vetor
for i in X:
    if i % B == 0 and i % C == 0:
        Contador = Contador + 1
    
print(Contador) #Impressao da resposta