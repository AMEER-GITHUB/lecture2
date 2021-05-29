import sys

# only classes should be given in 'except' check the errors name in terminal

try:
    x = int(input("x:"))
    y = int(input("y:"))
except ValueError:
    print("Error:Invalid input.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error:Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")