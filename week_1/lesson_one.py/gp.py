#program that creates geometric progression
# date: 20/02/2024
#name: Faith Mukami
 
a = float(input("Enter the first term of the sequence : "))
r = float(input("Enter the common ratio : "))
n = float(input ("Enter the number of terms in the sequence :"))

nth= a * (r **(n-1) )
print("The nth term of the sequence is :",nth)