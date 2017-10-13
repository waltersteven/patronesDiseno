#cambias el decorado de la función pero sin meterme en su implementación.
def f_decorator(func_a_decorar):
    def f_wrapper(dicc): #los mismos parametros que tiene la funcion a decorar
        return func_a_decorar(dicc).upper()
    return f_wrapper

@f_decorator
def formatear_xml(diccionario):
    cad = '<data>\n'
    for key, value in diccionario.items():
        cad = cad + '\t<%s>%s</%s>\n' % (key, value, key)
        cad = cad + '</data>\n'
    return cad


def main():
    persona = {
        "nombre": "Billy",
        "edad": 30
    }
    print(formatear_xml(persona))

if __name__ == '__main__':
    main()
