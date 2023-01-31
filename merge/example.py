arr = [3, 1, 8, 2, 5, 10, 4, 0, 6, 7]

def merge(left, right):
    r = []

    while len(left) > 0 and len(right) > 0:
        if right[0] > left[0]:
            r.append(left.pop(0))
        else:
            r.append(right.pop(0))

    r.extend(left)
    r.extend(right)

    return r

def sort(a):
    if len(a) == 1:
        return a

    mid = len(a) // 2

    left = sort(a[:mid])
    right = sort(a[mid:])

    return merge(left, right)

r = sort(arr)
print(r)