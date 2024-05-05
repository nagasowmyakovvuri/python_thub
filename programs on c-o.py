##class Car():
##    def __init__(self):#constructor-->double underscore,self is the particular object
##        print("hi")
##    def display(self):
##        print("hello")
##a=Car()#object
##a.display()
##
##b=Car()
##b.display()

##program-1 -->to access the parameters from the objects
class Car():
    def __init__(self,name,model):
        self.name=name
        self.model=model
        
    def display(self):
        print(self.name,self.model)
s,m=map(str,input().split())
k,l=map(int,input().split())
a=Car(s,k)#object
a.display()
b=Car(m,l)
b.display()












