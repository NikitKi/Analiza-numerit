import sympy as sp


def spline_cubic(xList, yList, x, fTag0, fTagN):
    n = len(xList) - 1
    h_list = [xList[i + 1] - xList[i] for i in range(n)]
    lamda_list = [h_list[i] / (h_list[i] + h_list[i + 1]) for i in range(n - 1)]
    miu_list = [1 - lamda_list[i] for i in range(n - 1)]
    d_list = [6 * ((yList[i + 2] - yList[i + 1]) / h_list[i + 1] - (yList[i + 1] - yList[i]) / h_list[i]) / (
                h_list[i] + h_list[i + 1]) for i in range(n - 1)]

    A = sp.zeros(n - 1)
    for i in range(n - 1):
        A[i, i] = 2
        if i > 0:
            A[i, i - 1] = lamda_list[i - 1]
            A[i - 1, i] = miu_list[i - 1]
    d = sp.Matrix(d_list)

    M = A.LUsolve(d)
    M = [0] + list(M) + [0]

    for i in range(n):
        if xList[i] <= x <= xList[i + 1]:
            break


    h = xList[i + 1] - xList[i]
    spline_result = ((M[i] * (xList[i + 1] - x) ** 3 + M[i + 1] * (x - xList[i]) ** 3) / (6 * h)
                     + (yList[i] - M[i] * h ** 2 / 6) * (xList[i + 1] - x) / h
                     + (yList[i + 1] - M[i + 1] * h ** 2 / 6) * (x - xList[i]) / h)

    return float(spline_result)


def main():
    xList = [1, 2, 3, 4, 5]
    yList = [2, 4, 6, 8, 10]
    x = 2.5
    fTag0 = 0
    fTagN = 0

    result = spline_cubic(xList, yList, x, fTag0, fTagN)
    print(f"Spline cubic result for x = {x}: {result}")


if __name__ == "__main__":
    main()
