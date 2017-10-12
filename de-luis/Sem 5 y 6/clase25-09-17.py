#Patron Singleton 25/09/17

class Alumno:
    instancia= None
    codigo=None

    @classmethod
    def get_instance(cls):
        if cls.instancia==None:
            cls.instancia=Alumno()
        return cls.instancia

    #def __init__(self,codigo):
    #    self.codigo = codigo


def main():
    #alu1=alumno('20143434')
    Alumno.codigo='23432423'
    alu1=Alumno.get_instance()
    alu2=Alumno.get_instance()
    alu1.codigo='2016772'

    Alumno.get_instance().codigo

    print(alu2.codigo)


if __name__=='__main__':
    main()
