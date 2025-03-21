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
        self.count = 0
        self.capacity = capacity
        self.array = [None]*capacity #pseudo array

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def get(self, index):
        if index >= self.count:
            raise IndexError("Index out of range.")

        return self.array[index]

    def add(self, element, index=None): 

        #Call adding at a index version.
        if not index == None:
            self.__add_at_index(element, index)
            return

        #We're full. Create bigger array, copy elements, and add new element.
        if self.count == self.capacity:

            new_array = [None]*(self.capacity*2)
            self.capacity = self.capacity*2
        
            i = 0
            while i < len(self.array):
                new_array[i] = self.array[i]
                i += 1
            new_array[i] = element
            self.array = new_array
            self.count +=1 
            
        #There is nothing in the array, add new element.
        elif self.isEmpty():
            self.array[self.count] = element
            self.count += 1
        #There already is elements in the array, add new element.
        else:
            self.array[self.count] = element
            self.count += 1

    def __add_at_index(self, element, index=None):
        
        #Do we have room to add one more element?
        if self.count + 1 < self.capacity:

            for i in range(self.count-1, index-1, -1):
                self.array[i+1] = self.array[i]
            self.array[index] = element



    def remove(self, index=None):
        pass

    def __remove_at_index(self, index):
        pass

    def set(self, index, element):
        pass 

    def clear(self): 
        pass

    def __str__(self):
        return ''

    def __eq__(self):
        return False

    



