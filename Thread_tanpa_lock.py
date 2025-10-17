import threading
import time

saldo = 100
print_lock = threading.Lock()  # tambahan lock untuk print

def tarik_uang(nama, jumlah):
    global saldo
    with print_lock:
        print(f"{nama} mencoba menarik {jumlah}")
    time.sleep(1)
    if saldo >= jumlah:
        time.sleep(0.5)
        saldo -= jumlah
        with print_lock:
            print(f"{nama} berhasil menarik {jumlah}")
    else:
        with print_lock:
            print(f"{nama} gagal, saldo tidak cukup.")

t1 = threading.Thread(target=tarik_uang, args=("Cloey", 80))
t2 = threading.Thread(target=tarik_uang, args=("Grace", 80))

t1.start()
t2.start()
t1.join()
t2.join()

with print_lock:
    print(f"\nSaldo akhir: {saldo}")
