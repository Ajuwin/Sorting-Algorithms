def quickSort(arr):
    
    length = len(arr)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    greater_elements = []
    smaller_elements = []

    for element in arr:
        if element > pivot:
            greater_elements.append(element)
        else:
            smaller_elements.append(element)

    return quickSort(smaller_elements) + [pivot] + quickSort(greater_elements)

# Driver code
array = [64, 34, 25, 12, 22, 11, 90] 
print(quickSort(array))
