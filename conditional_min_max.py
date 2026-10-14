# Print the smallest number if all three numbers are even;
# otherwise, print the largest number.

x = 41
y = 12
z = 14

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    comparator = lambda a, b: a < b
else:
    comparator = lambda a, b: a > b

result = x
if comparator(y, result):
    result = y
if comparator(z, result):
    result = z

print(result)