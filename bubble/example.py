arr = [5, 3, 1, 4, 8, 2]

def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort():
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                swap(j, j+1)

bubble_sort()
print(arr)