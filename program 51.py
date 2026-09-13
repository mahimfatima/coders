#Check if a number is a palindrome
n = int(input("Enter a number: "))
original_n = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original_n == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")