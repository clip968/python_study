def count_one(num):
    return num.count('1')

def find_pi(data):
    

def Quine_Mccluskey(minterms):
    numberCnt = {}
    number_binary = []
    for minterm in minterms:
        a = bin(minterm)
        number_binary.append(a[2:])
    
    for number in number_binary:
        b = count_one(number)
        if b not in numberCnt:
            numberCnt[a] = []
        numberCnt[a].append(number)
    pi = []
    
    for nums in sorted(numberCnt.keys()):
        c = numberCnt[nums]
        