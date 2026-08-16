try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = a / b
except ValueError as e:
    print(e)
print(f"{a} / {b} = {c}")
