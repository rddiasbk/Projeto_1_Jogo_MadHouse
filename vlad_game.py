import desc
import time
import random
import Config


def vlad_says_hello():
    print('\033[1;97m Você escolheu Vlad!')
    print('>>>>VLAD diz:...\033[0;0m', end='')
    print('Olá, eu sou Vlad e estou com pressa, vamos!')


def chose_gate_or_jump_the_wall_vlad():
    print('  Você olha ao redor e precisa tomar a primeira decisão: Entrar pelo horripilante portão central ou procurar'
          ' outro caminho')
    caminho = ' '
    while caminho not in 'pm':
        caminho = str(input(
            '\033[1;97mDigite P para entrar pelo PORTÃO ou M para pular o MURO [P/M]:\033[0;0m')).lower().strip().split()[
            0]
        if caminho == 'p':
            print('Você empurra devagar o grande portão de ferro.')
            desc.description_mansion()
        if caminho == 'm':  # MURO
            print('Você decide sair do óbvio e procura um lugar para pular o muro e ter acesso ao quintal')
            desc.description_burzum_on_the_wall()
            desc.description_backyard()
            vlad_garden_conflit()



def vlad_chose_door_or_backyard():
    caminho = ' '
    while caminho not in 'pc':
        # description_mansion
        caminho = str(input(
            f'\033[1;97m Digite P para entrar pela PORTA CENTRAL ou C para circular a casa [P/C]:\033[0;0m')).lower().strip().split()[0]
        if caminho == 'p':  # PORTA PRINCIPAL
            desc.description_main_door()
            test_sanity_vlad()


        if caminho == 'c':
            desc.description_backyard()
            vlad_garden_conflit()


def test_sanity_vlad():
    print('Ao pisar no interior da casa, cenas do horror que você viu naquela ilha voltam à tona.')
    print('Você lembra do sangue, do medo, do horror. Do horror.')
    print('Seria possível resistir mais uma vez a esta visão?')
    print('Sua sanidade será testada contra o poder de loucura da mansão.')
    print('Seu ceticismo te dá uma resistência de [100] contra [100] da casa')
    loucura = random.randint(0, 100)
    sanidade = random.randint(0, 100)
    time.sleep(1.5)
    print(f'Sua crença no método científico te da uma resistência {sanidade}')
    print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura}')
    if sanidade >= loucura:
        print('Você resistiu! Você sabia que sua crença na razão seria maior! ')
        time.sleep(2)
        print('Você vai logo para dentro da casa')
        Config.doors()
    elif loucura > sanidade:
        print('Você sucumbiu!')
        print('Infiel')
        Config.slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
        time.sleep(1.5)


def vlad_garden_conflit():
    print('Então algo surge dos arbustos e pula em você!')
    print('Você desvia rapidamente!')
    print('A pequena criatura emite um ganido!')
    print('Você saca rapidamente e atira.')
    monstrinho = random.randint(0, 10)
    ataque_personagem = random.randint(0, 15)
    print(f'Seu tiro causou {ataque_personagem} de dano')
    print(f'O monstro tinha uma defesa de {monstrinho}')
    if ataque_personagem > monstrinho:
        print('Você acertou e foi o fim da criatura!')
        print('É melhor entrar de vez na casa!')
        time.sleep(2)
        Config.doors()
    if monstrinho > ataque_personagem:
        print('Você errou!')
        time.sleep(1.5)
        print('Agora é a vez da aberração!')
        time.sleep(2)
    if monstrinho > ataque_personagem:
        print(f'O monstro te atacou com {monstrinho} e sua defesa foi {ataque_personagem}')
        time.sleep(1.5)
        print('Ele te acertou!')
        time.sleep(1.5)
        Config.slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
    '''if ataque_personagem > monstrinho:
        time.sleep(1.5)
        print('Ele errou! Você não arrisca e corre!')
        time.sleep(2)'''


def format_text_history(chose_color, texto):
    print(chose_color('italico', (f"{texto:^80}")))


# FORMATAÇÃO DE UM TRECHO
def format_option(opc):
    print('-' * 40)
    print(opc)
    print('-' * 40)


def chart():
    personagem = (
        'Personagem 1:', 'Vlad Blackwood', 'Profissão:', 'Piloto', 'Experiência Paranormal:', 'Perseguido por Abissais',
        'Trauma:', 'A incompreensão do que aconteceu.', 'Característica:', 'Ceticismo.')

    Config.character_chart(personagem)


def play():
    vlad_says_hello()
    desc.character_description()
    chose_gate_or_jump_the_wall_vlad()
    vlad_chose_door_or_backyard()

