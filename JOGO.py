from random import randint

#formatação de apresentação dos personagens
def opções(opc):
    print('*' * 30)
    print(opc)
    print('*' * 30)


def character():     # ESCOLHA DO PERSONAGEM
    personagem = ' '
    confirmar = ' '
    while confirmar != 's':
        while personagem not in 'vba':
            opções('Vlad [V]\nBill [B]\nAbel [A]')
            personagem = str(input('Escolha uma das opções:')).lower().strip().split()[0]
            confirmar = str(input('Confirma a escolha? [S/N]?:')).lower().strip().split()[0]
            if personagem not in 'vba':
                print('Personagem não encontrado. Tente novamente!')
    if personagem == 'v':
        #aprofundar rapidamente o personagem
        print('Olá, eu sou Vlad e estou com pressa, vamos!')
    if personagem == 'a':
        print('O que vocês querem de novo?! Ah.. Chego em breve!')
    if personagem == 'b':
        print('...alguma novidade no meu caso?')


def main():
    print(F"{'MAD HOUSE':^40}")
    print('='*40)
    print(f'Vocês foram chamados ao Bureau de Pesquisas e Defesa Paranormal (B.P.D.P)')

    comeco = (input('Quando quiser começar, digite a palavra jogar:'))
    if comeco == 'jogar':
        character()
    else:
        print('Até logo então :)')


main()


print('_' * 30)
print('Veja quem você pode chamar:')
print('_' * 30)
# APRESENTAÇÃO DO PERSONAGEM
vlad = ('Personagem 1:', 'Vlad Blackwood', 'Profissão:', 'Piloto', 'Experiência Paranormal:', 'Perseguido por Abissais',
        'Trauma:', 'A incompreensão do que aconteceu.')
bill = ( 'Personagem 2:', 'Bill Liechtenstein', 'Profissão:', 'Agricultor', 'Experiência Paranormal:', 'Viu um Lobisomem',
'Trauma:', 'A morte do filho.')
abel = ('Personagem 3:', 'Abel ', 'Profissão:', 'Ladrão', 'Experiência Paranormal:', 'Viu um demônio.',
        'Trauma:', 'A morte de uma criança.')


# APRESENTAÇÃO DA TABELA DE PERSONAGENS
def tabela(char):
    print('#' * 30)
    for pos in range(0, len(char)):
        if pos % 2 == 0:
            print(f'{char[pos]:-<20}', end='')
        if pos % 2 != 0:
            print(f' {char[pos]:>6}')

tabela(vlad)
tabela(bill)
tabela(abel)

# Caso o jogador morra
def jogador_morreu():
    print('Mais uma vítima da casa!')
    resposta = (input('Game Over!\n\nDigite J para jogar denovo! :'))
    if resposta == 'j':
        main()
    else:
        print('Então tá, até a próxima.')


character()
print('Você chega em uma casa escura e dentro dela se depara com portas diferentes.')
def doors():
    porta = ' '
    while porta not in 'var':
        opções('PORTA VERDE [V]\nPORTA AMARELA[A]\nPORTA ROXA[R]')
        porta = str(input('Escolha a porta:')).lower().strip().split()[0]
        if porta not in 'var':
            print('Isso não é uma porta. Tente novamente!')
    if porta == 'v':
        print('Morreu!')
    if porta == 'a':
        print('Morreu!')
    if porta == 'r':
        print('Inimigo apareceu!')
doors()

print('Você saca rapidamente e atira:')


def combate():
    vitoria = ' '
    while not vitoria == 0 or vitoria == 1:
        monstro = randint(0, 10)
        ataque_arma = randint(0, 10)
        print(f'Seu tiro causou {ataque_arma} de dano')
        print(f'O monstro tinha uma defesa de {monstro}')
        if ataque_arma > monstro:
            print('Você acertou! Ganhou o jogo!')
            vitoria = 1
        elif monstro > ataque_arma:
            vitoria = 0
            print('Você errou!')
            print('Agora é a vez do monstro')
        monstro = randint(0, 10)
        ataque_arma = randint(0, 10)
        if monstro > ataque_arma:
            print(f'O monstro te atacou com {monstro} e sua defesa foi {ataque_arma}')
            vitoria = 0
            print('Ele te acertou! Você morreu!')
        elif ataque_arma > monstro:
            vitoria = 1
            print('Ele errou! Você tem uma nova chance!')
combate()
