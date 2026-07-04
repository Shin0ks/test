
#biblioteca 
import time
from inputimeout import TimeoutOccurred, inputimeout

#Desafio
print('Desarme a bomba')
print('Dica : salve as torres')
print('Você tem 9 segundos')

#Codigo
cod = '0711'

#Loop
for c in range(9, 0, -1):
    print(f'Contagem regressiva : {c}')
    try:        
        tentativa = inputimeout(
            prompt='Digite o codigo :', timeout=1.5
        )
        
#Condição
        if tentativa == cod:            
            print('Bomba desarmada com sucesso!')
            break
        else:
            print('Continue tentando')
    except TimeoutOccurred:       
        pass
else:
    print('O tempo acabou')
