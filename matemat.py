import math

def combinations(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

def probablity_all_from_first(n, m, k, r):
    total = n + m
    if k > total:
        return None
    if r > n or r > k:
        return 0.0
    favorable = combinations(n, r) * combinations(m, k - r)
    all_outcomes = combinations(total, k)
    return favorable / all_outcomes

def get_int(prompt, min_value=0, allow_zero=True):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"значение должно быть >= {min_value}")
                continue
            if not allow_zero and value == 0:
                print("значение должно быть  > 0.")
                continue
            return value
        except ValueError:
            print("ведите целое число")

def main():
    print("=" * 60)
    print("калькулятор вероятности")
    print("=" * 60)
    print()
    print("задача:")
    print(" в ящике n элементов 1-й группы и m элементов второй группы")
    print(" случайно выбирается k элементов.")
    print(" найти вероятность ттого что все r выбранных элементов - из первой группы")
    print()
    print("введите параметр вашей задачи:")
    print("-" * 60)

    n = get_int(" n - элементов первой группы: ", min_value = 1, allow_zero = False)
    m = get_int(" m - элементов второй группы: ", min_value=1, allow_zero=False)
    k = get_int(" k - сколько элементов выбираем ", min_value=1, allow_zero=False)
    r = get_int(" r - сколько из них должно быть из первой группы ", min_value=1, allow_zero=False)

    print("-" * 60)

    if k > n + m:
        print(f"ошибка нельзя выбрать {k} элементов из {n + m} имеющихся")
        return
    if r > k:
        print(f"ошибка r ({r}) не может быть больше k({k}) ")
        return
    if r > n:
        print(f"предупреждение в первой группе только {n} элементов, нельзя выбдрать {r}. вероятность = 0")
        return

    p = probablity_all_from_first(n, m, k, r)

    print()
    print("результат:")
    print(f"всего элементов: {n + m}")
    print(f"выбираем: {k}")
    print(f"нужно из первой группы {r}")
    print(f"P = C({n},{r}) * C({m},{k-r}) / C({n+m},{k})")
    print(f" P = {combinations(n,r)} * {combinations(m, k - r)} / {combinations(n + m, k)}")
    print(f" вероятность {p:.6f} ({p*100:.4f} %)")
    print("=" * 60)

if __name__ == "__main__":
    main()