# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 017 - Number letter counts
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# ----------------------------------

numbers = [[1, 'one'], [2, 'two'], [3, 'three'], [4, 'four'], 
           [5, 'five'], [6, 'six'], [7, 'seven'], [8, 'eight'], 
           [9, 'nine'], [10, 'ten'], [11, 'eleven'], [12, 'twelve'], 
           [13, 'thirteen'], [14, 'fourteen'], [15, 'fifteen'], [16, 'sixteen'], 
           [17, 'seventeen'], [18, 'eighteen'], [19, 'nineteen']]

numbers2 = [[20, 'twenty'], [30, 'thirty'], [40, 'forty'], [50, 'fifty'], 
            [60, 'sixty'], [70, 'seventy'], [80, 'eighty'], [90, 'ninety']]

def number2Text(n):
    if n >= 1 and n <= 19:
        return numbers[n-1][1]
    elif n >= 20 and n <= 99:
        r = int(n / 10) * 10
        d = int(n % 10)
        for i in range(0, len(numbers2)):
            if numbers2[i][0] == r:
                return numbers2[i][1] + '-' + numbers[d-1][1] if d > 0 else numbers2[i][1]                
    elif n >= 100 and n <= 999:
        r = int(n / 100)
        d = int(n % 100)
        return numbers[r-1][1] + ' hundred' + (' and ' + number2Text(d) if d > 0 else '')
    elif n >= 1000 and n <= 9999:
        r = int(n / 1000)
        d = int(n % 1000)
        return numbers[r-1][1] + ' thousand' + (' and ' + number2Text(d) if d > 0 else '')
    return ''

def f(n):
    s = 0
    for i in range(n+1):
        s += len(number2Text(i).replace(' ', '').replace('-','').strip())
    return s

answer = f(1000)

assert answer == 21124

print(answer)