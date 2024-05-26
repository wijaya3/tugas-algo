# nilai_ujian.py

def input_nilai():
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    nilai = []
    for i in range(jumlah_siswa):
        nilai_siswa = float(input(f"Masukkan nilai ujian siswa ke-{i+1}: "))
        nilai.append(nilai_siswa)
    return nilai

def hitung_rata_rata(nilai):
    rata_rata = sum(nilai) / len(nilai)
    return rata_rata

def nilai_tertinggi_terendah(nilai):
    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)
    return nilai_tertinggi, nilai_terendah

def hitung_diatas_rata_rata(nilai, rata_rata):
    diatas_rata_rata = sum(1 for n in nilai if n > rata_rata)
    return diatas_rata_rata

def urutkan_nilai(nilai):
    nilai.sort()
    return nilai

def nilai_peringkat_ketiga_tertinggi(nilai):
    nilai_urut = sorted(nilai, reverse=True)
    return nilai_urut[2]

# Main program
if __name__ == "__main__":
    nilai = input_nilai()
    rata_rata = hitung_rata_rata(nilai)
    nilai_tertinggi, nilai_terendah = nilai_tertinggi_terendah(nilai)
    diatas_rata_rata = hitung_diatas_rata_rata(nilai, rata_rata)
    nilai_urut = urutkan_nilai(nilai)
    nilai_ketiga_tertinggi = nilai_peringkat_ketiga_tertinggi(nilai_urut)

    print("Rata-rata nilai ujian kelas:", rata_rata)
    print("Nilai ujian tertinggi:", nilai_tertinggi)
    print("Nilai ujian terendah:", nilai_terendah)
    print("Jumlah siswa dengan nilai di atas rata-rata:", diatas_rata_rata)
    print("Nilai ujian setelah diurutkan:", nilai_urut)
    print("Nilai ujian peringkat ketiga tertinggi:", nilai_ketiga_tertinggi)
