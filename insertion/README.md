# Insertion sort

Let's look to this _pseudo-python_ example:

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
- Imagine that we have a pointer(index of element) in each iteration that needs to iterate over the array to evaluate each element compared to the previous one.
- Now, while this pointer is higher than 0 and the element of pointer is lesser than the previous element, we need to swap them.
- :bulb: Maybe it is easier to think that in each step, we already sorted the previous elements, in the current, we just need to swap if we found something(previously) lesser than pointer element.
- Pointer will always running backward, remember that the **while loop** is inside of a **for loop**. So, thinking in the last iterations, we can see that if pointer is lesser that all previous values, we will iterating along all array.

<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif">
</p>

### Definition

| Comparison-based | Stable | Recursive | In-place | Adaptive | Online |
| :---:  | :---:  | :---:  | :---: |:---:  | :---: |
| :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |

- Uses "lesser than" operator to sort.
- Equals values should be preserve their position, so it's stable.
- Don't calls any process recursively. So isn't recursive.
- The algorithm could change the array without knowning the initial input. So, it's _in-place_.
- If data continue coming, the algorithm keep working. So it's online!

## Hackerrank

- https://www.hackerrank.com/challenges/insertionsort1/problem
- https://www.hackerrank.com/challenges/insertionsort2/problem

## References

- [Time and space complexity analysis (big-O notation)](https://www.udemy.com/course/complexity-analysis/learn/lecture/24722488#overview)
- [Insert sort](https://pt.wikipedia.org/wiki/Insertion_sort)