import math as mt



def biseccion(a,b):

    """
    Divide la funcion en un intervalo mas pequeño (Biseccion)

    Parameters
    ----------
    a : float
        Limite inferior del intervalo
    b : float
        Limite superior del intervalo


    Returns
    -------
    float
        Aproximacion a la raiz de la funcion
    """

    diferencia = 1

    
    #Esta variable controla la precision con que se quiere calcular la raiz
    #inicialmente es 1x10^(-5) = 0.00005
    #si se requiere mayor precision se puede modificar este valor
    precision = 1*(10**(-5))

    while (diferencia > precision ):
        #calculamos el valor medio
        c = (a+b)/2
        d = fx(a) * fx(c)
        #si se encuentra en el primer intervalo se actualiza el limite final a el valor medio
        if(d < 0):
            b = c
        else:
            d = fx(c) * fx(b)
            #si la raiz se encuentra en el segundo intervalo se actualiza el limite inicial al valor medio
            if (d < 0):
                a = c
        diferencia = abs(a - b)
    return (a)



def fx(x):

    """
    Evalua una funcion f(x) en el punto x
        
    se puede cambiar esta funcion, por ejemplo para usar la funcion cos(x)
    return mt.cos(x)

    Parameters
    ----------
    x : float
        Punto donde queremos evaluar la funcion

    Returns
    -------
    float
        Valor de la funcion en el punto x
    """

    return mt.sin(x)


def busca_intervalo(a,b):
    """
    Decide si hay una raiz en el intervalo (a,b)

    Parameters
    ----------
    a : float
        Limite inferior del intervalo
    b : float
        Limite superior del intervalo


    Returns
    -------
    False
        Si no existe una raiz en el invervalo

    True
        Si existe una raiz en el intervalo
    """

    c = fx(a) * fx(b)
    if(c < 0):
        return True
    else :
        return  False


def main():
    #Lista para guardar las raices
    raices = []

    a = float(input("ingresa el limite inferior del intervalo \n"))
    b = float(input("ingresa el limite superior del intervalo \n"))



    #Si necesitamos intervalos mas pequeños podemos cambiar esta variable
    paso = 0.1


    #Si existe una raiz en los limites del intervalo las guardamos
    if (fx(a) == 0):
        raices.append(a)
    if (fx(b) == 0):
        raices.append(b)

    i = a + paso


    #El cliclo se detiene cuando llegamos al limite superior del intervalo
    while (i <= b):
        print("Buscando en el intervalo... (",a,",",i,")")
        if(busca_intervalo(a,i)):
            print("\t\t Hay una raiz \n\t\t Haciendo la biseccion...")
            r = biseccion(a,i)
            print("**********************************************************************\n*\t\t\t La raiz es: ", r
                  , "\n**********************************************************************")
            raices.append(r)

        a = round(i,3)
        i = round(a + paso,3)


    print("Metodo de biseccion terminado, desea imprimir las raices?? \n 1->Si \n 2->No")
    res = int(input())
    if (res == 1):
        print("Raices -> ",raices)



# Ejecuta la funcion principal
if __name__ == '__main__':
    main()