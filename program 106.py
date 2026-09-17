n = int(input("Enter size: "))

for i in range(3):
    for j in range(n):
        if (i + j) % 4 == 1 or (i == 1 and j % 4 == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()