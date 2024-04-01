my_laptop = {"make":"hp" , "colour":"black" , "weight":"1.2" , "year":"2022"}

print(my_laptop["make"])
print(my_laptop["weight"])

#to change the values in a dictionary
my_laptop["colour"] = "grey"
my_laptop["year"] = "2024"

my_laptop["size"] = "1200mm x 600mm"
print(my_laptop)

del my_laptop["colour"]
print(my_laptop)

siz_laptop = my_laptop.copy()
print (siz_laptop)


for key,value in my_laptop.items():
    print(key)
    print("\n")
    print(value)
