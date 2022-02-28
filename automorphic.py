num = int(input("Enter the number to check whether it is automorphic or not-> "))
temp = num
num_sq = num ** 2
flag = True

while temp:
    if temp % 10 != num_sq % 10:
        flag = False
        break
    temp //= 10
    num_sq //= 10
if flag is True:
    print(f"{num} is a automorphic number")
else:
    print(f"{num} is not a automorphic number") 