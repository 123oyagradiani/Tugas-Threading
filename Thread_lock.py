import threading
import time

saldo = 100  
lock = threading.Lock()  

def tarik_uang(nama, jumlah):
    """
    Fungsi untuk menarik uang dengan proteksi lock.
    Lock memastikan hanya satu thread yang bisa mengakses saldo
    pada satu waktu sehingga data tetap konsisten.
    """
    global saldo
    print(f"{nama} mencoba menarik {jumlah}")
    time.sleep(1)  
    with lock:  
        if saldo >= jumlah:
            saldo -= jumlah
            print(f"{nama} berhasil menarik {jumlah}")
        else:
            print(f"{nama} gagal, saldo tidak cukup.")

t1 = threading.Thread(target=tarik_uang, args=("Cloey", 80))
t2 = threading.Thread(target=tarik_uang, args=("Grace", 80))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Saldo akhir: {saldo}")

