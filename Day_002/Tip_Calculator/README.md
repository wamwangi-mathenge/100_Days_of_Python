# Simple Tip Calculator

This is a Python program that calculates the amount each person should pay when splitting a bill, including a tip. It takes user input for the total bill, the desired tip percentage, and the number of people sharing the bill.

## How to Use
1. Run the program in a Python environment (e.g., IDLE, Jupyter Notebook, or a code editor like Visual Studio Code).

2. The program will display a welcome message and prompt you to enter the following information:

    - Total bill amount (in dollars).
    - Desired tip percentage (10, 12, or 15).
    - Number of people sharing the bill.
3. After you've entered these values, the program will calculate the cost per person, including the tip, and display it rounded to two decimal places.

4. The final output will show how much each person should pay.

### Example
```
Welcome to the tip calculator
What was the total bill?
$100.00
What percentage would you like to give? 10, 12 or 15?
12
How many people to split the bill?
4
Each person should pay: $31.00

```

## How it Works

The program takes the user's input for the total bill, tip percentage, and number of people, performs the following calculations:

- It calculates the total bill amount with the tip included using the formula: total_bill * (1 + (tip_percentage / 100)).
- Then, it divides this amount by the number of people to get the cost per person.
- Finally, it rounds the cost per person to two decimal places and displays the result.

## License
This project is licensed under the MIT License

## Author
Brian Mathenge