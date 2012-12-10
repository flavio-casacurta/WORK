class Carro(object):

    def __init__(self,**kargs):
        for chave,valor in kargs.items():
            self.__dict__[chave] = valor.strip()

class Moto(object):

    def __init__(self,**kargs):
        for chave,valor in kargs.items():
            self.__dict__[chave] = valor.strip()

