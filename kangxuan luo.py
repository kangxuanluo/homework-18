def f(x):
    if x==1 or x==0:
        return(1)
    else:
        return x*f(x-1)

x = int(input("x:"))
print(f(x))
