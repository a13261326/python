for a in range(1, 101):
    if int(str(a)[len(str(a)) - 1]) in [2, 3, 4] and a not in [12,13,14]:
        b = 'процента'
    elif a in [1, 21, 31, 41, 51, 61, 71, 81, 91]:
        b = "процент"
    else:
        b = 'процентов'
    print(a, b)
