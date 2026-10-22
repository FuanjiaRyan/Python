from functools import reduce

nums = [4,6,2,7,9,3,1,5,8]

#for i in nums:
#    if i % 2 == 0:
#        evens.append(i)

#def is_even(n):
#    return n % 2 == 0

#def double_it(n):
#    return n * 2

#def sum_it(a, b):
#    return a + b

evens = list(filter(lambda n : n % 2 == 0, nums))
doubles = list(map( lambda n : n * 2, evens))
sum = reduce( lambda a, b : a + b, doubles)

print("Evens: ", evens)
print("Doubles: ", doubles)
print("Sum: ", sum)