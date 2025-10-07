#input
nama = input("masukan nama pembeli:")
barang = input("masukan nama barang:")
harga = int(input("masukan harga sepatu(Rp):"))
uang = int(input("masukan uang bayar(Rp):"))

#proses
kembalian = uang - harga

#output
print("=================================")
print("          Struk barang           ")
print("=================================")
print(f"{'Nama pembeli':18}:{nama}")
print(f"{'kode barang':18}:{barang}")
print(f"{'harga barang (Rp)':18}:{harga}")
print(f"{'uang bayar (Rp)':18}:{uang}")
print(f"{'kembalian (Rp)':18}:{kembalian}")
print("=================================")
print("     Terimakasih telah membeli   ")
print("=================================")