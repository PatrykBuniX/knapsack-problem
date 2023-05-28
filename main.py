import knapsack
import plotter
from random import randint
from time import perf_counter


weights = [3, 2, 4, 3, 1]
values = [5, 3, 4, 4, 2]
weight_limit = 8

max_value = knapsack.dynamic(weight_limit, weights, values)
max_value2 = knapsack.approx(weight_limit, weights, values)
print("Maksymalna wartość plecaka:", max_value, max_value2)


# A weight-limit - const, n - increasing


def measure_with_const_weight_limit(weight_limit):
    print("A weight-limit - const, n - increasing")
    dynamicTimes = []
    approxTimes = []
    relativeErrors = []

    listSizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
                 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
    for size in listSizes:
        dynamicTimesScores = []
        approxTimesScores = []
        relativeErrorsScores = []

        for i in range(20):
            print(f"n = {size}")
            weights = [randint(1, 1000) for _ in range(size)]
            values = [randint(1, 1000) for _ in range(size)]

            print(
                f"Liczba elementów: {len(weights)}, waga plecaka: {weight_limit}", )
            dstart = perf_counter()
            max_value_dynamic = knapsack.dynamic(weight_limit, weights, values)
            print("Dynamiczne: wartość plecaka:", max_value_dynamic)
            dstop = perf_counter()
            dynamicAlgoTime = dstop - dstart
            print('dynamic time: ', dynamicAlgoTime)
            dynamicTimesScores.append(dynamicAlgoTime)

            astart = perf_counter()
            max_value_approx, final_approx_weight = knapsack.approx(
                weight_limit, weights, values)
            print("Zachłanne: wartość plecaka:", max_value_approx)
            print("Zachłanne: wage plecaka:", final_approx_weight)
            astop = perf_counter()
            approxAlgoTime = astop - astart
            print('approx time: ', approxAlgoTime)
            approxTimesScores.append(approxAlgoTime)

            relativeError = abs(max_value_dynamic -
                                max_value_approx) / max_value_dynamic
            relativeErrorsScores.append(relativeError)
            print("Błąd względny:", relativeError)

        dynamicTimes.append(sum(dynamicTimesScores) / len(dynamicTimesScores))
        approxTimes.append(sum(approxTimesScores) / len(approxTimesScores))
        relativeErrors.append(sum(relativeErrorsScores) /
                              len(relativeErrorsScores))

    plotter.create_chart([
        {"xdata": listSizes, "ydata": dynamicTimes,
            "color": "red", "label": "dynamic"},
        {"xdata": listSizes, "ydata": approxTimes,
            "color": "green", "label": "approx"}
    ], "Stała pojemność plecaka - czas", "Liczba elementów", "Czas [s]", "linear")

    relativeErrorsData = {}
    for i in range(len(listSizes)):
        size = listSizes[i]
        relativeErrorsData[size] = relativeErrors[i]

    plotter.create_bar_chart(
        relativeErrorsData, "Stała pojemność plecaka - błąd względny", "Liczba elementów", "Błąd względny")


measure_with_const_weight_limit(750)

# B weight-limit - increasing, n - const
