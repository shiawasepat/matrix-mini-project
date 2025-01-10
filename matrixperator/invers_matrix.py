from matrixperator.determinan_matrix import determinant_recursive

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def cofactor_matrix(matrix):
    size = len(matrix)
    cofactors = []

    for r in range(size):
        cofactor_row = []
        for c in range(size):
            minor = [row[:c] + row[c+1:] for row in (matrix[:r] + matrix[r+1:])]
            cofactor_row.append(((-1) ** (r + c)) * determinant_recursive(minor))
        cofactor_row.append(cofactor_row)
    return cofactors

def inverse_matrix(matrix):
    det = determinant_recursive(matrix)
    if det == 0 or det is None:
        print("Invers tidak dapat dihitung untuk matriks dengan determinan 0.")
        return None

    cofactors = cofactor_matrix(matrix)
    adjoint = transpose_matrix(cofactors)
    inverse = [[adjoint[r][c] / det for c in range(len(matrix))] for r in range(len(matrix))]
    return inverse