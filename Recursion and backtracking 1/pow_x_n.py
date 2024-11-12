
def pow(x, n):
    if n == 0:
        return 1

    calculated_pow = pow(x, n / 2)

    xn = calculated_pow * calculated_pow
    if n % 2 == 1:
        xn = xn * x
    return xn


print(pow(5, 3))
