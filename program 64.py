n = int(input("Enter N: "))

fact = 1
total = 0

for i in range(1, n + 1):
    fact *= i
    total += fact

print("Sum =", total)