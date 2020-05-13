def shellSort(arr):
    length = len(arr)
    gap = length//2

    while gap > 0:
        for i in range(gap, length):
            temp = arr[i]
            j=i
            while j>=gap and arr[j-gap]>temp:
                arr[j] = arr[j-gap]
                j-=gap
            arr[j] = temp
        gap//=2
    return arr
arr = [12, 34, 54, 2, 3]
print(shellSort(arr))