#!/usr/bin/env python3
"""Command line interface for the TUI calculator."""

import argparse


def main():
    """Parse command line arguments and run the TUI calculator."""
    parser = argparse.ArgumentParser(description="TUI calculator CLI")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    subparsers.add_parser("run", help="Launch the TUI calculator")

    args = parser.parse_args()

    if args.command == "run":
        from main import App  # Import here to avoid dependency during --help
        App().run()


if __name__ == "__main__":
    main()
