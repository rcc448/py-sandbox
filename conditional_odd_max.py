# Print the smallest number if all three numbers are even;
# otherwise, print the largest odd number.

x = 41
y = 12
z = 14

result = min(x, y, z)

if x % 2 != 0 or y % 2 != 0 or z % 2 != 0:
    result = x if x % 2 == 1 and x > result else result
    result = y if y % 2 == 1 and y > result else result
    result = z if z % 2 == 1 and z > result else result

print(result)