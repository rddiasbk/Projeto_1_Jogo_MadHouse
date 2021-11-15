def vlad_chose_door_or_backyard():
    caminho = ' '
    while caminho not in 'pc':
        #description_mansion
        caminho = str(input(f'\033[1;97m Digite P para entrar pela PORTA CENTRAL ou C para circular a casa [P/C]:\033[0;0m')).lower().strip().split()[0]
        if caminho == 'p':  # PORTA PRINCIPAL
            desc.description_main_door()
            test_sanity_vlad()
            doors()

        if caminho == 'c':
                desc.description_backyard()
                vlad_garden_conflit()
def test_sanity_vlad():
    #teste de sanidade
    loucura = randint(0, 10)
    sanidade = randint(0, 100)
    print(f'Sua crença no método científico te da uma resistência {sanidade}')
    print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura}')
    if sanidade >= loucura:
        print('Você resistiu! Você sabia que sua crença na razão seria maior! ')
        sleep(2)
        print('Você vai logo para dentro da casa')
        desc.description_mansion()
    elif loucura > sanidade:
        vitoria = 1
        print('Você sucumbiu!')
        print('Infiel')
        slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
        sleep(1.5)
        endgame()
def chose_gate_or_jump_the_wall_vlad():
    print('Você olha ao redor e precisa tomar a primeira decisão: Entrar pelo horripilante portão central ou procurar'
          ' outro caminho')
    caminho = ' '
    while caminho not in 'pm':
        caminho = str(input('\033[1;97mDigite P para entrar pelo PORTÃO ou M para pular o MURO [P/M]:\033[0;0m')).lower().strip().split()[0]
        if caminho == 'p':
            print('Você entra pelo portão.')
            desc.description_mansion()
        if caminho == 'm':  # MURO
            print('Você decide sair do óbvio e procura um lugar para pular o muro e ter acesso ao quintal')
            show_burzum_on_the_wall()
            desc.description_backyard()
            vlad_garden_conflit()
            doors()
def vlad_garden_conflit():
    print('Então algo pula em você!')
    print('Você desvia rapidamente!')
    print('A pequena criatura emite um ganido!')
    print('Você saca rapidamente e atira.')
    monstrinho = randint(0, 10)
    ataque_personagem = randint(0, 15)
    print(f'Seu tiro causou {ataque_personagem} de dano')
    print(f'O monstro tinha uma defesa de {monstrinho}')
    if ataque_personagem > monstrinho:
            print('Você acertou e foi o fim da criatura!')
            print('É melhor entrar de vez na casa!')
            sleep(2)
            doors()
    if monstrinho > ataque_personagem:
            print('Você errou!')
            sleep(1.5)
            print('Agora é a vez da aberração!')
            sleep(2)
    if monstrinho > ataque_personagem:
            print(f'O monstro te atacou com {monstrinho} e sua defesa foi {ataque_personagem}')
            sleep(1.5)
            print('Ele te acertou!')
            sleep(1.5)
            slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
            endgame()
    if ataque_personagem > monstrinho:
            sleep(1.5)
            print('Ele errou! Você não arrisca e corre!')
            sleep(2)
def vlad_attack():
    monstro = randint(0, 10)
    ataque_personagem = randint(0, 10)
    print(f'Seu tiro causou {ataque_personagem} de dano')
    print(f'O monstro tinha uma defesa de {monstro}')
    if ataque_personagem > monstro:
        print('Você acertou! ')
        print('\033[1;33mGANHOU O JOGO!!!\033[0;0m')
        sleep(1.5)
        endgame()
    if ataque_personagem == monstro:
        print('Essa foi por pouco!')
        print('Você atira novamente!')
        vlad_attack()
    elif monstro > ataque_personagem:
        print('Você errou!')
        sleep(1.5)
        print('Agora é a vez do monstro')
        sleep(1.5)
        monster_attack()