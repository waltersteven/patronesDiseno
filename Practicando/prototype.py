import copy

class Alumno:
    def __clone__(self): #preguntar
        return copy.deepcopy(self)

def main():
    alu1 = Alumno()
    alu1.codigo = '20140989'

    alu2 = alu1.__clone__()

    print(alu1.codigo)
    print(alu2.codigo)

if __name__ == '__main__':
    main()
