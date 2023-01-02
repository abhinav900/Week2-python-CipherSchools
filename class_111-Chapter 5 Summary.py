def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print("numbers must be int or floats")
    except :
        print("Unexepcted error")
print(divide(10,'2'))
