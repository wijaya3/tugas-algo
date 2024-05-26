import nilai_ujian

def main():
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    nilai_siswa = []
    for i in range(jumlah_siswa):
        nilai = float(input(f"Masukkan nilai ujian siswa ke-{i+1}: "))
        nilai_siswa.append(nilai)

    print("Rata-rata nilai ujian kelas tersebut:", nilai_ujian.hitung_rata_rata(nilai_siswa))
    print("Nilai ujian tertinggi dalam kelas:", nilai_ujian.nilai_tertinggi(nilai_siswa))
    print("Nilai ujian terendah dalam kelas:", nilai_ujian.nilai_terendah(nilai_siswa))
    print("Jumlah siswa yang mendapatkan nilai di atas rata-rata:", nilai_ujian.jumlah_siswa_diatas_rata_rata(nilai_siswa))
    print("Nilai ujian yang telah diurutkan:", nilai_ujian.urutkan_nilai(nilai_siswa))
    peringkat = int(input("Masukkan peringkat tertinggi yang ingin ditampilkan: "))
    print(f"Nilai ujian siswa pada peringkat {peringkat} tertinggi:", nilai_ujian.nilai_peringkat_tertinggi(nilai_siswa, peringkat))

if __name__ == "__main__":
    main()
