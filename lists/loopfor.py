for i in range(2, 8, 3):
    print("The value of i is currently", i)


# example 2
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2


import time

for second in range(1, 6):
    print(second, "Mississippi")
    time.sleep(1)
	
print("Ready or not, here I come!")