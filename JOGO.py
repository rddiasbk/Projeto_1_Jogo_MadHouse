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
def main():
    print(F"{'MAD HOUSE':^40}")
    print('='*40)
    sleep(0.5)
    print(f'Vocês foram chamados ao Bureau de Pesquisas e Defesa Paranormal (B.P.D.P)')
    print(f'')
    comeco = (input('Quando quiser começar, digite a palavra jogar:'))
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
    print('#' * 30)
    for pos in range(0, len(char)):
        if pos % 2 == 0:
            print(f'{char[pos]:-<20}', end='')
        if pos % 2 != 0:
            print(f' {char[pos]:>6}')


# Caso o jogador morra
def jogador_morreu():
    slowprint('Mais uma vítima da casa!')
    endgame()


def endgame():
    resposta = (input('\n\nDigite J para jogar denovo! :')).upper().strip().split()[0]
    if resposta == 'J':
            main()
    else:
        print('Então tá, até a próxima.')


def character():     # ESCOLHA DO PERSONAGEM
    personagem = ' '
    confirmar = ' '
    while confirmar != 's':
        while personagem not in 'vba':
            opções('Vlad [V]\nBill [B]\nAbel [A]')
            personagem = str(input('Escolha um personagem acima:')).lower().strip().split()[0]
            confirmar = str(input('Confirma a escolha? [S/N]?:')).lower().strip().split()[0]
            if confirmar =='n':
                endgame()
            if personagem not in 'vba':
                print('Personagem não encontrado. Tente novamente!')
            if personagem == 'v':
                    # aprofundar rapidamente o personagem
                    print('Você escolheu Vlad!')
                    print('VLAD diz: Olá, eu sou Vlad e estou com pressa, vamos!')
            if personagem == 'a':
                    print('Você escolheu Abel!')
                    print('ABEL dizO que vocês querem de novo?! Ah.. Chego em breve!')
            if personagem == 'b':
                    print('Você escolheu Bill!')
                    print('BILL diz:...Vamos matar esse bicho!')


main()


def combate():
    vitoria = ' '
    while not vitoria == 1:
        monstro = randint(0, 10)
        ataque_arma = randint(0, 10)
        print(f'Seu tiro causou {ataque_arma} de dano')
        print(f'O monstro tinha uma defesa de {monstro}')
        if ataque_arma > monstro:
            print('Você acertou! Ganhou o jogo!')
            sleep(2)
            endgame()
        if monstro > ataque_arma:
            vitoria = 1
            print('Você errou!')
            print('Agora é a vez do monstro')
            sleep(2)
            monstro = randint(0, 10)
            ataque_arma = randint(0, 10)
        if monstro > ataque_arma:
            print(f'O monstro te atacou com {monstro} e sua defesa foi {ataque_arma}')
            vitoria = 1
            print('Ele te acertou!')
            sleep(1)
            slowprint('VOCÊ MORREU!')
        if ataque_arma > monstro:
            vitoria = 1
            print('Ele errou! Você tem uma nova chance!')
            sleep(2)


print('Você chega em uma casa escura e dentro dela se depara com portas diferentes.')
def doors():
    porta = ' '
    while porta not in 'var':
        opções('PORTA VERDE [V]\nPORTA AMARELA[A]\nPORTA ROXA[R]')
        porta = str(input('Escolha a porta:')).lower().strip().split()[0]
        if porta not in 'var':
            print('Isso não é uma porta. Tente novamente!')
    if porta == 'v':
        print('Você ouve o som do descarrilhar de correntes e sente uma dor intensa em seu abdomen! '
              '\nUma lança te atravessa! '
              '\nChegou seu fim!')
        jogador_morreu()
    if porta == 'a':
        print('Morreu!')
        jogador_morreu()
    if porta == 'r':
        print('Inimigo apareceu!')
        print('Você saca rapidamente e atira:')
        combate()
doors()





