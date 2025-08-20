import numpy as np
import sys

def get_matrix_from_user(matrix_name=""):
    """
    Prompts the user to enter the dimensions and elements of a matrix.
    Includes error handling for invalid input.
    
    Args:
        matrix_name (str): The name of the matrix to display in the prompt (e.g., "Matrix A").
        
    Returns:
        numpy.ndarray: The matrix created from user input, or None if input is invalid.
    """
    while True:
        try:
            # Get matrix dimensions from the user
            if matrix_name:
                print(f"\n--- Enter details for {matrix_name} ---")
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            if rows <= 0 or cols <= 0:
                print("Error: Dimensions must be positive integers. Please try again.")
                continue

            print(f"Enter the {rows * cols} elements for the {rows}x{cols} matrix, separated by spaces:")
            elements_str = input().strip().split()
            
            # Validate the number of elements entered
            if len(elements_str) != rows * cols:
                print(f"Error: You must enter exactly {rows * cols} elements. You entered {len(elements_str)}.")
                continue
            
            # Convert elements to numbers and create the matrix
            elements = [float(e) for e in elements_str]
            matrix = np.array(elements).reshape(rows, cols)
            print("Matrix created successfully:")
            print(matrix)
            return matrix

        except ValueError:
            print("Invalid input. Please enter only numbers for dimensions and elements. Try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

def print_result(operation_name, result_matrix, matrix_a=None, matrix_b=None, operation_symbol=""):
    """
    Prints the result of a matrix operation in a structured format.
    """
    print("\n" + "="*15 + " Result " + "="*15)
    print(f"Operation: {operation_name}")
    
    if matrix_a is not None:
        print("\nMatrix A:")
        print(matrix_a)
    if matrix_b is not None:
        print("\nMatrix B:")
        print(matrix_b)
    
    print(f"\nResult:")
    print(result_matrix)
    print("="*38 + "\n")

def main_menu():
    """
    Displays the main menu and handles user interaction.
    """
    while True:
        print("\n===== Matrix Operations Tool =====")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices (Dot Product)")
        print("4. Transpose Matrix")
        print("5. Calculate Determinant")
        print("6. Exit")
        print("==================================")
        
        choice = input("Select an option (1-6): ")

        if choice == '1': # Addition
            print("\n** Matrix Addition (A + B) **")
            a = get_matrix_from_user("Matrix A")
            b = get_matrix_from_user("Matrix B")
            if a.shape != b.shape:
                print("\nError: Matrices must have the same dimensions for addition.")
            else:
                result = a + b
                print_result("Addition", result, a, b)

        elif choice == '2': # Subtraction
            print("\n** Matrix Subtraction (A - B) **")
            a = get_matrix_from_user("Matrix A")
            b = get_matrix_from_user("Matrix B")
            if a.shape != b.shape:
                print("\nError: Matrices must have the same dimensions for subtraction.")
            else:
                result = a - b
                print_result("Subtraction", result, a, b)

        elif choice == '3': # Multiplication
            print("\n** Matrix Multiplication (A . B) **")
            a = get_matrix_from_user("Matrix A")
            b = get_matrix_from_user("Matrix B")
            # Check if columns of A match rows of B
            if a.shape[1] != b.shape[0]:
                print("\nError: The number of columns in Matrix A must equal the number of rows in Matrix B.")
            else:
                result = np.dot(a, b)
                print_result("Multiplication (Dot Product)", result, a, b)

        elif choice == '4': # Transpose
            print("\n** Matrix Transpose **")
            a = get_matrix_from_user("Matrix")
            result = a.T
            print_result("Transpose", result, a)

        elif choice == '5': # Determinant
            print("\n** Calculate Determinant **")
            a = get_matrix_from_user("Matrix")
            # Check if the matrix is square
            if a.shape[0] != a.shape[1]:
                print("\nError: Determinant can only be calculated for a square matrix.")
            else:
                try:
                    result = np.linalg.det(a)
                    print_result("Determinant", f"{result:.4f}", a)
                except np.linalg.LinAlgError as e:
                    print(f"\nError calculating determinant: {e}")

        elif choice == '6': # Exit
            print("Exiting the Matrix Operations Tool. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

        # Ask user if they want to continue
        another_op = input("Do you want to perform another operation? (yes/no): ").lower()
        if another_op != 'yes':
            print("Exiting the Matrix Operations Tool. Goodbye!")
            break

if __name__ == "__main__":
    main_menu()