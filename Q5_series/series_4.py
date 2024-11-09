x = int(input("Enter the value of X :"))
n = int(input("Enter the value of n :"))
sum = 0
fact = 1
for i in range (1,n+1):
    fact*=i
    sum += (x**i)/fact
print("Sum of the series is : ",sum)