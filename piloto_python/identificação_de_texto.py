#Coleta de dados
print('Identificador de palavra')
txt = str(input('Cole o texto :').strip())

#Colocar oq quer verificar
print ('Seu texto tem linux ? {}'.format('linux' in txt.lower()))
