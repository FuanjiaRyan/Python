a = 10   # Global Variable

def something():

    a = 15  # Local Variable
    globals()["a"] = 20

    print("Inside: ", a)

something()

print("Outside: ",a)