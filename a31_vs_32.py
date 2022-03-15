t = int(input())

for i in range(t):
    dest = int(input())
    t_31 = 31
    t_32 = 32
    if dest <= 31:
        print(31)
        continue
    if dest == 32:
        print(32)
        continue
    while dest > t_31 or dest > t_32:
        if t_31 < dest:
            t_31 += 4
        if t_32 < dest:
            t_32 += 4
    if t_31 < t_32:
        print(31)
    else:
        print(32)
    