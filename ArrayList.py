'''
based on https://cs.pomona.edu/classes/cs62/assets/slides/L6-arraylists.pdf
'''

class EmptyError(Exception):
       '''
       Empty Error exception for when ArrayList is empty and an element is tried to be removed.
       '''
       def __init__(self, message):
           self.message = message


class ArrayList:
    '''
    A Python impelentation of the Array List data structure.
    '''

    def __init__(self, capacity = 10):
        '''
        Constructor for ArrayList.

        Parameters:
            capacity (int): The starting size of the array list. Default 10 elements.
        '''
        #Private fields
        self.__count = 0
        self.__capacity = capacity
        self.__array = [None]*capacity #pseudo array

    def __makeEmptyArray(self, size):
        '''
        Returns a empty pseudo array of provided size.
        
        Parameters:
            size (int): Capacity of new internal array.

        Returns:
            list: Empty Python list filled with None.
        '''
        return [None]*(size)

    def isEmpty(self):
        '''
        Checks is the Array List is empty.

        Returns:
            boolean: True if empty.
        '''
        return self.__count == 0

    def size(self):
        '''
        Returns the number of elements in the Array List.

        Returns:
            int: The number of elemets in the Array List.
        '''
        return self.__count

    def get(self, index):
        '''
        Returns the element at requested index.
        
        Parameters:
            index (int): Location of element to be returned.

        Returns:
            T (type of stored element): Element stored at index requested.

        Raises:
            IndexError: If the Array List is empty or index is < 0.
        '''
        if index >= self.__count or index < 0:
            raise IndexError("Index out of range.")

        return self.__array[index]

    def add(self, element, index=None): 
        '''
        Appends the provided element to the end of the Array List. If index is provided, insert at index and shift displaced
        elements to the right.
        
        Parameters:
            element (T - type of stored element)
            index (int): (Optional) Location of where to put element. Default None.
        '''
        #Call adding at a index polymorphic version.
        if not index == None:
            self.__add_at_index(element, index)
            return

        #We're full. Create bigger array, copy elements, and add new element to the end.
        if self.__count == self.__capacity:

            #Double the capacity
            new_array = self.__makeEmptyArray(self.__capacity*2)
            self.__capacity = self.__capacity*2
        
            i = 0
            while i < len(self.__array):
                new_array[i] = self.__array[i]
                i += 1

            #Add new element.
            new_array[i] = element
            self.__array = new_array
            self.__count +=1 
            
        #There is nothing in the array, add new element to the end.
        elif self.isEmpty():
            self.__array[self.__count] = element
            self.__count += 1
        #There already is elements in the array, add new element to the end.
        else:
            self.__array[self.__count] = element
            self.__count += 1

    def __add_at_index(self, element, index=None):
        '''
        Polymorphic version of add method. Insert at index and shift displaced elements to the right.
        
        Parameters:
            element (T - type of stored element)
            index (int): Location of where to put element. Default None.
        '''
        #Do we have room to add one more element? If yes, add it.
        if self.__count + 1 < self.__capacity:

            for i in range(self.__count-1, index-1, -1):
                self.__array[i+1] = self.__array[i]
            self.__array[index] = element
            self.__count += 1

        #We're full. Create bigger array, copy elements, and add new element at index.
        else:
            #Double the capacity
            new_array = self.__makeEmptyArray(self.__capacity*2)
            self.__capacity = self.__capacity*2

            #Copy elements from old arry up to the index for new element and then copy the rest.
            start = self.__count # +1 element -1 for indexing purposes
            for i in range(start, -1, -1):
                if i == index:
                    new_array[i] = element
                    self.__count += 1
                else:
                    new_array[i] = self.__array[i-1] #Accounting for added element 
            self.__array = new_array

                
    def remove(self, index=None):
        '''
        Removes the element at the end of the Array List and return it. If index is provided, remove
        the element at that index, shift elements from the left, return element.
        
        Parameters:
            index (int): (Optional) Location of element to be returned.

        Returns:
            T (type of stored element): Element stored at index requested.

        Raises:
            EmptyError: If the Array List is empty.
            IndexError: If index is < 0 or greater than the number of elements -1.
        '''
        #We are empty.
        if self.isEmpty():
            raise EmptyError("Cannot remove element from empty array.")

        if index == None:
            #Get last element on the array.
            element = self.__array[self.__count-1]
            self.__array[self.__count-1] = None
            self.__count -= 1
            #Return it.
            return element
        else:
            #Index is geater than the number of elements in the Array List.
            if index >= self.__count or index < 0:
                raise IndexError("Index out of range.")
            return self.__remove_at_index(index)

    def __remove_at_index(self, index):
        '''
        Polymorphic version of remove method. Removes the element at that index, shift elements from the left, return element.
        
        Parameters:
            index (int): (Optional) Location of element to be returned.

        Returns:
            T (type of stored element): Element stored at index requested.

        '''
        element = None
        found = False

        for i in range(0, self.__count):
            #Continue until we get to the index. 
            if i == index:
                #Remove the element.
                element = self.__array[i]
                self.__count -= 1
                found = True
            elif found:
                #Shift the remaining elements left.
                self.__array[i-1] = self.__array[i]
        self.__array[self.__count] = None
        return element


    def set(self, index, element):
        '''
        Replace element at index.
        
        Parameters:
            index (int): Location of element to be replaced.
            element (T - type of stored element)

        Raises:
            IndexError: If index is < 0 or greater than the number of elements -1.
        '''
        if index >= self.__count or index < 0:
            raise IndexError("Index out of range.")
        
        old_element = self.__array[index]
        self.__array[index] = element
        return old_element

    def clear(self):
        '''
        Clears all the elements in the Array List, maintains the current capacity.
        '''
        self.__count = 0
        self.__array = self.__makeEmptyArray(self.__capacity)

    def __str__(self):
        if self.isEmpty():
            return '[]'
        
        if self.__count == 1:
            return '[{}]'.format(str(self.__array[0]))
        
        str_of_array = []
        str_of_array.append('[')
        for e in range(0, self.__count):
            str_of_array.append(str(self.__array[e]))
            str_of_array.append(', ')
        
        str_of_array.pop()
        str_of_array.append(']')

        return ''.join(str_of_array)

    def __eq__(self, other):
        if isinstance(other, ArrayList):
            if not other.__count == self.__count:
                return False
            else:
                for i in range(0, self.__count):
                    if not other.__array[i] == self.__array[i]:
                        return False
                return True
        elif isinstance(other, list):
            if not len(other) == self.__count:
                return False
            else:
                for i in range(0, self.__count):
                    if not other[i] == self.__array[i]:
                        return False
                return True
        else:
            return NotImplemented

    



