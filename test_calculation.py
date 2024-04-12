import pytest
from main import read_population_data, calculate_population_change

# Фікстура, що надає зразкові дані про популяцію для тестів
@pytest.fixture
def sample_population_data():
    return {
        'Country1': {2000: 100, 2001: 110, 2002: 120},
        'Country2': {2000: 200, 2001: 210, 2002: 220}
    }
