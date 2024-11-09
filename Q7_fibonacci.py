n = int(input("Enter the end limit of the fibonacci : "))
a = 0 
b = 1
c = a+b
print(a)
print(b)
print(c)
for i in range(n):
    a = b
    b = c
    c = a+b
    print(c)