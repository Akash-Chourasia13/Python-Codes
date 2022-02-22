num = int(input("Enter a number to check whether it is odd or not -> "))

def odd(num):
    if num % 2 != 0:
        print(f"{num} is an odd number")
    else:
        print(f"{num} is not an odd number")
        
odd(num)   