
import threading
import time

saldo = 100  # saldo awal
lock = threading.Lock()  # membuat kunci untuk mencegah konflik data

def tarik_uang(nama, jumlah):
    """
    Fungsi untuk menarik uang dengan proteksi lock.
    Lock memastikan hanya satu thread yang bisa mengakses saldo
    pada satu waktu sehingga data tetap konsisten.
    """
    global saldo
    print(f"{nama} mencoba menarik {jumlah}")
    time.sleep(1)  # simulasi proses
    with lock:  # bagian kritis, hanya satu thread yang bisa masuk
        if saldo >= jumlah:
            saldo -= jumlah
            print(f"{nama} berhasil menarik {jumlah}")
        else:
            print(f"{nama} gagal, saldo tidak cukup.")

# Membuat dua thread (Cloey dan Grace)
t1 = threading.Thread(target=tarik_uang, args=("Cloey", 80))
t2 = threading.Thread(target=tarik_uang, args=("Grace", 80))

# Menjalankan kedua thread secara bersamaan
t1.start()
t2.start()

# Menunggu kedua thread selesai
t1.join()
t2.join()

# Menampilkan saldo akhir
print(f"Saldo akhir: {saldo}")
