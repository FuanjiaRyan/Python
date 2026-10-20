def square(num):
    return num * num

def cube(num):
    return num * num * num

def operate(num, operation):

    for i in nums:
        result = operation(i)
        print(result)
    #return operation(num)  #square(num)

nums = [5,6,7,8]
operate(nums, square)
#print(result)