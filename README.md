# Python Array List

A Python 3 implementation of Array List Data structure.

## Description

Array List in Python 3. Uses the Python list structure as the underlaying array. Adding an element beyond this starting capacity, the capacity is doubled and old array copied over. Supports str() and == for other Array List Objects and Python lits.

Methods
* __init__(capacity -Optional) - Constructor, capacity default size 10.
* isEmpty() - Checks if the array list is empty.
* size() - Returns the number of elemets in the array list.
* get(index) - Returns element at index.
* add(element, index -Optional) - Insert an element at the end of the array list. If index is provided, insert the element at index.
* remove (index -Optional) - Removes and returns the element at the end of the array list. If index is provided, the element at index is removed and returned.
* set (index, element) - Replaces the element at index with new element.
* clear() - Removes all elements in the array list. Maintains the current capacity.

### Concurrency

*Currently not thread safe.*

## Unit Tests

To run unit tests for ArrayList, run the following.
```
python TestArrayList.py
```

## References
* [Outline Source](https://cs.pomona.edu/classes/cs62/assets/slides/L6-arraylists.pdf)
