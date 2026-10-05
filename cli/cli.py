import os
import sys
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

load_dotenv()
API_KEY_NAME = "FMP_API_KEY"


# Reads the current status from the API_KEY environment variable (loaded from .env).
# Args: none
# Returns: "online" if API_KEY has a non-empty value, otherwise "offline".
def get_status():
    if os.getenv(API_KEY_NAME, ""):
        return "online"
    return "offline"


# Prints every symbol returned by screen_stocks() in screener/screener.py.
# Args: none
# Returns: nothing.
def load_screener():
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from screener.screener import screen_stocks

    for symbol in screen_stocks():
        print(symbol)


# Runs the interactive loop: echoes input, handles "status" and "load screener", stops on "exit".
# Args: none
# Returns: nothing.
def main():
    while True:
        try:
            line = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        command = line.strip().lower()
        if command == "exit":
            break
        if command == "status":
            print(get_status())
            continue
        if command == "load screener":
            load_screener()
            continue
        print(line)


if __name__ == "__main__":
    main()
