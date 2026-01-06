def bubbleSort(arr): # Bubble Sort
    indexLengh = len(arr)-1
    for i in len(arr)-1:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def uniqueArray(arr): # Insertio Sort
    indexLength = len(arr)-1
    for i in indexLength:
        if arr[i] == arr[i+1]:
            arr =  arr.pop(arr[i])
    return arr

def main():
    A = [5, 3, 8, 5, 2, 3, 9, 1, 8]
    sortedArray = bubbleSort(A)
    print("Original Array:", A)
    print("Sorted Array:", sortedArray)
    
    B = uniqueArray(sortedArray)
    print("Array after removing duplicates:", B)
    