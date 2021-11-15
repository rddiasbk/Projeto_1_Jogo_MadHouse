from random import randint
from time import sleep
import time
import desc
import abel_game
import vlad_game
import bill_game

vlad = ('Personagem 1:', 'Vlad Blackwood', 'Profissão:', 'Piloto', 'Experiência Paranormal:', 'Perseguido por Abissais',
        'Trauma:', 'A incompreensão do que aconteceu.')
bill = (
    'Personagem 2:', 'Bill Liechtenstein', 'Profissão:', 'Agricultor', 'Experiência Paranormal:', 'Viu um Lobisomem',
    'Trauma:', 'A morte do filho.')
abel = ('Personagem 3:', 'Abel ', 'Profissão:', 'Ladrão', 'Experiência Paranormal:', 'Viu um demônio.',
        'Trauma:', 'A morte de uma criança.')


# MENU
def main():
    print(chose_color('italico', f"{'MAD HOUSE':^80}"))
    print('=' * 80)
    sleep(0.5)
    print(f"{'Vocês foram chamados ao Bureau de Pesquisas e Defesa Paranormal (B.P.D.P)':^40}")
    print(f"{'Quando quiser começar, digite a palavra JOGAR:':^80}")
    print('')
    print(f"{'Senão, digite qualquer tecla para sair...':^80}")
    print('')
    comeco = (input(f"{'JOGAR??:':^80}")).lower().strip().split()[0]
    if comeco == 'jogar':
        print('_' * 30)
        print('Veja qual personagem você pode chamar:')
        print('_' * 30)
        character_chart(vlad)
        character_chart(bill)
        character_chart(abel)
        select_character()
    else:
        endgame()


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


def format_text_history(estilo, texto):
    print(chose_color('italico', (f"{texto:^80}")))


# JOGAR NOVAMENTE?
def endgame():
    resposta = (input('\n\nDigite J para jogar denovo ou digite qualquer tecla para sair! :')).lower().strip().split()[
        0]
    if resposta == 'j':
        main()
    else:
        print('Então tá, até a próxima.')


# FORMATAÇÃO DE UM TRECHO
def format_option(opc):
    print('-' * 40)
    print(opc)
    print('-' * 40)


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


def player_died():
    slowprint('\033[31mMais uma vítima da casa!\033[0;0m')
    endgame()


def select_character():  # ESCOLHA DO PERSONAGEM
    personagem = ' '
    confirmar = ' '
    sleep(1)
    while confirmar != 's':  # COMO TRANSFORMAR ESSA PERGUNTA DE CONFIRMAÇÃO EM DEF?
        while personagem not in 'vba':
            format_option('\033[1;97mVlad [V]\nBill [B]\nAbel [A]\033[0;0m')
            personagem = str(input('\033[1;97mEscolha um personagem acima:')).lower().strip().split()[0]
            confirmar = str(input('Confirma a escolha? [S/N]?:\033[0;0m')).lower().strip().split()[0]
            print('-' * 40)
            if confirmar == 'n':
                endgame()
            if personagem not in 'vba':
                print('Personagem não encontrado. Tente novamente!')
            if personagem == 'v':
                # aprofundar rapidamente o personagem
                print('\033[1;97m Você escolheu Vlad!')
                print('>>>>VLAD diz:...\033[0;0m', end='')
                print('Olá, eu sou Vlad e estou com pressa, vamos!')
                desc.description_road_to_madhouse()
                desc.description_front_propriety()
                vlad_game.chose_gate_or_jump_the_wall_vlad()
                vlad_game.vlad_chose_door_or_backyard()
                vlad_game.test_sanity_vlad()
                doors()
            elif personagem == 'a':
                print('\033[1;97m Você escolheu Abel!')
                print('>>>>ABEL diz:...\033[0;0m', end='')
                print('O que vocês querem de novo?! Ah.. Chego em breve!')
                desc.description_road_to_madhouse()
                desc.description_front_propriety()
                abel_game.abel_chose_garden_or_backyard()
            elif personagem == 'b':
                print('\033[1;97m Você escolheu Bill!')
                print('>>>>Bill diz:...\033[0;0m', end='')
                print('Vamos matar esse bicho!')
                desc.description_road_to_madhouse()
                desc.description_front_propriety()
                bill_game.chose_gate_or_jump_the_wall_bill()


def monster_attack():
    monstro = randint(0, 10)
    ataque_personagem = randint(0, 10)
    print(f'O monstro tinha um ataque de {monstro}')
    print(f'Sua defesa é {ataque_personagem}')
    if monstro > ataque_personagem:
        print('O monstro errou')
        sleep(1.5)
        print('Agora é a sua vez')
        sleep(1.5)
        monster_attack()
    if ataque_personagem == monstro:
        print('Essa foi por pouco!')
        print('Você atira novamente!')
    if ataque_personagem > monstro:
        print('Você acertou! ')
        print('\033[1;33mGANHOU O JOGO!!!\033[0;0m')
        sleep(1.5)
        endgame()


def final_battle():
    monster_attack()
    vlad_game.vlad_attack()


def doors():
    print('Apesar do a escuridão que toma o resto da casa você se depara com 3 portas diferentes.')
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
            player_died()
        if porta == 'a':
            print('As portas se trancam atrás de você! A sala é preenchida por gás.')
            slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
            print(' ')
            player_died()
        if porta == 'r':
            print('Inimigo apareceu!')
            desc.description_boss()
            print('Você saca rapidamente e atira:')
            vlad_game.vlad_attack()
            sleep(1)
        if porta not in 'var':
            print('Isso não é uma porta. Tente novamente!')


main()
