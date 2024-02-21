# program that calculates hire purchase price
#date: 20/02/2024
#name: Faith Mukami
 
dep = float(input("Enter the deposited amount :" ))
n = float(input("Enter the number of the months :" ))
inst= float(input("Enter the monthly instalment paid :"))

hpp = (dep) + (n * inst )

print ( "The hire purchase price is :", hpp)