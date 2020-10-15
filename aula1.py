#Exercicio 1.1
def comprimento(lista):
    if lista == []:
        return 0
    return 1+comprimento(lista[1:])

#Exercicio 1.2
def soma(lista):
    if lista==[]:
        return 0
    return lista[0]+soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
    if lista:
        if elem == lista[0]:
            return True
        else:
            return existe(lista[1:],elem)
    else:
	    return False

#Exercicio 1.4
def concat(l1, l2):
    if l2:
        l1.append(l2[0])
        return concat(l1,l2[1:])
    else:
        return l1

#Exercicio 1.5
def inverte(lista):
    if lista:
        return [lista[-1]] + inverte(lista[:-1])
    else:
        return lista

#Exercicio 1.6
def capicua(lista):
    if lista:
        if lista[0] == lista[-1]:
            return capicua(lista[1:-1])
        else:
            return False
    else:
        return True

#Exercicio 1.7
def explode(lista):
    if lista:
        return lista[0] + explode(lista[1:])
    else:
        return lista

#Exercicio 1.8
def substitui(lista, original, novo):
    if lista ==[]:
        return []
    else:
        if(lista[0] == original):
            lista[0] = novo
        
        return [lista[0]] + substitui(lista[1:],original,novo)

#Exercicio 1.9
def junta_ordenado(lista1, lista2):
    if lista2:
        if lista1:
            if lista2[0] < lista1[0]:
                return [lista2[0]] + junta_ordenado(lista1, lista2[1:])
            else:
                return [lista1[0]] + junta_ordenado(lista1[1:], lista2)
        else:
            return lista2
    else:
        return lista1

#Exercicio 2.1
def separar(lista):
    if lista ==[]:
        return [],[]

    r = separar(lista[1:])
    return [lista[0][0]] + r[0], [lista[0][1]] + r[1]

#Exercicio 2.2
def remove_e_conta(lista, elem):
    if lista==[]:
        return ([],0)
    else:
        (l,num) = remove_e_conta(lista[1:],elem)
        if lista[0] == elem:
            return l,1+num
        else:
            return [lista[0]] + l, 0+num

#Exercicio 3.1
def cabeca(lista):
    if lista==[]:
        return None
    return lista[0]

#Exercicio 3.2
def cauda(lista):
    if lista==[]:
        return None
    return lista[1:]

#Exercicio 3.3
def juntar(l1, l2):
    if len(l1) != len(l2):
        return None
    else:
        if l1:
            return [(l1[0],l2[0])] + juntar(l1[1:],l2[1:])
        else:
            return l1

#Exercicio 3.4
#erro
def menor(lista):
    if lista==[]:
        return None
    first = lista[0]
    rest = lista[1:]
    s = menor(rest)

    if first < s:
        return first
    
    return s

#Exercicio 3.6
def max_min(lista):
    if lista==[]:
        return None
    else:
        a = menor(lista)
        if lista[0]>lista[1]:
            b = lista[0]
            return (a,b)
        else:
            return max_min(lista[1:])



