import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_directory_structure(path, prefix=''):
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
            print_directory_structure(item, prefix + '    ')
        else:
            print(f"{prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python hw03.py /path/to/directory")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"Error: The path '{directory_path}' does not exist.")
        sys.exit(1)

    if not directory_path.is_dir():
        print(f"Error: The path '{directory_path}' is not a directory.")
        sys.exit(1)

    init(autoreset=True)
    print(f"{Fore.BLUE}{directory_path.name}{Style.RESET_ALL}")
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()


import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Помилка: Будь ласка, вкажіть шлях до директорії.")
    print(f"Використання: python {sys.argv[0]} /шлях/до/директорії")
    sys.exit(1)

directory = Path(sys.argv[1])

if not directory.exists() or not directory.is_dir():
    print("Помилка: Вказаний шлях не є директорією або не існує.")
    sys.exit(1)

print(f"Шлях до директорії: {directory}")
