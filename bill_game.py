def test_sanity_bill():
    ouvir = ' '
    while ouvir not in 'oi':
        loucura_bill = randint(0, 100)
        sanidade_bill = randint(0, 100)
        print('Ao pisar na propriedade você ouve uma voz que soa como uma lembrança.')
        print('A voz entoa:')
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
            ouvir = str(input('\033[1;97mDigite O para ouvir ou I para ignorar [O/I]:\033[0;0m')).lower().strip().split()[0]
            if ouvir == 'o':
                print(f'Sua fé divinina te da uma resistência {sanidade_bill}')
                print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura_bill}')
                if sanidade_bill >= loucura_bill:
                    print('Você resistiu! Você sabia que sua fé seria maior! ')
                    sleep(2)
                    test_faith_bill()
                if loucura_bill > sanidade_bill:
                    print('Você sucumbiu!')
                    print('Infiel')
                    slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
                    sleep(1.5)
                    endgame()
            elif ouvir == 'i':
                desc.description_mansion()
                #description_main_door()
                doors()
def chose_gate_or_jump_the_wall_bill():
    print('Você olha ao redor e precisa tomar a primeira decisão: Entrar pelo horripilante portão central ou procurar'
          ' outro caminho')
    caminho_bill = ' '
    while caminho_bill not in 'pm':
        caminho_bill = str(input('\033[1;97mDigite P para entrar pelo PORTÃO ou M para pular o MURO [P/M]:\033[0;0m')).lower().strip().split()[0]
        if caminho_bill == 'p':
            print('Você entra pelo portão.')
            test_sanity_bill()#voz
            desc.description_mansion()
        elif caminho_bill == 'm':  # MURO
            print('Você decide sair do óbvio e procura um lugar para pular o muro e ter acesso ao quintal')
            desc.description_backyard()
            bill_garden_conflit()
def bill_garden_conflit():
    monstrinhos = randint(0, 10)
    ataque_bill = randint(0, 15)
    print('Você ouve a voz do seu filho!')
    print('Ele grita: Pai atrás do seu lado!')
    print('Você se depara com uma cena horrível.')
    print('De buracos no chão eclodem criaturas magricelas, asquerosas e moles. Os monstrinhos tem bolhas que crescem e explodem conforme elas se movimentam, algumas pingam pus outras e escorrem vermes.')
    print('Você saca rapidamente e atira.')
    print(f'Seu tiro causou {ataque_bill} de dano')
    print(f'O monstro tinha uma defesa de {monstrinhos}')
    if ataque_bill > monstrinhos:
        print('Você já matou ratos maiores no campo. Essa foi fácil!')
        print('É melhor entrar de vez na casa!')
        sleep(2)
        doors()
    if monstrinhos > ataque_bill:
        print('Você errou!')
        sleep(1.5)
        print('Agora é a vez das pequenas criaturas!')
        sleep(2)
    if monstrinhos > ataque_bill:
        print(f'O monstro te atacou com {monstrinhos} e sua defesa foi {ataque_bill}')
        sleep(1.5)
        print('Um deles morde sua perna!')
        print('Você sente seu sangue queimar a partir da mordida')
        print('Não é a primeira vez que você foi envenenado, mas você sabe que aquele veneno é muito mais potente do que qualquer cobra que já tenha encontrado no campo.')
        sleep(1.5)
        slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
        endgame()
    if ataque_bill > monstrinhos:
        sleep(1.5)
        print('Ele errou! Você não arrisca e corre!')
        print('A voz do seu filho retorna:')
        print('Pai, não se arrisque, os pequenos te esperam em casa!')
        print('Obrigado por tudo, eu vou descansar!')
        print('Você corre em direção ao portão com as criaturas ganindo atrás de você')
        print('Você sai daquele lugar insano e retorna até sua família!')
        print('O jogo acabou pra você')
        sleep(1)
def test_faith_bill(): # teste de fé do bill com partes de exorcismo real
    loucura = randint(0, 100)
    sanidade = randint(0, 100)
    print('A voz ecoa com força em sua mente!')
    print('Ela te persegue conforme você caminha.')
    print('Você precisa testar sua fé contra a maldade do ser:')
    print(f'Sua fé divinina te da uma resistência {sanidade}')
    print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura}')
    if sanidade >= loucura:
        print('Você inicia uma oração:')
        print('Gloriosíssimo Príncipe da Milícia Celeste, São Miguel Arcanjo, defenda-nos no Combate e nas lutas,'
              'que travamos contra os principados e potestades, contra os dirigentes deste mundo de Trevas,'
              'contra as armadilhas espirituais. Acorra em auxílio dos homens, os quais Deus criou inextinguíveis,'
              'à Sua Imagem e Semelhança, resgatado da tirania do Diabo a grande penhor. Peleja com o Exército dos'
              'Santos Anjos as batalhas do Senhor, assim como batalhastes outrora contra Lúcifer, chefe orgulhoso,'
              'e seus anjos rebeldes.')
        loucura = randint(0, 100)
        sanidade = randint(0, 110)
        print(f'Sua fé divina aumenta sua resistência em {sanidade}')
        print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura}')
        if sanidade >= loucura:
            print('Acorrei, Condutor invencível, em auxílio do Povo de Deus contra as seduções espirituais que se erguem'
                  'e que vençamos!')
            print('A voz desvanece e some!')
            print('\033[1;33mGANHOU O JOGO!!!\033[0;0m')
            endgame()
        sleep(2)
    if loucura > sanidade:
        print('Você sucumbiu!')
        print('Infiel')
        print('''Estranha é a noite em que estrelas negras sobem,
E estranhas luas o céu percorrem  
Mas ainda mais estranha é a
Perdida...Perdida....Perdida...''')
        print('RIYL’EH – BUADIH – GELB – RUMENA – GWELLER - - GUL – ZHELTYY - HWANGSAEG')
        slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
        sleep(1.5)
