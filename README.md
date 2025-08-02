# Terminal Calculator

This project originally relied on the obsolete `npyscreen` library to
provide a terminal user interface. It now uses Python's built-in
`curses` module to deliver a lightweight text UI that runs in any
terminal without external dependencies.

## Installation

No external dependencies are required.

## Usage

Launch the calculator from the command line:

```bash
./app run
```

Use the on-screen menu to perform calculations, review the history log,
or delete stored history entries. Navigate with the arrow keys or press
the number keys `1`‑`4` to select an option.

