import random

import desc
import time


def chose_color(cor, texto):
    if cor == 'red':
        return f'\033[91m {texto} \033[0m'

    if cor == 'blue':
        return f'\033[94m {texto} \033[0m'

    if cor == 'yellow':
        return f'\033[93m {texto} \033[0m'

    if cor == 'green':
        return f'\033[92m {texto} \033[0m'

    if cor == 'white':
        return f'\033[1;97m {texto} \033[0m'

    if cor == 'italico':
        return f'\33[3m {texto} \033[0;0m'


def format_text_history(chose_color, texto):
    print(chose_color('italico', (f"{texto:^80}")))


# FORMATAÇÃO DE UM TRECHO




# TEXTO LENTO
def slowprint(texto, atraso=0.1):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(atraso)






def character_attack():
    monstro = random.randint(0, 10)
    ataque_personagem = random.randint(0, 10)
    print(f'Seu tiro causou {ataque_personagem} de dano')
    print(f'O monstro tinha uma defesa de {monstro}')
    if ataque_personagem > monstro:
        print('Você acertou! ')
        print('\033[1;33mGANHOU O JOGO!!!\033[0;0m')
        time.sleep(1.5)
    if ataque_personagem == monstro:
        print('Essa foi por pouco!')
        print('Você atira novamente!')
        character_attack()
    elif monstro > ataque_personagem:
        print('Você errou!')
        time.sleep(1.5)
        print('Agora é a vez do monstro')
        time.sleep(1.5)
        monster_attack()


def monster_attack():
    monstro = random.randint(0, 10)
    ataque_personagem = random.randint(0, 10)
    print(f'O monstro tinha um ataque de {monstro}')
    print(f'Sua defesa é {ataque_personagem}')
    if monstro > ataque_personagem:
        print('O monstro errou')
        time.sleep(1.5)
        print('Agora é a sua vez')
        time.sleep(1.5)
        monster_attack()
    if ataque_personagem == monstro:
        print('Essa foi por pouco!')
        print('Você atira novamente!')
    if ataque_personagem > monstro:
        print('Você acertou! ')
        print('\033[1;33mGANHOU O JOGO!!!\033[0;0m')
        time.sleep(1.5)


def doors():
    print('''Você olha desesperado e nota 3 portas diferentes.
        Você sabe que toda a verdade se revelará atrá de uma daquelas portas. 
        Chegou a hora!''')
    # time.sleep(1.5)
    print('Escolha uma porta:')
    porta = ' '
    while porta not in 'var':
        print('\033[1;97m>' * 10, '\033[1;32mPORTA VERDE [V]\033[0;0m')
        print('\033[1;97m>' * 10, '\033[1;33mPORTA AMARELA [A]\033[0;0m')
        print('\033[1;97m>' * 10, '\033[1;35mPORTA ROXA [R]\033[0;0m')
        print('')
        porta = str(input('\033[1;97mEscolha a porta:\033[0;0m')).lower().strip().split()[0]
        print('-' * 40)
        if porta == 'v':
            print('Você ouve o som do descarrilhar de correntes e sente uma dor intensa em seu abdomen! '
                  '\nUma lança te atravessa! '
                  '\nChegou seu fim!')
            slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
            print(' ')

        if porta == 'a':
            print('As portas se trancam atrás de você! A sala é preenchida por gás.')
            slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
            print(' ')

        if porta == 'r':
            print('Inimigo apareceu!')
            desc.description_boss()
            print('Você saca rapidamente e atira:')
            character_attack()
            time.sleep(1)
        if porta not in 'var':
            print('Isso não é uma porta. Tente novamente!')


def character_chart(char):
    # sleep(1.5)
    print('#' * 30)
    for pos in range(0, len(char)):
        if pos % 2 == 0:
            print(f'\033[1;97m {char[pos]:-<20}\033[0;0m', end='')
        if pos % 2 != 0:
            print(f' {char[pos]:>6}')



def get_value(cor='red'):
    texto = "Digite um dos valores aceitos: "
    return input(chose_color(cor, texto)).lower().strip()

