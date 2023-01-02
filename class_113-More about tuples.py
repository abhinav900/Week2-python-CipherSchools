# looping in tuples
# tuple with one element
# tuples without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed = (1,2,3,3.0)

# for loop and tuple
# for i in mixed:
#    print(i)

# tuple with one element
num = (1)
words = ('word1')
# print(type(num))
# print(type(words))

# tuple without parenthesis
guiters = 'yamaha', 'button rouge','taylor'
# print(type(guiters))

# tuple_unpacking
guitarists = ('Maneli Jamal','Eddie Van Der Meer','Andrew Foy')
guitarist1,guitarist2,guitarist3 = (guitarists)
# print(guitarist1)

# list inside tuples
favourites = ('southern mongolia', ['tokyo ghoul theme','landscape'])
favourites[1].pop()
favourites[1].append("We made it")
print(favourites)
