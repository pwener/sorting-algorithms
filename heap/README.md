# Heap

A heap is a data structure similar to a binary tree that satisfies the following properties:

> In a max heap, the value in each node must be greater than the values of its children. 
> Conversely, in a min heap, the value in each node must be lesser than or equal to the values of its children.

A common implementation of heaps involves the use of arrays, where each child can be identified by the positions 2i and 2i+1.

- The left child of a node at position i is located at 2i.
- The right child is located at 2i + 1.

Due to this arrangement, the root of the heap is positioned at index 1, and index 0 is not used. Otherwise, the left child would have the same position as its parent.

### Other properties

- The parent position is at i // 2;
- When a new element is inserted, it is possible for the heap property to be violated;
- To fix and construct a heap, it is necessary to perform the same process, typically referred to as "heapify."
- To transform an array into a heap, you can begin with the element at a[k], where k = N // 2, and proceed upwards to the element at a[1], heapifying each element consecutively.
- From the same array, we can generate different heaps by heapifying the elements in different orders.

### References

- https://staffwww.fullcoll.edu/aclifton/cs133/lecture-11-binary-heaps.html
- https://algs4.cs.princeton.edu/24pq/
- https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/heaps/