import os
os.system("tput civis")
def run(app):
    print("\033[33m─\033[0m" * os.get_terminal_size().columns)
    print("\033[2J\033[H", flush=True)
    print("\033[36mKoala\033[0m".center(os.get_terminal_size().columns))
    print("\033[33m─\033[0m" * os.get_terminal_size().columns)
    app()
def terminal():
    while True:
        os.system("tput civis")
        a = input(">")
        os.system("tput civis")
        if a != "exit":
            os.system(a)
        
c = os.get_terminal_size().columns
print("\033[33m─\033[0m" * os.get_terminal_size().columns)
print("\033[2J\033[H", flush=True)
print("\033[36mKoala\033[0m".center(os.get_terminal_size().columns))
c = os.get_terminal_size().columns
print("\033[33m─\033[0m" * os.get_terminal_size().columns)
print("\033[34m", end="")
if os.get_terminal_size().lines < 6:
    print("Autumn")
else:
    print("Sh../\\ /^\\".center(c))
    print(" /^\\/  \\   \\".center(c))
    print(" /__\\  /_____\\\n".center(c))
print("\033[0m", end="")

print(" > | Lynx".center(c))
print("Apps >".center(c))

os.system("tput civis")
g = input()
match g:
    case "1":
        run(terminal)