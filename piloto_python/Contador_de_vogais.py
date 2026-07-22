#coleta de dados
nome = input ('Digite seu nome: ').strip()

#Saida
print(f"Olá, >>{nome}<<")

#Resultado
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu nome tem {} letras a'.format(nome.count('a')))
print('Seu nome tem {} letras e'.format(nome.count('e')))
print('Seu nome tem {} letras i'.format(nome.count('i')))
print('Seu nome tem {} letras o'.format(nome.count('o')))
print('Seu nome tem {} letras u'.format(nome.count('u')))

#Descubra quantas vogais seu nome tem 😁 

