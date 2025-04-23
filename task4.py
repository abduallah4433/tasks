test = [5, 4, 17, 19, 30, 2, 7, 10, 45]

filter = lambda func : [i for i in func if i % 2 == 0 ]

print(filter(test))