import os
import time

from matrixperator.jumlah_matrix import add_matrix
from matrixperator.kurang_matrix import subtract_matrix
from matrixperator.kali_matrix import multiply_matrix
from matrixperator.determinan_matrix import determinant_recursive
from matrixperator.invers_matrix import inverse_matrix
from matrixperator.elemen_matrix import create_matrix, display_matrix

def clear_console():
    """Clears the console screen."""
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')
clear_console()

if __name__ == "__main__":
    try:
        print("Pilih operasi yang ingin dilakukan:")
        print("1. Penjumlahan Matriks")
        print("2. Pengurangan Matriks")
        print("3. Perkalian Matriks")
        print("4. Determinan Matriks")
        print("5. Invers Matriks")
        print("6. Keluar")
        choice = int(input("Masukkan pilihan (1-6): "))
        time.sleep(1)
        clear_console()

        if choice in [1, 2, 3]:
            rows1 = int(input("Masukkan jumlah baris matriks pertama: "))
            cols1 = int(input("Masukkan jumlah kolom matriks pertama: "))
            print("Matriks pertama:")
            matrix1 = create_matrix(rows1, cols1)

            time.sleep(0.5)
            clear_console()

            rows2 = int(input("Masukkan jumlah baris matriks kedua: "))
            cols2 = int(input("Masukkan jumlah kolom matriks kedua: "))
            print("Matriks kedua:")
            matrix2 = create_matrix(rows2, cols2)

            time.sleep(0.5)
            clear_console()

            if choice == 1:
                if rows1 == rows2 and cols1 == cols2:
                    time.sleep(1)
                    clear_console()
                    print("Hasil Penjumlahan Matriks:")
                    display_matrix(jumlah(matrix1, matrix2))
                else:
                    time.sleep(1)
                    clear_console()
                    print("Matriks harus memiliki ukuran yang sama untuk dijumlahkan.")

            elif choice == 2:
                if rows1 == rows2 and cols1 == cols2:
                    time.sleep(1)
                    clear_console()
                    print("Hasil Pengurangan Matriks:")
                    display_matrix(kurang(matrix1, matrix2))
                else:
                    time.sleep(1)
                    clear_console()
                    print("Matriks harus memiliki ukuran yang sama untuk dikurangkan.")

            elif choice == 3:
                result = kali(matrix1, matrix2)
                if result:
                    time.sleep(1)
                    clear_console()
                    print("Hasil Perkalian Matriks:")
                    display_matrix(result)

        elif choice == 4:
            rows = int(input("Masukkan ukuran matriks persegi (baris = kolom): "))
            matrix = create_matrix(rows, rows)
            det = determinant_recursive(matrix)
            time.sleep(1)
            clear_console()
            print(f"Determinan Matriks: {det:.2f}")

        elif choice == 5:
            rows = int(input("Masukkan ukuran matriks persegi (baris = kolom): "))
            matrix = create_matrix(rows, rows)
            inv = inverse_matrix(matrix)
            if inv:
                time.sleep(1)
                clear_console()
                print("Invers Matriks:")
                display_matrix(inv)

        elif choice == 6:
            time.sleep(1)
            clear_console()
            print("Terima kasih telah menggunakan program ini.")

        else:
            time.sleep(1)
            clear_console()
            print("Pilihan tidak valid.")

    except ValueError:
        time.sleep(1)
        clear_console()
        print("Input harus berupa angka.")