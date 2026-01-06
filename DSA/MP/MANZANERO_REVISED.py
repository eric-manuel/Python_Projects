def bubbleSort(arr): 
    indexLength = len(arr)-1
    Sorted = False
    while not Sorted:
        Sorted = True
        for i in range(0, indexLength):
            if arr[i] > arr[i+1]:
                Sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def uniqueArray(arr):
    return list(set(arr))

def main():
    A = [5, 3, 8, 5, 2, 3, 9, 1, 8]
    print("Original Array:", A)
    
    sortedArray = bubbleSort(A)
    print("Sorted Array:", sortedArray)
    
    B = uniqueArray(sortedArray)
    print("Array after removing duplicates:", B)
    
main()