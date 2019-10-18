def recProduct(a, b): 
    if a == 0 or b == 0:
        return 0
    if b > 0: 
        return a + recProduct(a, b - 1)
    elif a > 0 and b < 0:
        return b + recProduct(a - 1, b)
    else:
        return 0 - a + recProduct(a, b + 1)

print(recProduct(-10, -2))
