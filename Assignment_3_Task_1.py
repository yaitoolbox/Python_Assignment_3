
# Calcualting Factorial using LOOP Method

# Defining Factorial function

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i
    return result

# Calling the function with sample number
sam_num = 7

result = factorial(sam_num)

print(f'The factorial of {sam_num} is {result} - LOOP Method')

# Calculating Factorial using RECURSION method

# Defining Factorial function

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num -1)

samp_numb = 10
output = factorial(samp_numb)

print(f"The factorial of {samp_numb} is {output}  - RECURSION Method")