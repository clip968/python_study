def iPower(x, n):
    result = 1
    for i in range(n):
        result *= x
    
    return result

def rPower(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return rPower(x*x, n//2)
    else:
        return x * rPower(x*x, (n-1)//2)
    
count = 0
    
def rFibo(n):
    global count
    count += 1
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return rFibo(n - 1) + rFibo(n - 2)
    
def iFibo(n):
    array = [0, 1]
    for i in range(2, n + 1):
        array.append(array[i-1]+array[i-2])
    return array[n]
    
    
print('iPower : %d' %(iPower(2, 10)))
print('rPower : %d' %(rPower(3, 10)))
print('rFibo : %d - count : %d' %(rFibo(10), count))
print(iFibo(10))