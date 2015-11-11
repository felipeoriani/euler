# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 020 - Factorial digit sum 
# Find the sum of the digits in the number 100!
# ----------------------------------

# function to calculate the factorial of a given number 
def factorial(n):
    if (n <= 1):
        return 1
    return n * factorial(n - 1)

def f(n):
    return sum(map(int, str(n)))

anwser = f(factorial(100))

assert anwser == 648

print 'Answer: ', anwser
