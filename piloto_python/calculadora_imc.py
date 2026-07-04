#Coleta de dados 
nome = input ('Qual o seu nome? ')
idade = input ('Qual a sua idade? ')
peso = float (input ('Qual o seu peso? '))
altura =  float (input ('Qual a sua altura? '))
   
#Calculadora 
imc = peso / (altura * altura )

#resultado
print (f'IMC: {imc:.2f}')

#Definir imc 
if imc <=18.5: 
   print ('raquitismo') 
   
elif 18.5 <= imc < 25:
	print ('normal')
	 
elif 25<= imc <30:
    print ('gordo') 
else: 
   print ('vai morrer')