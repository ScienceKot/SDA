die = [1, 2, 3, 4, 5, 6]
favorable_nb = []
def gcd(a, b):
    ''' Implimentation of the Euclidian algorithm'''
    if a == 0:
        return b
    return gcd(b % a, a)
inp = input("Introduce the numbers that Yakko and Wakko got:")
a, b = tuple(inp.split())
a, b = int(a), int(b)
for n in die:
    if n == a or n == b or n >= a + b:
        favorable_nb.append(n)
numerator = len(favorable_nb)
denominator = len(die)
gcd = gcd(numerator, denominator)
print(gcd)
numerator //= gcd
denominator //= gcd
print("{} / {}".format(numerator, denominator))
