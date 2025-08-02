#!/usr/bin/env python3
"""Command line interface for the calculator."""

import argparse


def main():
    """Parse command line arguments and run the calculator."""
    parser = argparse.ArgumentParser(description="Calculator CLI")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    subparsers.add_parser("run", help="Launch the calculator")

    args = parser.parse_args()

    if args.command == "run":
        from main import run as run_cli  # Import here to keep startup fast
        run_cli()


if __name__ == "__main__":
    main()
