x = int(input("Enter the value of X :"))
n = int(input("Enter the value of n :"))
sum = 0
for i in range(n):
    if i%2 == 0 :
        sum += x**i
    else:
        sum -= x**i
print("Sum of the series is : ",sum)