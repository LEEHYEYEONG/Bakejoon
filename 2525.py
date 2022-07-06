a, b = map(int, input().split())
c = int(input())

if b+c < 60:
    print(a, b+c)
else:
    a = a + (b+c)//60
    total = (b+c) % 60
    if a >= 24:
        a = a-24
        print(a, total)
    else:
        print(a, total)