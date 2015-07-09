# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 011 - Largest product in a grid
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
# ----------------------------------

def to_binary(n):
    return "{0:b}".format(n)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def f(m):    
    s = 0
    for i in range(1, m):        
        if is_palindrome(i):
            b = to_binary(i)
            if is_palindrome(b):
                s += i
    return s

answer = f(10**6)

assert answer == 872187

print('Answer: ', answer)