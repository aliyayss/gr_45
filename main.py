from decouple import config
from logic import guess_number_game

def main():
    min_number = int(config('min_number'))
    max_number = int(config('max_number'))
    attempts = int(config('attempts'))
    capital = int(config('capital'))

    guess_number_game(min_number, max_number, attempts, capital)

if __name__ == "__main__":
    main()
