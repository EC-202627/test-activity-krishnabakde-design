T = int(input())
for i in range(T):
    X = int(input())
    if X >= 2000 and X < 10000:
        print("Yes")
    elif X >= 10000:
        print("It's Too Much")
    else:
        print("NO")
