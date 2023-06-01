# To use the definition described we are considering the first node as 1,
# that way we can calculate the left and right nodes of a node i as: 2*i and 2*i+1.
# This strategy is using in-place sorting, so we are not creating a new array to store the sorted elements.
def heapify(arr, size, i):
    greatest = i

    left = 2 * i
    right = 2 * i + 1

    if left < size and arr[left] > arr[greatest]:
        greatest = left

    if right < size and arr[right] > arr[greatest]:
        greatest = right

    if i != greatest:
        arr[i], arr[greatest] = arr[greatest], arr[i]
        heapify(arr, size, greatest)


# This function utilizes an in-place strategy where it disregards the elements after index i.
# It focuses solely on sorting the elements before index i by employing the heapify operation.
def sortdown(arr, i):
    arr[1], arr[i] = arr[i], arr[1]
    heapify(arr, i, 1)


def heap_sort(arr):
    # we are considering the first node as 1
    arr.insert(0, None)

    start = len(arr) // 2

    # create the heap
    for i in range(start, 0, -1):
        heapify(arr, len(arr), i)

    # sort the heap
    for i in range(len(arr)-1, 1, -1):
        sortdown(arr, i)

    # remove the unused first element
    arr.pop(0)


array = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]

heap_sort(array)

print(array)

