class Students:
    school=str(input("enter your school:"))
    m1=int(input("enter your marks for maths:"))
    m2=int(input("enter your marks for english:"))
    m3=int(input("enter your marks for science:"))

    def avg(self):  #created a function for average of the numbers
        return (self.m1+self.m2+self.m3)/3


s1=Students() #creating an object
print("you are from the school -->", s1.school)
print("Your result is ==>",s1.avg()) #using it to call the functions we created





                      
