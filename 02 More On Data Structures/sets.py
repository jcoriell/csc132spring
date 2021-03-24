
# Ex: a set of values
a = {1,2,3,4,5,6,5,6,7}
print('a = ', a)

# Looking at subsets
b = {1,2,3, 10}
print('b = ', b)

c = a - b
print("c = ", c)

d = a | b # union (i.e. OR)
e = a & b # intersection (i.e. AND)
print("d = ", d)
print("e = ", e)

# the use of set()
print(set('aaabbbccc'))
print(''.join(set('aaabbbccc')))
print(set([1,2,3,4,4,4,4,5]))


