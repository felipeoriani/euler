# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 012 - Highly divisible triangular number
# What is the value of the first triangle number to have over five hundred divisors?
# ----------------------------------
        
def f(n):
    s = 0
    c = 0
    jump = 1
    lc = 0
    for i in range(1, n*n+1):
        print(i)
        if c > 3:
            c = 0
        else:
            lc += 1
            if lc >= jump:
                s += i
                c += 1
            else:
                lc = 0
                jump += 2 

    return s

anwser = f(5)

#assert anwser == 76576500

print('Answer: ', anwser)