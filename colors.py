COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'pink': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'close': '\033[0m'
}

def give_color(text, color): 
    if not color in COLORS: return text
    return COLORS[color]+text+COLORS['close']