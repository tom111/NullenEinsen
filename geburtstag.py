def geburtstags_wahrscheinlichkeit (n):
    pbar = 1.0;
    for i in range (n):
        pbar = pbar * (1 - float(i)/365)
    return (1 - pbar)

print [(n,geburtstags_wahrscheinlichkeit(n)) for n in range (50)]

