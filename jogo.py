import random

def jogar():
    usuario = input('\'pe\' para pedra\n\'pa\' para papel\n\'te\' para tesoura\nQual a sua jogada? ')
    usuario = usuario.lower()
    computador = random.choice(['pe', 'pa', 'te'])
    if usuario not in ['pe', 'pa', 'te']:
        print('Jogada inválida!')
    if usuario == computador: 
        print('EMPATE!')
    elif usuario == 'pe':
        if computador == 'pa':
            print(f'Você: pedra\nComputador:papel\nResultado: COMPUTADOR VENCEU!')
        elif computador == 'te':
            print(f'Você: pedra\nComputador: tesoura\nResultado: VOCÊ VENCEU!')
    elif usuario == 'pa':
        if computador == 'pe':
            print(f'Você: papel\nComputador:pedra\nResultado: VOCÊ VENCEU!')
        elif computador == 'te':
            print(f'Você: papel\nComputador: tesoura\nResultado: COMPUTADOR VENCEU!')
    elif usuario ==  'te':
        if computador == 'pe':
            print(f'Você: tesoura\nComputador:pedra\nResultado: COMPUTADOR VENCEU!')
        elif computador == 'pa':
            print(f'Você: tesoura\nComputador: papel\nResultado: VOCÊ VENCEU!')

partidas = int(input('Quantidas partidas você quer jogar? '))
for i in range(partidas):
    print('====='*5)
    jogar()