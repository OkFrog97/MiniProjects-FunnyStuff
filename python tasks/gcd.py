#1/usr/bin/evn python3d

def gcd (a, b):
    while a and b:
        if a >= b:
            a%=b
        else:
            b%=a
    return max(a,b)


def gcd_tests(func):
    import random
    for i in range (100):
        c = random.randint(0, 1024)
        b = random.randint(0, 128)
        a = random.randint(0, 129)
        assert gcd (a, a) == gcd (a, 0) == a
        assert gcd (b, b) == gcd (b, 0) == b
        assert gcd (a, 1) == gcd (b, 1) == 1
        d = gcd(a, b)
        assert a%d == b%d == 0
    return "OK"


def main():
    print(gcd (100, 12))
    print(gcd (8, 2))
    print(gcd (10, 5))
    print(gcd_tests(gcd))


if __name__ == "__main__":
    main()
