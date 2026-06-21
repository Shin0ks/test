
#Variaveis e biblioteca
import requests 
from dotenv import dotenv_values

#Chaves 
token = dotenv_values(".env")
token = token["TOKEN"]

#Loop 
while True:
    cidade = input('Digite o nome da sua cidade: ')
    
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={token}&lang=pt_br'
    
 #Teste com o servidor     
    print('Verificando conexão...') 

    try:
        teste_api = requests.head('https://api.openweathermap.org', timeout=5)
        if teste_api.status_code >= 400:
            print(f'Erro no servidor (Status : {teste_api.status_code}')
            continue 
            
    except requests.exceptions.Timeout:
        print("Erro: O serviço de clima demorou  (Timeout). Tente novamente.")      
        continue
       
#Usuario sem conexão
    except requests.exceptions.RequestException:
        print('Erro: Não foi possível conectar à internet')
        break       

#Teste de conexão
    try:
        req = requests.get(link)
        req_dic = req.json()

        if str(req_dic.get('cod')) == '404':
            print('Tente de novo')
            continue 

#coleta dos dados         
        else: 
            desc = req_dic['weather'][0]['description']
            temp = req_dic['main']['temp'] - 273.15
            umid = req_dic['main']['humidity']
                   
#Como vai aparecer 
            print('-' * 25)
            print(f'Cidade: {cidade.title()}')
            print(f'Clima: {desc.capitalize()}')
            print(f'Temperatura: {temp:.1f}°C')
            print(f'Umidade: {umid}%')
            print('-' * 25)
            break
                   
#Tratar os erros               
    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')
        
