#of cylinder cone cube sphere
import math

#1 surface area of cylinder
def values(r,h):
    return math.pi * r**2 * 2 + math.pi * 2*r * h
s1=values(7,21)
print(s1)

#2surface area of cone
def values(r,l):
    return math.pi * r**2  + math.pi *r * l
s2=values(7,21)
print(s2)

#3surface area sphere
def values(r):
    return math.pi * r**2 * 4 
s3=values(21)
print(s3)

#4surface area cube
def values(s):
    return 6*s**2
s4=values(21)
print(s4)