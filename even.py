num = int(input("Enter the number you want to check -> "))

def even(num):
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is not an even number")
        
even(num)      