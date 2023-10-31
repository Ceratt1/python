print ("\n" * 100) 

class comprimento():
    def __init__(self, frase):
        self.frase = frase
        self.lst = None
        self.lw = None
        self.retorno = None
    def separador(self):
        lol = self.frase.split()
        self.lst = lol
        lol = lol[-1]
        self.lw = lol
        self.retorno = len(lol)
    def mostrar(self):
        print(self.frase)
        print(self.lst)
        print(self.lw)
        print(self.retorno)



cool = comprimento("bem vindo ceratti")
cool.separador()
cool.mostrar()
