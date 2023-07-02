def selection_sort(array: list):
    size = len(array)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])

def print_list(array: list):
    for el in array:
        print(el, end=" ")

nums = [5, 1, 8, 92, -1, 30]

print("Original list:")
print_list(nums)

selection_sort(nums)

print("\nSorted list:")
print_list(nums)