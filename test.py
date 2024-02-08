from pyfiglet import Figlet

def create_colored_ascii_art(name, font='slant', color='red'):
    fig = Figlet(font=font)
    ascii_art = fig.renderText(name)
    
    # ANSI color codes
    color_codes = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m',
    }

    # Apply color to the ASCII art
    colored_ascii_art = f"{color_codes[color]}{ascii_art}{color_codes['reset']}"
    
    return colored_ascii_art

# Replace 'Your Name' with the desired name
name = 'Night Stalker'

# Replace 'red' with your desired color (e.g., 'blue', 'green', 'yellow', etc.)
ascii_art = create_colored_ascii_art(name, color='cyan')

# Print the colored ASCII art
print(ascii_art)