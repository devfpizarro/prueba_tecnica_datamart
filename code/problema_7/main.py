
def removeDuplicates(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

#---------------------------------------------------------------- 
#---------------------------------------------------------------- 

lista = [1, 2, 2, 3, 4, 4, 5, 5]
print(f'resultado: {removeDuplicates(lista)}') # Salida: [1, 2, 3, 4, 5]