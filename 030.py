# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 030 - Digit fifth powers
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
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

print 'Answer: ', anwser
