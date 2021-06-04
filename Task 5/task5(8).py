class publisher():
    def __init__(self,title):
        self.title = title
        print("Title :",title)

class book(publisher):
    def __init__(self,page_no ):
        print("Page no :",page_no)

class tape(publisher):
    def __init__(self,time_of_playing ):
        print("Time of Playing :",time_of_playing)

c = publisher("Dhairya")
c = book(72)
c = tape("5 hours")