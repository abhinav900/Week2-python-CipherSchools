# function returning two function
def func(int1,int2):
    add = int1+ int2
    multiply= int1*int2
    return add, multiply
add,multiply = func(2,3)
print(add)
print(multiply)
