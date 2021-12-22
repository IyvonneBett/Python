# exercise 1
x = 5
y = 10
z = 8

print(x > y)
print(y > z)


# exercise 2
x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)


# exercise 3
x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

# exercise 4
x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")
