import desc
import time
import random
import Config



def test_sanity_bill():
    print('''
        Ao pisar na propriedade você ouve uma voz
        que soa como uma lembrança.
        A voz entoa:
    ''')
    ouvir = ' '
    while ouvir not in 'oi':
        loucura_bill = random.randint(0, 100)
        sanidade_bill = random.randint(0, 100)
        print('''
    \33[3mO mar quebra pela orla, vago,
    Os sóis gêmeos afundam sob o lago,
    As sombras se alongam
    Em Carcosa.
    Estranha é a noite em que estrelas negras sobem,
    E estranhas luas o céu percorrem
    Mas ainda mais estranha é a
    Perdida Carcosa.\033[0;0m
    ''')
        print('Você sente um incomôdo intenso:.')
        while ouvir not in 'oi':
            ouvir = \
                str(input('\033[1;97mDigite O para ouvir ou I para ignorar [O/I]:\033[0;0m')).lower().strip().split()[0]
            if ouvir == 'o':
                print('Cenas do dia da morte de Henry invadem sua mente')
                print('Você ouve ele chamar por seu nome!')
                print('Sua sanidade será testada contra o poder de loucura da mansão.')
                # time.sleep(1.5)
                print(f'Sua fé divinina te da uma resistência {sanidade_bill}')
                # time.sleep(1.5)
                print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura_bill}')
                if sanidade_bill >= loucura_bill:
                    print('Você resiste!')
                    print('A voz recua!')
                    print('E então você vê sua família chorando!')
                    print('O horror! O horror!')
                    time.sleep(2)
                    test_faith_bill()
                if loucura_bill > sanidade_bill:
                    print('Você sucumbiu!')
                    print('Infiel')
                    Config.slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
                    time.sleep(1.5)

            elif ouvir == 'i':
                desc.description_mansion()
                # description_main_door()
                Config.doors()


def chose_gate_or_jump_the_wall_bill():
    print('Você olha ao redor e precisa tomar a primeira decisão: Entrar pelo horripilante portão central ou procurar'
          ' outro caminho')
    caminho_bill = ' '
    while caminho_bill not in 'pm':
        caminho_bill = str(input(
            '\033[1;97mDigite P para entrar pelo PORTÃO ou M para pular o MURO [P/M]:\033[0;0m')).lower().strip().split()[
            0]
        if caminho_bill == 'p':
            print('Você entra pelo portão.')
            test_sanity_bill()  # voz

        elif caminho_bill == 'm':  # MURO
            print('Você decide sair do óbvio e procura um lugar para pular o muro e ter acesso ao quintal')
            desc.description_backyard()
            bill_garden_conflit()


def bill_garden_conflit():
    monstrinhos = random.randint(0, 10)
    ataque_bill = random.randint(0, 15)
    print('Você ouve a voz do seu filho!')
    print('Ele grita: Pai atrás do seu lado!')
    print('Você se depara com uma cena horrível.')
    print(
        'De buracos no chão eclodem criaturas magricelas, asquerosas e moles. Os monstrinhos tem bolhas que crescem e explodem conforme elas se movimentam, algumas pingam pus outras e escorrem vermes.')
    print('Você saca rapidamente e atira.')
    print(f'Seu tiro causou {ataque_bill} de dano')
    print(f'O monstro tinha uma defesa de {monstrinhos}')
    if ataque_bill > monstrinhos:
        print('Você já matou ratos maiores no campo. Essa foi fácil!')
        print('É melhor entrar de vez na casa!')
        time.sleep(2)
        Config.doors()
    if monstrinhos > ataque_bill:
        print('Você errou!')
        time.sleep(1.5)
        print('Agora é a vez das pequenas criaturas!')
        time.sleep(2)
    if monstrinhos > ataque_bill:
        print(f'O monstro te atacou com {monstrinhos} e sua defesa foi {ataque_bill}')
        time.sleep(1.5)
        print('Um deles morde sua perna!')
        print('Você sente seu sangue queimar a partir da mordida')
        print(
            'Não é a primeira vez que você foi envenenado, mas você sabe que aquele veneno é muito mais potente do que qualquer cobra que já tenha encontrado no campo.')
        time.sleep(1.5)
        Config.slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')

    if ataque_bill > monstrinhos:
        time.sleep(1.5)
        print('Ele errou! Você não arrisca e corre!')
        print('A voz do seu filho retorna:')
        print('Pai, não se arrisque, os pequenos te esperam em casa!')
        print('Obrigado por tudo, eu vou descansar!')
        print('Você corre em direção ao portão com as criaturas ganindo atrás de você')
        print('Você sai daquele lugar insano e retorna até sua família!')
        print('O jogo acabou pra você')
        time.sleep(1)


def test_faith_bill():  # teste de fé do bill com partes de exorcismo real
    loucura = random.randint(0, 100)
    sanidade = random.randint(0, 100)
    print('A voz ecoa com força em sua mente!')
    print('Ela te persegue conforme você tenta resistir e caminha para a mansão.')
    print('Você precisa testar sua fé contra a loucura da casa')
    # time.sleep(1.5)
    print(f'Sua fé divinina te da uma resistência {sanidade}')
    print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura}')
    if sanidade >= loucura:
        print('Você inicia uma oração:')
        desc.bill_exorcism()
        loucura = random.randint(0, 100)
        sanidade = random.randint(0, 110)
        print(f'Sua fé divina aumenta sua resistência em {sanidade}')
        print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura}')
        if sanidade >= loucura:
            print(
                'E segurando o pequeno terço que sempre carregou consigo, você grita: Acorrei, Condutor invencível, em auxílio do Povo de Deus contra as seduções espirituais que se erguem'
                'e que vençamos! Assim, confiados à tua proteção e tutela, sob a autoridade de nosso Sagrado Ministério, nos reunimos, firmes e com Fé, para rechaçar as infestações da fraude diabólica, em Nome de Jesus Cristo, Deus e Senhor nosso.')
            print('A voz desvanece e some!')
            print('Um vento quente chacoalha as árvores.')
            print('O silencio toma conta!')
            print('O mal se foi..')
            print('\033[1;33mGANHOU O JOGO!!!\033[0;0m')

        time.sleep(2)
    if loucura > sanidade:
        print('Você sucumbiu!')
        print('Infiel')
        print('''Estranha é a noite em que estrelas negras sobem,
E estranhas luas o céu percorrem  
Mas ainda mais estranha é a
Perdida...Perdida....Perdida...''')
        print('RIYL’EH – BUADIH – GELB – RUMENA – GWELLER - - GUL – ZHELTYY - HWANGSAEG')
        Config.slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')

        time.sleep(1.5)


def chart():
    personagem = (
        'Personagem 2:', 'Bill Liechtenstein', 'Profissão:', 'Agricultor', 'Experiência Paranormal:',
        'Viu um Lobisomem', 'Trauma:', 'A morte do filho.', 'Característica:', 'Fé.')

    Config.character_chart(personagem)


def play():
    print('\033[1;97m Você escolheu Bill!')
    print('>>>>Bill diz:...\033[0;0m', end='')
    print('Vamos matar esse bicho!')
    desc.description_road_to_propriety()
    chose_gate_or_jump_the_wall_bill()
