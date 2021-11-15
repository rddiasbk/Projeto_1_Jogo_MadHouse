def abel_chose_garden_or_backyard():
    print('Você já esteve em propriedades como essa por motivos muito menos nobres')
    print(
        'É sempre a mesma estrutura: uma grande porta que dá para uma sala enorme onde todos podem ver quem entra, uma porta lateral para os criados e um porão entre os arbustos')
    caminho_abel = ' '
    while caminho_abel not in 'pj':
        caminho_abel = str(input(
            '\033[1;97m Digite [P] para seguir pelo porão ou [J] para ir pelo jardim [P/J]:\033[0;0m')).lower().strip().split()[
            0]
        if caminho_abel == 'p':
            print('Você tem 03 tentativas para abrir o cadeado')
            abel_lock_basement()
        if caminho_abel == 'j':
            description_solomons_grave()
            solomons_candle()

def abel_inside_basement_the_yellow_king():
    confirmar_alavanca = ' '
    print('Está muito escuro então você usa seu isqueiro para te guiar.')
    print('Você pega sua faca e atira contra a criatura.')
    print('Ela move as mãos e te levanta no ar')
    print('Você sente todos os músculos e nervos do seu corpo te estirar')
    print('Ao lado você percebe uma caixa com 3 alavancas ligada a fiação da casa')
    lâmpada = ' '
    while confirmar_alavanca != 's':
        while lâmpada not in 'va':
            print('\033[1;97mVermelho [V]\nAmarelo [A]\033[0;0m')
            lâmpada = str(input('\033[1;97mEscolha uma lâmpada acima:')).lower().strip().split()[0]
            confirmar_alavanca = str(input('Confirma a escolha? [S/N]?:\033[0;0m')).lower().strip().split()[0]
            print('-' * 40)
            if lâmpada not in 'va':
                print('Você optou por ceder! A criatura racha seu corpo')
                player_died()
            if lâmpada == 'a':
                print('Você venceu!')
                endgame()
            if lâmpada == 'v':
                print('Você perdeu!')
                endgame()


def abel_lock_basement():
    tentativa = 0
    while tentativa != 3:
        cadeado = 1
        jogador = randint(0, 9)
        print('O cadeado tem 7 de dificuldade')
        print(f'Você tirou {jogador}')
        if jogador > cadeado:
            print('Você ouve um click! Você conseguiu!')
            abel_inside_basement_the_yellow_king()
        if cadeado >= jogador:
            tentativa += 1
        print(f'tentativa{tentativa}')
        if tentativa == 3:
            print('Algo naquela situação te incomoda. A sua concentração não é a mesma')
            print('Tem dias que a sorte não está para o ladrão')
            print('Você tem muito medo desse ser o dia do azar')
            print('É melhor procurar outro caminho')
            description_solomons_grave()
            solomons_candle()


def catch_a_fire():
    print('Você pega o isqueiro e o pequeno cantil de whisky.')
    print('Tira o cachecol e encharca com bebida')
    print('E diz: Ninguém precisa saber o que aconteceu aqui')
    print('Isso simplesmente não precisa existir')
    print('E então bota fogo na casa')
    endgame()


def test_sanity_abel():
    loucura_abel = randint(0, 1)
    sanidade_abel = randint(0, 100)
    print('Ao pisar na propriedade você ouve uma voz que soa como uma lembrança.')
    print('A voz entoa:')
    print('''\33[3m
                                    Lobos dormem noite a dentro
                                    Morcegos voam ao relento
                                    Uma alma perdida que dorme jamais
                                    Com medo de bruxas e sombras fatais

                                    Solitária em pesadelo está
                                    A boneca assombrada pelo LADRÃO
                                    Pago em ouro e de frio coração
                                    Que vem e vai sem nada deixar além de aflição.\033[0;0m
        ''')
    print('Você sente um incomôdo intenso:.')
    print(
        'Você nunca foi um homem de fé mas nunca duvidou do sobrenatural, ainda mais depois do que viu naquele dia, naquele quarto.')
    print(f'Sua incerteza tem um valor de resistência de {sanidade_abel}')
    print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura_abel}')
    if sanidade_abel >= loucura_abel:
        print('Você resistiu!')
        sleep(1)
        catch_a_fire()
    if loucura_abel > sanidade_abel:
        print('Você sucumbiu!')
        print('A voz disse:')
        print('Venha ladrão, tenho um túmulo para você.')
        print('O Rei de Amarelo te espera!')
        slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
        sleep(1.5)
        endgame()


def solomons_candle():
    print('Você se incomoda pelo desprezo com que foi enterrado aquele indivíduo')
    print('Vê alguns restos de velas nas sepulturas vizinhas e nenhuma naquela')
    print('Você sente o isqueiro em seu bolso')
    print('E passa pela sua cabeça acender uma vela pra iluminar aquele ser que não teve luz em vida')
    acender_vela = ' '
    while acender_vela not in 'ai':
        acender_vela = str(input(
            chose_color('white', 'Digite [A] para acender uma vela ou [I] para ignorar'))).lower().strip().split()[0]
        if acender_vela == 'a':
            print('Um vento quente sopra das árvores ao redor')
            print('Você se sente bem e resolve ir pela porta principal')
            description_main_door()
            test_sanity_abel()
        elif acender_vela == 'i':
            print('Uma mão sai do túmulo e segura sua perna com força')
            monstro = randint(0, 1)
            resistencia_abel = randint(0, 15)
            print(f'Você força sua perna com uma resistência de {resistencia_abel}')
            print(f'A criatura aperta com uma força de {monstro}')
            if resistencia_abel > monstro:
                print('Você pega sua faca e crava na mão podre da criatura')
                print('Você corre em direção a casa!')
                sleep(2)
                doors()
            if monstro > resistencia_abel:
                print('Você não consegue se soltar')
                print('A força do monstro é absurda')
                sleep(1.5)
                print('Agora é a vez da aberração!')
                sleep(2)
            if monstro > resistencia_abel:
                print(
                    f'O monstro começa a te puxar para o solo com {monstro} de força e sua resistência é {resistencia_abel}')
                sleep(1.5)
                print('Ele é mais forte')
                sleep(1.5)
                print('Ele te puxa pro subsolo')
                slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
                endgame()
            if resistencia_abel > monstro:
                sleep(1.5)
                print('Ele errou! Você não arrisca e corre!')
                sleep(2)