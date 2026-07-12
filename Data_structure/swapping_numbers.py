x = 5
y = 9
z = 1

if x > y:
    x, y = y, x

if x > z:
    x, z = z, x

if y > z:
    y, z = z, y

print("x =", x)
print("y =", y)
print("z =", z)

