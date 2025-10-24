#input
print("================  Data Karyawan  =================")
nama_karyawan = input("masukan nama karyawan  :")
golongan = input("golongan jabatan (G1,G2,G3) :")
pendidikan = input("masukan pendidkan terakhir (SMA,D1,D3,S1) :")
jam_kerja = int(input("masukan jam kerja   :"))
print("===================================================")

gaji = 300000

print()
#proses 
if golongan == "g1"or golongan == "G1":
    tunjangan_jabatan = 0.05 * gaji
elif golongan == "g2" or golongan == "G2":
    tunjangan_jabatan = 0.10 * gaji
elif golongan == "g3" or golongan == "G3":
    tunjangan_jabatan = 0.15 * gaji
else:
    tunjangan_jabatan = 0
    print("Golongan tidak valid, tunjangan jabatan = 0")

# Hitung Tunjangan Pendidikan
if pendidikan == "SMA" or pendidikan == "sma":
    tunjangan_pendidikan = 0.025 * gaji
elif pendidikan == "D1" or pendidikan == "d1":
    tunjangan_pendidikan = 0.05 * gaji
elif pendidikan == "D3" or pendidikan == "d3":
    tunjangan_pendidikan = 0.20 * gaji
elif pendidikan == "S1" or pendidikan == "s1":
    tunjangan_pendidikan = 0.30 * gaji
else:
    tunjangan_pendidikan = 0
    print("Pendidikan tidak valid, tunjangan pendidikan = 0")

# Hitung Honor Lembur
if jam_kerja > 8:
    honor_lembur = (jam_kerja - 8) * 3500
else:
    honor_lembur = 0

# Hitung total gaji
total_gaji = gaji + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur
print()

# Output hasil
print("======================================================")
print("                 Rincian Gaji Karyawan                ")
print("======================================================")
print(f"Karyawan yang bernama  : {nama_karyawan}")
print(f"Honor yang diterima    :")
print(f"  Tunjangan Jabatan    : Rp {tunjangan_jabatan:,.0f}")
print(f"  Tunjangan Pendidikan : Rp {tunjangan_pendidikan:,.0f}")
print(f"  Honor Lembur         : Rp {honor_lembur:,.0f}")
print("------------------------------------")
print(f"Total Gaji             : Rp {total_gaji:,.0f}")
print("========================================================")

