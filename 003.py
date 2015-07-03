# --------------------  --------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 003 - Largest prime factor
# What is the largest prime factor of the number 600851475143 ?
# ----------------------------------
import math

#get factors a number n has
def factors(n):
    fcs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0: fcs.append(i)
    return fcs

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if not n % i:
           return False
    return True  
        
def f(n):
    p = factors(n)
    m = 0
    for i in p:
        if isPrime(i):
            m = max(m, i)
    return m
        
anwser = f(600851475143)

assert anwser == 6857

print('Answer: ', anwser)