# Python Lists and Tuples

This repository covers essential concepts about Python lists, tuples, and sequences. Below is an overview of the topics explained:

---

### General

* Introduction to fundamental data structures in Python.

### What are Lists and How to Use Them

* Lists are mutable, ordered collections used to store multiple items.
* Example:

  ```python
  my_list = [1, 2, 3, "apple"]
  print(my_list)
  ```

### Differences and Similarities Between Strings and Lists

* **Similarity:** Both are ordered sequences.
* **Difference:** Lists are mutable; strings are immutable.

### Most Common Methods of Lists and How to Use Them

* `.append(item)`: Adds item to end of list.

  ```python
  my_list.append(4)
  ```
* `.remove(item)`: Removes first occurrence of item.

  ```python
  my_list.remove(2)
  ```
* `.pop(index)`: Removes and returns item at index.

  ```python
  item = my_list.pop(0)
  ```

### How to Use Lists as Stacks and Queues

* **Stack (LIFO):** Use `.append()` and `.pop()` methods.

  ```python
  stack = []
  stack.append(1)
  stack.pop()
  ```
* **Queue (FIFO):** Use `collections.deque`.

  ```python
  from collections import deque
  queue = deque()
  queue.append(1)
  queue.popleft()
  ```

### What are List Comprehensions and How to Use Them

* Concise way to create lists.
* Example:

  ```python
  squares = [x**2 for x in range(10)]
  ```

### What are Tuples and How to Use Them

* Immutable, ordered collections.
* Example:

  ```python
  my_tuple = (1, 2, "apple")
  ```

### When to Use Tuples Versus Lists

* **Tuples:** When immutability is required.
* **Lists:** When items need modification.

### What is a Sequence

* An ordered collection of items.
* Examples: strings, lists, tuples.

### What is Tuple Packing

* Grouping multiple values into a single tuple.
* Example:

  ```python
  packed_tuple = 1, 2, 3
  ```

### What is Sequence Unpacking

* Extracting values from a sequence into variables.
* Example:

  ```python
  a, b, c = packed_tuple
  ```

### What is the del Statement and How to Use It

* Removes items by index or slices.
* Example:

  ```python
  del my_list[0]  # removes first item
  del my_list[1:3]  # removes items from index 1 to 2
  ```

---

