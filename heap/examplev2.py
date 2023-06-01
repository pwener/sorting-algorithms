# this is a insert function that fix the heap after the insertion
def insert(arr, i):
    arr.append(i)
    fix_up(arr, len(arr)-1)


# this is a fix_up function that fix the heap after the insertion
def fix_up(arr, n):
    pointer = n

    while pointer != 1:
        parent = pointer//2

        if arr[pointer] <= arr[parent]:
            break

        arr[pointer], arr[parent] = arr[parent], arr[pointer]
        pointer = parent


def build_heap(arr):
    heap = []
    heap.insert(0, None)

    for element in arr:
        insert(heap, element)

    return heap


# heap condition
def is_heap(A):
    for i in range(2, len(A)):
        if A[i] > A[i // 2]:
            return False
    return True


# the same array from the previous example
array = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]

res = build_heap(array)

# different output from the previous example
print("arr:", array)
print("heap:", res)
print("is heap:", is_heap(res))
