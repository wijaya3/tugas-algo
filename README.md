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
    Masukkan nilai ujian siswa ke-3: 95
Masukkan nilai ujian siswa ke-4: 95
Masukkan nilai ujian siswa ke-5: 90
Masukkan nilai ujian siswa ke-6: 90
Masukkan nilai ujian siswa ke-7: 92
Rata-rata nilai ujian kelas: 94.28571428571429
Nilai ujian tertinggi: 100.0
Nilai ujian terendah: 90.0
Jumlah siswa dengan nilai di atas rata-rata: 4
Nilai ujian setelah diurutkan: [90.0, 90.0, 92.0, 95.0, 95.0, 98.0, 100.0]
Nilai ujian peringkat ketiga tertinggi: 95.0
