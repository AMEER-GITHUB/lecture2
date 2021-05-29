n = int(input("Number:")) #All "input" values will be str type , we use "int" to convert 

if n>0:
    print(f"n={n}, is a Positive number")
elif n<0:
    print(f"n={n}, is a negative number")
else:
    print(f"n={n}, is ZERO")