def main():
    n = int(input('Enter the value of n->'))
    print_prime_numbers(n)

def print_prime_numbers(n):
    num = 2
    while n!= 0:
        if is_prime(num) is True:
            print(f'{num =} is a prime number')
            n = sum((n, -1))
        num = sum((num,1)) 

def is_prime(num):
    if count_of_factors(num) == 2:
        return True 
    return False

def count_of_factors(num):
    res = 0
    for n in range(1,num +1):
        if num % n == 0:
            res = sum((res,1)) 
    return res

main()                             
