import math

#Exercicio 4.1
impar = lambda n : n%2 != 0

#Exercicio 4.2
positivo = lambda n : n>0

#Exercicio 4.3
comparar_modulo = lambda x,y : abs(x) < abs(y)

#Exercicio 4.4
cart2pol = lambda x,y : (math.sqrt(x**2 + y**2), math.asin(y/(x**2 + y**2)))

#Exercicio 4.5
ex5 = lambda f,g,h : lambda x,y,z : h(f(x,y),g(y,z))

#Exercicio 4.6
def quantificador_universal(lista, f):
    if lista==[]:
        return True
    else:
        if (len(lista)==1):
            if f(lista[0]):
                return True
            else:
                return False
        else:
            return quantificador_universal(lista[1:],f)

#Exercicio 4.9
def ordem(lista, f):
    if (lista == []):
        return []

    if (len(lista) == 1):
        return lista[0]

    if (f(lista[0], lista[1])):
        return ordem([lista[0]] + lista[2:], f)

    return ordem([lista[1]] + lista[2:], f)

#Exercicio 4.10
def filtrar_ordem(lista, f):
    elem = ordem(lista, f)
    outrosElems = [e for e in lista if e != elem]
    return elem, outrosElems

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    if lista == []:
        return []
    elem, outrosElems = filtrar_ordem(lista, ordem)
    return [elem] + ordenar_seleccao(outrosElems, ordem)



