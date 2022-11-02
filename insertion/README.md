# Insertion sort

| Comparison-based | Stable | Recursive | In-place | Adaptive | Online |
| :---:  | :---:  | :---:  | :---: |:---:  | :---: |
| X | X | X | X | X | X |


## Algorithm

Ordering example:

```python
    for i in range(1, length):
        pointer = i
        previous = pointer - 1

        while pointer > 0 and arr[pointer] < arr[previous]:
            swap(previous, pointer)
            pointer = pointer - 1
            previous = pointer - 1
```
### Explaining

- We should start iterating along the input array.
- Imagine that we have a pointer in each iteration that needs to iterate over the array to evaluate each element compared to the previous one.
- Now, while this pointer is higher than 0 and the element of pointer is lesser than the previous element, we need to swap them.
- > Maybe it is easier to think that in each step, we already sorted the previous elements, in the current, we just need to swap if we found something lesser than pointer.
- Pointer will always running backward, remember that the **while loop** is inside of a **for loop**. So, thinking in the last iterations, we can see that if pointer is lesser that all previous values, we will iterating along all array.
- 

![example of insert sort, font: wikipedia](https://pt.wikipedia.org/wiki/Insertion_sort#/media/Ficheiro:Insertion-sort-example-300px.gif)