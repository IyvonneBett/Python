# There are two types of loops in Python: while and for: the while loop executes a statement or a set of statements as long as a specified boolean condition is true,

# the for loop executes a set of statements many times; it's used to iterate over a sequence

# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# You can use the break and continue statements to change the flow of a loop
# You use break to exit a loop

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

# you use continue to skip the current iteration, and continue with the next iteration,
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

# The while and for loops can also have an else clause in Python. The else clause executes after the loop finishes its execution as long as it has not been terminated by break
n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

# The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: range(start, stop, step), where:

#start is an optional parameter specifying the starting number of the sequence (0 by default)
#stop is an optional parameter specifying the end of the sequence generated (it is not included),
#and step is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

