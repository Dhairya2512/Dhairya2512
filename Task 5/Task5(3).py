class cal3 :
    def __init__(self,P,R,T):
        self.n1 =P
        self.n2 = R
        self.n3 = T

    def callinterest(self):
        self.interest =((self.n1*self.n2*self.n3/100))

    def display(self):
        print("interest of given parameters:",self.interest)

c=cal3(100,30,2)
c.callinterest()
c.display()