### Nama:Simfrosa Gradiani
### Kelas:TI 23 B2
### NIM:312310748

# Tugas-Threading

## CodeThread_Lock,py
<img width="911" height="695" alt="screenshot Code Thread-lock" src="https://github.com/user-attachments/assets/492dc97d-fb8f-438b-b6c0-709bdaf7b155" />

### Hasil Output/Run
<img width="728" height="239" alt="Screenshot Run Thread-lock" src="https://github.com/user-attachments/assets/35f5851a-d48d-4472-aabe-bd36b6f0cd3c" />

* Hasil selalu konsisten,karena Lock membuat Akses saldo bergantian.
* Haya Satu orang yang bisa menarik uang terlebih dahalu.

## Code Thread_Tanpa_lock,py
<img width="881" height="677" alt="Screenshot code Thread-Tanpa-Lock" src="https://github.com/user-attachments/assets/8c7d318c-95c9-466d-b6f5-dd8f53061a83" />

### Hasil Output/Run
<img width="819" height="272" alt="Screenshot Run Thread- Tanpa-lock" src="https://github.com/user-attachments/assets/6aa926e0-7d91-44ae-bd3b-7ee2ae5e08fc" />

* Hasil bisa berbeda-beda tiap dijalankan,karena terjadi Race Condition.
* Kedua Thread bisa membaca saldo lama (100) sebelum pengurangan,sehingga saldo akhir bisa Negatif.

## Komentar setiap Kode
* saldo = 100 —  saldo awal.
* lock = threading.Lock() — membuat kunci agar akses ke saldo bergantian
* with lock: — bagian kritis yang hanya boleh diakses satu thread.
* t1.start() & t2.start() — menjalankan thread secara bersamaan.
* t1.join() & t2.join() — memastikan kedua thread selesai sebelum menampilkan saldo akhir.

## Kesimpulan
* Mengapa Lock penting?
Lock sangat penting dalam pemrograman multithreading karena mencegah terjadinya race condition.
Ketika dua thread (Cloey dan Grace) mencoba mengakses atau mengubah data yang sama (saldo) pada waktu bersamaan, maka hasil akhirnya bisa tidak konsisten.
Dengan menggunakan threading.Lock(), hanya satu thread yang diizinkan mengakses bagian kritis kode (misalnya saat membaca dan mengurangi saldo).
Thread lain harus menunggu sampai lock dilepas, sehingga data tetap aman dan hasil perhitungan selalu benar.
Contohnya:
Thread 1 (Cloey) menarik uang → masuk ke blok with lock:
Thread 2 (Grace) menunggu → baru berjalan setelah Andi selesai
Hasil akhir: saldo tidak pernah negatif, dan urutan transaksi jelas.

* Apa yang terjadi jika Lock Dihapus?
Jika lock dihapus, maka dua thread bisa mengakses saldo secara bersamaan tanpa koordinasi.
Akibatnya, program akan mengalami race condition, yaitu kondisi di mana hasil akhir tergantung pada urutan eksekusi thread yang tidak bisa diprediksi.
Dampaknya:
Kedua thread bisa membaca saldo 100 di waktu bersamaan.
Keduanya merasa saldo cukup, lalu masing-masing mengurangi 80.
Hasil akhirnya:bisa menjadi saldo negatif (-60) atau salah tampil di output.
