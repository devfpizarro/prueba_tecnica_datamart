
from concurrent.futures import ThreadPoolExecutor

def busquedaBinaria(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1
    
    if inicio > fin:
        return False

    medio = (inicio + fin) // 2
  
    if lista[medio] == objetivo:
        return True
    elif lista[medio] > objetivo:
        return busquedaBinaria(lista, objetivo, inicio, medio - 1)
    else:
        return busquedaBinaria(lista, objetivo, medio + 1, fin)

def processLists(list1, list2, max_workers=4):
    list1.sort()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(lambda x: busquedaBinaria(list1, x), list2))
    
    return results

#---------------------------------------------------------------- 
#---------------------------------------------------------------- 

domain = [100, 3, 30, 6, 14, 56, 91, 27, 10]  
targets = [3, 6, 11, 14]
maxWorkers = 4  

print(f"Resultados de la búsqueda: {processLists(domain, targets, maxWorkers)}")

#---------------------------------------------------------------- 
#---------------------------------------------------------------- 

#-- Explicación

# Impacto de la complejidad:

#     Búsqueda secuencial: Tiene una complejidad de O(n), lo que significa que, en el peor de los casos, debe recorrer toda la lista 
#                          para encontrar el elemento o determinar que no está.

#     Búsqueda binaria: Tiene una complejidad de O(log n), lo que es significativamente más rápido cuando la lista es grande.

#     Paralelización: Si hay m elementos en la segunda lista y se usan workers en paralelo, el tiempo total de ejecución
#                     sería O(m * log n / w), lo que significa que la paralelización ayuda a distribuir el trabajo, reduciendo el
#                     tiempo de procesamiento si w es suficientemente grande.

# Consideraciones adicionales:

#     La paralelización solo tiene sentido si las listas son grandes, ya que tiene un costo de gestión de hilos.
#     La ordenación de la primera lista tiene un costo de O(n log n), pero esta ordenación solo se realiza una vez,
#     y la búsqueda binaria subsecuente es mucho más rápida.