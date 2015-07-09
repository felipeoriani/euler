# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 020 - Factorial digit sum 
# Find the sum of the digits in the number 100!
# ----------------------------------
import sys

def f(p):
    s = 0
    for i in range(2, 6*9**p):
        digitSum = 0
        for digit in map(int, str(i)):
            digitSum += digit ** p
        if i == digitSum:
            s += i
    return s

anwser = f(5)

assert anwser == 443839

print('Answer: ', anwser)