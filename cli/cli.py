import os

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


# Runs the interactive loop: echoes input, handles "status", stops on "exit".
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
        print(line)


if __name__ == "__main__":
    main()
