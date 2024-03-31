L1 = [3, 5, 7, 9]
L2 = ['A', 'B', 'C', 'D']

for e in L2:
    print(e, end=' ')

print()    
print(L1[2])

L2[1] = L1[-1]
print(L2)

L1.append(11)
print(L1)

print(L1.pop())
print(L1)

L2.extend(L1)
print(L1)
print(L2)