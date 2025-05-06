# Crie uma lista apenas com elementos numéricos
numeros = [1, 2, 3, 4, 5]
print(numeros)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = ['Mário', 10, 7.5, 'Benfica', 38, 'Joana', 1999]
print(mista)

# Imprima na tela apenas os 5 primeiros elementos da lista
x = 5
print(mista[0:x])

# Crie um slice na lista para que imprima na tela os elementos de índice par
listanumeros = [1,2,3,4,5,6,7,8,9,10]
print(listanumeros[1:-1:2])

# Remova da lista o último item
mista.pop()
print(mista)

# Insira na lista um novo item
mista.append('Gandhi')
print(mista)


# Remova da lista um item específico
mista.remove(38)
print(mista)