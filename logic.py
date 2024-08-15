import random

def guess_number_game(min_number, max_number, attempts, capital):
    rand_number = random.randint(min_number, max_number)
    print(f'У вас осталось {attempts} попыток')

    for attempt in range(1, attempts + 1):
        print(f"Попытка {attempt}.")
        bet = int(input(f"Введите вашу ставку: "))

        guess = int(input(f"Введите число: "))

        if guess == rand_number:
            winnings = bet * 2
            capital += winnings
            print(f"Вы угадали число. Ваш капитал: {capital}")
            break
        else:
            capital -= bet
            print(f"Неверно. Ваш капитал: {capital}")

        if capital <= 0:
            print("Вы потеряли весь капитал!")
            break

    if capital > 0 and guess != rand_number:
        print(f"Вы не угадали число. Загаданное число было: {rand_number}")


    print("Игра окончена.")
