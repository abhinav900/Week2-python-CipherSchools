def greater(a,b):
    if a>b:
        return a
    return b
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
bigger=greater(num1,num2)
print(f"{bigger} is greater")
