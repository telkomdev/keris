#!/usr/bin/env python

import sys
import common
from colors import give_color
from port_scanner import scan_ports

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

 :a collection of brute force tools and network utility: version 0.0.0                                          
'''

def menu_whois():
    host = input(give_color('input some domain [eg: www.example.com]:', 'red'))
    if len(host) <= 0:
        print(give_color('invalid host', 'red'))
        return


    lines = common.who_is(host)
    for line in lines:
        print(line)

def menu_port_scanner():
    host = input(give_color('input some domain [eg: www.example.com]:', 'red'))

    if len(host) <= 0:
        print(give_color('invalid host', 'red'))
        return

    from_port = input(give_color('from port [eg: 8000]:', 'red'))
    if (not from_port.isdigit()):
        print(give_color('invalid port number', 'red'))
        return
    
    to_port = input(give_color('to port [eg: 9000]:', 'red'))
    if (not to_port.isdigit()):
        print(give_color('invalid port number', 'red'))
        return

    result = scan_ports(host, int(from_port), int(to_port))
    if (result != "DONE"):
        print(give_color('error {}'.format(result), 'red'))
        return

def menu_ssh():
    host = input(give_color('input some domain for brute ssh [eg: www.example.com]: ', 'red'))

def manu_exit():
    print(give_color('bye..', 'cyan'))
    sys.exit(0)

menus = [
    {'show whois data': menu_whois},
    {'brute ssh': menu_ssh},
    {'port scanner': menu_port_scanner},
    {'exit': manu_exit}
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