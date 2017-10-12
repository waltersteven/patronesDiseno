import sys

class RecetarioComidaMarina:
    def obtener_recetas(self):
        print('Ceviche')
        print('Mariscos')

class RecetarioComidaCriolla:
    def obtener_recetas(self):
        print('Lomo saltado')
        print('Chifa')

#escribiendo clase Factory
class RecetarioComidaFactory:
    def obtener_recetarioComida(self, tipo_comida):
        if tipo_comida == 'marina':
            return RecetarioComidaMarina()
        elif tipo_comida == 'criolla':
            return RecetarioComidaCriolla()
        else:
            return None

def main():
    factory = RecetarioComidaFactory()
    recetarioDeComida = factory.obtener_recetarioComida(sys.argv[1])
    recetarioDeComida.obtener_recetas()

if __name__ == '__main__':
    main()
