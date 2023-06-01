# This is a example of heapify function that can be used to build a heap.
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


# build a heap from an array using in-place strategy
def build_heap(arr):
    arr.insert(0, None)

    start = len(arr) // 2

    for i in range(start, 0, -1):
        heapify(arr, len(arr), i)


# heap condition
def is_heap(A):
    for i in range(2, len(A)):
        if A[i] > A[i // 2]:
            return False
    return True


array = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]

print("arr:", array)
build_heap(array)
print("heap:", array)
print("is heap:", is_heap(array))
