from typing import List, Dict


# Helper for memoization recursion
def _cut_rod_memo_helper(
    k: int, prices: List[int], memo: List[int], cuts_memo: List[int]
) -> int:
    """
    Рекурсивна функція для знаходження максимального прибутку
    за допомогою мемоізації.

    Args:
        k: поточна довжина стрижня
        prices: список цін
        memo: таблиця для зберігання вже обчислених результатів
        cuts_memo: таблиця для зберігання оптимального першого розрізу для кожної довжини

    Returns:
        Максимальний прибуток для стрижня довжини k
    """
    if k == 0:
        return 0

    if memo[k] != -1:
        return memo[k]

    max_p = -1

    for j in range(1, k + 1):
        current_p = prices[j - 1] + _cut_rod_memo_helper(k - j, prices, memo, cuts_memo)
        if current_p > max_p:
            max_p = current_p
            cuts_memo[k] = j

    memo[k] = max_p
    return max_p


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """

    memo = [-1] * (length + 1)
    cuts_memo = [0] * (length + 1)

    max_profit = _cut_rod_memo_helper(length, prices, memo, cuts_memo)

    cuts = []
    current_length = length
    while current_length > 0:
        cut_size = cuts_memo[current_length]
        cuts.append(cut_size)
        current_length -= cut_size

    number_of_cuts = len(cuts) - 1

    return {"max_profit": max_profit, "cuts": cuts, "number_of_cuts": number_of_cuts}


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """

    dp = [0] * (length + 1)
    s = [0] * (length + 1)

    for i in range(1, length + 1):
        max_p = -1

        for j in range(1, i + 1):
            current_p = prices[j - 1] + dp[i - j]
            if current_p > max_p:
                max_p = current_p
                s[i] = j
        dp[i] = max_p

    max_profit = dp[length]

    cuts = []
    current_length = length
    while current_length > 0:
        cut_size = s[current_length]
        cuts.append(cut_size)
        current_length -= cut_size

    number_of_cuts = len(cuts) - 1

    return {"max_profit": max_profit, "cuts": cuts, "number_of_cuts": number_of_cuts}


def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {"length": 5, "prices": [2, 5, 7, 8, 10], "name": "Базовий випадок"},
        # Тест 2: Оптимально не різати
        {"length": 3, "prices": [1, 3, 8], "name": "Оптимально не різати"},
        # Тест 3: Всі розрізи по 1
        {"length": 4, "prices": [3, 5, 6, 7], "name": "Рівномірні розрізи"},
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test["length"], test["prices"])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test["length"], test["prices"])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")


if __name__ == "__main__":
    run_tests()
