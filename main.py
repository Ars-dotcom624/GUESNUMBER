import random


def play_game():
    print("Добро пожаловать в игру «Угадай число»!")
    print("Я загадал число от 1 до 100. Попробуй его угадать.\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("Введи число (или 'q' для выхода): ").strip()

        if user_input.lower() == "q":
            print(f"Вы вышли из игры. Загаданное число было: {secret_number}")
            break

        if not user_input.isdigit():
            print("Пожалуйста, введи целое число.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < 1 or guess > 100:
            print("Число должно быть от 1 до 100.")
            continue

        if guess < secret_number:
            print("Моё число **больше**. Попробуй ещё.\n")
        elif guess > secret_number:
            print("Моё число **меньше**. Попробуй ещё.\n")
        else:
            print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток 🎉")
            break


if __name__ == "__main__":
    play_game()
