# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# Language.......: Python
# Problem 0006...: Sum square difference
# ----------------------------------

def sumOfSquare(n):
    s = 0
    for i in range(1, n+1):
        s += i ** 2
    return s

def squareOfSum(n):
    return sum(range(1, n+1)) ** 2

answer = squareOfSum(100) - sumOfSquare(100)

assert answer == 25164150

print('Answer: ', answer)
