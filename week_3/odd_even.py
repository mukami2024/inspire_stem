no=18

if no % 2:
    print("odd number")
else :
    print("even number") 
    print("\n")
    #list of odd numbers 
    def print_odds(first_no,last_no):
     for i in range(first_no,last_no,2):
      print(i%2)     
print_odds(1,100)  

print("\n")

def print_even(first_no,last_no):
   for i in range(first_no,last_no,3):
    print(i%3)
print_even(1,100)