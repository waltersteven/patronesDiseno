#Los observadores siempre deben tener una clase base
class Alumno:
    def on_fijas_dadas(self):
        pass

class Ricardo(Alumno):
    def on_fijas_dadas(self):
        print("Apunta en su cuaderno")

class Diego(Alumno):
    def on_fijas_dadas(self):
        print("Apunta en un notepad")

class Anthony(Alumno):
    def on_fijas_dadas(self):
        print("Solo se lo memoriza")

#Definimos a la clase observado
class Profesor:
    def __init__(self):
        self.observadores = []
    def add_observador(self, observador):
        self.observadores.append(observador)
    def dar_fijas(self): #este es el evento a lanzar
        for obs in self.observadores:
            obs.on_fijas_dadas()

def main():
    anthony = Anthony()
    ricardo = Ricardo()
    diego = Diego()

    #agregamos al observado
    profesor = Profesor()

    #añadimos a los observadores
    profesor.add_observador(anthony)
    profesor.add_observador(ricardo)
    profesor.add_observador(diego)

    profesor.dar_fijas()

if __name__ == '__main__':
    main()
