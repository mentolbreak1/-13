"""
Тесты для модуля финансового калькулятора.
"""
import pytest
from calculator import (
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_tax
)


class TestSimpleInterest:
    """Тесты для функции расчета простых процентов."""

    def test_calculation_correctness(self):
        """Проверка правильности расчета."""
        # Тест 1: Стандартный случай
        assert calculate_simple_interest(1000, 5, 3) == 150.0  # 1000 * 5 * 3 / 100 = 150
        
        # Тест 2: Другой пример
        assert calculate_simple_interest(5000, 10, 2) == 1000.0  # 5000 * 10 * 2 / 100 = 1000
        
        # Тест 3: С десятичными значениями
        result = calculate_simple_interest(1500.50, 7.5, 2.5)
        expected = 1500.50 * 7.5 * 2.5 / 100
        assert result == pytest.approx(expected, rel=1e-10)

    def test_zero_values(self):
        """Проверка работы с нулевыми значениями."""
        # Все аргументы равны нулю
        assert calculate_simple_interest(0, 0, 0) == 0.0
        
        # Нулевая основная сумма
        assert calculate_simple_interest(0, 5, 3) == 0.0
        
        # Нулевая ставка
        assert calculate_simple_interest(1000, 0, 3) == 0.0
        
        # Нулевое время
        assert calculate_simple_interest(1000, 5, 0) == 0.0

    def test_negative_values_raise_error(self):
        """Проверка вызова ValueError при отрицательных значениях."""
        # Отрицательная основная сумма
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(-100, 5, 3)
        
        # Отрицательная ставка
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(1000, -5, 3)
        
        # Отрицательное время
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(1000, 5, -3)
        
        # Все аргументы отрицательные
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(-1000, -5, -3)


class TestCompoundInterest:
    """Тесты для функции расчета сложных процентов."""

    def test_calculation_correctness(self):
        """Проверка правильности расчета."""
        # Тест 1: Годовая капитализация (n=1)
        result = calculate_compound_interest(1000, 5, 3, n=1)
        expected = 1000 * (1 + 5/100)**3  # 1157.625
        assert result == pytest.approx(expected, rel=1e-10)
        
        # Тест 2: Ежемесячная капитализация
        result = calculate_compound_interest(1000, 5, 3, n=12)
        expected = 1000 * (1 + 5/(100*12))**(12*3)
        assert result == pytest.approx(expected, rel=1e-10)
        
        # Тест 3: Ежеквартальная капитализация с другой суммой
        result = calculate_compound_interest(5000, 8, 5, n=4)
        expected = 5000 * (1 + 8/(100*4))**(4*5)
        assert result == pytest.approx(expected, rel=1e-10)

    def test_zero_values(self):
        """Проверка работы с нулевыми значениями."""
        # Нулевая основная сумма
        assert calculate_compound_interest(0, 5, 3, n=1) == 0.0
        
        # Нулевая ставка
        assert calculate_compound_interest(1000, 0, 3, n=1) == 1000.0
        
        # Нулевое время
        assert calculate_compound_interest(1000, 5, 0, n=1) == 1000.0
        
        # Все нули
        assert calculate_compound_interest(0, 0, 0, n=1) == 0.0

    def test_negative_values_raise_error(self):
        """Проверка вызова ValueError при отрицательных значениях."""
        # Отрицательная основная сумма
        with pytest.raises(ValueError, match="principal, rate и time должны быть неотрицательными"):
            calculate_compound_interest(-1000, 5, 3, n=1)
        
        # Отрицательная ставка
        with pytest.raises(ValueError, match="principal, rate и time должны быть неотрицательными"):
            calculate_compound_interest(1000, -5, 3, n=1)
        
        # Отрицательное время
        with pytest.raises(ValueError, match="principal, rate и time должны быть неотрицательными"):
            calculate_compound_interest(1000, 5, -3, n=1)

    def test_invalid_n_raises_error(self):
        """Проверка вызова ValueError при некорректном значении n."""
        # n не целое число
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 3, n=1.5)
        
        # n отрицательное
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 3, n=-1)
        
        # n = 0
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 3, n=0)
        
        # n не число
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 3, n="12")


class TestTax:
    """Тесты для функции расчета налога."""

    def test_calculation_correctness(self):
        """Проверка правильности расчета."""
        # Тест 1: Стандартная ставка НДФЛ
        assert calculate_tax(50000, 13) == 6500.0  # 50000 * 13 / 100 = 6500
        
        # Тест 2: НДС
        assert calculate_tax(1000, 20) == 200.0  # 1000 * 20 / 100 = 200
        
        # Тест 3: С десятичными значениями
        result = calculate_tax(1234.56, 15.5)
        expected = 1234.56 * 15.5 / 100
        assert result == pytest.approx(expected, rel=1e-10)

    def test_zero_values(self):
        """Проверка работы с нулевыми значениями."""
        # Нулевая сумма
        assert calculate_tax(0, 13) == 0.0
        
        # Нулевая ставка
        assert calculate_tax(50000, 0) == 0.0
        
        # Все нули
        assert calculate_tax(0, 0) == 0.0

    def test_boundary_values(self):
        """Проверка граничных значений tax_rate."""
        # Минимальная ставка (0)
        assert calculate_tax(50000, 0) == 0.0
        
        # Максимальная ставка (100)
        assert calculate_tax(50000, 100) == 50000.0

    def test_invalid_tax_rate_raises_error(self):
        """Проверка вызова ValueError при некорректной ставке налога."""
        # Отрицательная ставка
        with pytest.raises(ValueError, match="Ставка налога должна быть от 0 до 100"):
            calculate_tax(50000, -5)
        
        # Ставка больше 100
        with pytest.raises(ValueError, match="Ставка налога должна быть от 0 до 100"):
            calculate_tax(50000, 150)

    def test_negative_amount_raises_error(self):
        """Проверка вызова ValueError при отрицательной сумме."""
        with pytest.raises(ValueError, match="Сумма должна быть неотрицательной"):
            calculate_tax(-50000, 13)
