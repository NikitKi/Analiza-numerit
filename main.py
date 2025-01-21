def is_dominant_diagonally(A):
    sum_of_row = 0
    num_of_rows_and_cols = len(A)
    for i in range(num_of_rows_and_cols):
        for j in range(num_of_rows_and_cols):
            if j != i:
                sum_of_row += abs(A[i][j])
        if sum_of_row >= A[i][i]:
            return False
        sum_of_row = 0
    return True

def make_diagonal_dominant(A):
    num_of_cols_and_rows = len(A)
    L = [[0] * num_of_cols_and_rows for _ in range(num_of_cols_and_rows)]
    U = [[0] * num_of_cols_and_rows for _ in range(num_of_cols_and_rows)]
    D = [[0] * num_of_cols_and_rows for _ in range(num_of_cols_and_rows)]

    for i in range(num_of_cols_and_rows):
        for j in range(num_of_cols_and_rows):
            if i > j:
                L[i][j] = A[i][j]
            elif i < j:
                U[i][j] = A[i][j]
            else:
                D[i][j] = A[i][j]

    return L, U, D


def gauss_seidel_method(L, U, D, Y, X, epsilon=0.00001, max_iterations=1000):
    num_of_cols_and_rows = len(D)
    for iteration in range(max_iterations):
        X_new = X.copy()
        for j in range(num_of_cols_and_rows):
            summ_val = Y[j] - sum(L[j][k] * X_new[k] for k in range(j)) - sum(U[j][k] * X[k] for k in range(j + 1, num_of_cols_and_rows))
            X_new[j] = summ_val / D[j][j]

        max_diff = max(abs(X_new[i] - X[i]) for i in range(len(X)))
        X = X_new

        print(f"Iteration {iteration + 1}: {X}")

        if max_diff < epsilon:
            print(f"Converged after {iteration + 1} iterations.")
            return X

    print("Did not converge within the maximum number of iterations")
    return X


def jacobi_method(L, U, D, Y, X, epsilon=0.00001, max_iterations=1000):
    num_of_cols_and_rows = len(D)
    for iteration in range(max_iterations):
        X_new = X.copy()
        for j in range(num_of_cols_and_rows):
            summ_val = Y[j] - sum(L[j][k] * X[k] for k in range(num_of_cols_and_rows)) - sum(U[j][k] * X[k] for k in range(num_of_cols_and_rows))
            X_new[j] = summ_val / D[j][j]

        max_diff = max(abs(X_new[i] - X[i]) for i in range(len(X)))
        X = X_new

        print(f"Iteration {iteration + 1}: {X}")

        if max_diff < epsilon:
            print(f"Converged after {iteration + 1} iterations.")
            return X

    print("did not converge within the maximum number of iterations")
    return X


def is_diagonally_dominant(matrix_A):
    if is_dominant_diagonally(matrix_A):
        return matrix_A
    else:
        for i in range(len(matrix_A)):
            for j in range(i + 1, len(matrix_A)):
                matrix_A[i], matrix_A[j] = matrix_A[j], matrix_A[i]
                if is_dominant_diagonally(matrix_A):
                    return matrix_A
                matrix_A[i], matrix_A[j] = matrix_A[j], matrix_A[i]
    return None



matrix_A = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
vector_B = [2, 6, 5]
initial_guess = [0, 0, 0]

L, U, D = make_diagonal_dominant(matrix_A)

dominant_matrix = is_diagonally_dominant(matrix_A)

if dominant_matrix:
    print("Matrix is diagonally dominant")
else:
    print("Matrix is not diagonally dominant. Running limited iterations.")


method_choice = input("Enter 1 for Gauss-Seidel method or 2 for Jacobi method: ")


if method_choice == '1':
    print("Using Gauss-Seidel Method:")
    print("Xr+1, Yr+1, Zr+1")
    gauss_seidel_method(L, U, D, vector_B, initial_guess)
elif method_choice == '2':
    print("Using Jacobi Method:")
    print("Xr+1, Yr+1, Zr+1")
    jacobi_method(L, U, D, vector_B, initial_guess)
else:
    print("Invalid choice. Please choose either 'Gauss-Seidel' or 'Jacobi'.")

