#Entrada
nome = input('Nome do estudante: ')
n1 = float(input('Primeira nota 0 a 10 :'))
n2 = float(input('Segunda nota 0 a 10 :'))
freq = float(input('Frequência (0 a 100%): '))
 
#Soma
media = (n1 + n2) / 2

#Condição
if freq < 75:
    situacao = 'Reprovado'
    motivo = 'frequência abaixo de 75%'
    
elif media < 5.0:
    situacao = 'Reprovado'
    motivo = 'média abaixo de 5.0'
    
elif media < 7.0:
    situacao = 'Recuperação'
    motivo = 'média entre 5.0 e 6.9'
    
else:
    situacao = 'Aprovado'
    motivo = 'requisitos atingidos'
    
#Motivos 

print(f'Aluno: {nome}')

print(f'Média: {media:.1f} | Frequência: {freq}% |')
print(f'Situação: |{situacao}| ({motivo})')