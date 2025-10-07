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
print("Nama pembeli:",nama)
print("kode barang:",barang)
print("Harga barang (Rp):",harga)
print("uang bayar (Rp):",uang)
print("kembalian(Rp):",kembalian)
print("=================================")
print("     Terimakasih telah membeli   ")
print("=================================")