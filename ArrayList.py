'''
based on https://cs.pomona.edu/classes/cs62/assets/slides/L6-arraylists.pdf

Standard Operations of ArrayList<E> class

• ArrayList(): Constructs an empty ArrayList with an initial capacity of 2 (can vary across
implementations, another common initial capacity is 10).
• ArrayList(int capacity): Constructs an empty ArrayList with the specified initial capacity.
• isEmpty(): Returns true if the ArrayList contains no elements.
• size(): Returns the number of elements in the ArrayList.
• get(int index): Returns the element at the specified index.
• add(E element): Appends the element to the end of the ArrayList.
• add(int index, E element): Inserts the element at the specified index and shifts the element
currently at that position (if any) and any subsequent elements to the right (adds one to their indices).
• E remove(): Removes and returns the element at the end of the ArrayList.
• E remove(int index): Removes and returns the element at the specified index. Shifts any
subsequent elements to the left (subtracts one from their indices).
• E set(int index, E element): Replaces the element at the specified index with the specified
element and returns the olde element.
• clear(): Removes all elements.
'''

class ArrayList:

    def __init__(self, capacity = 10):
        #Private fields
        self.__count = 0
        self.__capacity = capacity
        self.__array = [None]*capacity #pseudo array

    def isEmpty(self):
        return self.__count == 0

    def size(self):
        return self.__count

    def get(self, index):
        if index >= self.__count:
            raise IndexError("Index out of range.")

        return self.__array[index]

    def add(self, element, index=None): 

        #Call adding at a index version.
        if not index == None:
            self.__add_at_index(element, index)
            return

        #We're full. Create bigger array, copy elements, and add new element.
        if self.__count == self.__capacity:

            new_array = [None]*(self.__capacity*2)
            self.__capacity = self.__capacity*2
        
            i = 0
            while i < len(self.__array):
                new_array[i] = self.__array[i]
                i += 1
            new_array[i] = element
            self.__array = new_array
            self.__count +=1 
            
        #There is nothing in the array, add new element.
        elif self.isEmpty():
            self.__array[self.__count] = element
            self.__count += 1
        #There already is elements in the array, add new element.
        else:
            self.__array[self.__count] = element
            self.__count += 1

    def __add_at_index(self, element, index=None):
        
        #Do we have room to add one more element?
        if self.__count + 1 < self.__capacity:

            #Start from the back of the array and move the elements forward by 1. This will end at the index location for the new element.
            for i in range(self.__count-1, index-1, -1):
                self.__array[i+1] = self.__array[i]
            self.__array[index] = element



    def remove(self, index=None):
        pass

    def __remove_at_index(self, index):
        pass

    def set(self, index, element):
        if index >= self.__count:
            raise IndexError("Index out of range.")
        
        old_element = self.__array[index]
        self.__array[index] = element
        return old_element

    def clear(self):
        self.__count = 0
        self.__array = [None] * self.__capacity 

    def __str__(self):
        return ''

    def __eq__(self):
        return False

    



