from random import randint
from time import sleep
#formatação de apresentação dos personagens
import time

# APRESENTAÇÃO DO PERSONAGEM
vlad = ('Personagem 1:', 'Vlad Blackwood', 'Profissão:', 'Piloto', 'Experiência Paranormal:', 'Perseguido por Abissais',
        'Trauma:', 'A incompreensão do que aconteceu.')
bill = ( 'Personagem 2:', 'Bill Liechtenstein', 'Profissão:', 'Agricultor', 'Experiência Paranormal:', 'Viu um Lobisomem',
'Trauma:', 'A morte do filho.')
abel = ('Personagem 3:', 'Abel ', 'Profissão:', 'Ladrão', 'Experiência Paranormal:', 'Viu um demônio.',
        'Trauma:', 'A morte de uma criança.')
def endgame():
    resposta = (input('\n\nDigite J para jogar denovo! :')).upper().strip().split()[0]
    if resposta == 'J':
            main()
    else:
        print('Então tá, até a próxima.')
def main():
    print(f"{'MAD HOUSE':^80}")
    print('='*80)
    sleep(0.5)
    print(f"{'Vocês foram chamados ao Bureau de Pesquisas e Defesa Paranormal (B.P.D.P)':^40}")
    print(f"{'Quando quiser começar, digite a palavra JOGAR:':^80}")
    print('')
    print(f"{'Senão, digite qualquer tecla...':^80}")
    print('')
    comeco = (input(f"{'JOGAR??:':^80}")).lower().strip().split()[0]
    if comeco == 'jogar':
        print('_' * 30)
        print('Veja qual personagem você pode chamar:')
        print('_' * 30)
        tabela(vlad)
        tabela(bill)
        tabela(abel)
        character()
    else:
        endgame()
def opções(opc):
    print('*' * 30)
    print(opc)
    print('*' * 30)

def slowprint(texto, atraso=0.1):
  for c in texto:
    print(c,end='',flush=True)
    time.sleep(atraso)

# APRESENTAÇÃO DA TABELA DE PERSONAGENS
def tabela(char):
    sleep(1.5)
    print('#' * 30)
    for pos in range(0, len(char)):
        if pos % 2 == 0:
            print(f'\033[1;97m {char[pos]:-<20}\033[0;0m', end='')
        if pos % 2 != 0:
            print(f' {char[pos]:>6}')


# Caso o jogador morra
def jogador_morreu():
    slowprint('\033[31m Mais uma vítima da casa!\033[0;0m')
    endgame()


def character():     # ESCOLHA DO PERSONAGEM
    personagem = ' '
    confirmar = ' '
    sleep(1.5)
    while confirmar != 's':
        while personagem not in 'vba':
            opções('\033[1;97mVlad [V]\nBill [B]\nAbel [A]\033[0;0m')
            personagem = str(input('\033[1;97mEscolha um personagem acima:')).lower().strip().split()[0]
            confirmar = str(input('Confirma a escolha? [S/N]?:\033[0;0m')).lower().strip().split()[0]
            if confirmar =='n':
                endgame()
            if personagem not in 'vba':
                print('Personagem não encontrado. Tente novamente!')
            if personagem == 'v':
                    # aprofundar rapidamente o personagem
                    print('\033[1;97m Você escolheu Vlad!\033[0;0m')
                    print('\033[1;92mVLAD diz: Olá, eu sou Vlad e estou com pressa, vamos!\033[0;0m')
            if personagem == 'a':
                    print('\033[1;97m Você escolheu Abel!\033[0;0m')
                    print('\033[0;0mABEL diz: O que vocês querem de novo?! Ah.. Chego em breve!\033[0;0m')
            if personagem == 'b':
                    print('\033[1;97m Você escolheu Bill!')
                    print('\033[0;0mBILL diz:...Vamos matar esse bicho!\033[0;0m')


main()


def combate():
    vitoria = ' '
    while not vitoria == 1:
        monstro = randint(0, 10)
        ataque_arma = randint(0, 10)
        print(f'Seu tiro causou {ataque_arma} de dano')
        print(f'O monstro tinha uma defesa de {monstro}')
        if ataque_arma > monstro:
            print('Você acertou! ')
            print('\033[1;33m GANHOU O JOGO!!!\033[0;0m')
            sleep(2)
            endgame()
        if monstro > ataque_arma:
            vitoria = 1
            print('Você errou!')
            sleep(1.5)
            print('Agora é a vez do monstro')
            sleep(2)
            monstro = randint(0, 10)
            ataque_arma = randint(0, 10)
        if monstro > ataque_arma:
            print(f'O monstro te atacou com {monstro} e sua defesa foi {ataque_arma}')
            vitoria = 1
            sleep(1.5)
            print('Ele te acertou!')
            sleep(1.5)
            slowprint('\033[1;31mVOCÊ MORREU!')
        if ataque_arma > monstro:
            vitoria = 1
            sleep(1.5)
            print('Ele errou! Você tem uma nova chance!')
            sleep(2)
            combate()


print('\033[1;97m Você chega em uma casa escura e dentro dela se depara com portas diferentes.')
def doors():
    porta = ' '
    while porta not in 'var':
        print('\033[1;97m>'*10,'\033[1;32mPORTA VERDE [V]\033[0;0m')
        print('\033[1;97m>'*10,'\033[1;33mPORTA AMARELA [A]\033[0;0m')
        print('\033[1;97m>'*10,'\033[1;35mPORTA ROXA [R]\033[0;0m')
        print('')
        porta = str(input('\033[1;97mEscolha a porta:\033[0;0m')).lower().strip().split()[0]
        if porta not in 'var':
            print('Isso não é uma porta. Tente novamente!')
        if porta == 'v':
            print('Você ouve o som do descarrilhar de correntes e sente uma dor intensa em seu abdomen! '
                  '\nUma lança te atravessa! '
                  '\nChegou seu fim!')
            slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
            jogador_morreu()
        if porta == 'a':
            print('As portas se trancam atrás de você! A sala é preenchida por gás')
            slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
            print(' ')
            jogador_morreu()
        if porta == 'r':
            print('Inimigo apareceu!')
            print('Você saca rapidamente e atira:')
            sleep(1.5)
            combate()
doors()





