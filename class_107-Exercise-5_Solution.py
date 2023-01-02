# common element finder function
# define a function which take 2 lists as input and return a list
# which contains common elements of both lists
def common_finder(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common_finder([1,3,4,5],[3,4,7,8]))
