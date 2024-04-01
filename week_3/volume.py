#of cylinder cone sphere cube 
import math

#1volume of cylinder
def values(r,h):
    return math.pi * r**2 * h
v1=values(7,14)
print(v1)

#2volume of cone
def values(r,h):
    return math.pi * 1/3* r**2 * h
v2=values(7,14)
print(v2)

#3volume of sphere
def values(r,h):
    return math.pi * 4/3* r**3 * h
v3=values(7,14)
print(v3)

#4volume of cube
def values(l,w,h):
    return l * w * h
v4=values(7,14,21)
print(v4)