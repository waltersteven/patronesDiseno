def f_decorator(func_a_decorar):
    def f_wrapper(dicc):
        return func_a_decorar(dicc).upper() #Cómo le pasa el nombre de la func_a_decorar??
    return f_wrapper

def formatear_xml(diccionario):
    cad = '<data>\n'
    for key, value in diccionario.items():
        cad = cad + '\t<%s>%s</%s>\n' % (key, value, key)
    cad = cad + '</data>\n'
    return cad

def main():
    persona = {
        "nombre": "Walter",
        "edad": 20
    }

    print(formatear_xml(persona))

    f_decorada = f_decorator(formatear_xml)
    print(f_decorada(persona))

if __name__ == '__main__':
    main()
