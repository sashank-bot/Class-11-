n = int(input("Enter any number to see if it is armstrong number or not :"))
count = len(str(n))
org_n = n 
sum = 0
while (n > 0):
    digit = n%10
    sum += digit**count
    n =  n//10
if sum == org_n:
    print(f"{org_n} is an armstrong number ")
else:
    print(f"{org_n} is not an armstrong number " )
