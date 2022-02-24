# # # # # # # # def capital_indexes(var):
# # # # # # # #     list_in = []
# # # # # # # #     var = list(var)
# # # # # # # #     l = len(var)
# # # # # # # #     for i in range(0,l,1):
# # # # # # # #         if var[i].isupper():
# # # # # # # #         #  == ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] is True:
# # # # # # # #             list_in.append(i)  
# # # # # # # #     print(list_in)

# # # # # # # # capital_indexes(var = "AkasH")    

# # # # # # # def capital_indexes(var):
# # # # # # #     list_in = []
# # # # # # #     var = list(var)
# # # # # # #     l = len(var)
# # # # # # #     for i in range(0,l,1):
# # # # # # #         if var[i] in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
# # # # # # #             list_in.append(i)  
# # # # # # #     print(list_in)

# # # # # # # capital_indexes(input("Enter the string -> "))    

# # # # # # # for i in range(2000, 3201, 1):
# # # # # # #     if(i % 7 == 0 and i // 5 != 0):
# # # # # # #         print(i, end =",")

# # # # # # # l=[]
# # # # # # # for i in range(2000, 3201):
# # # # # # #     if (i%7==0) and (i%5!=0):
# # # # # # #         l.append(str(i))

# # # # # # # print (','.join(l))     


# # # # # # l=[]
# # # # # # for i in range(2000, 3201):
# # # # # #     if (i%7==0) and (i%5!=0):
# # # # # #         l.append(i)

# # # # # # print (l)  


# # # # # # values=input()
# # # # # # print(values)
# # # # # # l=values.split(",")
# # # # # # t=tuple(l)
# # # # # # print (l)
# # # # # # print (t)

# # # # # print("Akash how r you \r j")
# # # # # print("I don't care")


# # # # # num1 = int(input("Enter first number -> "))


# # # # num = int(input("Enter the number you want to check -> "))

# # # # def even(num):
# # # #     if num % 2 == 0:
# # # #         print(f"{num} is an even number")
# # # #     else:
# # # #         print(f"{num} is not an even number")
        
# # # # even(num)      

# # # num = int(input("Enter a number to check whether it is odd or not -> "))

# # # def odd(num):
# # #     if num % 2 != 0:
# # #         print(f"{num} is an odd number")
# # #     else:
# # #         print(f"{num} is not an odd number")
# # # odd            

# # # num = int(input("Enter a number to find out its factorial -> "))

# # # def factorial(num):
# # #     fact = 1
# # #     while num > 0:
# # #         fact *= num
# # #         num -= 1
# # #     print(f"Factorial of {num} is {fact}")    

# # # factorial(num)        

# # num1 = int(input("Enter the number whose table you want to print -> "))
# # num2 = int(input("Enter upto which number you want the multiplication -> "))

# # def table(num1, num2):
# #     for i in range(1, num2 + 1, 1):
# #         print(f"{num1} * {i} = {num1 * i}")

# # table(num1, num2)        

# x = int(input("Enter the base number -> "))
# n = int(input("Enter the power which you want to raise to the base -> "))

# def power_of(x, n):
#     power = 1
#     for i in range(n):
#         power *= x
#     print(f"{x} to the power of {n} is {power}")    

# # power_of(x,n)    


print("Code Started")
print("The code is used to check if a given number is prime or not")

def main():
    num = int(input("Enter the number -> "))
    is_prime(num)

def is_prime(num):
    if no_of_factors(num) == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

def no_of_factors(num):
    res =0
    for i in range(1, num + 1):
        if num % i == 0:
            res += 1
    return res        

main()
print("Code has ended")