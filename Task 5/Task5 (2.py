class cal2 :
    def setData (self ,r):
        self.rad = r

    def area(self):
        self._Total_area = 3.14*self.rad*self.rad

    def display(self):
        print("area of circle :",self._Total_area)

c=cal2()
c.setData(14)
c.area()
c.display()