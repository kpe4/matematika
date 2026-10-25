# -*- coding: utf-8 -*-

# функции

def read_float(prompt):
    """Читает одно вещественное число с повторным запросом при ошибке."""
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print("  [ошибка] Введите число (например, 3.5 или -2).")


def read_int(prompt):
    """Читает одно целое число с повторным запросом при ошибке."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  [ошибка] Введите целое число.")


def read_vector(name, n):
    """Ввод вектора длины n (список float)."""
    print(f"Введите {n} компонент(ы) вектора {name}:")
    return [read_float(f"  {name}[{i}] = ") for i in range(n)]


def read_matrix(name, rows, cols):
    """Ввод матрицы rows x cols (список списков float)."""
    print(f"Введите элементы матрицы {name} ({rows}x{cols}) по строкам:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(read_float(f"  {name}[{i}][{j}] = "))
        matrix.append(row)
    return matrix


# ЛИНЕЙНАЯ АЛГЕБРА (вручную, без NumPy)

def vec_add(a, b):
    """Сложение векторов одинаковой длины."""
    return [a[i] + b[i] for i in range(len(a))]


def vec_scale(a, k):
    """Умножение вектора на скаляр"""
    return [x * k for x in a]


def vec_norm(a):
    """Евклидова длина вектора."""
    return sum(x * x for x in a) ** 0.5


def mat_vec_mul(matrix, vector):
    """
    Умножение матрицы (M x N) на вектор-столбец (N).
    Результат — вектор длины M
    """
    m = len(matrix)
    n = len(matrix[0])
    if len(vector) != n:
        raise ValueError(f"Несовпадение размеров: матрица {m}x{n}, вектор {len(vector)}")
    result = []
    for i in range(m):
        s = 0.0
        for j in range(n):
            s += matrix[i][j] * vector[j]
        result.append(s)
    return result


def mat_mat_mul(a, b):
    """
    Умножение матриц A (m x n) на B (n x p).
    Результат — матрица m x p. Циклическая реализация
    """
    m = len(a)
    n = len(a[0])
    n2 = len(b)
    p = len(b[0])
    if n != n2:
        raise ValueError(f"Несовпадение размеров: A {m}x{n}, B {n2}x{p}")
    result = [[0.0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            s = 0.0
            for k in range(n):
                s += a[i][k] * b[k][j]
            result[i][j] = s
    return result


def mat_add(a, b):
    """Поэлементное сложение матриц одинакового размера."""
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_to_col(matrix):
    """Преобразует матрицу m x 1 в вектор-столбец (список)."""
    return [matrix[i][0] for i in range(len(matrix))]


def col_to_mat(vector):
    """Преобразует вектор в матрицу-столбец."""
    return [[x] for x in vector]


def mat_print(name, matrix):
    """Красивый вывод матрицы."""
    print(f"{name} =")
    for row in matrix:
        print("  [" + ", ".join(f"{x:8.3f}" for x in row) + "]")


def vec_print(name, vector):
    """Красивый вывод вектора."""
    print(f"{name} = [" + ", ".join(f"{x:8.3f}" for x in vector) + "]")


def approx_equal(a, b, eps=1e-9):
    """Сравнение двух вещественных чисел с допуском."""
    return abs(a - b) < eps


def vec_approx_equal(a, b, eps=1e-9):
    return len(a) == len(b) and all(approx_equal(a[i], b[i], eps) for i in range(len(a)))


# Динамическая телепортация персонажа

def task1():
    print("\n" + "=" * 60)
    print("ЗАДАЧА 1. Динамическая телепортация персонажа")
    print("=" * 60)

    # Ввод координат точки A (2D)
    print("Введите координаты начальной точки A:")
    A = [read_float("  xA = "), read_float("  yA = ")]

    # Ввод векторов u и v
    u = read_vector("u", 2)
    v = read_vector("v", 2)

    # Результирующий вектор перемещения r = u + v
    r = vec_add(u, v)

    # Итоговая позиция B = A + r
    B = vec_add(A, r)

    # Длина пути: |u| + |v| (два последовательных телепорта)
    path_len = vec_norm(u) + vec_norm(v)

    # Вывод
    vec_print("u", u)
    vec_print("v", v)
    vec_print("r = u + v", r)
    vec_print("A", A)
    vec_print("B = A + r", B)
    print(f"Длина пути (|u| + |v|) = {path_len:.6f}")

    # Дополнительная проверка: A + u + v == B
    check = vec_add(vec_add(A, u), v)
    if vec_approx_equal(check, B):
        print("Проверка A + u + v == B: OK")
    else:
        print("Проверка A + u + v == B: ОШИБКА")


# ЗАДАЧА 2. Произвольный поворот и масштабирование

def task2():
    print("\n" + "=" * 60)
    print("ЗАДАЧА 2. Произвольный поворот и масштабирование в 2D")
    print("=" * 60)

    # Вектор-столбец x = (x1, x2)
    x = read_vector("x", 2)

    # Матрица поворота R (2x2)
    print("Введите матрицу поворота R (2x2):")
    R = read_matrix("R", 2, 2)

    # Матрица масштабирования S (2x2)
    print("Введите матрицу масштабирования S (2x2):")
    S = read_matrix("S", 2, 2)

    # Промежуточные координаты x1 = R x
    x1 = mat_vec_mul(R, x)

    # Итоговые координаты x2 = S x1
    x2 = mat_vec_mul(S, x1)

    # Матрица общего преобразования T = S * R
    T = mat_mat_mul(S, R)

    # Проверка T x == x2
    Tx = mat_vec_mul(T, x)

    # Вывод
    mat_print("R", R)
    mat_print("S", S)
    vec_print("x", x)
    vec_print("x1 = R x", x1)
    vec_print("x2 = S x1", x2)
    mat_print("T = S R", T)
    vec_print("T x", Tx)

    if vec_approx_equal(Tx, x2):
        print("Проверка T x == x2: OK")
    else:
        print("Проверка T x == x2: НЕ СОВПАДАЕТ (проверьте ввод)")


# Параметризуемый нейронный слой

def dense_layer(x, W, b):
    """
    Полносвязный слой: z = W x + b.
    x — вектор длины N
    W — матрица M x N
    b — вектор длины M
    Возвращает вектор длины M.
    """
    if not x:
        raise ValueError("Вектор x пуст")
    if not W or not W[0]:
        raise ValueError("Матрица W пуста")
    if not b:
        raise ValueError("Вектор b пуст")

    M = len(W)
    N = len(W[0])
    if len(x) != N:
        raise ValueError(f"x имеет длину {len(x)}, ожидается N={N}")
    if len(b) != M:
        raise ValueError(f"b имеет длину {len(b)}, ожидается M={M}")
    for i, row in enumerate(W):
        if len(row) != N:
            raise ValueError(f"Строка {i} матрицы W имеет длину {len(row)}, ожидается {N}")

    # W x
    Wx = mat_vec_mul(W, x)
    # + b
    return vec_add(Wx, b)


def task3():
    print("\n" + "=" * 60)
    print("ЗАДАЧА 3. Параметризуемый полносвязный слой")
    print("=" * 60)

    # Ввод размерностей
    while True:
        N = read_int("Введите размерность входа N (>0): ")
        if N > 0:
            break
        print("  [ошибка] N должно быть положительным.")

    while True:
        M = read_int("Введите размерность выхода M (>0): ")
        if M > 0:
            break
        print("  [ошибка] M должно быть положительным.")

    # Ввод данных
    x = read_vector("x", N)
    W = read_matrix("W", M, N)
    b = read_vector("b", M)

    # Вычисление
    try:
        z = dense_layer(x, W, b)
    except ValueError as e:
        print(f"[ошибка] {e}")
        return

    # Вывод
    mat_print("W", W)
    vec_print("x", x)
    vec_print("b", b)
    vec_print("z = W x + b", z)


# ТОЧКА ВХОДА

def main():
    while True:
        print("\n" + "#" * 60)
        print("Выберите задачу:")
        print("  1 — Динамическая телепортация персонажа")
        print("  2 — Поворот и масштабирование в 2D")
        print("  3 — Параметризуемый нейронный слой")
        print("  0 — Выход")
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("  [ошибка] Неизвестный пункт меню.")


if __name__ == "__main__":
    main()
