import math as ma #importing math module for all mathematical functions and named as 'ma'

#Asking the user to input the number

number = float(input("Enter the Number : "))

square_root = ma.sqrt(number) # Square root of the number
log_number = ma.log(number) # Natural Logarithm of number
sin_number = ma.sin(number) # Sin of the number

print(f"The Square root of  {number} is {square_root:.3f}")
print(f"The Natural Logarithm (log base e) of  {number} is {log_number:.3f}")
print(f"The Sin of {number} in radians is {sin_number:.3f}")

