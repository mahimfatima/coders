n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()