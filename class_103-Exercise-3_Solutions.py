# define a functon that take list of words as argument and
# return list with reverse of every element in that list

def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])

    return elements
words = ['abc','xyz','rty']
print(reverse_elements(words))
