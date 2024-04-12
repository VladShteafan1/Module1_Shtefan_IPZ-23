def main():
    # Запитуємо у користувача назву файлу
    file_name = input("Введіть назву файлу з даними про популяцію (з розширенням .txt): ")
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


