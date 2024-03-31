pi = 3.141592
perimeter = 0

def calc_perimeter(radius):
    global perimeter
    
    print('Pi :', pi)
    perimeter = 2 * pi * radius
    
if __name__ == '__main__':
    calc_perimeter(10)
    print('원둘레(r=10) = ', perimeter )