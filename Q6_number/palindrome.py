n = input("enetr any number or string :")
rev = n[-1::-1]
if n == rev :
    print(f"{n} is a palindrome " )
else:
    print(f"{n} is not a palindrome ")