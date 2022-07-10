def convert(o):
    i = 0
    d= 0
    while o != 0:
        di = o % 10
        d += di * pow(8, i)
        o //= 10
        i += 1
    #print( decimal)
    b = 0
    rem = 0
    i = 1
    while d != 0:
        rem = d % 2
        d //= 2
        b += rem * i
        i *= 10
    print(b)
o= int(input())
convert(o)