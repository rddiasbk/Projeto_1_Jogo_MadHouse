print('_'*30)
print('Veja quem você pode chamar:')
print('_'*30)
print('Personagem 1: \nProfissão: piloto: \nHistória:  ')
print('_'*30)


def opções(opc):
    print('*'*30)
    print(opc)
    print('*'*30)
personagem = ' '
confirmar = ' '
porta = ' '

while confirmar != 's':
    while personagem not in 'vba':
         opções('Vlad [V]\nBill [B]\nAbel [A]')
         personagem = str(input('Escolha uma das opções:')).lower().strip().split()[0]
         confirmar = str(input('Confirma a escolha? [S/N]?:')).lower().strip().split()[0]
         if personagem not in 'vba':
            print('Personagem não encontrado. Tente novamente!')

    #if personagem == 'a':

while porta not in 'bav':
    opções('PORTA [1]\nPORTA[2]\nPORTA[3]')
    porta = int(input('Escolha a porta:'))

    if porta == 1:
        print('Morreu!')
    if porta == 2:
        print('Morreu!')
    if porta == 3:
        print('Inimigo')






