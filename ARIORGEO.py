t = int(input())
for i in range (0, t):
    a, b, c = map(float, input().split())

    d1 = b - a
    d2 = c - b

    r1 = (b * 1.0) / a
    r2 = (c * 1.0) / b

    fla = 0
    flg = 0

    if d1 == d2:
        fla = 1

    if r1 == r2:
        flg = 1

    if fla and flg:
        print("Both")

    elif fla:
        print("Arithmetic")

    elif flg:
        print("Geometric")

    else:
        print("None")
