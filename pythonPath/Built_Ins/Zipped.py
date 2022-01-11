N_X = list(map(int,input().split()))
studs_rec = []

for i in range(N_X[1]):
    studs_rec.append(list(map(float,input().split())))

studs_rec = zip(*studs_rec)

for x in studs_rec:
    print(round(sum(x)/N_X[1],1))
