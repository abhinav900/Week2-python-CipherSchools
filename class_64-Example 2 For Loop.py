# ask user a number like 1256
# calculate the sum of digits ---> 1+2+5+6
total=0
num=input("Enter any number:")
for i in range(0, len(num)):
    total +=int(num[i])
print(total)


