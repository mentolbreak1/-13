# Примеры использования финансового калькулятора

## Пример 1: Расчет ипотеки
```python
from calculator import calculate_compound_interest

# Сумма кредита: 3,000,000 руб.
# Ставка: 10% годовых
# Срок: 15 лет
# Ежемесячная капитализация

principal = 3_000_000
rate = 10
time = 15
n = 12

total = calculate_compound_interest(principal, rate, time, n)
print(f"Общая сумма к выплате: {total:,.2f} руб.")
print(f"Переплата: {total - principal:,.2f} руб.")
