# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
#Nome=('Mário')
nome = input('Qual o teu nome? ')

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
#total_dias=(5)
total_dias = input('Quantos dias por semana estudas? ')

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
#total_horas=(8)
total_horas = input('Quantas horas por dia estudas? ')

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
#curso=('Iniciação a Python')
curso = input('Qual o nome do curso que estás a fazer? ')

total_horas = int(total_horas)
total_dias = int(total_dias)

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(f'O', nome, 'dedicou', total_dias, 'dias e', total_horas, 'horas a estudar para o curso', curso, 'totalizando', (total_dias*total_horas), 'semanais')