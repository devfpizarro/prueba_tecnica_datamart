
def busquedaBinaria(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1
    
    # Caso base: Si el intervalo es inválido, el número no está en la lista
    if inicio > fin:
        return False
    
    # Calculamos el índice medio
    medio = (inicio + fin) // 2
    
    # Comprobamos si el número objetivo está en el medio
    if lista[medio] == objetivo:
        return True
    # Si el número objetivo es menor que el valor medio, buscamos en la mitad izquierda
    elif lista[medio] > objetivo:
        return busquedaBinaria(lista, objetivo, inicio, medio - 1)
    # Si el número objetivo es mayor que el valor medio, buscamos en la mitad derecha
    else:
        return busquedaBinaria(lista, objetivo, medio + 1, fin)

#---------------------------------------------------------------- 
#---------------------------------------------------------------- 

lista = [1, 3, 5, 7, 9, 11, 13, 15]
objetivo = 7

print(f'El número está en la lista: {busquedaBinaria(lista, objetivo)}')