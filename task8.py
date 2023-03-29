from functools import reduce

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5))) #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1 = range(10) #range(0,10)
A2 = sorted([i for i in A1 if i in A0]) #empty list
A3 = sorted([A0[s] for s in A0]) #[1,2...5]
A4 = [i for i in A1 if i in A3] #[1,2...5]
A5 = {i:i*i for i in A1} #will print disct with key being main value and it's pair would be the square
A6 = [[i,i*i] for i in A1] #nested list with square, similar to above but in lists
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33]) #21
A8 = map(lambda x: x*2, [1,2,3,4]) #will return object

print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)
print(A7)
print(A8)