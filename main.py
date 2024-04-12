def read_population_data(file_name):
    # Створюємо порожній словник для зберігання даних про популяцію
    population_data = {}
    # Відкриваємо файл для читання
    with open(file_name, 'r') as file:
        # Проходимося по кожному рядку у файлі
        for line in file:
            # Розбиваємо рядок на компоненти: країна, рік, популяція
            country, year, population = line.strip().split(',')
            # Перетворюємо рік і популяцію у цілі числа
            year = int(year)
            population = int(population)
            # Якщо країна відсутня у словнику, створюємо для неї новий словник
            if country not in population_data:
                population_data[country] = {}
            # Додаємо популяцію для відповідного року
            population_data[country][year] = population
    # Повертаємо словник з даними про популяцію
    return population_data

def calculate_population_change(population_data):
    # Створюємо порожній словник для зберігання змін популяції
    population_change = {}
    # Проходимося по кожній країні та її даним про популяцію
    for country, data in population_data.items():
        # Сортуємо роки у порядку зростання
        years = sorted(data.keys())
        change = {}
        # Проходимося по кожному році, обчислюємо зміну популяції
        for i in range(1, len(years)):
            prev_year = years[i - 1]
            curr_year = years[i]
            prev_population = data[prev_year]
            curr_population = data[curr_year]
            population_difference = curr_population - prev_population
            # Додаємо зміну до словника
            change[curr_year] = population_difference
        # Додаємо словник зі змінами популяції для країни до загального словника
        population_change[country] = change
    # Повертаємо словник зі змінами популяції
    return population_change

def main():
    # Запитуємо у користувача назву файлу
    file_name = "population.txt"
    try:
        # Зчитуємо дані з файлу
        population_data = read_population_data(file_name)
        # Обчислюємо зміни популяції
        population_change = calculate_population_change(population_data)
        # Виводимо результат
        for country, change in population_change.items():
            print(f"Зміна населення у країні {country}:")
            for year, population_change in change.items():
                print(f"Рік {year}: Зміна населення {population_change}")
            print()
    except FileNotFoundError:
        # Обробляємо випадок, коли файл не знайдено
        print("Файл не знайдено.")
    except Exception as e:
        # Обробляємо інші винятки
        print("Виникла помилка:", e)

if __name__ == "__main__":
    main()


