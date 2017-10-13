class Alumno: #El uso de Singleton es para que una clase tenga una única instancia.
    instancia = None

    @classmethod #pasamos la clase como primer argumento en vez de la instancia de la clase (self)
    def get_instance(cls):
        if cls.instancia == None:
            cls.instancia = Alumno()
        return cls.instancia

def main():
    alu1 = Alumno.get_instance()
    alu2 = Alumno.get_instance()

    alu1.codigo = '20140989'

    print(alu1.codigo)
    print(alu2.codigo)

if __name__ == '__main__':
    main()
