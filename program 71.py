n = float(input("Enter decimal number: "))

binary = ""

if n == 0:
    binary = "0"

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print("Binary =", binary)