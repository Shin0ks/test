
#Variaveis e bibliotecas

import requests 
import time 

api = '5ee47719292a3f7b495c60fbbb266d2b'

cidade = input('DIGITE O NOME DA SUA CIDADE : ')

#Aqui eu vou implementar o while true  ainda(caso digite errado ou algo do tipo) 

link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api}&lang=pt_br'

#verificação 

print('Verificando conexão...'), time.sleep(1.5)

#condição 
try:
	teste_api = requests.head('https://api.openweathermap.org', timeout=5)
	if teste_api.status_code >= 400 :
		print(f'Erro : (Status : {teste_api.status_code}).Tente novamente depois')
		exit()
except  requests.exceptions.Timeout:
    print("Erro: O serviço de clima demorou muito para responder (Timeout).")
    exit()
except requests.exceptions.RequestException:
    print("Erro: Não foi possível conectar à internet ou ao servidor de clima.")
    exit()
			
#Teste e coleta 

try :
       req = requests.get(link)
       req_dic = (req.json())
       
       if req_dic.get('cod') == '404' or  req_dic.get('cod') == '404':
       	print('Cidade não encontrada, ou digite corretamente')
       else : 
               desc =                req_dic['weather'] [0] ['description']
               temp = req_dic['main'] ['temp'] -273.15
               umid = req_dic['main'] ['humidity']
               
 #saida   
               print('-' *15)
               print(f'Cidade: {cidade.title()}')
               print(f'Clima: {desc.capitalize()}')
               print(f'Temperatura: {temp:.1f}°C')
               print(f'Umidade : {umid}')
               print('-' *15)
               
 #correção 
 
except Exception as erro:
    
    print(f"Ocorreu um erro inesperado {erro}")

#sometimes i dream of saving the world saving everyone from the invisible hand 🤖 
     
