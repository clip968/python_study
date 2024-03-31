from Car import Car

#클래스 상속
class SuperCar(Car):
    
    def __init__(self, color, speed = 0, bTurbo = True):
        #부모 클래스 생성자(__init__) 호출
        super().__init__(color, speed)
        self.bTurbo = bTurbo
    
    def setTurbo(self, bTurbo = True):
        self.bTurbo = bTurbo
        
    def speedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()
            
    def __str__(self):
        if self.bTurbo:
            return '[%s][speed = %s] Turbo' % (self.color, self.speed)
        else:
            return '[%s][speed = %s] Normal' % (self.color, self.speed)
                    
        
if __name__ == "__main__":
    s1 = SuperCar("Gold")
    s2 = SuperCar("Silver", 50, False)
    
    print(s1); print(s2)
    s1.speedUp(); s2.speedUp()
    print(s1); print(s2)
        