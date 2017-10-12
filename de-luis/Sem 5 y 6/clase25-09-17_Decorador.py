#cambias el decorado de la función pero sin meterme en su implementación.

def formatear_xml(diccionario):
    cad = '<data>\n'
    for key, value in diccionario.items():
        cad = cad + '\t<%s>%s</%s>\n' % (key, value, key)
        cad = cad + '</data>\n'
    return cad

def f_decorator(func_a_decorar):
    def f_wrapper(dicc): #los mismos parametros que tiene la funcion a decorar
        return func_a_decorar(dicc).upper()
    return f_wrapper
    
def main():
    persona = {
        "nombre": "Billy",
        "edad": 30
    }

    #print(formatear_xml(persona))
    f_decorada = f_decorator(formatear_xml)
    print(f_decorada(persona)) #imprime el return de la funcion f_wrapper

if __name__ == '__main__':
    main()
