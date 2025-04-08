while True : 
    idade = int(input('Digite sua idade: '))
    if idade <= 12:
        print('Você é uma criança')
    elif idade <  18:
        print('Você é um adolescente')
    elif idade <  70:
        print('Você é um adulto')
    else: 
        print('Você é um idoso')
    resposta = input('Deseja continuar? ')
    if resposta == 'sim':
        continue
    else:
        break
