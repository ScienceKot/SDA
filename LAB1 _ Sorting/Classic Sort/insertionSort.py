def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
lista = [1, 5, 2, 4, 3, -1]
print(insertionSort(lista))