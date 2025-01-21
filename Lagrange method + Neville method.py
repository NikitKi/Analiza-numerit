def lagrange_interpolation(x_list, y_list, x):
    n = len(x_list)

    if x in x_list:
        return y_list[x_list.index(x)]

    if x < min(x_list) or x > max(x_list):
        print("The value is outside the interpolation range.")
        return None

    result = 0.0
    for i in range(n):
        term = y_list[i]
        for j in range(n):
            if j != i:
                term *= (x - x_list[j]) / (x_list[i] - x_list[j])
        result += term

    return result


def neville_interpolation(x_list, y_list, x):
    n = len(x_list)

    if x in x_list:
        return y_list[x_list.index(x)]


    if x < min(x_list) or x > max(x_list):
        print("The value is outside the interpolation range.")
        return None


    memo = {}


    for i in range(n):
        memo[(i, i)] = y_list[i]


    for offset in range(1, n):
        for i in range(n - offset):
            j = i + offset
            xi, xj = x_list[i], x_list[j]
            memo[(i, j)] = ((x - xi) * memo[(i + 1, j)] + (xj - x) * memo[(i, j - 1)]) / (xj - xi)
            print(f"p({i},{j}) = {memo[(i, j)]}")

    final_result = memo[(0, n - 1)]
    print(f"The final result p(0, {n - 1}) = {final_result}")
    return final_result

x_points = [1, 1.3, 1.6, 1.9, 2.2]
y_points = [0.7651, 0.6200, 0.4554, 0.2818, 0.1103]
x_to_find = 1.5

lagrange_result = lagrange_interpolation(x_points, y_points, x_to_find)
if lagrange_result is not None:
    print(f"The interpolated value at x = {x_to_find} using Lagrange method is {lagrange_result}")

neville_result = neville_interpolation(x_points, y_points, x_to_find)
if neville_result is not None:
    print(f"The interpolated value at x = {x_to_find} using Neville method is {neville_result}")

