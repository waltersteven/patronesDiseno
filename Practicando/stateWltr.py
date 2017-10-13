class EstadoAlumno:
    def __init__(self,alumno):
        self.alumno = alumno
    def matriculado(self):
        pass
    def terminar_ciclo(self):
        pass
    def expulsado(self):
        pass
    def suspendido(self):
        pass
    def egresado(self):
        pass
    def terminar_suspension(self):
        pass

class EstadoNoMatriculado(EstadoAlumno):
    def matriculado(self):
        self.alumno.estado = EstadoMatriculado(self.alumno) #self.alumno se refiere a EstadoAlumno que es un Alumno y .estado se refiere al atributo del Alumno
    def expulsado(self):
        self.alumno.estado = EstadoExpulsado(self.alumno)

class EstadoMatriculado(EstadoAlumno):
    def terminar_ciclo(self):
        self.alumno.estado = EstadoNoMatriculado(self.alumno)
    def egresado(self):
        self.alumno.estado = EstadoEgresado(self.alumno)
    def expulsado(self):
        self.alumno.estado = EstadoExpulsado(self.alumno)
    def suspendido(self):
        self.alumno.estado = EstadoSuspendido(self.alumno)

class EstadoExpulsado(EstadoAlumno):
    pass

class EstadoSuspendido(EstadoAlumno):
    def terminar_suspension(self):
        self.alumno.estado = EstadoMatriculado(self.alumno)

class EstadoEgresado(EstadoAlumno):
    pass

class Alumno:
    def __init__(self):
        self.estado = EstadoNoMatriculado(self) #Al momento de pasarle self se le pasa al constructor de EstadoAlumno

def main():
    alumno = Alumno() # alumno.estado? => NoMatriculado
    alumno.estado.matricular() # alumno.estado? => Matriculado
    alumno.estado.matricular() # alumno.estado? => Matriculado
    alumno.estado.terminar_ciclo() # alumno.estado? => NoMatriculado
    alumno.estado.egresar() # alumno.estado? => NoMatriculado
    alumno.estado.expulsar() # alumno.estado? => Expulsado

if __name__ = '__main__':
    main()
