S = input()
lower = sorted([ch for ch in S if ch.islower()])
upper = sorted([ch for ch in S if ch.isupper()])
odd = sorted([num for num in S if num.isdigit() if int(num)%2 == 1])
even = sorted([num for num in S if num.isdigit() if int(num)%2 == 0])

print("".join(lower+upper+odd+even))
