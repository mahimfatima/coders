def pattern(n, i=1):
    if i > n:
        return

    print(i, end=" ")
    pattern(n, i + 1)
    print(i, end=" ")

n = int(input("Enter N: "))
pattern(n)