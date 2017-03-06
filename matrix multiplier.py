def dotProduct(vec_a, vec_b):
    # takes the dot product of two vectors
    try: 
        assert(len(vec_a) == len(vec_b))
        dimension = len(vec_a)
        soln = 0
        for a, b in zip(vec_a, vec_b):
            soln += a * b
        return soln
    except: 
        print("Dot Product failed. Check that vectors are of the same dimension.")


def getColumn(i, matrix):
    try:
        assert i < len(matrix[0])
        column = []
        for a in matrix:
            column.append(a[i])
        return column
    except:
        print("Column is out of range.")


def matrixMultiply(matrix1, matrix2):
    try: 
        assert(len(matrix1[0]) == len(matrix2))
        m = len(matrix1)
        p = len(matrix2[0])
        soln = []
        for i in range(m):
            row = []
            soln.append(row)
            for j in range(p):
                row.append(dotProduct(matrix1[i], getColumn(j, matrix2)))
        return soln
    except:
        print("Check dimensions of matrices. The number of columns in the first matrix must equal the number of rows in the second matrix.")
            

def getMatrix():
    print("This is an integer matrix multiplier.")
    n_raw = input("Enter the number of rows in your first matrix: ")
    m_raw = input("Enter the number of columns in your first matrix and the number of rows in your second matrix. They must be the same. ")
    p_raw = input("Enter the number of columns in your second matrix: ")
    try: 
        n = int(n_raw)
        m = int(m_raw)
        p = int(p_raw)
    except: 
        print("n, m, and p must be integers.")
        
    print("Enter your matrices.")
    matrix1 = []
    matrix2 = []
    print("Enter matrix 1 (",n, "x", m,"): ")
    for y in range(n):
        row = []
        matrix1.append(row)
        for x in range(m):
            print("Enter the number in row ",y, " column ", x,": ")
            raw = input()
            try:
                num_input = int(raw)
                row.append(num_input)
            except:
                print("All entries must be integers. Try again.")
                getMatrix()
    print("Matrix 1 complete! Enter matrix 2.")
    for y in range(m):
        row = []
        matrix2.append(row)
        for x in range(p):
            raw = input()
            try:
                print("Enter the number in row ",y, " column ", x,": ")
                num_input = int(raw)
                row.append(num_input)
            except:
                print("All entries must be integers. Try again.")
                getMatrix()    
    print("Matrix 2 complete!")
    print("The result is: ")
    print(matrixMultiply(matrix1, matrix2))
    
getMatrix()

    
    
    

        
    
    