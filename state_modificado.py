ESTADO_UNO = 1
ESTADO_DOS = 2
ESTADO_TRES = 3

class Estado:
    def __init__(self,c lasesita):
        self.entidad = clasesita

    def evento_a(self):
        pass
    def evento_b(self):
        pass

class EstadoUno(Estado):
    def evento_a(self):
        self.entidad.estado = EstadoDos(self.entidad) #self.entidad es clasesita
    def evento_b(self):
        self.entidad.estado = EstadoTres(self.entidad)

class EstadoDos(Estado):
    pass
class EstadoTres(Estado):
    pass


class Clasesita:
    def __init__(self):
        self.estado = EstadoUno(self)

def main():
    objeto = Clasesita() # objeto.estado = EstadoUno
    objeto.estado.evento_a() # objeto.estado = EstadoDos
    objeto.estado.evento_b() # objeto.estado = EstadoDos

    if isinstance(objeto.estado, EstadoUno):
        print("Objeto en EstadoUno")
    elif isinstance(objeto.estado, EstadoDos):
        print("Objeto en EstadoDos")
    elif isintance(objeto.estado, EstadoTres):
        print("Objeto en EstadoTres")

if __name__ == '__main__':
    main()
