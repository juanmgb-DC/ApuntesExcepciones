
class NussError (Exception):
    def __init__(self,nuss):
        self.setNuss(nuss)



    def getNuss(self):
        return self.nuss

    def setNuss(self,nuss):
        if len(nuss) != 16:
            raise NussError ("Lonxitude incorrecta (16)")
        elif nuss[2]!='/' or nuss[-3]!='/':
            raise NussError ("O formato e incorrecto. Erro na posición")
        elif not nuss[:2].isdigit() or not nuss [3:-3] or not nuss[-2:]:
            raise NussError ("O formato e incorrecto. Erro nos díxitos")
        self.nuss = nuss

