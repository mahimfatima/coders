choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

if choice == "C":
    c = float(input("Enter Celsius: "))
    f = (c * 9 / 5) + 32
    print("Fahrenheit =", f)

elif choice == "F":
    f = float(input("Enter Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("Celsius =", c)

else:
    print("Invalid choice")
