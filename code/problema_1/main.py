
def mergeArrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged

#---------------------------------------------------------------- 
#---------------------------------------------------------------- 

arr1 = [10, 30, 50, 70]
arr2 = [20, 40, 60, 80]

print(f'resultado: {mergeArrays(arr1, arr2)}')