import sys

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

def main():
    # $ python adapter.py pepito 36 xml
    # <persona nombre="pepito" edad="36/>
    # $ python adapter.py pepito 36 json
    # { "nombre" : "pepito", "edad":36 }
    nombre = sys.argv[1]
    edad = sys.argv[2]
    tipo = sys.argv[3]

    persona = Persona(nombre, edad)

    if tipo == 'xml':
        xml='<persona nombre="%s" edad="%s" />'
        xml = xml % (persona.nombre, persona.edad)
        print(xml)
    elif tipo == 'json':
        json= '{ "nombre":"$s", "edad": $s }'
        json = json % (persona.nombre, persona.edad)
        print(json)
    else:
        print('Formato invalido')
if __name__=='__main__':
    main()
