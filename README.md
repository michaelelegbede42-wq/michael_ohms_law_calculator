# Ohm's Law and Power Calculator

## What it does
This Python program calculates voltage, current, resistance, or electrical power using Ohm's Law and the power formula. It displays the result with the correct unit and handles invalid numeric input and division by zero.

## How to run it
1. Install Python 3.
2. Save the Python file as `ohms_law.py`.
3. Open a terminal in the folder containing the file.
4. Run:

   `python ohms_law.py`

On a phone, you can use a Python app such as Pydroid 3 on Android, or a Python environment that supports running scripts on your device.

## Sample output
```text
--- Ohm's Law and Power Calculator ---
1. Calculate voltage
2. Calculate current
3. Calculate resistance
4. Calculate power
Choose an option (1-4): 1
Enter current in amperes (A): 2
Enter resistance in ohms (Ω): 5
Voltage = 10.00 V

Would you like to calculate again? (yes/no): no
Thank you for using the calculator!
```

## My own twist
I added a power-category feature. When power is calculated, the program labels it Low (below 10 W), Moderate (10–100 W), or High (above 100 W). These are example categories chosen for this project, not universal electrical safety ratings.

## What I learned
- How to use functions, loops, and conditional statements in Python.
- How to convert input with `float()` and handle invalid input with `try` and `except`.
- How to apply basic electrical formulas in a program.

## Author
[Elegbede Michael], ND1 Mechatronics Engineering, YabaTech.
