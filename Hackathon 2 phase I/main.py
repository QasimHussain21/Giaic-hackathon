"""Console Todo Application - Main Entry Point.

A modular, console-based todo application that stores tasks in memory.
Built following spec-driven development principles.
"""

from src.cli.menu import run_application_loop


def main() -> None:
    """Main entry point for the console todo application."""
    run_application_loop()


if __name__ == "__main__":
    main()
