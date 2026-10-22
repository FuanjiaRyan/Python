def person(name, **kwlargs):
    print("Name: ", name)
    for k,v in kwlargs.items():
        print(k," : ", v)

person(name="Ryan", age=45, loc="Buea", tech="python") #keyword argument






#def add(num1=0, num2=0):  #default arguments
#   return num1 + num2

#def add(num1, *num2):  #variable length arguments 
#    sum = num1
#    for n in num2:
#        sum += n

#    return sum

#result = add(4,5,6,7)

#print(result)