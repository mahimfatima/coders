n = abs(int(input("Enter number: ")))

if n == 0:
    largest = smallest = 0
else:
    largest = 0
    smallest = 9

    while n > 0:
        digit = n % 10

        if digit > largest:
            largest = digit

        if digit < smallest:
            smallest = digit

        n //= 10

print("Largest digit =", largest)
print("Smallest digit =", smallest)