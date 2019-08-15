
BANNER = '''                                            
@@@  @@@  @@@@@@@@  @@@@@@@   @@@   @@@@@@   
@@@  @@@  @@@@@@@@  @@@@@@@@  @@@  @@@@@@@   
@@!  !@@  @@!       @@!  @@@  @@!  !@@       
!@!  @!!  !@!       !@!  @!@  !@!  !@!       
@!@@!@!   @!!!:!    @!@!!@!   !!@  !!@@!!    
!!@!!!    !!!!!:    !!@!@!    !!!   !!@!!!   
!!: :!!   !!:       !!: :!!   !!:       !:!  
:!:  !:!  :!:       :!:  !:!  :!:      !:!   
 ::  :::   :: ::::  ::   :::   ::  :::: ::   
 :   :::  : :: ::    :   : :  :    :: : :

 brute force tools                                                
'''


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

def menu_one():
    print('call menu_one()')
    input('press [Enter]..')

def menu_two():
    print('call menu_two()')
    input('press [Enter]..')

menus = [
    {'menu one': menu_one},
    {'menu two': menu_two},
    {'exit': exit}
]

def main_menu():
    for menu in menus:
        print('['+ give_color(str(menus.index(menu)), 'red') +'] ' + list(menu.keys())[0])

if __name__ == '__main__':
    while True:
        print(give_color(BANNER, 'red'))
        main_menu()

        choice = input('>> ')
        try:
            if int(choice) < 0: raise ValueError

            menu = menus[int(choice)]
            list(menu.values())[0]()
        except(ValueError, IndexError):
            main_menu()