def quick_sort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quick_sort(A, lo, p - 1)
        quick_sort(A, p + 1, hi)


def partition(A, left, right):
    pivot = A[right]
    
    pointer = left

    for i in range(left, right):
        if A[i] <= pivot:
            A[i], A[pointer] = A[pointer], A[i]
            pointer = pointer + 1
    
    A[pointer], A[right] = A[right], A[pointer]

    return pointer


# arr = [10, 2, 3, 1, 5, 6, 7, 8, 9, 4]

arr = [2, 3, 1, 5, 4]

quick_sort(arr, 0, len(arr) - 1)

print(arr)