# Bubble sort

```python
    def bubble_sort():
        n = len(arr)
        for i in range(n - 1, 0, -1):
            for j in range(0, i):
                if arr[j] > arr[j+1]:
                    swap(j, j+1)
```

### Explaining

- We start iterating in an inverse way, basically because this algorithm separate the bigger elements into the end.
- Inside we have a loop in a opposite direction, that compare elements in pairs, and swap them based on comparative operator.

> :bulb: we can think that the first loop give to us a sorted part in each iteration, like the image above ilustrate as black squares.

<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif">
</p>


### Definition

| Comparison-based | Stable | Recursive | In-place | Adaptive | Online |
| :---:  | :---:  | :---:  | :---: |:---:  | :---: |
| :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: |  :x: |

- Need some conditional operator to sort.
- Equals values should preserve their position, which makes it stable.
- Don't calls any process recursively. So isn't recursive.
- It's in-place because the algorithm just change the input data.
- A pre-sorted list will spent less time. So it's adaptative.
- The algorithm will not process correctly new elements after process, it's not online.

# References

- [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)