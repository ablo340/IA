a = [1, 2, 8, 4, 5]

c = iter(a)
b = None
while b is None or b == 1:
    b = next(c)

print(b)
