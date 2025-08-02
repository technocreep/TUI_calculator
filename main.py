"""Curses-based terminal interface for the calculator."""

import curses

from calc.operations import plus, minus, multi, divis, power
from calc.history import log_create, log_del, log_read

MENU = ["Calculate", "History", "Delete History", "Exit"]


def _draw_menu(stdscr, selected):
    """Render the main menu with the selected item highlighted."""
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    for idx, row in enumerate(MENU):
        x_pos = width // 2 - len(row) // 2
        y_pos = height // 2 - len(MENU) // 2 + idx
        if idx == selected:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y_pos, x_pos, row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y_pos, x_pos, row)
    stdscr.refresh()


def _prompt(stdscr, prompt, line):
    """Prompt the user for input on a given line and return the string."""
    stdscr.addstr(line, 0, prompt)
    stdscr.clrtoeol()
    stdscr.refresh()
    curses.echo()
    value = stdscr.getstr(line, len(prompt)).decode()
    curses.noecho()
    return value


def _calculate(stdscr):
    """Collect operands and operation, perform calculation and log it."""
    stdscr.clear()
    try:
        a_num = float(_prompt(stdscr, "Operand #1: ", 0))
        b_num = float(_prompt(stdscr, "Operand #2: ", 1))
        oper = _prompt(stdscr, "Operation (+, -, *, /, **): ", 2)
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
        log_create(a_num, b_num, oper, result)
        stdscr.addstr(4, 0, f"Result: {result}")
    except Exception as exc:  # pylint: disable=broad-except
        stdscr.addstr(4, 0, str(exc))
    stdscr.addstr(6, 0, "Press any key to return to menu")
    stdscr.getch()


def _show_history(stdscr):
    """Display the stored calculation history."""
    stdscr.clear()
    history = log_read()
    if history:
        stdscr.addstr(0, 0, history)
    else:
        stdscr.addstr(0, 0, "Log file is empty.")
    stdscr.addstr(2, 0, "Press any key to return to menu")
    stdscr.getch()


def _delete_history(stdscr):
    """Delete the history log file if present."""
    stdscr.clear()
    stdscr.addstr(0, 0, log_del())
    stdscr.addstr(2, 0, "Press any key to return to menu")
    stdscr.getch()


def _main(stdscr):
    """Entry point for the curses application."""
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    current = 0
    while True:
        _draw_menu(stdscr, current)
        key = stdscr.getch()
        if key == curses.KEY_UP and current > 0:
            current -= 1
        elif key == curses.KEY_DOWN and current < len(MENU) - 1:
            current += 1
        elif key in (curses.KEY_ENTER, ord("\n")):
            if current == 0:
                _calculate(stdscr)
            elif current == 1:
                _show_history(stdscr)
            elif current == 2:
                _delete_history(stdscr)
            elif current == 3:
                break
        elif key in (ord("1"), ord("2"), ord("3"), ord("4")):
            selection = key - ord("1")
            if selection == 0:
                _calculate(stdscr)
            elif selection == 1:
                _show_history(stdscr)
            elif selection == 2:
                _delete_history(stdscr)
            elif selection == 3:
                break


def run():
    """Run the calculator TUI."""
    curses.wrapper(_main)


if __name__ == "__main__":
    run()
