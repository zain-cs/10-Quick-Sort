def partition(arr, low, high):
    pivot = arr[high]      # choose last element as pivot
    i = low - 1            # pointer for smaller element
    
    for j in range(low, high):  # traverse from low to high-1
        if arr[j] <= pivot:     # if current element <= pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap
    
    # place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)  # partition index
        quick_sort(arr, low, pivot_index - 1)    # sort left
        quick_sort(arr, pivot_index + 1, high)   # sort right


# Example
arr = [10, 7, 8, 9, 1, 5]
print("Original:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted:", arr)
