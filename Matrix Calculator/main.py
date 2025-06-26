import numpy as np

operation = input("Enter which operation you want to perform : ")
# Gets the matrix dimensions

if (operation == "addition") or (operation == "subtraction") or (operation == "multiplicaiton") : 

    rows = int(input("Enter the number of rows for the first matrix :"))
    cols = int(input("Enter the number of columns for the first matrix :"))

    # Input matrix A

    print("Enter the elements of matrix A:")
    A = []
    for i in range(rows):
        row = list(map(int,input(f"Enter row {i+1} values separated by space: ").split())) # If you use int(input()) instead of map(int, ...), you'd be taking only one integer input at a time. This means users wouldn't be able to enter multiple numbers separated by spaces, like "1 2 3", and have them automatically converted into a list of integers.

        A.append(row)
    A = np.array(A)

    rows = int(input("Enter the number of rows for the second matrix :"))
    cols = int(input("Enter the number of columns for the second matrix :"))
    # Input matrix B

    print("Enter the elements of matrix B:")
    B = []
    for i in range(rows):
        row = list(map(int,input(f"Enter row {i+1} values separated by space: ").split()))
        B.append(row)
    B = np.array(B)

elif (operation == "transpose") or (operation == "determinant") or (operation == "inverse"):
     rows = int(input("Enter the number of rows of the matrix: "))
     cols = int(input("Enter the number of columns of the matrix: "))
     matrix = []

     for i in range(rows):
            row = list(map(int, input(f"Enter the values of row {i+1} : ").split()))
            matrix.append(row)

     matrix = np.array[matrix]

shapeA = np.shape(A)
shapeB = np.shape(B)

# Check if shapes match
if operation == "addition":
    if A.shape == B.shape:

        # Perform matrix additon

        result = A + B

        print("Matrix A:")
        print(A)
        print("Matrix B:")
        print(B)
        print("Addition of A and B:")
        print(result)

    else:
        print("Matrices must have the same shape to be added")

elif operation == "subtraction":
    if A.shape == B.shape:
        result = A - B

        print("Matrix A:")
        print(A)
        print("Matrix B:")
        print(B)
        print("Subtraction of A and B:")
        print(result)

    else:
        print("Matrices must have the same shape to be added")

elif operation == "multiplicatiion":

    if shapeA[1] == shapeB[0]:
        result = np.matmul(A @ B)  # or A, B
        print("Matrix A:")
        print(A)
        print("Matrix B:")
        print(B)
        print("Multiplication of A and B:")
        print(result)

    else:
        print("Error: columns of Matrix A must be equal to rows of Matrix B for multiplication of the two matrices")       

elif operation == "transpose":
    print("Original Matrics")
    print(matrix)

    transpose = matrix.T
    print("Transpose of the matrix")
    print(transpose)

elif operation == "determinant":
    try:
        det = np.linalg.det(matrix)
        print(f"\nDeterminant: {det:.2f}")
    except np.linalg.LinAlgError:
        print("\nDeterminant: Not defined (matrix may be invalid)")

elif operation == "inverse":
    if matrix.shape[0] == matrix.shape[1]:
        if np.linalg.det(matrix) != 0:
            inverse = np.linalg.inv(matrix)
            inverse = np.linalg.inv(matrix)
            print("\nInverse of the Matrix:")
            print(inverse)
        else:
            print("\nInverse: Matrix is singular (det = 0), so inverse doesn't exist.")
    else:
        print("\nInverse: Not defined for non-square matrices.")

# you can also add more features to this as per your choice
