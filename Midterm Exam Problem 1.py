class Circle:
    def __init__(self,measure):
        self.measure = measure
    def Area(self):
          return (self.measure*self.measure)*3.14
    def Peri(self):
        return (self.measure*2*3.14)
    def Aread(self):
        return (self.measure/2)*(self.measure/2)*3.14
    def Perid(self):
        return (self.measure/2)*2*3.14
    def Display1(self):
        print("The area is", self.Area())
        print("The perimeter is", self.Peri())

    def Display2(self):
        self.measure
        print("The area is", self.Aread())
        print("The perimeter is", self.Perid())

meas = Circle(int(input("Enter here:")))
x = str(input("Enter (r)Radius or (d)Diamater"))
if x == "r":
    meas.Display1()
else:
    meas.Display2()


