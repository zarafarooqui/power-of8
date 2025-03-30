def is_power_of_8(n):
    return n>0 and (n &(n-1))==0 and (n-1)%3==0

num=int(input("Enter a number:"))
if is_power_of_8(num):
    print(f" Yes {num} is a power of 8.")
else:
    print(f" No {num} is not a power of 8.")