import os
import time
os.system("tput civis")
def resl():
    print("\033[2J\033[H", flush=True)
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
        print("Sh.../\\ /^\\   ".center(c))
        print(" /^\\/  \\   \\   ".center(c))
        print(" /__\\  /_____\\   \n".center(c))
    print("\033[0m", end="")
    print(" > | Lynx".center(c))
    print("Apps >".center(c))
    os.system("tput civis")
    g = input()
    match g:
        case "1":
            run(terminal)
        case "\x02":
            os.system("tput cnorm")
            os.system("clear")
            os.system("exit")
def run(app):
    print("\033[33m─\033[0m" * os.get_terminal_size().columns)
    print("\033[2J\033[H", flush=True)
    os.system("tput civis")
    print("\033[36mKoala\033[0m".center(os.get_terminal_size().columns))
    print("\033[33m─\033[0m" * os.get_terminal_size().columns)
    print("".center(c))
    print("".center(c))
    print("".center(c))
    print(" ____".center(c))
    print("[____]".center(c))
    time.sleep(0.02)
    print("\033[2J\033[H", flush=True)
    print("\033[36mKoala\033[0m".center(os.get_terminal_size().columns))
    print("\033[33m─\033[0m" * os.get_terminal_size().columns)
    print("".center(c))
    print("".center(c))
    print("".center(c))
    print(" ______".center(c))
    print("[>_____]".center(c))
    time.sleep(0.02)
    print("\033[2J\033[H", flush=True)
    time.sleep(0.02)
    
    print("\033[36mKoala\033[0m".center(os.get_terminal_size().columns))
    print("\033[33m─\033[0m" * os.get_terminal_size().columns)
    print("".center(c))
    print("_______".center(c))
    print("|>     |".center(c))
    print("|      |".center(c))
    print("[______]".center(c))
    time.sleep(0.02)
    print("\033[2J\033[H", flush=True)
    time.sleep(0.02)
    
    print("\033[36mKoala\033[0m".center(os.get_terminal_size().columns))
    print("\033[33m─\033[0m" * os.get_terminal_size().columns)
    print("".center(c))
    print("___________".center(c))
    print("|>        |".center(c))
    print("|         |".center(c))
    print("[_________]".center(c))
    time.sleep(0.02)
    print("\033[2J\033[H", flush=True)
    time.sleep(0.02)
    
    print("\033[36mKoala\033[0m".center(os.get_terminal_size().columns))
    print("\033[33m─\033[0m" * os.get_terminal_size().columns)
    print("".center(c))
    print("____________".center(c))
    print("|>         |".center(c))
    print("|          |".center(c))
    print("[__________]".center(c))
    time.sleep(0.05)
    print("\033[2J\033[H")
    print("\033[36mKoala\033[0m")
    print("\033[33m─\033[0m" * os.get_terminal_size().columns)
    os.system("tput cnorm")
    app()    
def terminal():
    while True:
        os.system("tput civis")
        a = input(">")
        os.system("tput civis")
        if a != "CloseProcess":
            os.system(a)
        else:
            resl() 
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
    print("Sh../\\ /^\\   ".center(c))
    print(" /^\\/  \\   \\   ".center(c))
    print(" /__\\  /_____\\   \n".center(c))
    
print("\033[0m", end="")

print(" >       |       Lynx".center(c))
print("Apps         >".center(c))

os.system("tput civis")
g = input()
match g:
    case "1":
        run(terminal)
