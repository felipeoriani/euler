# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 028 - Number spiral diagonals
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
# ----------------------------------

def f(n):
    s = 1    
    count = 0
    jump = 1
    countJump = 1
    for i in range(2, n*n+1):        
        if count < jump:
            count += 1
        elif count == jump:
            count = 0            
            s += i
            if countJump == 4:
                jump += 2
                countJump = 1
            else:
                countJump += 1
    return s

anwser = f(1001)

assert anwser == 669171001

print('Answer: ', anwser)