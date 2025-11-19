"""def my_data(func):
    def wrapper():
        print("Yaidekar Sudeep")
        func()
        print(f"Age : {19}")
    return wrapper
@my_data
def intro():
    print(f"Father Name : {"Hemanna"}")
    
    print(f"Mother Name : {"kenchamma"}")

intro()"""

def show_res(fanc):
    def wrapper(a,b):
        print(f"Function '{fanc.__name__}' is beging called = ",end=" ")
        fanc(a,b)
    return wrapper
@show_res
def add(a,b):
    print(a+b)

@show_res
def sub(a,b):
    print(a-b)
@show_res
def mul(a,b):
    print(a*b)
@show_res
def div(a,b):
    print(a/b)

add(4,5)
sub(8,2)
mul(9,3)
div(6,2)