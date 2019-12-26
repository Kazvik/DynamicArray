
from vector import Vector

v = Vector(10)

for i in range(len(v)):
    v[i] = i + 1


for x in v:
    print(x)

del v[5]

print(len(v))

print(v[5])