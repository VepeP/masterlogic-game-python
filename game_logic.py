import random, math, os
import print_to_console as p

def clear():
    os.system('cls') if os.name == "nt" else os.system('clear')


def main(LIVES):
    clear()
    guess_count = 0
    guess_number = get_number_to_guess()   
    player_guess = -1
    guesses = []
    while guess_count < LIVES and guess_number != player_guess:
        clear()
        print("    Guess a four digit number!")
        # print(guess_number)
        p.print_previos_guesses(guesses)
        player_guess = get_player_guess(guess_count)
        evaluated_guess = evaluate_guess(guess_number, player_guess)
        guesses.append([player_guess, evaluated_guess])
        guess_count += 1
    clear()
    p.print_previos_guesses(guesses)
    if guess_number == player_guess:
        p.print_winner()
    else:
        p.print_looser()
    print(f"  The number was: {guess_number}")
    input('  Press ENTER to return to main menu!')
    clear()
    main_menu()


def evaluate_guess(guess_number, player_guess):
    result = ""
    good_in_place = 0
    good_not_in_place = 0
    for index, num in enumerate(str(guess_number)):
        if num == str(player_guess)[index]:
            good_in_place += 1
        elif num in str(player_guess):
            good_not_in_place += 1            
    result = " ".join("X" * good_in_place + "O" * good_not_in_place) if good_in_place + good_not_in_place > 0 else "-"
    return result


def get_player_guess(guess_count):
    number = ""
    while check_number(number) and number != "quit":
        number = input("{:>10}. try: ".format(guess_count + 1))
    if number == 'quit':
        clear()
        main_menu()
    else:
        return int(number)


def get_number_to_guess():
    NUMFROM = 1000
    NUMTO = 10000
    number = random.randint(NUMFROM, NUMTO)
    while has_doubles(number):
        number = random.randint(NUMFROM, NUMTO)
    return number


def check_number(number):
    return has_doubles(number) or not number.isdigit() or len(str(number)) != 4 or int(number) < 1000


def has_doubles(number):
    return len(set(str(number))) < len(str(number))