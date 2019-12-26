

class Vector():
    
    def __init__(self, nr):
        self._elem = [None] * nr
    
    def __setitem__(self, index, data):
        self._elem[index] = data
    
    def __getitem__(self, index):
        return self._elem[index]
    
    def __delitem__(self, index):
        del self._elem[index] 
    
    def __next__(self, index):
        if index + 1 < len(self._elem):
            return self._elem[index+1]
    
    def __len__(self):
        return len(self._elem)
    
    def __iter__(self):
        return self._elem.__iter__()

    
class ShellSort():
    
    def __init__(self):
        pass
    
    @staticmethod
    def sorted(l, function):
        #function that sorts a list based on a function of comparing
        #l = the list to be sorted
        #function = the funcion used for comparing
        #it returns the sorted list
        length = len(l)
        gap = length // 2
        while gap > 0:
            for i in range(gap, length):
                aux = l[i]
                j = i
                while j >= gap and function(l[j - gap], aux):
                    l[j] = l[j - gap]
                    j = j - gap
                l[j] = aux
            gap = gap // 2
        return l

class Filter():
    
    def __init__(self):
        pass
    
    @staticmethod
    def filter(l, acceptanceFunction):
        #function that filters a list based on an acceptanceFunction
        #l = the list to be filtered
        #acceptanceFunction = the function that checks if an element passes the filter
        #returns a list with all the elements that pass the given filter
        filteredList = []
        for element in l:
            if acceptanceFunction(element):
                filteredList.append(element)
        return filteredList
                
        