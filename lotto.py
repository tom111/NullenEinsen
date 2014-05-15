from math import factorial

def binomial(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

def lotto_wiederholungs_wahrscheinlichkeit (n):
    ereignisse = binomial(49,6)
    pbar = 1.0;
    for i in range (n):
        pbar = pbar * (1 - float(i)/ereignisse)
    return (1 - pbar)

print [lotto_wiederholungs_wahrscheinlichkeit(n) for n in [4,8,51,103]]

