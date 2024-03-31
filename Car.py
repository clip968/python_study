class Car:
    #생성자
    def __init__(self, color, speed = 0): 
        #self가 없으면 멤버가 아니다. 무조건 self라는 이름으로 접근
        #멤버 변수
        self.color = color
        self.speed = speed
    
    def speedUp(self):
        self.speed += 10
    
    def speedDown(self):
        self.speed -= 10

    def isEqual(self, other):
        if self.color == other.color: 
            return True
        else:
            return False
        
    def __eq__(self, other):
        return "Yes" if self.color == other.color else "No"
    
    def __str__(self):
        return "Color : %s, Speed : %d" %(self.color, self.speed)
    
    def __ge__(self, other):
        return "Faster" if self.speed >= other.speed else "Slower"
    
#파이썬은 모든 변수가 객체이고, 변수는 래핑되어져 메모리의 주소에 각인된다.
#car1.color 라고 하는 것은 car1이라는 주소로 따라가 color 변수를 가져오는 것
if __name__ == '__main__':
    car1 = Car('Black')
    car2 = Car('Red', 100)
    car3 = Car('Yellow')
    
    print('Color : %s - Speed : %d' %(car1.color, car1.speed))
    print('Color : %s - Speed : %d' %(car2.color, car2.speed))
    print('Color : %s - Speed : %d' %(car3.color, car3.speed))
    
    car1.speedUp()
    car2.speedDown()
    print()
        
    print('Color : %s - Speed : %d' %(car1.color, car1.speed))
    print('Color : %s - Speed : %d' %(car2.color, car2.speed))
    print('Color : %s - Speed : %d' %(car3.color, car3.speed))
    
    print()
    
    #두 차량의 색깔 비교
    print(car2.isEqual(car3))
    print(car1 == car2)
    print(car1); print(car2)
    print()
    
    print(car1 >= car3)