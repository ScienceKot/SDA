arr = [1, 5, 2, 4, 3, -1]
def partision(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <=pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
def qsort(low, high):
    global arr
    if low < high:
        part_index = partision(arr, low, high)
        qsort(low, part_index-1)
        qsort(part_index+1, high)

qsort(0, len(arr)-1)
print(arr)