
#Bibliotecas 
import string
import secrets

#Comando base
def gerar_senha(sen=10):
       
    caracteres = string.ascii_letters + string.digits + string.punctuation
        
    senha = "".join(secrets.choice(caracteres) for _ in range(sen))
    return senha

#Condição
if __name__ == "__main__":
    print('Criador de senha')
    
#loop    
    while True:
        try:
            tam = int(input('Digite um numero : ').strip())
            
            if tam < 10:
                print('Um numero maior que 10')
                continue 
                
            senha = gerar_senha(tam)
            print(f' Sua senha é : {senha}')
            break 
            
        except ValueError:
            print('Digite um número inteiro')