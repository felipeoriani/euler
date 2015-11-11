# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 015 - Lattice paths
# How many such routes are there through a 20�20 grid?
# ----------------------------------

# based on the lattices path concept: 
# http://robertdickau.com/lattices.html

def f(n):
    paths = {}
    for r in range(0, n + 1):
        for c in range(0, n + 1):
            if r == 0 or c == 0:
                paths[r, c] = 1
            else:
                paths[r, c] = paths[r - 1, c] + paths[r, c - 1]
    return paths[n, n]

anwser = f(20)

assert anwser == 137846528820

print 'Answer: ', anwser
