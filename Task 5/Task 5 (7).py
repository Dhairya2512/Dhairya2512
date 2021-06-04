class cal6:
    def __init__(self,length):
        self.length = length

    def area(self):
        self.ans = self.length * self.length

    def display(self):
        print("Area of sqaure:",self.ans)

c =cal6(6)
c.area()
c.display()