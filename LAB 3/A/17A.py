def isprime(n):
    div = 0
    for i in range(2, n+1):
        if n % i == 0:
            div+=1
    if div == 1:
        return True
    else:
        return False
def get_prime_numbers(start, finish):
    prime_nb = []
    for i in range(start, finish+1):
        if isprime(i):
            prime_nb.append(i)
    return prime_nb
inp = input("ENter the n and k:")
n, k = tuple(inp.split())
n, k = int(n), int(k)
prime_nb =get_prime_numbers(2, n)
suit = 0
for i in range(2, n):
    for j in range(len(prime_nb)-1):
        if i == prime_nb[j] + prime_nb[j+1] + 1:
            suit +=1
print(suit)
if suit == k:
    print("YES")
else:
    print('NO')