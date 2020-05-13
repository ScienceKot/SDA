def heap(arr, length, i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < length and arr[i] < arr[left]:
        largest = left
    if right < length and arr[largest] < arr[right]:
        largest = right
    if largest !=i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, length, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heap(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)
    return arr
lista = [1, 5, 2, 4, 3, -1]
print(heapSort(lista))