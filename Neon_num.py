num = int(input("Enter a number -> "))

def main(num):
    if num == neon(num):
        print(f"{num} is a neon number")
    else:
        print(f"{num} is not a neon number") 

def neon(num):
    s = 0
    # k = num
    num = num ** 2
    while num > 0:
        s += last_digit(num)
        num = remove_last_digit(num)
    return s
 
def last_digit(num):
    num = num % 10
    return num

def remove_last_digit(num):
    num = num // 10
    return num

main(num)    
