a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if a > b :
    ma = b
else :
    ma = a 
for i in range (1,ma+1):
    if a%i== 0 and b%i==0:
        hcf = i 
print(f"Ther GCD of {a},{b} is {hcf}")
