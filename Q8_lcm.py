n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
max_num = max(n1,n2)
while (True):
    if max_num%n1 == 0 and max_num%n2 == 0 :
        break
    max_num +=1
print(f"the LCM of {n1},{n2} is {max_num}").