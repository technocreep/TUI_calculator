"""Simple command-line interface for the calculator.

This module replaces the previous npyscreen-based TUI with a basic
standard-library driven menu that can run in any terminal.
"""

from calc.operations import plus, minus, multi, divis, power
from calc.history import log_create, log_del, log_read


def _calculate():
    """Prompt the user for a calculation and log the result."""
    a_num = float(input("Operand #1: "))
    b_num = float(input("Operand #2: "))
    oper = input("Operation (+, -, *, /, **): ")

    if oper == "+":
        result = plus(a_num, b_num)
    elif oper == "-":
        result = minus(a_num, b_num)
    elif oper == "*":
        result = multi(a_num, b_num)
    elif oper == "/":
        result = divis(a_num, b_num)
    elif oper == "**":
        result = power(a_num, b_num)
    else:
        raise ValueError("Unknown operation")

    print(f"Result: {result}")
    log_create(a_num, b_num, oper, result)


def run():
    """Run a simple menu-driven calculator interface."""
    while True:
        print("\n1) Calculate\n2) History\n3) Delete History\n4) Exit")
        choice = input("Select option: ")

        if choice == "1":
            try:
                _calculate()
            except Exception as error:  # pylint: disable=broad-except
                print(error)
        elif choice == "2":
            history = log_read()
            if history:
                print(history)
            else:
                print("Log file is empty.")
        elif choice == "3":
            print(log_del())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Unknown option")


if __name__ == "__main__":
    run()

