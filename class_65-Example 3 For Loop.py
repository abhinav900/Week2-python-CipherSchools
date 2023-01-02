# ask user a name and count each character
name=input("Enter your name:")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]
