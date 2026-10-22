import sys
from time import sleep

sys.setrecursionlimit(100000)
print(sys.getrecursionlimit())

count = 1

def greet():
    global count
    print("Hello", count)
    count = count + 1
    greet()

greet()