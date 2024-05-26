# Modul kelas_ujian.py

def rata_rata(nilai_siswa):
    return sum(nilai_siswa) / len(nilai_siswa)

def nilai_tertinggi(nilai_siswa):
    return max(nilai_siswa)

def nilai_terendah(nilai_siswa):
    return min(nilai_siswa)

def diatas_rata(nilai_siswa):
    rata = rata_rata(nilai_siswa)
    return sum(1 for nilai in nilai_siswa if nilai > rata)

def urutkan_nilai(nilai_siswa):
    return sorted(nilai_siswa)

def nilai_peringkat_ketiga_tertinggi(nilai_siswa):
    sorted_nilai = urutkan_nilai(nilai_siswa)
    return sorted_nilai[-3:]

if __name__ == "__main__":
    nilai_siswa = [75, 80, 90, 65, 85, 95, 70, 88, 92, 78]

    print("Rata-rata nilai kelas:", rata_rata(nilai_siswa))
    print("Nilai ujian tertinggi:", nilai_tertinggi(nilai_siswa))
    print("Nilai ujian terendah:", nilai_terendah(nilai_siswa))
    print("Jumlah siswa yang mendapatkan nilai di atas rata-rata:", diatas_rata(nilai_siswa))
    print("Urutan nilai ujian dari terendah ke tertinggi:", urutkan_nilai(nilai_siswa))
    print("Nilai ujian peringkat ketiga tertinggi:", nilai_peringkat_ketiga_tertinggi(nilai_siswa))
