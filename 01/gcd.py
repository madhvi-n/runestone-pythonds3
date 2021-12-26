def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


def lcm(x, y):
    n = (x*y) // gcd(x, y)
    return n

def main():
    g = gcd(49, 52)
    print(g)

    l = lcm(49, 52)
    print(l)


if __name__ == '__main__':
    main()
