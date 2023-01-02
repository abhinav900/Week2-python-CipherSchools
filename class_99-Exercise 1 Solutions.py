# define a fucntion which will take list containing numbers as input
# and return list containing sqaure of every elements

def sqaure_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

# list,str
numbers = list(range(1,11))
print(sqaure_list(numbers))
