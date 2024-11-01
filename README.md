
# Prime Number Checker
## Description
This simple Python program allows users to check if a given number is a prime number. It includes an `is_prime` function to determine if a number is prime and a main function that interacts with the user for input.

## Features
- **Prime Number Detection**: The `is_prime` function determines if an input number is prime.
- **User Input Validation**: Ensures that only non-negative integers are processed.
- **Interactive Feedback**: Informs users whether the entered number is prime or not.

## Usage
1. Clone or download the script.
2. Run the script from the terminal or command line:
   ```bash
   python prime_checker.py
   ```
3. When prompted, enter a non-negative integer to check if it is a prime number.

### Example
```plaintext
Enter a number: 17
17 is a prime number

Enter a number: 18
18 is not a prime number
```

## Functions
- **`is_prime(number)`**: Checks if the provided number is prime.
    - **Arguments**: `number (int)`: the number to check.
    - **Returns**: `True` if the number is prime; otherwise, `False`.

- **`main()`**: Prompts the user for input, validates it, and displays whether the number is prime.

## Requirements
- **Python 3.x**

## License
This project is licensed under the MIT License.