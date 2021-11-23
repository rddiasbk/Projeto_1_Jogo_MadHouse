import random
from random import randint
import time
from time import sleep
import Config
import desc

vlad = ('Personagem 1:', 'Vlad Blackwood', 'Profissão:', 'Piloto', 'Experiência Paranormal:', 'Perseguido por Abissais',
        'Trauma:', 'A incompreensão do que aconteceu.')
bill = (
    'Personagem 2:', 'Bill Liechtenstein', 'Profissão:', 'Agricultor', 'Experiência Paranormal:', 'Viu um Lobisomem',
    'Trauma:', 'A morte do filho.')
abel = ('Personagem 3:', 'Abel ', 'Profissão:', 'Ladrão', 'Experiência Paranormal:', 'Viu um demônio.',
        'Trauma:', 'A morte de uma criança.')


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
            ouvir = \
                str(input('\033[1;97mDigite O para ouvir ou I para ignorar [O/I]:\033[0;0m')).lower().strip().split()[0]
            if ouvir == 'o':
                print('-' * 100)
                print(f'Sua fé divinina te da uma resistência {sanidade_bill}')
                print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura_bill}')
                print('-' * 100)
                if sanidade_bill >= loucura_bill:
                    print('Você resistiu! Você sabia que sua fé seria maior! ')
                    sleep(1.5)
                    test_faith_bill()
                if loucura_bill > sanidade_bill:
                    print('Você sucumbiu!')
                    print('Infiel')
                    Config.slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
                    sleep(1.5)
                    endgame()
            if ouvir == 'i':
                desc.description_mansion()
                doors()

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
        if caminho_bill == 'm':  # MURO
            print('Você decide sair do óbvio e procura um lugar para pular o muro e ter acesso ao quintal')
            desc.description_backyard()
            bill_garden_conflit()

def bill_garden_conflit():
    monstrinhos = randint(0, 10)
    ataque_bill = randint(0, 15)
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
        sleep(2)
        doors()
    if monstrinhos > ataque_bill:
        print('Você errou!')
        sleep(1.5)
        print('Agora é a vez das pequenas criaturas!')
        sleep(2)
    if monstrinhos == ataque_bill:
        print(f'O monstro te atacou com {monstrinhos} e sua defesa foi {ataque_bill}')
        sleep(1.5)
        print('Um deles morde sua perna!')
        print('Você sente seu sangue queimar a partir da mordida')
        print(
            'Não é a primeira vez que você foi envenenado, mas você sabe que aquele veneno é muito mais potente do que qualquer cobra que já tenha encontrado no campo.')
        sleep(1.5)
        Config.slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
        endgame()

def test_faith_bill():  # teste de fé do bill com partes de exorcismo real
    loucura = randint(0, 100)
    sanidade = randint(0, 100)
    print('A voz ecoa com força em sua mente!')
    print('Ela te persegue conforme você caminha.')
    print('Você precisa testar sua fé contra a maldade do ser:')
    print('-' * 100)
    print(f'Sua fé divinina te da uma resistência {sanidade}')
    print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura}')
    print('-' * 100)
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
        print('-' * 100)
        print(f'Sua fé divina aumenta sua resistência em {sanidade}')
        print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura}')
        print('-' * 100)
        if sanidade >= loucura:
            print(
                'Acorrei, Condutor invencível, em auxílio do Povo de Deus contra as seduções espirituais que se erguem'
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
        Config.slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
        sleep(1.5)

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
            desc.description_solomons_grave()
            solomons_candle()

def abel_inside_basement_the_yellow_king():
    confirmar_alavanca = ' '
    print('Está muito escuro então você usa seu isqueiro para te guiar.')
    print('Você pega sua faca e atira contra a criatura.')
    print('Ela move as mãos e te levanta no ar')
    print('Você sente todos os músculos e nervos do seu corpo te estirar')
    print('Ao lado você percebe uma caixa com 3 alavancas ligada a fiação da casa!')
    print('Cada uma ligada a uma lâmpada colorida.')
    print('Escolha e puxe uma das alavancas')
    lâmpada = ' '
    while confirmar_alavanca not in 's':
        while lâmpada not in 'va':
            print('Alavanca da lâmpada:')
            print('\033[1;97mVermelho [V]\nAmarelo [A]\033[0;0m')
            lâmpada = str(input('\033[1;97mEscolha uma lâmpada acima:')).lower().strip().split()[0]
            confirmar_alavanca = str(input('Confirma a escolha? [S/N]?:\033[0;0m')).lower().strip().split()[0]
            print('=' * 40)
            if confirmar_alavanca == 'n':
                abel_inside_basement_the_yellow_king()
            if lâmpada not in 'va':
                print('Você optou por ceder! A criatura racha seu corpo')
                Config.player_died()
                endgame()
            if lâmpada == 'a':
                catch_a_fire()
                endgame()
            if lâmpada == 'v':
                print(
                    'Uma escolha pode definir o fim da vida. As vezes ao puxar do gatilho. As vezes ao puxar uma alavanca.')
                print('Você perdeu!')
                endgame()

def abel_lock_basement():
    tentativa = 0
    while tentativa == False:
        cadeado = 5
        jogador = randint(0, 10)
        print('O cadeado tem 5 de dificuldade')
        sleep(1.5)
        print(f'Você tirou {jogador}')
        sleep(1.5)
        if jogador >= cadeado:
            print('Você ouve um click! Você conseguiu!')
            tentativa += 1
            print(f'tentativa [{tentativa}]')
            abel_inside_basement_the_yellow_king()
            sleep(1.5)
        elif tentativa == 3:
            print('Algo naquela situação te incomoda. A sua concentração não é a mesma')
            print('Tem dias que a sorte não está para o ladrão')
            print('Você tem muito medo desse ser o dia do azar')
            print('É melhor procurar outro caminho')
            desc.description_solomons_grave()
            solomons_candle()

def catch_a_fire():
    print('Você pega o isqueiro e o pequeno cantil de whisky.')
    print('Tira o cachecol e encharca com bebida')
    print('E diz: Ninguém precisa saber o que aconteceu aqui')
    print('Isso simplesmente não precisa existir')
    print('E então bota fogo na casa')
    print('\033[1;33mVocê venceu!!!!\033[0;0m')

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
    print('-' * 100)
    print(f'Sua incerteza tem um valor de resistência de {sanidade_abel}')
    print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de {loucura_abel}')
    print('-' * 100)
    if sanidade_abel >= loucura_abel:
        print('Você resistiu!')
        sleep(1)
        catch_a_fire()
    if loucura_abel > sanidade_abel:
        print('Você sucumbiu!')
        print('A voz disse:')
        print('Venha ladrão, tenho um túmulo para você.')
        print('O Rei de Amarelo te espera!')
        Config.slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
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
            chose_color('white', 'Digite [A] para acender uma vela ou [I] para ignorar:'))).lower().strip().split()[0]
        if acender_vela == 'a':
            print('Um vento quente sopra das árvores ao redor')
            print('Você se sente bem e resolve ir pela porta principal')
            desc.description_main_door()
            test_sanity_abel()
        elif acender_vela == 'i':
            print('Uma mão sai do túmulo e segura sua perna com força')
            monstro = randint(0, 1)
            resistencia_abel = randint(0, 15)
            print('-' * 100)
            print(f'Você força sua perna com uma resistência de {resistencia_abel}')
            print(f'A criatura aperta com uma força de {monstro}')
            print('-' * 100)
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

                print(
                    f'O monstro começa a te puxar para o solo com {monstro} de força e sua resistência é {resistencia_abel}')
                sleep(1.5)
                print('Ele é mais forte')
                sleep(1.5)
                print('Ele te puxa pro subsolo')
                Config.slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
                endgame()
            if resistencia_abel == monstro:
                sleep(1.5)
                print('Ele errou! Você não arrisca e corre!')
                sleep(2)
                doors()

def vlad_chose_door_or_backyard():
    caminho = ' '
    while caminho not in 'pc':
        caminho = str(input(
            f'\033[1;97m Digite P para entrar pela PORTA CENTRAL ou C para circular a casa [P/C]:\033[0;0m')).lower().strip().split()[
            0]
        if caminho == 'p':  # PORTA PRINCIPAL
            desc.description_main_door()
            test_sanity_vlad()
            doors()

        if caminho == 'c':
            desc.description_backyard()
            vlad_garden_conflit()
def test_sanity_vlad():
    loucura = randint(0, 10)
    sanidade = randint(0, 100)
    print('Você sente a voz gritar em sua mente! Ela testa sua sanidade!')
    print('-'*100)
    print(f'Sua crença no método científico te da uma resistência \033[1;97m{sanidade}\033[0;0m ')
    print(f'A a voz passa a ecoar na sua cabeça com uma intesidade de \033[1;97m{loucura}\033[0;0m ')
    print('-'*100)
    if sanidade >= loucura:
        print('Você resistiu! Você sabia que sua crença na razão seria maior! ')
        sleep(2)
        print('E então corre para dentro da casa')
        #desc.description_mansion()
    elif loucura > sanidade:
        print('Você sucumbiu!')
        print('Infiel')
        Config.slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
        sleep(1.5)
        endgame()

def chose_gate_or_jump_the_wall_vlad():
    print('Você olha ao redor e precisa tomar a primeira decisão: Entrar pelo horripilante portão central ou procurar'
          ' outro caminho')
    caminho = ' '
    while caminho not in 'pm':
        caminho = str(input(
            '\033[1;97mDigite P para entrar pelo PORTÃO ou M para pular o MURO [P/M]:\033[0;0m')).lower().strip().split()[
            0]
        if caminho == 'p':
            print('Você entra pelo portão.')
            sleep(1.5)
            desc.description_mansion()
        if caminho == 'm':  # MURO
            print('Você decide sair do óbvio e procura um lugar para pular o muro e ter acesso ao quintal')
            desc.description_burzum_on_the_wall()
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
    print(f'Seu tiro causou \033[1;97m{ataque_personagem} de dano\033[0;0m')
    print(f'O monstro tinha uma defesa de \033[1;97m{monstrinho}\033[0;0m')
    if ataque_personagem > monstrinho:
        print('Você acertou e foi o fim da criatura!')
        print('É melhor entrar de vez na casa!')
        sleep(2)
        doors()
    elif monstrinho > ataque_personagem:
        print(f'O monstro te atacou com {monstrinho} e sua defesa foi {ataque_personagem}')
        sleep(1.5)
        print('Ele te acertou!')
        sleep(1.5)
        Config.slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
        endgame()
    if ataque_personagem == monstrinho:
        sleep(1.5)
        print('Ele errou! Você não arrisca e corre!')
        sleep(2)
        doors()

def vlad_attack():
    monstro = randint(0, 10)
    ataque_personagem = randint(0, 10)
    print(f'Seu tiro causou \033[1;97m {ataque_personagem}\033[0;0m de dano')
    print(f'O monstro tinha uma defesa de \033[1;97m {monstro}\033[0;0m ')
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

def doors():
    print('''Você olha desesperado e nota 3 portas diferentes.
E em seu âmago sabe que toda a verdade se revelará atrá de uma daquelas portas. 
Chegou a hora!''')
    sleep(1.5)
    print('Escolha uma porta:')
    porta = ' '
    while porta not in 'var':
        print('\033[1;97m>' * 10, '\033[1;32mPORTA VERDE [V]\033[0;0m')
        print('\033[1;97m>' * 10, '\033[1;33mPORTA AMARELA [A]\033[0;0m')
        print('\033[1;97m>' * 10, '\033[1;35mPORTA ROXA [R]\033[0;0m')
        print('')
        sleep(1.5)
        porta = str(input('\033[1;97mEscolha a porta:\033[0;0m')).lower().strip().split()[0]
        print('=' * 100)
        sleep(1.5)
        if porta == 'v':
            print('Você ouve o som do descarrilhar de correntes e sente uma dor intensa em seu abdomen! '
                  '\nUma lança te atravessa! '
                  '\nChegou seu fim!')
            Config.slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
            print(' ')
            endgame()
        if porta == 'a':
            print('As portas se trancam atrás de você! A sala é preenchida por gás.')
            Config.slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
            print(' ')
            endgame()
        if porta == 'r':
            print('Inimigo apareceu!')
            desc.description_boss()
            print('Você saca rapidamente e atira:')
            character_attack()
            time.sleep(1)
        if porta not in 'var':
            print('Isso não é uma porta. Tente novamente!')

def vlad_chose_door_or_backyard():
    caminho = ' '
    while caminho not in 'pc':
        caminho = str(input(
            f'\033[1;97m Digite P para entrar pela PORTA CENTRAL ou C para circular a casa [P/C]:\033[0;0m')).lower().strip().split()[
            0]
        if caminho == 'p':  # PORTA PRINCIPAL
            desc.description_main_door()
            test_sanity_vlad()
            doors()

        if caminho == 'c':
            desc.description_backyard()
            vlad_garden_conflit()


def chose_gate_or_jump_the_wall_vlad():
    print('Você olha ao redor e precisa tomar a primeira decisão: Entrar pelo horripilante portão central ou procurar'
          ' outro caminho')
    caminho = ' '
    while caminho not in 'pm':
        caminho = str(input(
            '\033[1;97mDigite P para entrar pelo PORTÃO ou M para pular o MURO [P/M]:\033[0;0m')).lower().strip().split()[
            0]
        if caminho == 'p':
            print('Você entra pelo portão.')
            desc.description_mansion()
        if caminho == 'm':  # MURO
            print('Você decide sair do óbvio e procura um lugar para pular o muro e ter acesso ao quintal')
            desc.description_burzum_on_the_wall()
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
    print(f'Seu tiro causou \033[1;97m {ataque_personagem}\033[0;0m de dano')
    print(f'O monstro tinha uma defesa de \033[1;97m {monstrinho}\033[0;0m')
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
        Config.slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
        endgame()
    if ataque_personagem > monstrinho:
        sleep(1.5)
        print('Ele errou! Você não arrisca e corre!')
        sleep(2)

def vlad_attack():
    monstro = randint(0, 10)
    ataque_personagem = randint(0, 10)
    print(f'Seu tiro causou \033[1;97m {ataque_personagem}\033[0;0m de dano')
    print(f'O monstro tinha uma defesa de \033[1;97m {monstro}\033[0;0m')
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

def main():
    print('=' * 100)
    print(f"\033[1;91m{'-MAD HOUSE-':^100}\033[0;0m")
    print('=' * 100)
    sleep(0.5)
    print(f"{'Vocês foram chamados ao Bureau de Pesquisas e Defesa Paranormal (B.P.D.P)':^100}")
    print(f"{'Quando quiser começar, digite a palavra JOGAR:':^100}")
    print('')
    print(f"{'Senão, digite qualquer tecla para sair...':^100}")
    print('')
    comeco = (input(f"{'JOGAR??:':^100}")).lower().strip().split()[0]
    if comeco == 'jogar':
        print('_' * 100)
        print(f"{'Veja qual personagem você pode chamar:':^100}")
        print('_' * 100)
        sleep(1.5)
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
    jogo = True
    while jogo:
        resposta = \
        (input('\n\nDigite J para jogar denovo ou digite qualquer letra para sair! :')).lower().strip().split()[0]
        if resposta == 'j':
            jogo == True
            main()
        elif resposta != 'j':
            print('Então tá, até a próxima.')
            break

def format_option(opc):
    print('=' * 40)
    print(opc)
    print('=' * 40)

def character_chart(char):
    #sleep(1.5)
    print('#' * 30)
    for pos in range(0, len(char)):
        if pos % 2 == 0:
            print(f'\033[1;97m {char[pos]:-<20}\033[0;0m', end='')
        if pos % 2 != 0:
            print(f' {char[pos]:>6}')

def select_character():  # ESCOLHA DO PERSONAGEM
    personagem = ' '
    confirmar = ' '
    sleep(1)
    while confirmar != 's':  # COMO TRANSFORMAR ESSA PERGUNTA DE CONFIRMAÇÃO EM DEF?
        while personagem not in 'vba':
            format_option('\033[1;97mVlad [V]\nBill [B]\nAbel [A]\033[0;0m')
            personagem = str(input('\033[1;97mEscolha um personagem acima:')).lower().strip().split()[0]
            confirmar = str(input('Confirma a escolha? [S/N]?:\033[0;0m')).lower().strip().split()[0]
            print('=' * 100)
            if confirmar == 'n':
                select_character()
            if personagem not in 'vba':
                print('Personagem não encontrado. Tente novamente!')
            if personagem == 'v':
                print('\033[1;97m Você escolheu Vlad!')
                print('>>>>VLAD diz:...\033[0;0m', end='')
                print('Olá, eu sou Vlad e estou com pressa, vamos!')
                desc.description_road_to_madhouse()
                desc.description_front_propriety()
                chose_gate_or_jump_the_wall_vlad()
                vlad_chose_door_or_backyard()
            if personagem == 'a':
                print('\033[1;97m Você escolheu Abel!')
                print('>>>>ABEL diz:...\033[0;0m', end='')
                print('O que vocês querem de novo?! Ah.. Chego em breve!')
                desc.description_road_to_madhouse()
                desc.description_front_propriety()
                abel_chose_garden_or_backyard()
            elif personagem == 'b':
                print('\033[1;97m Você escolheu Bill!')
                print('>>>>Bill diz:...\033[0;0m', end='')
                print('Vamos matar esse bicho!')
                desc.description_road_to_madhouse()
                desc.description_front_propriety()
                chose_gate_or_jump_the_wall_bill()

def character_attack():
    monstro = random.randint(0, 10)
    ataque_personagem = random.randint(0, 10)
    print(f'Seu tiro causou \033[1;97m {ataque_personagem}\033[0;0m de dano')
    print(f'O monstro tinha uma defesa de \033[1;97m {monstro}\033[0;0m')
    if ataque_personagem > monstro:
        print('Você acertou! ')
        print('\033[1;33mGANHOU O JOGO!!!\033[0;0m')
        time.sleep(1.5)
        endgame()
    if ataque_personagem == monstro:
        print('Essa foi por pouco!')
        print('Você atira novamente!')
        character_attack()
    elif monstro > ataque_personagem:
        print('Você errou!')
        time.sleep(1.5)
        print('Agora é a vez do monstro')
        time.sleep(1.5)
        monster_attack()

def monster_attack():
    monstro = random.randint(0, 10)
    ataque_personagem = random.randint(0, 10)
    print(f'O monstro tinha um ataque de {monstro}')
    print(f'Sua defesa é {ataque_personagem}')
    if monstro > ataque_personagem:
        print('O monstro errou')
        time.sleep(1.5)
        print('Agora é a sua vez')
        time.sleep(1.5)
        monster_attack()
    if ataque_personagem == monstro:
        print('Essa foi por pouco!')
        print('Você atira novamente!')
    if ataque_personagem > monstro:
        print('Você acertou! ')
        print('\033[1;33mGANHOU O JOGO!!!\033[0;0m')
        time.sleep(1.5)
        endgame()


main()
