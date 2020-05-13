def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
lista = [1, 5, 2, 4, 3, -1]
print(BubbleSort(lista))