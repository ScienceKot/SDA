# Importing ceil function from math library
from math import ceil
n = int(input("Enter the length of the Theatre Square:"))
m = int(input("Enter the width of the Theatre Square:"))
a = int(input("Enter the length of side of the flagstone:"))
length = ceil(n/a)
width = ceil(m/a)
number_of_flagstones = length * width
print("{} flagstones are needed to cover the ceil of Theatre Square".format(number_of_flagstones))