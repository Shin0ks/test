
#Base
def obter_resposta(pergunta):
    while True:
        try:
            valor = int(input(f'{pergunta} (0-3): '))
            if 0 <= valor <= 3:
                return valor
            print(' Digite um número entre 0 e 3.')
        except ValueError:
            print(' Entrada inválida. Digite um número inteiro.')

def classificar_nivel(pontuacao, tipo):
 
 #Dicionário
    escalas = {
        'depressao': {9: 'Normal', 13: 'Leve', 20: 'Moderado', 27: 'Grave'},
        'ansiedade': {7: 'Normal', 9: 'Leve', 14: 'Moderado', 19: 'Grave'},
        'estresse': {14: 'Normal', 18: 'Leve', 25: 'Moderado', 33: 'Grave'}
    }
    
    escala_atual = escalas[tipo]
    
    for limite, nivel in escala_atual.items():
        if pontuacao <= limite:
            return nivel
    return 'Extremamente Grave'

#Como funciona
def aplicar_formulario(perguntas):
    print('\n' + '='*40)
    print('Responds com  0 A 3')
    print('='*40)
    print('0 = Não se aplicou de modo nenhum a mim')
    print('1 = Aplicou-se a mim algumas vezes')
    print('2 = Aplicou-se a mim boa parte do tempo')
    print('3 = Aplicou-se a mim a maior parte do tempo\n')
    
    respostas = {}
    for i, pergunta in enumerate(perguntas, start=1):
        respostas[f"S{i}"] = obter_resposta(f"Questão {i}: {pergunta}")
    return respostas

def calcular_e_exibir_resultados(respostas):
    
#Metodo da  soma
    itens_depressao = ["S3", "S5", "S10", "S13", "S16", "S17", "S21"]
    itens_ansiedade = ["S2", "S4", "S7", "S9", "S15", "S19", "S20"]
    itens_estresse = ["S1", "S6", "S8", "S11", "S12", "S14", "S18"]

    depressao = sum(respostas[p] for p in itens_depressao) * 2
    ansiedade = sum(respostas[p] for p in itens_ansiedade) * 2
    estresse = sum(respostas[p] for p in itens_estresse) * 2

#Saida    
    print('RESULTADO')
    
    print(f'Depressão: {depressao:02d} | Nível: {classificar_nivel(depressao, "depressao")}')
    
    print(f'Ansiedade: {ansiedade:02d} | Nível: {classificar_nivel(ansiedade, "ansiedade")}')
    
    print(f'Estresse:  {estresse:02d} | Nível: {classificar_nivel(estresse, "estresse")}')
    
#Observação :)    
    print('Este aplicativo não substitui um diagnóstico profissional.')
    print('Em caso de dúvidas procure ajuda (188).')


# As 21 perguntas 
list_perg = [
    'Achei difícil me acalmar.',
    'Senti minha boca seca.',
    'Não consegui vivenciar nenhum sentimento positivo.',
    'Tive dificuldade em respirar (ex. respiração rápida, falta de ar).',
    'Achei difícil tomar a iniciativa para fazer as coisas.',
    'Tive a tendência a reagir de forma exagerada às situações.',
    'Senti tremores (ex. nas mãos).',
    'Senti que estava sempre nervoso.',
    'Preocupe-me com situações em que eu pudesse entrar em pânico e parecer ridículo.',
    'Senti que não tinha nada a esperar do futuro.',
    'Senti-me agitado.',
    'Achei difícil relaxar.',
    'Senti-me abatido e melancólico.',
    'Fui intolerante com as coisas que me impediam de continuar o que estava fazendo.',
    'Senti que estava prestes a entrar em pânico.',
    'Senti-me incapaz de me entusiasmar com nada.',
    'Senti que não tinha muito valor como pessoa.',
    'Senti que estava um pouco emotivo/sensível demais.',
    'Senti os batimentos do meu coração acelerados sem esforço físico.',
    'Senti medo sem motivo aparente.',
    'Senti que a vida não tinha sentido.'
]

# Execução do programa
if __name__ == "__main__":
    dados_coletados = aplicar_formulario(list_perg)
    calcular_e_exibir_resultados(dados_coletados)
