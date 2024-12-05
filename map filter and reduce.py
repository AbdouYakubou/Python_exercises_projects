#map filter and reducce

#numbers = [1, 2, 3]

#def double(a): 
 #   return a * 2
 
#double = lambda a : a * 2

#result = map(lambda a : a* 2, numbers)
#
#print(list(result))

#numbers = [1, 2, 3]

##def isEven(n):
#    return n % 2 == 0


#result = filter(lambda n : n % 2 == 0, numbers)

#print(list(result))
from functools import reduce
expenses = [
    ('Dinner', 80),
    ('car repair', 120)
    ]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

    
print(sum)




