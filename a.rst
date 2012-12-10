from veiculos import *

l = ["Carro marca = 'Porsche' , modelo = '911  ', cor = 'azul   ', ano = '1991', proprietario = 'Soso'"
    ,"Moto  marca = 'Honda'   , modelo = 'CB450', cor = 'preta  ', ano = '1995'"
    ,"Carro marca = 'BMW'     , modelo = 'X3   ', cor = 'branca ', ano = '2011'"
    ,"Moto  marca = 'Kawasaki', modelo = 'Ninja', cor = 'amarela', ano = '2012'"]

firstWord = lambda line: line.split()[0]
nextWords = lambda line, arg:line.split(arg)[1].strip()

for n, i in enumerate(l):
    exec  'veiculo{} = {}({})'.format(str(n), firstWord(i), nextWords(i, firstWord(i)))


