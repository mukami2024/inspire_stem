friends
friends=["Wayne","Renish","Bridgette","Michael","Angela"]
for friend in friends:
    print(friend)

enemies=friends[:]#to copy one list into another
print(enemies)

fruits=["guava","lemon","banana","pineapple","apple"]
#slice part of lists #index to(:) index...eg[0:3]
print(fruits[0:3])

del fruits[0]
print(fruits)

squares=[]#starts empty list
for x in range(0,11):
    squares.append(x**2)    
print(squares)