"""
Модуль с функциями для финансовых расчетов.
Содержит функции для расчета простых и сложных процентов, а также налогов.
"""

def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Расчет простых процентов.
    
    Формула: principal * rate * time / 100
    
    Args:
        principal: Основная сумма (неотрицательная)
        rate: Процентная ставка (неотрицательная)
        time: Время в годах (неотрицательное)
    
    Returns:
        float: Сумма процентов
    
    Raises:
        ValueError: Если любой аргумент отрицательный
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    
    return principal * rate * time / 100


def calculate_compound_interest(principal: float, rate: float, time: float, n: int = 1) -> float:
    """
    Расчет сложных процентов.
    
    Формула: principal * (1 + rate/(100*n))**(n*time)
    
    Args:
        principal: Основная сумма (неотрицательная)
        rate: Процентная ставка (неотрицательная)
        time: Время в годах (неотрицательное)
        n: Количество начислений процентов в год (целое положительное)
    
    Returns:
        float: Итоговая сумма (основная сумма + проценты)
    
    Raises:
        ValueError: Если аргументы некорректны
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("principal, rate и time должны быть неотрицательными")
    
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n должно быть целым положительным числом")
    
    return principal * (1 + rate/(100*n))**(n*time)


def calculate_tax(amount: float, tax_rate: float) -> float:
    """
    Расчет налога.
    
    Формула: amount * tax_rate / 100
    
    Args:
        amount: Сумма (неотрицательная)
        tax_rate: Ставка налога (от 0 до 100 включительно)
    
    Returns:
        float: Сумма налога
    
    Raises:
        ValueError: Если tax_rate не в диапазоне [0, 100] или amount отрицательный
    """
    if amount < 0:
        raise ValueError("Сумма должна быть неотрицательной")
    
    if not (0 <= tax_rate <= 100):
        raise ValueError("Ставка налога должна быть от 0 до 100")
    
    return amount * tax_rate / 100


# Дополнительные полезные функции (опционально)
def calculate_total_with_tax(amount: float, tax_rate: float) -> float:
    """
    Расчет общей суммы с налогом.
    
    Args:
        amount: Сумма до налога
        tax_rate: Ставка налога
    
    Returns:
        float: Сумма с налогом
    """
    tax = calculate_tax(amount, tax_rate)
    return amount + tax


def calculate_annual_percentage_yield(rate: float, n: int) -> float:
    """
    Расчет годовой процентной доходности (APY).
    
    Args:
        rate: Номинальная процентная ставка
        n: Количество начислений в год
    
    Returns:
        float: Эффективная годовая ставка
    """
    return ((1 + rate/(100*n))**n - 1) * 100


if __name__ == "__main__":
    # Примеры использования
    print("=== Финансовый калькулятор ===\n")
    
    # Пример простых процентов
    p = 1000
    r = 5
    t = 3
    simple = calculate_simple_interest(p, r, t)
    print(f"Простые проценты:")
    print(f"Сумма: {p}, ставка: {r}%, время: {t} года")
    print(f"Сумма процентов: {simple:.2f}")
    print(f"Итоговая сумма: {p + simple:.2f}\n")
    
    # Пример сложных процентов
    compound = calculate_compound_interest(p, r, t, n=12)
    print(f"Сложные проценты (ежемесячная капитализация):")
    print(f"Сумма: {p}, ставка: {r}%, время: {t} года")
    print(f"Итоговая сумма: {compound:.2f}")
    print(f"Сумма процентов: {compound - p:.2f}\n")
    
    # Пример налога
    amount = 50000
    tax_rate = 13
    tax = calculate_tax(amount, tax_rate)
    print(f"Налог:")
    print(f"Сумма: {amount}, ставка налога: {tax_rate}%")
    print(f"Сумма налога: {tax:.2f}")
    print(f"Сумма после налога: {amount - tax:.2f}")
