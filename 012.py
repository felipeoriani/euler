# --------------------  --------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 012 - Highly divisible triangular number
# What is the value of the first triangle number to have over five hundred divisors?
# ----------------------------------
import math

#count how many factors a number n has
def countFactors(n):
    count = 0 
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0: count += 2
    return count

def trianguleNumbers():
    counter = 0
    while True:
        counter += 1
        number = sum(range(1, counter + 1))
        factors = countFactors(number)
        yield number, factors
        
def f(n):
    for number, factors in trianguleNumbers():
        if factors > n:
            return number
        
anwser = f(500)

assert anwser == 76576500

print('Answer: ', anwser)