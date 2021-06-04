class cal4:

    def setdata(self,a):
        self.num = a

    def display(self):
        return self.num*self.num

c=cal4()
c.setdata(4)
print(c.display())