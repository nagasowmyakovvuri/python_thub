##class Car():
##    def _init_(self):#constructor
##        print("hi")
##    def display(self):
##        print("hello")
##a=Car()#object
##a.display()
##
##
##b=Car()
##b.display()

#-----------------------------------------------------

##class Car():
##    pass ## an empty class
##a=Car()
##print(a)
##
##out put=<__main__.Car object at 0x0000022293BD5C60>
 #---------------------------------------------------------

##class Car():
##    def __init__(self): which will be executed without any call of function ,whenever the object is created
##        print("HI")
##a=Car() -->object

#--------------------------------------------------------------
##class Car():
##    def __init__(self):
##        print("HI")
##    def display(self):##--->here self is nothing but the created object
##        print("10")
##a=Car()
##a.display()
##
##b=Car()
##b.display()



##class Car():
####book="hope never dies"## class variable which can't change for object to object
##    def __init__(self,name,character):
##        self.name=name##-->these are the instance variables as there vary from one variable  to another variable
##        self.character=character##->these are the instance variables
##    def display(self):
##        print(self.name,self.character,self.book)
##a=Car("arjun","cid")
##a.display()
##
##b=Car("sakshi","reporter")
##b.display()

#-------------------------------------------------------------------------
##class Car():
##    
##    def __init__(self,name,character):
##        self.name=name##-->these are the instance variables
##        self.character=character##->these are the instance variables
##    def display(self):
##        print(self.name,self.character)
##a=Car("arjun","cid")
##a.display()
##
##b=Car("sakshi","reporter")
##b.display()

#---------------------------------------------------------------------------------
##class Student():
##    college="aditya college"
##    def __init__(self,name,roll_no):
##        self.name=name
##        self.roll_no=roll_no
##    def display(self):
##        print(self.name, "  ",self.roll_no,"    ",self.college)
##k=input()
##l=input()
##p=input()
##d=input()
##print("Name  ","Roll_no     ","College  ")
####student_1=Student("sowmya","21p31a0526")
##student_1=Student(k,l)
##student_1.display()
##student_2=Student(p,d)
####student_2=Student("Vishnu","21p31a0527")
##student_2.display()
##--------------------------------------------------------------------------------------------------------------------------------

##class Student():
##    college="aditya"
##    def __init__(self,name,roll,college,sub1,sub2):
##        self.name=name
##        self.roll=roll
##        self.college=college## instance variables have more priority than class variable
##        self.sub1=sub1
##        self.sub2=sub2
##    def display(self):
##        d=(int(self.sub1)+int(self.sub2))/2
##        print(self.name,self.roll,self.college,d)
##a=Student("kia","123","acet","54","67")
##a.display()
 
#--------------------------------------------------------------------------------------------------------------------------------------------
##class Student():
####    college="aditya college"
##    def __init__(self,name,roll_no,college):
##        self.name=name
##        self.roll_no=roll_no
##        self.college=college
##    def display(self):
##        print(self.name, "  ",self.roll_no,"    ",self.college)
##    @classmethod
##    def sample(cls):##cls is the default parameter
##        cls.college="ace"
##        print(cls.college)
##a=Student("kia","123","acet")
##a.sample()
##a.display()

#----------------------------------------------------------------------------------------------------------------------------------------
##class Student():
####    college="aditya college"
##    def __init__(self,name,roll_no,college):
##        self.name=name
##        self.roll_no=roll_no
##        self.college=college
##    def display(self):
##        print(self.name, "  ",self.roll_no,"    ",self.college)
##    @classmethod
##    def sample(cls):##cls is the default parameter
##        cls.college="ace"
##        print(cls.college)
##    @ staticmethod
##    def staticm:
##        print("hi")
##a=Student("kia","123","acet")
##a.sample()
##a.display()
#----------------------------------------------------------------------------------------------------------------------------------
##oops has three concepts:
##    1)inheretence-->accquiring the properties of the others
##    -->a class which access the properties-->child class
##    -->a class which gives the properties-->parent class
##    1.single inherentance-->only one child class and one parent class
##    2.multiple inherentance-->more than one parent class  and one child
##    3.multi level-->both the parent class acts as child and parent class
##    hierachial inherentance-->one parent two childs
##    2)abstrction
##    3)polymorphism

#---------------------------------------------------------------------------------------------------------------------------------
##class person():##parent class
##    def __init__(self,name,adhar_no):
##        self.name=name
##        self.adhar_no=adhar_no
##    def display(self):
##        print(self.name,self.adhar_no)
##class Student(person):
##    def __init__(self,roll,college,name,adhar_no):
##        self.roll=roll
##        self.college=college
##        super().__init__(name,adhar_no)
##    def display(self):
##        print(self.roll,self.college,self.name,self.adhar_no)
##b=Student("aec","123","sowmya","1343509")##child class
##b.display()
        
##a=person("sowmya","134")
##a.display()
#------------------------------------------------------------------------------------------------------------------------
##class person1():##parent class
##    def __init__(self,name1,adhar_no1):
##        self.name1=name1
##        self.adhar_no1=adhar_no1
##    def display(self):
##        print(self.name1,self.adhar_no1)
##class person2():##parent class
##    def __init__(self,name2,adhar_no2):
##        self.name2=name2
##        self.adhar_no2=adhar_no2
##    def display(self):
##        print(self.name2,self.adhar_no2)
##
##class Student(person1,person2):
##    def __init__(self,roll,college,name1,adhar_no1,name2,adhar_no2):
##        self.roll=roll
##        self.college=college
##        person1. __init__ (name1,adhar_no1)
##        person2. __init__ (name2,adhar_no2)
##    def display(self):
##        print(self.roll,self.college,self.name1,self.adhar_no1,self.name2,self.adhar_no2)
##b=Student("123","aec","sowmya","1343509","vishnu","43556")##child class
##b.display()
####priority order:
####    child instance-->parent instance-->child class-->parent class
##-------------------------------------------------------------------------------------------------------
##polymorphism-->same function name different properties in their positions of usage

class Code():
    def intro(self):
        print("coding is easy")
    def properties(self):
        print("coding languages have syntaxes")
class pythonn(Code):
    def properties(self):
          print("pyhton is easy")
class javaa(Code):
    def properties(self):
        print("java has a brackets for syntax")

a=Code()
a.intro()
a.properties()
b=pythonn()
b.intro()
b.properties()
c=javaa()
c.intro()
c.properties()
##the properties is in both parent and child classes but priority is for child class function














