class Polynomial():
    def __init__(self):
        self.arr = []
        self.length = 0
        
    def degree(self, i):
        return self.length - 1 - i
    
    def display(self, first):
        print(first, end='')
        for i in range(self.length):
            a = self.degree(i)
            if (i == self.length - 1):
                print(self.arr[i])
            else:
                print(str(self.arr[i])+"x^"+str(a), end=' + ')
                
    def read(self):
        self.arr = list(map(int, input("Input degrees in order : ").split()))
        self.length = len(self.arr)
        
    def add(self, arrB):
        arrC = Polynomial()
        
        if self.length < arrB.length:
            arrC.length = arrB.length
            tmp = self.arr
            self.arr = [0] * (arrB.length - self.length) + self.arr
            arrC.arr = [0] * arrC.length
            for i in range(self.length + 1):
                arrC.arr[i] = arrB.arr[i] + self.arr[i]
            self.arr = tmp
            
        else:
            arrC.length = self.length
            arrC.arr = [0] * arrC.length
            arrB.arr = [0] * (self.length - arrB.length) + arrB.arr
            tmp = arrB.arr
            for i in range(arrB.length):
                arrC.arr[i] = arrB.arr[i] + self.arr[i]
            arrB.arr = tmp
        
        return arrC
            
if __name__ == '__main__':
    a = Polynomial()
    b = Polynomial()
    
    
    a.read()
    b.read()
    
    c = a.add(b)
    
    a.display("A(x) = ")
    b.display("B(x) = ")
    c.display("C(x) = ")
    # print("C(2) = ", c.eval(2))