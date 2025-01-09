def create_matrix(rows, cols):
    matrix = []
    print("Masukkan elemen matriks satu per satu:")
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    value = float(input(f"Masukkan elemen [{i+1}, {j+1}]: "))
                    row.append(value)
                    break
                except ValueError:
                    print("Input harus berupa angka. Coba lagi.")
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print("\t".join(map(lambda x: f"{x:.2f}", row)))