class Polynomial():
    def __init__(self):
        self.arr = list(map(int, input("Input degrees in order").split()))
        self.length = len(self.arr)
        
    def degree(self, i):
        return self.length - i
    
    def read(self):
        for i in
            
if __name__ == '__main__':
    a = Polynomial()
    b = Polynomial()
    
    
    a.read()
    b.read()
    
    c = a.add(b)
    
    a.display("A(x) = ")
    b.display("B(x) = ")
    c.display("C(x) = ")
    print("C(2) = ", c.eval(2))