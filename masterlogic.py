import print_to_console as p
import game_logic as g


def main_menu():
    g.clear()
    p.print_title()
    p.print_options()
    choice = None
    while choice not in ['0', '1', '2']:
        choice = input("       Select: ")
    if choice == '0':
        g.clear()
        exit()
    elif choice == '1':
        LIVES = 10
        g.main(LIVES)
    elif choice == '2':
        g.clear()
        p.print_title()
        p.print_rules()
        input('  Press ENTER to return to main menu!')
        g.clear()
        main_menu()


if __name__ == '__main__':
    main_menu()