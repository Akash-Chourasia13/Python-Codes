x = int(input("Enter the base number -> "))
n = int(input("Enter the power which you want to raise to the base -> "))

def power_of(x, n):
    power = 1
    for i in range(n):
        power *= x
    print(f"{x} to the power of {n} is {power}")    

power_of(x,n)
