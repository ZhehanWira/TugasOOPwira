from abc import ABC, abstractmethod


# ABSTRACTION + ENCAPSULATION
class BarangElektronik(ABC):
    def __init__(self, nama, stok, harga_dasar):
        self.nama = nama
        self.__stok = stok        # private
        self.__harga_dasar = harga_dasar  # private

    # Getter stok
    def get_stok(self):
        return self.__stok

    # Getter harga dasar (biar bisa dipakai anak class)
    def get_harga_dasar(self):
        return self.__harga_dasar

    # Method untuk tambah stok dengan validasi
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")

    @abstractmethod
    def tampilkan_detail(self, jumlah_beli):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass



# INHERITANCE + POLYMORPHISM
class Laptop(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, processor):
        super().__init__(nama, stok, harga_dasar)
        self.processor = processor

    def hitung_harga_total(self, jumlah):
        harga = self.get_harga_dasar()
        pajak = harga * 0.10
        subtotal = (harga + pajak) * jumlah
        return subtotal, pajak

    def tampilkan_detail(self, jumlah_beli):
        harga = self.get_harga_dasar()
        subtotal, pajak = self.hitung_harga_total(jumlah_beli)

        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"   Harga Dasar: Rp {harga:,.0f} | Pajak(10%): Rp {pajak:,.0f}")
        print(f"   Beli: {jumlah_beli} unit | Subtotal: Rp {subtotal:,.0f}\n")


class Smartphone(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, kamera):
        super().__init__(nama, stok, harga_dasar)
        self.kamera = kamera

    def hitung_harga_total(self, jumlah):
        harga = self.get_harga_dasar()
        pajak = harga * 0.05
        subtotal = (harga + pajak) * jumlah
        return subtotal, pajak

    def tampilkan_detail(self, jumlah_beli):
        harga = self.get_harga_dasar()
        subtotal, pajak = self.hitung_harga_total(jumlah_beli)

        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"   Harga Dasar: Rp {harga:,.0f} | Pajak(5%): Rp {pajak:,.0f}")
        print(f"   Beli: {jumlah_beli} unit | Subtotal: Rp {subtotal:,.0f}\n")



# POLYMORPHISM (KERANJANG)
def proses_transaksi(daftar_barang):
    total = 0

    print("\n--- STRUK TRANSAKSI ---")
    nomor = 1

    for barang, jumlah in daftar_barang:
        print(f"{nomor}. ", end="")
        barang.tampilkan_detail(jumlah)
        subtotal, _ = barang.hitung_harga_total(jumlah)
        total += subtotal
        nomor += 1

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {total:,.0f}")



# ALUR PROGRAM (USER STORY)
print("--- SETUP DATA ---")

laptop = Laptop("ROG Zephyrus", 0, 20_000_000, "Ryzen 9")
hp = Smartphone("iPhone 13", 0, 15_000_000, "12MP")

laptop.tambah_stok(10)
hp.tambah_stok(-5)   # harus gagal
hp.tambah_stok(20)

# User membeli:
keranjang = [
    (laptop, 2),   # beli 2 laptop
    (hp, 1)        # beli 1 hp
]

proses_transaksi(keranjang)
