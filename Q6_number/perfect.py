n = int(input("Enter any number to check if it is perfect number or not :"))
per = 0 
for i in range(1,n):
    if n%i == 0 :
        per+=i
if n == per:
    print(f"{n} is a perfect number ")
else:
    print(f"{n} is not a perfect number ")
    

