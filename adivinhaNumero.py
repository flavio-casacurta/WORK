# coding: utf-8

import os

cores = {"azul":{1, 6, 14, 21, 22}
        ,"vermelho":{2, 5, 13, 15, 20}
        ,"verde":{9, 12, 16, 23, 25}
        ,"roxo":{3, 4, 10, 17, 18}
        ,"preto":{7, 8, 11, 19, 24}}

casas = {"casaA":{1, 4, 11, 12, 13, 30}
        ,"casaB":{2, 9, 10, 21, 24 ,26}
        ,"casaC":{8, 14, 17, 20, 25, 28}
        ,"casaD":{3, 5, 19, 22, 23, 27}
        ,"casaE":{6, 7, 15, 16, 18, 29}}


icor = ''
while icor not in cores.keys():
    os.system('cls' if os.name == 'nt' else 'clear')
    if  icor:
        print 'Ops... Tente novamente'
        print ''
    print 'ADIVINHANDO O SEU NUMERO'
    print ''
    print '_'*37
    for cor in cores.keys():
        print '| {:8} |'.format(cor),
        for num in cores[cor]:
            print '{:2} |'.format(num),
        print ''
        print '_'*37
    print ''
    icor = raw_input('Informe a cor do seu Numero: ').lower()

icasa = ''
while icasa not in casas.keys():
    os.system('cls' if os.name == 'nt' else 'clear')
    if  icasa:
        print 'Ops... Tente novamente'
        print ''
    print '_'*40
    for casa in sorted(casas.keys()):
        print '| casa {} |'.format(casa[-1]),
        for num in casas[casa]:
            print '{:2} |'.format(num),
        print ''
        print '_'*40
        print ''
    icasa = 'casa' + raw_input('Informe a casa do seu Numero: ').upper()

os.system('cls')
print '='*35
print 'O Numero que voce escolheu eh : ', list(cores[icor].intersection(casas[icasa]))[0]
print '='*35
