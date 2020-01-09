from copy import deepcopy


class DynamicArray():
    
    def __init__(self):
        self._current = 0
        self._capacity = 1
        self._elem = self.__create(self._capacity)
    
    def __create(self, capacity):
        return [None] * capacity
    
    def __resize(self, new_capacity):
        new_array = self.__create(new_capacity)
        for i in range(self._current):
            new_array[i] = self._elem[i]
        self._elem = new_array
        self._capacity = new_capacity
    
    def append(self, data):
        if self._current == self._capacity:
            self.__resize(2 * self._capacity)
        self._elem[self._current] = data
        self._current = self._current + 1
    
    def __setitem__(self, index, data):
        if index >= self._current or index < 0:
            raise Exception("DynamicArray list index out of range!")
        else:
            self._elem[index] = data
    
    def __getitem__(self, index):
        if index >= self._current or index < 0:
            raise Exception("DynamicArray list index out of range!")
        else:
            return self._elem[index]
    
    def __delitem__(self, index):
        if index >= self._current or index < 0:
            raise Exception("DynamicArray list index out of range!")
        else:
            for i in range(index, self._current - 1):
                self._elem[i] = self._elem[i+1]
            self._current = self._current - 1
            
    def __next__(self, index):
        if index + 1 < self._current:
            return self._elem[index + 1]
    
    def __len__(self):
        return self._current
    
    def __iter__(self):
        l = self._elem[:self._current]
        return l.__iter__()

    def shell_sort(self, function):
        #function that sorts a list based on a function of comparing
        #l = the list to be sorted
        #function = the funcion used for comparing
        #it returns the sorted list
        length = self._current
        gap = length // 2
        while gap > 0:
            for i in range(gap, length):
                aux = self._elem[i]
                j = i
                while j >= gap and function(self._elem[j - gap], aux):
                    self._elem[j] = self._elem[j - gap]
                    j = j - gap
                self._elem[j] = aux
            gap = gap // 2
    
    def filter(self, acceptanceFunction):
        #function that filters a list based on an acceptanceFunction
        #l = the list to be filtered
        #acceptanceFunction = the function that checks if an element passes the filter
        #returns a list with all the elements that pass the given filter
        filteredList = []
        for element in self._elem:
            if acceptanceFunction(element):
                filteredList.append(element)
        return filteredList
                
        