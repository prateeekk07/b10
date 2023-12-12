# OOPS 
# Object Oriented Programming System

# Python --- everything as an object


# class ClassName():
#     '''docstring'''
    # method
        #  --- instance method  --> for dealing with instance variable -- CRUD operations  -- first argument -- self
        #  --- static method
        #  --- class method --> for dealing with class level variable -- CRUD operations
                            #    first argument -- cls
                            # decorator -- @classmethod
    # variables
       # class level variable/static variable
       # instance variable



#normal class

class Person:
    name = "Prateek"
    age="25"
    occupation="SD"
    def info(self):
        print(f"{self.name} is a {self.age} and work as {self.occupation}.")

record = Person() #refrence vairiable
record.name = "abhijeet"
record.age = "12"
record.occupation = "hr"
record.info()

#init method class/constructor/dunder

class Person:

    def __init__(self, n , a, o):
        self.name = n
        self.age = a
        self.occupation = o
    def info(self):
        print(f"{self.name} is a {self.age} and work as {self.occupation}.")

record1 = Person("prateeK", 65, "SD")
record2 = Person("ABHIJEET", 5, "SD2")
record3 = Person("BATUL", 6, "D")
record4 = Person("tee", 6325, "SDD")
record1.info()
record2.info()
record3.info()
record4.info()


#repr
class Person:
    def __init__(self,n,a,s) -> None:
        self.Name = n
        self.age = a
        self.Salary = s

    def __str__(self):
        print("in str")
        return f"{self.__dict__}"
    
    def __repr__(self) -> str:
        print("in repr")
        return str(self)
    
r1 = Person("pRATEEK", 22 , 5000)
r2 = Person("abhijeet", 22 , 5000) 
emp_list = [r1,r2]
lst = [i.Name for i in emp_list]
print(lst)

#class method

class Employee:
    no_of_leaves = 8

    def __init__(self,aname,salary,role):
        self.name = aname
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"{self.aname} {self.salary} {self.role}"
    
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves
    
harry = Employee("Harry", 255 , "admin")
harry.change_leaves(10)

print(harry.no_of_leaves)
