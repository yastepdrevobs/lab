while True:
    # Запит шляху до файлу
    filename = input("Введіть шлях до файлу: ")

    try:
        # Відкриваємо файл
        with open(filename, "r") as file:
            # Робимо змінні для статистики по нулях
            num_lines = 0
            num_empty_lines = 0
            num_z_lines = 0
            num_z_chars = 0
            num_and_lines = 0

            # Читаємо файл по рядках
            for line in file:
                # Збільшуємо рядки
                num_lines += 1

                # Перевіряємо, чи є рядок порожнім
                if line.strip() == "":
                    num_empty_lines += 1

                # Перевіряємо, чи містить рядок літеру "z"
                if "z" in line:
                    num_z_lines += 1

                # Рахуємо кількість літер "z" у файлі
                num_z_chars += line.count("z")

                # Перевіряємо, чи містить рядок групу символів "and"
                if "and" in line:
                    num_and_lines += 1

            # Виводимо статистику на екран
            print("Кількість рядків: ", num_lines)
            print("Кількість порожніх рядків: ", num_empty_lines)
            print("Кількість рядків з літерою 'z': ", num_z_lines)
            print("Кількість літер 'z' у файлі: ", num_z_chars)
            print("Кількість рядків з групою символів 'and': ", num_and_lines)
            # Вивід попередження наявності z
            if num_z_chars > 1:
                print("Ви що наробили...")
            else:
                print("Підозрілих символів не виявлено.\nВи отримаєте додаткову ТАРІЛКУ БОРЩ!")

    # Так сказали в гайді на ютубі. Виводить помилку.
    except FileNotFoundError:
        print("Файл не знайдено.")

    # Запит користувача на продовження роботи програми
    answer = input("Проаналізувати ще один файл? (y/n): ")
    if answer.lower() == "n":
        break
#Кінець