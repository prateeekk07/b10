a = int(input("enter first number"))
b = int(input("enter second number"))
def get_func(a,b):
    add = a + b
    minus = a - b
    multiple = a * b
    divide = a / b
    
    return add, minus, multiple, divide

add, minus, multiple, divide = get_func(a,b)
print(f"addition = {add} minus = {minus} divide = {divide} multiple = {multiple}") 


 #keyword argument
def func(a,b,c):
    print(a,b,c)

func(b=10,c=3,a=1)

#default argument
def func(a,b,c=None):
    print(a,b,c)

func(b=10,a=1) 

 #variable lenght argument , type wil be tuple , min - 0 to max - infinte
def func(*args):
    print(args)

func(4,56,4)

def func(a,b,*agrs):
    print(a,b,agrs)

func(10,1,22,34,45)

def func(a,b,**kwagrs):
    print(a,b,kwagrs)

func(10,12,c=8,d=5,r=10)

def func(a,b,*args,**kwagrs):
    print(a,b,args,kwagrs)

func(10,12,45,56,c=8,d=5,r=10)

def display_info(**kwagrs):
    for key, value in kwagrs.items():
        print(f"{key}:{value}")

display_info(name="Prateek",age="14",place="indore")