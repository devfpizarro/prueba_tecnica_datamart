
def findMedian(arr):
    arr.sort()
    n = len(arr)
    mid = n // 2 

    if n % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        return arr[mid]

#---------------------------------------------------------------- 
#---------------------------------------------------------------- 

arr1 = [3, 1, 2, 5, 4]
print(f'resultado: {findMedian(arr1)}')