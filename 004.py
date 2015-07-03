# --------------------  --------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 004 - Largest palindrome product
# Find the largest palindrome made from the product of two 3-digit numbers.
# ----------------------------------

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def f(c):
    s = 1
    if c > 2:
        s = 10 ** (c - 1)
    m = 0
    for i in range(s, 10**c):
        for j in range(s, 10**c):
            r = i * j
            if is_palindrome(r):
                m = max(m, r)
    return m
        
anwser = f(3)

assert anwser == 906609

print('Answer: ', anwser)