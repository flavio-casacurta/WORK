# coding: utf-8
"""
Função que verifica em seu palpite de 15 ou mais números se algum cartão já premiado contém 15 números de seu palpite.

Modo de uso:
============

1. Vá na página de download dos jogos da Lotofacil e faça download do arquivo
   http://www1.caixa.gov.br/loterias/loterias/lotofacil/download.asp
2. Descompacte a pasta e coloque o arquivo D_LOTFAC.HTML no mesmo diretório do script verifica_lotofacil.py
3. Abra o terminal, navegue até a pasta do script e execute como mostrado nos exemplos a seguir

Exemplo 1: Com palpite contido em 1 cartão
------------------------------------------
$ python verifica_lotofacil.py --nums 10 17 16 12 14 24 08 07 05 20 21 01 13 02 22


Exemplo 2: Com palpite contido em vários cartões
------------------------------------------------
$ python verifica_lotofacil.py --nums 18 20 21 25 23 10 11 24 14 06 01 02 12 13 09 05 06 15 16 03 04


Exemplo 3: Especificando arquivo com os números a serem verificados separados por enter
---------------------------------------------------------------------------------------
$ python verifica_lotofacil.py --file-jogos numeros.txt
"""

import re, argparse, operator
from collections import Counter

# Uso da biblioteca argparse para facilitar a entrada de parametros via terminal
parser = argparse.ArgumentParser(description=u'Verifica se seu palpite já foi sorteado.')
parser.add_argument('--file', type=str, default='D_LOTFAC.HTM', dest='file',
    help=u'Arquivo com todos os jogos premiados: http://www1.caixa.gov.br/loterias/loterias/lotofacil/download.asp')
parser.add_argument('--file-jogos', type=str, default='numeros.txt', dest='file_jogos',
    help=u'Arquivo com os números a serem verificados separados por enter no formato: 01,02,04,07,08,10 ...')
parser.add_argument('--nums', nargs='+', type=str, default=None, dest='nums',
    help=u'Números a serem verificados. Ex.: python verifica_lotofacil.py --nums 18 20 25 23 10 11 ...')
args = parser.parse_args()

# Abrindo, lendo, gravando em memória e fechando o arquivo D_LOTFAC.HTM ou outro passado via o parametro --file
with open(args.file, 'r') as htm_lot:
    htm_doc = htm_lot.read()

# Capturando todos os dados que estão nas tags <td> da <table> com regex
captura_itens = re.findall(r'<td>.*</td>', htm_doc)

# Limpando dados capturados e guardando em listas, retirando as tags <td> e </td>
retira_td = ''.join(captura_itens).split('<td>')
lista_com_dados = ''.join(retira_td).split('</td>')

# Dividindo a lista que contém todos os dados em sublistas que contém apenas as bolas de cada jogo
# e inserindo as listas em uma lista chamada jogos
jogos = [lista_com_dados[i:i+15] for i in range(2, len(lista_com_dados), 30)]

print u'\nJogos que contém os 15 números do seu palpite:\n'

def verifica(jogos, numeros):
    tem_cartao_premiado = False

    for jogo in jogos:
        jogo_premiado = []
        for bola in jogo:
            if bola in numeros:
                jogo_premiado.append(bola)

        # A lista jogo_premiado deve conter mais de 14 items para ser visualizada
        if len(jogo_premiado) > 14:
            print '> %s - Jogo premiado encontrado!' % ' '.join(sorted(jogo_premiado))
            print 46 * '-'

            # Se chegar aqui, é porquê exsitem cartões premiados
            tem_cartao_premiado = True
            # Finalmente o uso do flag tem_cartao_premiado para indicar a mensagem negativa

    if not tem_cartao_premiado:
        print u'> Palpite não premiado'
        print 22 * '-'

# Se o usuário passar os números manualmente, essa ação será prioritária
if args.nums:
    verifica(jogos, args.nums)
# Caso contrário, o programa irá procurar pelo arquivo com os números do palpite para fazer a verificação
else:
    # Abrindo, retirando caracteres invisíveis, gerando lista de números no cartão e inserindo cartões na lista_palpites
    with open(args.file_jogos, 'r') as arquivo_palpites:
        lista_palpites = [[numero.strip() for numero in cartao.split(',')] for cartao in arquivo_palpites]

    for cartao in lista_palpites:
        verifica(jogos, cartao)

# Dicionário com 25 posições para guardar a quantidade de vezes que um número foi sorteado
numeros_sorteados = {'%02d' % n:0 for n in range(1, 26)}

# Loop para incrementar o contador de cada número
for jogo in jogos:
    for bola in jogo:
        numeros_sorteados[bola] += 1

print u'\nDicionário "normal" de números sorteados:'
print numeros_sorteados

print u'\nOcorrência de números sorteados ordenados pelo valor do maior para o menor:'
numeros_sorteados_ordenados_valor = sorted(numeros_sorteados.iteritems(), key=operator.itemgetter(1), reverse=True)
print numeros_sorteados_ordenados_valor

# Pega o número com maior ocorrência em cartões
numero_com_maior_ocorrencia = max(numeros_sorteados, key=numeros_sorteados.get)
print u'\nNúmero mais vezes sorteado: %s' % numero_com_maior_ocorrencia

print u'\nSugestão de cartão com os números que tem maior ocorrência:'
sugestao_numeros_maior_ocorrencia = [int(x[0]) for x in numeros_sorteados_ordenados_valor][:15]
print sorted(sugestao_numeros_maior_ocorrencia)

print u'\nDicionário "invertido" de números sorteados:'
dicionario_invertido_numeros_sorteados = {v: k for k, v in numeros_sorteados.items()}
print dicionario_invertido_numeros_sorteados

print u'\nGráfico com ocorrência de números sorteados usando "Counter" do "collections":'
count_numeros_sorteados = Counter(numeros_sorteados)
for item_numero in count_numeros_sorteados.iteritems():
    # Geração de gráfico, sendo que o palpite com menor ocorrência terá apenas uma unidade de medida
    print item_numero[0], (item_numero[1] - (int(min(numeros_sorteados.values()) - 1))) * '.', item_numero[1]
