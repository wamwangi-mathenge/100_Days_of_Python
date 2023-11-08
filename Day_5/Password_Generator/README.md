# Password Generator Project
This Python project is a simple password generator that allows users to create strong and secure passwords with a combination of letters, numbers, and symbols. 

Users can specify the number of letters, symbols, and numbers they want in their password. 

The project uses the random module to generate random characters from predefined lists of letters, numbers, and symbols.

## Project Overview
The password generator project is designed to accomplish the following:

1. Prompt the user to input the desired number of letters, symbols, and numbers for their password.
2. Generate a random selection of characters from the specified categories.
3. Concatenate the characters to create a gross password.
4. Randomly shuffle the gross password to produce the final, net password.

## Project Components
The project is divided into the following components:

### User Input:

The user is prompted to input the following information:
- Number of letters in the password.
- Number of symbols in the password.
- Number of numbers in the password.

### Generating Random Characters:

- The project uses predefined lists of letters, numbers, and symbols.
- Random characters are selected from each category based on the user's input.

### Creating a Gross Password:

- Randomly selected characters from each category are concatenated to form the gross password.

### Shuffling the Gross Password:

- The gross password is shuffled to ensure that the order of characters is random.


## Example
Here's an example of how the program works:

```
Welcome to the PyPassword Generator!
How many letters would you like in your password? 4
How many symbols would you like? 2
How many numbers would you like? 2

Generated Password: JduE&!91

```

## How to Use
1. Run the Python script, and it will prompt you for the number of letters, symbols, and numbers you want in your password.
2. After inputting your preferences, the script will generate a secure password for you.

## License
This project is licensed under the MIT License

## Author
Brian Mathenge