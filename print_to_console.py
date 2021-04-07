def print_title():
    print("""
     
                  __   ____ ______  ____  ___  __   __ __  __     
                 / /  / __/_  __( )/ __/ / _ \/ /  / _ \ \/ /     
                / /__/ _/  / /  |/_\ \  / ___/ /__/ __ |\  /      
               /____/___/_/_/    /___/ /_/  /____/_/_|_|/_/
        __  ___ __   ____ ____ ___ ___   _  ____  _ _ _ __ ____ __
       /  |/  / _ | / __/_  __/ __/ _ \/ / / __ \/ ___/  _/ ___/ /
      / /|_/ / __ |_\ \  / / / _// , _/ /_/ /_/ / (_ _/ // /__/_/ 
     /_/  /_/_/ |_/___/ /_/ /___/_/|_/____\____/\___/___/\___(_)  
                                                                  
     
""")


def print_options():
    print("""
                    +-----------------------------+
                    |          0 - Exit           |
                    |          1 - Play           |
                    |          2 - Rules          |
                    +-----------------------------+
""")


def print_rules():
    print("""
  +----------------------------------------------------------------------------+
  |  The program will think of a four digit number, which you have to guess.   |
  |                    EVERY DIGIT IS A DIFFERENT NUMBER!!!                    |
  |      After each guess, you will get an evaluation, about how you did.      |
  |       X - a number, which was good, and it was at the right place          |
  |       O - a number, which was good, but it was not at the right place      |
  | If you write 'quit' during the game, the program returns to the main menu. |
  +----------------------------------------------------------------------------+
""")


def print_winner():
    print("""
      _      __ __ _  _ _  __ ___ __  __
     | | /| / /  _/ |/ / |/ / __/ _ \/ /
     | |/ |/ _/ //    /    / _// , _/_/ 
     |__/|__/___/_/|_/_/|_/___/_/|_(_)  
                                       
""")


def print_looser():
    print("""
        __  ____  ____  ___ ____ __  __
       / / / __ \/ __ \/ __/ __/ _ \/ /
      / /_/ /_/ / /_/ _\ \/ _// , _/_/ 
     /____\____/\____/___/___/_/|_(_)  

""")


def print_previos_guesses(guesses):
    print()
    for index, line in enumerate(guesses, 1):
        print('{:>15}. {} {:>8}'.format(index, line[0], line[1]))
