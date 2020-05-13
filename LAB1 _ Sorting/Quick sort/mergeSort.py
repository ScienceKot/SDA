class Sort:
    def __init__(self, arr):
        self.arr = arr
    def mergeSort(self, arr):
        if len(arr)>1:
            print("1")
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0
            while i< len(left) and j <len(right):
                if left[i] < right[i]:
                    self.arr[k] = left[i]
                    i+=1
                else:
                    self.arr[k] = right[j]
                    j+=1
                k+=1
            while i < len(left):
                self.arr[k] = left[i]
                i+=1
                k+=1
            while j<len(right):
                self.arr[k] = right[j]
                j+=1
                k+=1
arr = [1, 5, 2, 4, 3, -1]
sort = Sort(arr)
sort.mergeSort(arr)
print(sort.arr)