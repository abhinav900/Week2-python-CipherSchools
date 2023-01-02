# fromkeys
# d = dict.fromkeys(['name','age'], 'unknown')
# print(d)

# get method(useful)
d = {'name' : 'Harshit', 'age' :  'unknown'}
# print(d['namess'])
# print(d.get('names')) better

# if 'name' in d:
#     print('present')
# else:
#     print('not present')

# if d.get('names'):
#    print('present')
# else:
#     print('not present')

# d.clear()
# print(d)
d1 = d.copy()
# print(d1.popitem())
# print(d)
print(d1 is d)
