def is_prime(n):
    sayac = 0
    for i in range(2, n):
        if n % i == 0:
            return False
            break
        else:
            sayac += 1
    if sayac == n - 2:
        return True


def term(n):
    x = 0
    sayac = 0
    while sayac != n:
        x += 1
        if is_prime(x) == True:
            sayac += 1
    print(x)


term(10001)