def finder(n):
    lst = []
    for i in range(60):
        if not i:
            if n%4 == 1 or n%4 == 2:
                lst.insert(0, 1)
            else:
                lst.insert(0, 0)
        else:
            if (n//(2**i))%2 and not n%2:
                lst.insert(0, 1)
            else:
                lst.insert(0, 0)
    return lst

A, B = map(int, input().split())

init = list('{:060b}'.format(A^(A+1)))
comp = finder(A+1)
res = finder(B)

for i in range(len(init)):
    if int(init[i]) != int(comp[i]):
        res[i] = str(int(not res[i]))
    else:
        res[i] = str(res[i])
        
print(int(''.join(res), 2))