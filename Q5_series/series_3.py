x = int(input("Enter the value of X :"))
n = int(input("Enter the value of n :"))
sum = 0
for i in range (1,n+1):
    if i%2==0:
        sum -= (x**i)/i
    else:
        sum +=(x**i)/i
print("Sum of the series is : ",sum)