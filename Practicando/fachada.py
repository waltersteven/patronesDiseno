class GestorDeReclamos: #funciona como Fachada
    def __init__(self):
        #Definamos la jerarquia
        self.profesor = Profesor()
        self.coordinador = Coordinador()
        self.secretario = SecretarioAcademico()
        self.director = Director()

        self.profesor.set_sucesor(self.coordinador)
        self.coordinador.set_sucesor(self.secretario)
        self.secretario.set_sucesor(self.director)

    def presentar_reclamo(self, reclamo):
        self.profesor.responder(reclamo)

class Empleado:
    def set_sucesor(self,sucesor):
        self.sucesor = sucesor
    def responder(self, reclamo):
        pass

class Profesor(Empleado):
    def responder(self, reclamo):
        if reclamo.puntos < 2:
            print('Lo resuelve el Profesor')
            return True
        else:
            return self.sucesor.responder(reclamo)

class Coordinador(Empleado):
    def responder(self, reclamo):
        if reclamo.puntos < 5:
            print('Lo resuelve el Coordinador')
            return True
        else:
            return self.sucesor.responder(reclamo)

class SecretarioAcademico(Empleado):
    def responder(self, reclamo):
        if reclamo.puntos < 7:
            print('Lo resuelve el Secretario Académico')
            return True
        else:
            return self.sucesor.responder(reclamo)

class Director(Empleado):
    def responder(self, reclamo):
        print('Lo resuelve el Director')
        return True

class Reclamo:
    def __init__(self, puntos):
        self.puntos = puntos

def main():
    #Creando el reclamo
    reclamo = Reclamo(2)

    instReclamo = GestorDeReclamos()
    instReclamo.presentar_reclamo(reclamo)

if __name__ == '__main__':
    main()
