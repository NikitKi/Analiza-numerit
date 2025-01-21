#idan veprisnki 323061770 nikita kimelblat 212363576

import sympy as sp

def find_sign_changes(polynomial, derivative, start_point, end_point, step=0.1):
    """Find intervals where f(x1) * f(x2) < 0 or potential roots in [start_point, end_point]."""
    intervals = []
    x = sp.Symbol('x')
    f = sp.lambdify(x, polynomial)
    f_prime = sp.lambdify(x, derivative)

    current = start_point
    while current < end_point:
        next_point = current + step
        if f(current) * f(next_point) < 0 or (f(current) == 0 and f_prime(current) * f_prime(next_point) <= 0):
            intervals.append((current, next_point))
        current = next_point
    return intervals


def Bisection_Method(polynomial, start_point, end_point, epsilon=0.0001):
    """Find a root using the Bisection Method."""
    x = sp.Symbol('x')
    f = sp.lambdify(x, polynomial)

    if f(start_point) * f(end_point) >= 0:
        print(f"Error: No sign change in interval [{start_point}, {end_point}].")
        return None, 0

    iterations = 0
    while (end_point - start_point) / 2 > epsilon:
        iterations += 1
        midpoint = (start_point + end_point) / 2
        midpoint_value = f(midpoint)

        print(f"Bisection Iteration {iterations}: midpoint = {midpoint}, f(midpoint) = {midpoint_value}")

        if abs(midpoint_value) < epsilon:
            return midpoint, iterations

        if f(start_point) * midpoint_value < 0:
            end_point = midpoint
        else:
            start_point = midpoint

    root = (start_point + end_point) / 2
    return root, iterations


def Newton_Raphson(polynomial, derivative, start_point, epsilon=0.0001, max_iterations=100):
    """Find a root using the Newton-Raphson Method."""
    x = sp.Symbol('x')
    f = sp.lambdify(x, polynomial)
    f_prime = sp.lambdify(x, derivative)

    current_point = start_point
    iterations = 0

    while iterations < max_iterations:
        iterations += 1
        value = f(current_point)
        derivative_value = f_prime(current_point)

        if abs(derivative_value) < epsilon:
            print("Error: Derivative is too small. Method may not converge.")
            return None, iterations

        next_point = current_point - value / derivative_value

        print(f"Newton-Raphson Iteration {iterations}: x = {current_point}, f(x) = {value}")

        if abs(next_point - current_point) < epsilon:
            return next_point, iterations

        current_point = next_point

    print("Error: Method did not converge within the maximum number of iterations.")
    return None, iterations


def Secant_Method(polynomial, start_point, end_point, epsilon=0.0001, max_iterations=100):
    """Find a root using the Secant Method."""
    x = sp.Symbol('x')
    f = sp.lambdify(x, polynomial)

    x0 = start_point
    x1 = end_point
    iterations = 0

    while iterations < max_iterations:
        iterations += 1
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < epsilon:
            print("Error: Division by zero or insufficient difference in function values.")
            return None, iterations

        # Calculate the next approximation
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        print(f"Secant Iteration {iterations}: x0 = {x0}, x1 = {x1}, x2 = {x2}, f(x2) = {f(x2)}")

        if abs(x2 - x1) < epsilon:
            return x2, iterations

        # Update points for next iteration
        x0, x1 = x1, x2

    print("Error: Method did not converge within the maximum number of iterations.")
    return None, iterations


if __name__ == "__main__":
    # Define the polynomial and its derivative
    x = sp.Symbol('x')
    polynomial = x**3 - x - 2
    derivative = sp.diff(polynomial, x)

    # Define interval to search for roots
    start = 0.0
    end = 3.0

    # Find intervals with sign changes
    sign_change_intervals = find_sign_changes(polynomial, derivative, start, end, step=0.1)

    # Desired accuracy
    epsilon = 0.0001

    # Apply all methods on each interval
    for interval in sign_change_intervals:
        x1, x2 = interval
        print(f"\nSearching in interval [{x1}, {x2}]:")

        # Bisection Method
        root_bisection, bisection_iterations = Bisection_Method(polynomial, x1, x2, epsilon)
        if root_bisection is not None:
            print(f"Bisection Method: Root = {root_bisection}, Iterations = {bisection_iterations}")

        # Newton-Raphson Method
        midpoint = (x1 + x2) / 2
        root_newton, newton_iterations = Newton_Raphson(polynomial, derivative, midpoint, epsilon)
        if root_newton is not None:
            print(f"Newton-Raphson Method: Root = {root_newton}, Iterations = {newton_iterations}")

        # Secant Method
        root_secant, secant_iterations = Secant_Method(polynomial, x1, x2, epsilon)
        if root_secant is not None:
            print(f"Secant Method: Root = {root_secant}, Iterations = {secant_iterations}")
