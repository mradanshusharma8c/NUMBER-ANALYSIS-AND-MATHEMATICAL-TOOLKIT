import random


# To check whether a number is prime or not
def check_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# To find all factors of a number
def get_factors(n):
    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors


# To find prime factors
def prime_factors(n):
    factors = []
    i = 2

    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i = i + 1

    return factors


# To find GCD of two numbers
def find_gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


# To find the smallest divisor
def smallest_divisor(n):
    if n < 2:
        return n

    for i in range(2, n + 1):
        if n % i == 0:
            return i


# To find factorial
def factorial(n):
    answer = 1

    for i in range(1, n + 1):
        answer = answer * i

    return answer


# To print Fibonacci series
def fibonacci(n):
    series = []

    first = 0
    second = 1

    for i in range(n):
        series.append(first)

        next_number = first + second
        first = second
        second = next_number

    return series


# To reverse a number
def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return reverse


# To convert decimal number into binary
def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary


# Main program

while True:

    print("\n===== NUMBER ANALYSIS & MATH TOOLKIT =====")
    print("1. Check Prime")
    print("2. Find Factors")
    print("3. Prime Factorization")
    print("4. Find GCD")
    print("5. Smallest Divisor")
    print("6. Factorial")
    print("7. Fibonacci Series")
    print("8. Reverse Number")
    print("9. Decimal to Binary")
    print("10. Character to ASCII")
    print("11. Square Root")
    print("12. Power")
    print("13. Random Number")
    print("14. Full Analysis")
    print("15. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        number = int(input("Enter a number: "))

        if check_prime(number):
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")

    elif choice == 2:

        number = int(input("Enter a number: "))

        print("Factors are:", get_factors(number))

    elif choice == 3:

        number = int(input("Enter a number: "))

        print("Prime factors are:", prime_factors(number))

    elif choice == 4:

        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))

        print("GCD is:", find_gcd(number1, number2))

    elif choice == 5:

        number = int(input("Enter a number: "))

        print("Smallest divisor is:", smallest_divisor(number))

    elif choice == 6:

        number = int(input("Enter a number: "))

        if number < 0:
            print("Factorial of a negative number is not possible.")
        else:
            print("Factorial is:", factorial(number))

    elif choice == 7:

        terms = int(input("Enter number of terms: "))

        print("Fibonacci series:", fibonacci(terms))

    elif choice == 8:

        number = int(input("Enter a number: "))

        print("Reverse of the number is:", reverse_number(number))

    elif choice == 9:

        number = int(input("Enter a decimal number: "))

        print("Binary number is:", decimal_to_binary(number))

    elif choice == 10:

        character = input("Enter a character: ")

        print("ASCII value is:", ord(character))

    elif choice == 11:

        number = float(input("Enter a number: "))

        if number < 0:
            print("Square root of a negative number is not possible.")
        else:
            print("Square root is:", number ** 0.5)

    elif choice == 12:

        base = int(input("Enter the base: "))
        power = int(input("Enter the power: "))

        result = base ** power

        print("Answer is:", result)

    elif choice == 13:

        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        number = random.randint(start, end)

        print("Random number is:", number)

    elif choice == 14:

        number = int(input("Enter a number: "))

        print("\n===== FULL ANALYSIS =====")
        print("Number:", number)

        if number % 2 == 0:
            print("Type: Even")
        else:
            print("Type: Odd")

        if check_prime(number):
            print("Prime: Yes")
        else:
            print("Prime: No")

        print("Factors:", get_factors(number))
        print("Reverse:", reverse_number(number))
        print("Binary:", decimal_to_binary(number))

    elif choice == 15:

        print("Thank you for using the Math Toolkit.")
        break

    else:

        print("Wrong choice. Please enter a number from 1 to 15.")