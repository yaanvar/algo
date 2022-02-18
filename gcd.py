def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    if b >= a:
        return gcd(a, b % a)

def lcm(a, b):
    return (a * b) / gcd(a, b)

#main
print(gcd(1680, 640))