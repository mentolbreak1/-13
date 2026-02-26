"""
Общие фикстуры для тестов.
"""
import pytest

@pytest.fixture
def sample_investment_data():
    """Образец данных для тестирования инвестиций."""
    return {
        'principal': 10000,
        'rate': 8,
        'time': 5,
        'n': 12
    }

@pytest.fixture
def sample_tax_data():
    """Образец данных для тестирования налогов."""
    return {
        'amount': 50000,
        'tax_rate': 13
    }
