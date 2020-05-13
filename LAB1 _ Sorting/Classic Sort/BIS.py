def BS(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
    if start > end:
        return start
    mid = (start+end)//2
    if arr[mid]<val:
        return BS(arr, val, mid+1, end)
    elif arr[mid] > val:
        return BS(arr, val, start, mid-1)
    else:
        return mid
def BIS(arr):
    for i in range(1, len(arr)):
        j = BS(arr, arr[i], 0, i-1)
        arr = arr[:j] + [arr[i]] + arr[j:i] + arr[i+1:]
    return arr
lista = [1, 5, 2, 4, 3, -1]

print(BIS(lista))