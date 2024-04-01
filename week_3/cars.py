#this is a class that describes cars
class car:
   def __innit__(self,model,make,year,fuel_consumption,horsepower,color,cylinders):
     self.model=model
     self.make=make
     self.year=year
     self.fuel_consumption=fuel_consumption
     self.horsepower=horsepower
     self.color=color
     self.cylinders=cylinders

   #make
   def print_make(self,make):
     print("car is of {0} make".format(self.make))   
   def set_make(self,make):
    self.make=make
   def get_make(self):
    return self.make
   
   #color
   def print_color(self,color):
     print("car is of {1} color.".format(self,color))
   def set_color(self,color):
    self.color=color
   def get_color(self):
    return self.color
   
my_car = car ("skyline","ford","1980","4000cc","red","V8:")   
my_friends_car = car ("Juke","ford","2015","1200cc","black","I4:")

my_car.print_make("nissan")
my_car.set_make("nissan")
my_friends_car.print_make("toyota")
my_friends_car.set_make("toyota")

my_car.set_color("blue")
my_friends_car.set_color("red")
print(my_car)