# Question 1: Prime Numbers

# Defining a function to determine if a given number is prime
def is_prime(number):
    """
    Determines if a given number is prime.

    Args:
        number (int): The number to be checked for primality
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    
    # Checks if number is divisible by another number other than itself and 1, and returns False
    for i in range(2, number):
        if number % i == 0:
            return False
    
    # If both checks fail, number is prime and returns True
    return True

# Defining the main function
def main():
    """
    The main function prompts the user to input a number and checks if the number
    is prime using the is_prime function. It prints a message indicating whether
    the number is prime.
    """
    number = 0  # Local variable to store the user's number

    # Input validation to ensure a non-negative number
    while (number := int(input("Enter a number: "))) < 0: 
        print("The number cannot be negative.")

    # Display whether the number is prime or not
    if is_prime(number):
        print(f"{number} is a prime number")
    
    else:
        print(f"{number} is not a prime number")

# Calling the main function
if __name__ == "__main__":
    main()