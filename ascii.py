import pyfiglet
from colorama import init, Fore, Style
import webbrowser

init()
url="https://www.instagram.com/code_dreamerr_?igsh=d21nZzlmbmw5ZHAO"

def show_banner():
    banner =r"""
                 / \  / ___| / ___|_ _|_ _|      / \  |  _ \_   _|
                / _ \ \___ \| |    | | | |_____ / _ \ | |_) || |
               / ___ \ ___) | |___ | | | |_____/ ___ \|  _ < | |
              /_/   \_\____/ \____|___|___|   /_/   \_\_| \_\|_|
                                                                    
             Developer:-Abhishek|version-1.0|By-pyhacker01|@code_dreamerr_                                                 
                                                                                   """
    print(Fore.YELLOW + banner + Style.RESET_ALL)  

def text_to_ascii_art(text, font="slant"):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    return ascii_art


show_banner()
webbrowser.open(url)

user_input = input("Enter a word or a small sentence, with or without symbols: ")

choice = input("Do you want the text in uppercase (A) or lowercase (L)? (default is original): ").strip().upper()
if choice == "A":
    user_input = user_input.upper()
elif choice == "L":
    user_input = user_input.lower()

available_fonts = ["slant", "standard", "digital", "block", "banner3-D"]
print("\nAvailable fonts:", ", ".join(available_fonts))
font_choice = input("Choose a font (default is slant): ").strip()
if font_choice == "":
    font_choice = "slant"

# Validate font choice
if font_choice not in available_fonts:
    print(f"Font '{font_choice}' is not available. Defaulting to 'slant'.")
    font_choice = "slant"

color_options = {
    "1": Fore.RED,
    "2": Fore.GREEN,
    "3": Fore.BLUE,
    "4": Fore.CYAN,
    "5": Fore.MAGENTA,
    "6": Fore.YELLOW,
    "7": Fore.WHITE,
}

print("\nChoose a color for the ASCII art:")
for key, value in color_options.items():
    print(f"{key}: {value}Sample Text{Style.RESET_ALL}")  
color_choice = input("Enter the number corresponding to your choice: ").strip()
selected_color = color_options.get(color_choice, Fore.GREEN)

ascii_banner = text_to_ascii_art(user_input, font=font_choice)
print(selected_color + ascii_banner + Style.RESET_ALL)  