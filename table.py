num1 = int(input("Enter the number whose table you want to print -> "))
num2 = int(input("Enter upto which number you want the multiplication -> "))

def table(num1, num2):
    for i in range(1, num2 + 1, 1):
        print(f"{num1} * {i} = {num1 * i}")
        
table(num1, num2)        