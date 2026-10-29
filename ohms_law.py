# Ohm's Law and Power Calculator
# ND1 Mechatronics Engineering Mini Project
# This program calculates voltage, current, resistance, or power.

def calculate():
    """Show the menu and perform one electrical calculation."""
    print("\n--- Ohm's Law and Power Calculator ---")
    print("1. Calculate voltage")
    print("2. Calculate current")
    print("3. Calculate resistance")
    print("4. Calculate power")

    choice = input("Choose an option (1-4): ").strip()

    try:
        if choice == "1":
            # Voltage = current x resistance
            current = float(input("Enter current in amperes (A): "))
            resistance = float(input("Enter resistance in ohms (Ω): "))
            voltage = current * resistance
            print(f"Voltage = {voltage:.2f} V")

        elif choice == "2":
            # Current = voltage / resistance
            voltage = float(input("Enter voltage in volts (V): "))
            resistance = float(input("Enter resistance in ohms (Ω): "))

            if resistance == 0:
                print("Error: Resistance cannot be zero.")
            else:
                current = voltage / resistance
                print(f"Current = {current:.2f} A")

        elif choice == "3":
            # Resistance = voltage / current
            voltage = float(input("Enter voltage in volts (V): "))
            current = float(input("Enter current in amperes (A): "))

            if current == 0:
                print("Error: Current cannot be zero.")
            else:
                resistance = voltage / current
                print(f"Resistance = {resistance:.2f} Ω")

        elif choice == "4":
            # Power = voltage x current
            voltage = float(input("Enter voltage in volts (V): "))
            current = float(input("Enter current in amperes (A): "))
            power = voltage * current
            print(f"Power = {power:.2f} W")

            # My extra feature: show a simple power category.
            # These are illustrative categories, not safety ratings.
            if power < 10:
                print("Power category: Low")
            elif power <= 100:
                print("Power category: Moderate")
            else:
                print("Power category: High")

        else:
            print("Invalid choice. Please choose a number from 1 to 4.")

    except ValueError:
        # Handle letters or other input that cannot be converted to a number.
        print("Invalid input. Please enter numbers only.")


# Keep running until the user chooses to stop.
while True:
    calculate()
    again = input("\nWould you like to calculate again? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thank you for using the calculator!")
        break
