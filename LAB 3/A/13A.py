def numberToBase(n, b):
    ''' This function converta any number to the chooses base '''
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
def gcd(a, b):
    ''' Implimentation of the Euclidian algorithm'''
    if a == 0:
        return b
    return gcd(b % a, a)
A = int(input("Enter the choosen number:"))
numerator = 0
denominator = 0
for i in range(2, A):
    numerator += sum(numberToBase(A, i))
    denominator +=1
gcd = gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd
print('{} / {}'.format(numerator, denominator))