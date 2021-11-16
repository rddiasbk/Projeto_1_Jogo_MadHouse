import time
import abel_game
import vlad_game
import bill_game
import Config


def print_msg_start_game():
    print(chose_color('italico', f"{'MAD HOUSE':^80}"))
    print('=' * 80)
    time.sleep(0.5)
    print(f"{'Vocês foram chamados ao Bureau de Pesquisas e Defesa Paranormal (B.P.D.P)':^40}")
    print(f"{'Quando quiser começar, digite a palavra JOGAR:':^80}")
    print('')

    print('_' * 30)
    print('Veja qual personagem você pode chamar:')
    print('_' * 30)

def print_line():
    print('-' * 40)

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


#def format_text_history(estilo, texto):
    #print(chose_color('italico', (f"{texto:^80}")))


def format_option(opc):
    print('-' * 40)
    print(opc)
    print('-' * 40)


def final_battle():
    Config.monster_attack()
    Config.character_attack()


def print_question_want_to_start(mensagem):
    pergunta = ''
    jogo = ''
    começar = input(mensagem).lower().strip()
    if começar == 's':
        pergunta = False
        pergunta = False
        jogo = True

        return pergunta, jogo

    elif começar == 'n':
        pergunta = False
        jogo = False
        print('Então tá, até a próxima.')
        return pergunta, jogo

    else:
        pergunta = True
        jogo = True
        print("Você digitou errado")
        return pergunta, jogo


def select_character():
    personagem = ' '
    confirmar = ' '
    time.sleep(1)
    while personagem not in 'vba':
            format_option('\033[1;97mVlad [V]\nBill [B]\nAbel [A]\033[0;0m')
            personagem = str(input('\033[1;97mEscolha um personagem acima:')).lower().strip().split()[0]
            #confirmar = str(input('Confirma a escolha? [S/N]?:\033[0;0m')).lower().strip().split()[0]
            print('-' * 40)
            if personagem == 'v':
                vlad_game.play()
                return False

            if personagem == 'a':
                abel_game.play()
                return False

            if personagem == 'b':
                bill_game.play()
                return False
            if personagem == 'n':
                select_character()
            else:
                print('Personagem não encontrado. Tente novamente!')
                return True


def print_character_chart():
    personagens = (vlad_game, bill_game, abel_game)
    for personagem in personagens:
        personagem.chart()


def play():
    jogo = True
    while jogo:

        print_msg_start_game()

        pergunta_começar = True
        while pergunta_começar:
            pergunta_começar, jogo = print_question_want_to_start("Deseja começar [S/N]? ")

        if jogo == True:
            print_character_chart()

        personagem = jogo
        while personagem:
            personagem = select_character()

        pergunta = jogo
        while pergunta:
            pergunta, jogo = print_question_want_to_start('\nDeseja jogar novamente [S/N]? ')

play()