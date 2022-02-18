def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0 
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))

#cool algorithm
def insertion_sort(array):
    for index in range(1, len(array)):
        current_value = array[index]
        current_position = index

        while current_position > 0 and array[current_position - 1] > current_value:
            array[current_position] = array[current_position - 1]
            current_position -= 1

        array[current_position] = current_value

#main
array = [5, 3, 2, 0, -1, 15]
insertion_sort(array)
print(array)