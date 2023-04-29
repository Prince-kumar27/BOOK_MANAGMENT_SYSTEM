x=100

def fun():
    y=10# y is local
    z=x+y#x is global variable
    return(z)
p=fun()

print(p)




