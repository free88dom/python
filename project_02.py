import random
from time import perf_counter
from datetime import date


def number_generator() -> list:
    while gen_num := [i for i in str(random.randint(1000, 9999))]:
        if len(gen_num) == len(set(gen_num)):
            gen_num_li = [i for i in gen_num]
            break
    return gen_num_li


def main_game(gen_num_list: list, number_to_guess: list) -> list:
    output_list = [0, 0]
    for x, y in zip(number_to_guess, gen_num_list):
        if x in gen_num_list:
            if x == y:
                output_list[0] += 1
            else:
                output_list[1] += 1
    return output_list


def open_results(filename, args, encoding):
    try:
        filename = open(filename, mode=args, encoding=encoding)
    except FileNotFoundError:
        return f"File with scores isn't available yet, try run first game to save/create the file"
    else:
        return filename


if __name__ == "__main__":
    print(f"**** Welcome to Bulls and Cows game ****",
          sep=f"{'*'*20}", end="\n")

    while not (player := input(f"Enter your name(nickname): ")):
        print(f"At least a nickname give us, don't worry, it's just for table score... :-) ")
    number_to_guess = number_generator()
    perf_counter()
    count_of_tries = 0

    while True:
        while not (number_list := input(f"Guess the number: ")).isdigit() or len(number_list) != len(set(number_list)) \
                or len(list(number_list)) != 4 or list(number_list)[0] == 0:
            print(f"Wrong input, has to be 4 exclusive digits.")
        number_list = list(number_list)
        game = main_game(number_list, number_to_guess)
        print(f"{game[0]} bull" if game[0] <= 1 else f"{game[0]} bulls", f"{game[1]} cow" if game[1] <= 1 else
              f"{game[1]} cows")
        count_of_tries += 1

        if game[0] == 4:
            print(f"That's the guessed number, it's cost you {count_of_tries} tries")
            record_to_insert = (f"{date.today()} - {player} - {count_of_tries} try\n" if count_of_tries == 1
                                else f"{date.today()} - {player} - {count_of_tries} tries\n")

            open_results("user_score.txt", "a", "utf-8").writelines(record_to_insert)

            show_results = (open_results("user_score.txt", "r", "utf-8").readlines())
            print(f"Summary of results", "".join([str(i) for i in show_results]), sep="\n")

            open_results("user_score.txt", "a", "utf-8").close()
            break
