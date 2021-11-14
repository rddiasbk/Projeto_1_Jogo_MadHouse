from random import randint
from time import sleep
#formatação de apresentação dos personagens
import time
#IDEIA: fazer um jogo com for pra completar a palavra carcosa.
#da pra colocar cont pra definir 3 tentativas.
# APRESENTAÇÃO DO PERSONAGEM
vlad = ('Personagem 1:', 'Vlad Blackwood', 'Profissão:', 'Piloto', 'Experiência Paranormal:', 'Perseguido por Abissais',
        'Trauma:', 'A incompreensão do que aconteceu.')
bill = ( 'Personagem 2:', 'Bill Liechtenstein', 'Profissão:', 'Agricultor', 'Experiência Paranormal:', 'Viu um Lobisomem',
'Trauma:', 'A morte do filho.')
abel = ('Personagem 3:', 'Abel ', 'Profissão:', 'Ladrão', 'Experiência Paranormal:', 'Viu um demônio.',
        'Trauma:', 'A morte de uma criança.')

#MENU
def main():
    print(chose_color('italico',(f"{'MAD HOUSE':^80}")))
    print('='*80)
    sleep(0.5)
    print(f"{'Vocês foram chamados ao Bureau de Pesquisas e Defesa Paranormal (B.P.D.P)':^40}")
    print(f"{'Quando quiser começar, digite a palavra JOGAR:':^80}")
    print('')
    print(f"{'Senão, digite qualquer tecla para sair...':^80}")
    print('')
    comeco = (input(f"{'JOGAR??:':^80}")).lower().strip().split()[0]
    if comeco == 'jogar':
        print('_' * 30)
        print('Veja qual personagem você pode chamar:')
        print('_' * 30)
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


#JOGAR NOVAMENTE?
def endgame():
    resposta = (input('\n\nDigite J para jogar denovo ou qualquer tecla para sair! :')).lower().strip().split()[0]
    if resposta == 'j':
        main()
    else:
        print('Então tá, até a próxima.')


#FORMATAÇÃO DE UM TRECHO
def format_option(opc):
    print('-' * 40)
    print(opc)
    print('-' * 40)

#TEXTO LENTO
def slowprint(texto, atraso=0.1):
  for c in texto:
    print(c,end='',flush=True)
    time.sleep(atraso)

def road_to_madhouse():
    print('Você entra no carro do delegado, um Ford T, preto e sem janelas,'
          'três vão atrás e um acompanha o motorista. '
          'Vocês partem e atravessam a cidade. No caminho veem as chaminés,'
          'verdadeiros dragões cuspindo fumaça preta no céu acinzentado.'
          'Raios começam a cair atrás de vocês e trovões o seguem.'
          'Vai chover, mais uma tarde chuvosa. Como tem sido por todo o outono.'
          'O carro vai trepidando nos pavimentos de pedra. Na periferia vocês sentem o calor e o fedor dos gases dos'
          ' detritos jogados na rua nos cortiços dos operários da fábrica.'
          'Crianças de 2 e 3 anos, cuidadas por meninas de 05,'
          'um tanto esqueléticas porém de barrigas inchadas,olham hipnotizadas enquanto vocês passam.')
#'Está muito frio e vai chover'
def description_front_propriety():
    print('Está muito frio e vai chover, são 13 horas mas já parece fim de tarde. Chove e a neblina cobre a mansão.'
          'Na frente de vocês há um portão enorme de ferro vazado, onde se veem as letras H P, da família Howard '
          'Phillips.'
          'O portão está apenas encostado.')
    print('Você olha ao redor e precisa tomar a primeira decisão: Entrar pelo horripilante portão central ou procurar'
          ' outro caminho')#'Está muito frio e vai chover'
#"A mansão é claramente muito antiga".
def description_mansion():
    print('Você entra na mansão')
    print('A mansão é claramente muito antiga. Há partes quebradas e destelhadas por tempestades.'
          'É alta, possuindo 2 andares muito largos. Em cada canto da casa há estatuetas apoiadas por uma torre.'
          'Nelas repousam gárgulas com olhos famintos que parecem querer devorar o inimigo ou talvez proteger ferozmente'
          'o seu dono das ameaças que vem distante.')
#"A porta de entrada é enorme e pesada"...
def description_main_door():
    print('A porta de entrada é enorme e pesada. Também está só encostada. A porta entreaberta revela atrás de si um grande salão,'
          'com piso quadriculado em preto e branco, parecendo um grande xadrez. Você entra e se percebe como um peão do tabuleiro.'
          'Ligado ao teto está um lustre enorme de cristais empoeirado.')
def description_boss():
    print('''tem aproximadamente dois metros de altura e uns 120 quilos. Veste uma roupa social, toda puída,
    com um forte cheiro de formol e podridão, mas não de carne vermelha, podridão de peixe.  A pele de seu rosto foi
    descolada,e é segurada por alguns clipes de aço cravados na carne do seu crânio. Isso retira qualquer expressão do
    seu rosto,deixando apenas deformidade. Os seus olhos são negros, mas não há pupilas, íris ou esclera. 
    Dentro há apenas uma escuridão opaca, como um buraco negro fosco, olhar nos olhos da criatura traz a sensação de ter
    sua vitalidade sugada. Aparentemente há uma forma física, mas com certeza aquela criatura é preenchida por alguma
    coisa mágica e antiga.''')
def description_backyard(): #'É possível ver a antiga casa.." Descrição precede combate.
    print('Você circula a casa.')
    print('''
    É possível ver a antiga casa do caseiro que foi parte demolida na ação da prefeitura e do tempo. Uma árvore tombada e suas raízes cortadas. E não muito mais que isso. Todos sentem algo roçar em suas nucas e o arrepio percorre a espinha.
    É como o toque do vento frio, ou de uma seda muito fina,mas seja o que for não é algo bom.
    Nesse momento uma rajada de vento chacoalha os galhos das árvores e levanta os pólens das verbenas e lantanas do jardim.''')
# APRESENTAÇÃO DA TABELA DE PERSONAGENS


def chose_door_or_backyard():
    caminho = ' '
    while caminho not in 'pc':
        #description_mansion
        caminho = str(input(f'\033[1;97m Digite P para entrar pela PORTA CENTRAL ou C para circular a casa [P/C]:\033[0;0m')).lower().strip().split()[0]
        if caminho == 'p':  # PORTA PRINCIPAL
            description_main_door()
            test_sanity_vlad()
            doors()

        if caminho == 'c':
                description_backyard()
                vlad_garden_conflit()


def show_burzum_on_the_wall():
    print('Você sente para um arrepio e olha para o lado.')
    print('Algumas palavras estão cravadas na parede:')
    print('-'*40)
    print(format_text_history('italico','''\33[3m
    Quando a noite cai
    Ela cobre o mundo
    Em uma escuridão impenetrável
    O frio se eleva
    Do solo
    E contamina o ar
    De repente
    A vida tem um novo significado\033[0;0m'''))
    print('-' * 40)


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

def character_chart(char):
    #sleep(1.5)
    print('#' * 30)
    for pos in range(0, len(char)):
        if pos % 2 == 0:
            print(f'\033[1;97m {char[pos]:-<20}\033[0;0m', end='')
        if pos % 2 != 0:
            print(f' {char[pos]:>6}')

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
        description_mansion()
    elif loucura > sanidade:
        vitoria = 1
        print('Você sucumbiu!')
        print('Infiel')
        slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
        sleep(1.5)
        endgame()


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
                    vitoria = 1
                    print('Você sucumbiu!')
                    print('Infiel')
                    slowprint('\033[1;31mVOCÊ ENLOUQUECEU!\033[0;0m')
                    sleep(1.5)
                    endgame()
            elif ouvir == 'i':
                description_mansion()
                #description_main_door()
                doors()


def chose_gate_or_jump_the_wall_bill():
    caminho = ' '
    while caminho not in 'pm':
        caminho = str(input('\033[1;97mDigite P para entrar pelo PORTÃO ou M para pular o MURO [P/M]:\033[0;0m')).lower().strip().split()[0]
        if caminho == 'p':
            print('Você entra pelo portão.')
            test_sanity_bill()#voz
            description_mansion()
        elif caminho == 'm':  # MURO
            print('Você decide sair do óbvio e procura um lugar para pular o muro e ter acesso ao quintal')
            description_backyard()
            bill_garden_conflit()


def chose_gate_or_jump_the_wall_vlad():
    caminho = ' '
    while caminho not in 'pm':
        caminho = str(input('\033[1;97mDigite P para entrar pelo PORTÃO ou M para pular o MURO [P/M]:\033[0;0m')).lower().strip().split()[0]
        if caminho == 'p':
            print('Você entra pelo portão.')
            description_mansion()
        if caminho == 'm':  # MURO
            print('Você decide sair do óbvio e procura um lugar para pular o muro e ter acesso ao quintal')
            show_burzum_on_the_wall()
            description_backyard()
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



#Caso o jogador morra
def player_died():
    slowprint('\033[31mMais uma vítima da casa!\033[0;0m')
    endgame()

def select_character():     # ESCOLHA DO PERSONAGEM
    personagem = ' '
    confirmar = ' '
    sleep(1.5)
    while confirmar != 's':#COMO TRANSFORMAR ESSA PERGUNTA DE CONFIRMAÇÃO EM DEF?
        while personagem not in 'vba':
            format_option('\033[1;97mVlad [V]\nBill [B]\nAbel [A]\033[0;0m')
            personagem = str(input('\033[1;97mEscolha um personagem acima:')).lower().strip().split()[0]
            confirmar = str(input('Confirma a escolha? [S/N]?:\033[0;0m')).lower().strip().split()[0]
            print('-' * 40)
            if confirmar == 'n':
                endgame()
            if personagem not in 'vba':
                print('Personagem não encontrado. Tente novamente!')
            if personagem == 'v':
                    # aprofundar rapidamente o personagem
                    print('\033[1;97m Você escolheu Vlad!')
                    print('>>>>VLAD diz:...\033[0;0m', end='')
                    print('Olá, eu sou Vlad e estou com pressa, vamos!')
                    road_to_madhouse()
                    description_front_propriety()
                    chose_gate_or_jump_the_wall_vlad()
                    #description_mansion() ja coloquei em doord or backyar
                    chose_door_or_backyard()
                    #description_main_door()
                    test_sanity_vlad()
                    doors()
            elif personagem == 'a':
                    print('\033[1;97m Você escolheu Abel!')
                    print('>>>>ABEL diz:...\033[0;0m', end='')
                    print('O que vocês querem de novo?! Ah.. Chego em breve!')
            elif personagem == 'b':
                    print('\033[1;97m Você escolheu Bill!')
                    print('>>>>Bill diz:...\033[0;0m',end='')
                    print('Vamos matar esse bicho!')
                    road_to_madhouse()
                    description_front_propriety()
                    chose_gate_or_jump_the_wall_bill()

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

def monster_attack():
    monstro = randint(0, 10)
    ataque_personagem = randint(0, 10)
    print(f'O monstro tinha um ataque de {monstro}')
    print(f'Sua defesa é {ataque_personagem}')
    if monstro > ataque_personagem:
        print('O monstro errou')
        sleep(1.5)
        print('Agora é a sua vez')
        sleep(1.5)
        monster_attack()
    if ataque_personagem == monstro:
        print('Essa foi por pouco!')
        print('Você atira novamente!')
    if ataque_personagem > monstro:
        print('Você acertou! ')
        print('\033[1;33mGANHOU O JOGO!!!\033[0;0m')
        sleep(1.5)
        endgame()

def final_battle():
    monster_attack()
    vlad_attack()



def doors():
    print('Apesar do a escuridão que toma o resto da casa você se depara com 3 portas diferentes.')
    porta = ' '
    while porta not in 'var':
        print('\033[1;97m>'*10,'\033[1;32mPORTA VERDE [V]\033[0;0m')
        print('\033[1;97m>'*10,'\033[1;33mPORTA AMARELA [A]\033[0;0m')
        print('\033[1;97m>'*10,'\033[1;35mPORTA ROXA [R]\033[0;0m')
        print('')
        porta = str(input('\033[1;97mEscolha a porta:\033[0;0m')).lower().strip().split()[0]
        print('-' * 40)
        if porta == 'v':
         print('Você ouve o som do descarrilhar de correntes e sente uma dor intensa em seu abdomen! '
                      '\nUma lança te atravessa! '
                      '\nChegou seu fim!')
         slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
         print(' ')
         player_died()
        if porta == 'a':
          print('As portas se trancam atrás de você! A sala é preenchida por gás.')
          slowprint('\033[1;31mVOCÊ MORREU!\033[0;0m')
          print(' ')
          player_died()
        if porta == 'r':
         print('Inimigo apareceu!')
         description_boss()
         print('Você saca rapidamente e atira:')
         vlad_attack()
         sleep(1)
        if porta not in 'var':
         print('Isso não é uma porta. Tente novamente!')

main()







