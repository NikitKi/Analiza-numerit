import sympy as sp

def linear_interpolation(x_points, y_points, x):
    for i in range(len(x_points) - 1):
        if x_points[i] <= x <= x_points[i + 1]:
            print(f"Iteration {i + 1}: Interval [{x_points[i]}, {x_points[i + 1]}]")
            return y_points[i] + (y_points[i + 1] - y_points[i]) * (x - x_points[i]) / (x_points[i + 1] - x_points[i])
    return None

def polynomial_interpolation(x_points, y_points, x):
    x_sym = sp.symbols('x')
    poly = sp.interpolate(list(zip(x_points, y_points)), x_sym)
    return poly.subs(x_sym, x)

def main():
    x_points = [1, 2, 3, 4]
    y_points = [2, 3, 5, 4]
    x = 2.5

    print("Linear Interpolation:")
    lin_result = linear_interpolation(x_points, y_points, x)
    print(f"Linear Interpolation result: {lin_result}\n")

    poly_result = polynomial_interpolation(x_points, y_points, x)
    print(f"Polynomial Interpolation result: {poly_result}")

if __name__ == "__main__":
    main()
