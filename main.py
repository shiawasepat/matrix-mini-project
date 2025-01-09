from matrixperator.jumlah import jumlah
from matrixperator.kurang import kurang
from matrixperator.kali import kali
from matrixperator.determinan import determinan
from.matrixperator.elemen import elemen

import time
import os

os.system("cls")
def user_input():
    while True:
        print("Operasi pada vektor 2D")
        print("1. Penjumlahan Matriks")
        print("2. Pengurangan Matriks")
        print("3. Perkalian Matriks")
        print("4. Determinan Matriks")
        print("5. Invers Matriks")
        print("6. Keluar")
        pilihan = input("Masukkan nomor 1-6: ")
        os.system("cls")

        if pilihan in [1, 2, 3]:
            rows1 = int(input("Masukkan jumlah baris matriks pertama: "))
            cols1 = int(input("Masukkan jumlah kolom matriks pertama: "))
            print("Matriks pertama:")
            matrix1 = create_matrix(rows1, cols1)

            time.sleep(0.5)
            os.system('cls')

            rows2 = int(input("Masukkan jumlah baris matriks kedua: "))
            cols2 = int(input("Masukkan jumlah kolom matriks kedua: "))
            print("Matriks kedua:")
            matrix2 = create_matrix(rows2, cols2)