from dynamicArray import DynamicArray

d = DynamicArray()

d.append(2)
d.append(3)
d.append(4)

d[0] = 1

del d[1]

d.append(6)

d.append(0)

def function(a, b):
    if a > b:
        return True
    else:
        return False
    
d.shell_sort(function)
for x in d:
    print(x)