# coding: utf-8
"""
Fun��o que verifica em seu palpite de 15 ou mais n�meros se algum cart�o j� premiado cont�m 15 n�meros de seu palpite.

Modo de uso:
============

1. V� na p�gina de download dos jogos da Lotofacil e fa�a download do arquivo
   http://www1.caixa.gov.br/loterias/loterias/lotofacil/download.asp
2. Descompacte a pasta e coloque o arquivo D_LOTFAC.HTML no mesmo diret�rio do script verifica_lotofacil.py
3. Abra o terminal, navegue at� a pasta do script e execute como mostrado nos exemplos a seguir

Exemplo 1: Com palpite contido em 1 cart�o
------------------------------------------
$ python verifica_lotofacil.py --nums 10 17 16 12 14 24 08 07 05 20 21 01 13 02 22


Exemplo 2: Com palpite contido em v�rios cart�es
------------------------------------------------
$ python verifica_lotofacil.py --nums 18 20 21 25 23 10 11 24 14 06 01 02 12 13 09 05 06 15 16 03 04


Exemplo 3: Especificando arquivo com os n�meros a serem verificados separados por enter
---------------------------------------------------------------------------------------
$ python verifica_lotofacil.py --file-jogos numeros.txt
"""

import re, argparse, operator
from collections import Counter

# Uso da biblioteca argparse para facilitar a entrada de parametros via terminal
parser = argparse.ArgumentParser(description=u'Verifica se seu palpite j� foi sorteado.')
parser.add_argument('--file', type=str, default='D_LOTFAC.HTM', dest='file',
    help=u'Arquivo com todos os jogos premiados: http://www1.caixa.gov.br/loterias/loterias/lotofacil/download.asp')
parser.add_argument('--file-jogos', type=str, default='numeros.txt', dest='file_jogos',
    help=u'Arquivo com os n�meros a serem verificados separados por enter no formato: 01,02,04,07,08,10 ...')
parser.add_argument('--nums', nargs='+', type=str, default=None, dest='nums',
    help=u'N�meros a serem verificados. Ex.: python verifica_lotofacil.py --nums 18 20 25 23 10 11 ...')
args = parser.parse_args()

# Abrindo, lendo, gravando em mem�ria e fechando o arquivo D_LOTFAC.HTM ou outro passado via o parametro --file
with open(args.file, 'r') as htm_lot:
    htm_doc = htm_lot.read()

# Capturando todos os dados que est�o nas tags <td> da <table> com regex
captura_itens = re.findall(r'<td>.*</td>', htm_doc)

# Limpando dados capturados e guardando em listas, retirando as tags <td> e </td>
retira_td = ''.join(captura_itens).split('<td>')
lista_com_dados = ''.join(retira_td).split('</td>')

# Dividindo a lista que cont�m todos os dados em sublistas que cont�m apenas as bolas de cada jogo
# e inserindo as listas em uma lista chamada jogos
jogos = [lista_com_dados[i:i+15] for i in range(2, len(lista_com_dados), 30)]

print u'\nJogos que cont�m os 15 n�meros do seu palpite:\n'

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

            # Se chegar aqui, � porqu� exsitem cart�es premiados
            tem_cartao_premiado = True
            # Finalmente o uso do flag tem_cartao_premiado para indicar a mensagem negativa

    if not tem_cartao_premiado:
        print u'> Palpite n�o premiado'
        print 22 * '-'

# Se o usu�rio passar os n�meros manualmente, essa a��o ser� priorit�ria
if args.nums:
    verifica(jogos, args.nums)
# Caso contr�rio, o programa ir� procurar pelo arquivo com os n�meros do palpite para fazer a verifica��o
else:
    # Abrindo, retirando caracteres invis�veis, gerando lista de n�meros no cart�o e inserindo cart�es na lista_palpites
    with open(args.file_jogos, 'r') as arquivo_palpites:
        lista_palpites = [[numero.strip() for numero in cartao.split(',')] for cartao in arquivo_palpites]

    for cartao in lista_palpites:
        verifica(jogos, cartao)

# Dicion�rio com 25 posi��es para guardar a quantidade de vezes que um n�mero foi sorteado
numeros_sorteados = {'%02d' % n:0 for n in range(1, 26)}

# Loop para incrementar o contador de cada n�mero
for jogo in jogos:
    for bola in jogo:
        numeros_sorteados[bola] += 1

print u'\nDicion�rio "normal" de n�meros sorteados:'
print numeros_sorteados

print u'\nOcorr�ncia de n�meros sorteados ordenados pelo valor do maior para o menor:'
numeros_sorteados_ordenados_valor = sorted(numeros_sorteados.iteritems(), key=operator.itemgetter(1), reverse=True)
print numeros_sorteados_ordenados_valor

# Pega o n�mero com maior ocorr�ncia em cart�es
numero_com_maior_ocorrencia = max(numeros_sorteados, key=numeros_sorteados.get)
print u'\nN�mero mais vezes sorteado: %s' % numero_com_maior_ocorrencia

print u'\nSugest�o de cart�o com os n�meros que tem maior ocorr�ncia:'
sugestao_numeros_maior_ocorrencia = [int(x[0]) for x in numeros_sorteados_ordenados_valor][:15]
print sorted(sugestao_numeros_maior_ocorrencia)

print u'\nDicion�rio "invertido" de n�meros sorteados:'
dicionario_invertido_numeros_sorteados = {v: k for k, v in numeros_sorteados.items()}
print dicionario_invertido_numeros_sorteados

print u'\nGr�fico com ocorr�ncia de n�meros sorteados usando "Counter" do "collections":'
count_numeros_sorteados = Counter(numeros_sorteados)
for item_numero in count_numeros_sorteados.iteritems():
    # Gera��o de gr�fico, sendo que o palpite com menor ocorr�ncia ter� apenas uma unidade de medida
    print item_numero[0], (item_numero[1] - (int(min(numeros_sorteados.values()) - 1))) * '.', item_numero[1]
