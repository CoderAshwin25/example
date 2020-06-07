def max_of_3(a , b , c):
    if a > b and a > c :
        return a
    elif b > a and b > c :
        return b
    elif c > a and c > b :
        return c

print(max_of_3(6,10,25))
