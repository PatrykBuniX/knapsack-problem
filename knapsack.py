def dynamic(weight_limit, weights, values, printTable=False):
    n = len(weights)

    # Inicjalizacja tablicy dynamicznej
    dp = [[0] * (weight_limit + 1) for _ in range(n + 1)]

    # Wykonanie obliczeń dla kolejnych przedmiotów
    for i in range(1, n + 1):
        for w in range(1, weight_limit + 1):
            # Jeśli waga przedmiotu jest większa od dostępnej wagi w plecaku
            # to nie możemy go wziąć i wartość plecaka pozostaje taka jak dla poprzedniego przedmiotu
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # W przeciwnym razie możemy zdecydować czy wziąć ten przedmiot czy nie
                # i wybieramy maksimum z wartości dla poprzedniego przedmiotu i wartości
                # dla obecnego przedmiotu + wartość plecaka dla wagi zmniejszonej o wagę obecnego przedmiotu
                dp[i][w] = max(dp[i - 1][w], values[i - 1] +
                               dp[i - 1][w - weights[i - 1]])

    if printTable:
        # Wyświetlenie tablicy dynamicznej
        for row in dp:
            print("\t".join(map(str, row)))

    # Zwracamy wartość plecaka dla maksymalnej dostępnej wagi
    return dp[n][weight_limit]


def approx(weight_limit, weights, values):
    n = len(weights)

    # Obliczanie wartości/wagi dla każdego przedmiotu
    ratios = [(values[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True)  # Sortowanie malejąco według wartości/wagi

    total_value = 0
    total_weight = 0
    # selected_items = []

    # Wybieranie przedmiotów w kolejności malejącej wartości/wagi, dopóki nie przekroczymy limitu wagi
    for ratio, index in ratios:
        if total_weight + weights[index] <= weight_limit:
            total_value += values[index]
            total_weight += weights[index]
            # selected_items.append(index)

    # return total_value, selected_items
    return total_value, total_weight
