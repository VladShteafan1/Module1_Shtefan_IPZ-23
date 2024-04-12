import pytest
from main import read_population_data, calculate_population_change

# Фікстура, що надає зразкові дані про популяцію для тестів
@pytest.fixture
def sample_population_data():
    return {
        'Country1': {2000: 100, 2001: 110, 2002: 120},
        'Country2': {2000: 200, 2001: 210, 2002: 220}
    }

# Тест для функції read_population_data
def test_read_population_data(tmp_path, sample_population_data):
    # Створюємо тимчасовий файл з даними про популяцію
    file_path = tmp_path / "population.txt"
    with open(file_path, 'w') as file:
        # Заповнюємо файл зразковими даними
        for country, data in sample_population_data.items():
            for year, population in data.items():
                file.write(f"{country},{year},{population}\n")
    # Викликаємо функцію read_population_data для тестування
    data = read_population_data(file_path)
    # Перевіряємо, чи отримані дані співпадають з очікуваними
    assert data == sample_population_data

# Тест для функції calculate_population_change
def test_calculate_population_change(sample_population_data):
    # Очікуваний результат обчислення зміни популяції
    expected_result = {
        'Country1': {2001: 10, 2002: 10},
        'Country2': {2001: 10, 2002: 10}
    }
    # Викликаємо функцію calculate_population_change для тестування
    result = calculate_population_change(sample_population_data)
    # Перевіряємо, чи отриманий результат співпадає з очікуваним
    assert result == expected_result