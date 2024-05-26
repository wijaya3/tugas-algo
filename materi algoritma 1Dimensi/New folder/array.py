nilai_siswa = {"90,80,70,60"}
print(nilai_siswa(2))

nilai_siswa.append(70) 

nilai_siswa[0] = 40

nilai_siswa.pop(0)
print(nilai_siswa)

print(len(nilai_siswa))
print(sum(nilai_siswa))

print(max(nilai_siswa))
print(min(nilai_siswa))

rata_rata = sum(nilai_siswa)/(nilai_siswa)
print(max(nilai_siswa))
print(min(nilai_siswa))
print(rata_rata)

nilai_diatas_rata_rata = sum(True for i in nilai_siswa if i > rata_rata)
print(nilai_diatas_rata_rata)