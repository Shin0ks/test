#Coleta de dados 
nome = input ('Qual o seu nome? ')
idade = input ('Qual a sua idade? ')
peso = float (input ('Qual o seu peso? '))
altura =  float (input ('Qual a sua altura? '))
   
#Calculadora 
imc = peso / (altura * altura )

#Resultado
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

#Calculadora imc bem básica e simples, precisa apenas colocar os dados  e já vai sair o resultado. 
#Lembrando que os padrões de imc são apenas estimativas de saúde, não levem a sério as classificações :). 
