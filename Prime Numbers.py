number = int(input("Enter the number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "False")
            break
    else:
        print(number, "True")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "False")
