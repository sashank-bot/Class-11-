n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))
n3 = int(input("Enter third number :"))

if n1 > n2 and n1 >n3:
    print(f"{n1} is greater then {n2} and {n3}")
elif n2 > n1 and n2 > n3 :
    print(f"{n2} is greater then {n1} and {n3}")
else:
    print(f"{n3} is greater then {n2} and {n1}")

if n1 < n2 and n1 < n3 :
    print(f"{n1} is smaller then {n2} and {n3}")
elif n2 < n1 and n2 < n3 :
    print(f"{n2} is smaller then {n1} and {n3}")
else:
    print(f"{n3} is smaller then {n2} and {n1}")