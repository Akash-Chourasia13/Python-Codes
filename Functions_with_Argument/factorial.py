num = int(input("Enter a number to find out its factorial -> "))

def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    print(f"Factorial of {num} is {fact}")    

factorial(num)        
