arr = [3, 1, 8, 2, 5, 10, 4, 0, 6, 7]

def swap(i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

def insert_sort():
    for i in range(1, len(arr)):
        pointer = i
        previous = pointer - 1

        while pointer > 0 and arr[pointer] < arr[previous]:
            swap(previous, pointer)
            pointer = pointer - 1
            previous = pointer - 1

insert_sort()
print(arr)