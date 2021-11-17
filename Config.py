import random

import desc
import time


def player_died():
    slowprint('\033[31mMais uma vítima da casa!\033[0;0m')
def slowprint(texto, atraso=0.1):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(atraso)

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

