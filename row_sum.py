def row_matrix_sum(given_matrix, number_of_rows, number_of_columns):
    row_sum = []
    for row in range(number_of_rows):
        r_sum = 0
        for column in range(number_of_columns):
            r_sum += given_matrix[row][column]
        row_sum.append(r_sum)
    return row_sum


try:
    rows = int(input("Enter number of rows : "))
    columns = int(input("Enter number of columns : "))
    matrix = [[int(input("Enter an integer to insert into the matrix : ")) for column in range(columns)] for row in
              range(rows)]
    print("The row-wise sum of given matrix is : ", row_matrix_sum(matrix, rows, columns))
except ValueError:
    print("Invalid Input. Please enter only integers")
