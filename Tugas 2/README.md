# Tugas 2 - Progjar F

```
Nama : Bagus Aji Sinto Susilo
NRP  : 05111640000068
```

### Soal
![tugas](https://user-images.githubusercontent.com/32744054/55008139-295be600-5013-11e9-88df-b5b2093993f4.jpg)



### Cara Menjalankan Program

1. Jalankan cmd lalu run program serverudp.py
2. Buka window cmd baru lalu run program clientudp.py
3. [optional] Tunggu program clientudp.py selesai running, lalu re-run program clientudp.py
4. [optional] Buka window cmd baru lalu run program clientudp.py lagi
5. Close semua cmd

### Deskripsi Singkat Alur Program

1. Server berjalan menunggu client untuk connect
2. Setelah client connect, server akan membuat folder baru untuk menampung file gambar yang akan dikirim ke client
3. Server akan mengirim file gambar ke folder yang sudah dibuat tadi
4. Apabila file gambar sudah terkirim semua, program client otomatis stop namun server tetap running menunggu apabila ada client yang akan connect

### Info Tentang Program

1. Folder penampung dibuat oleh server
2. File dikirim dari server ke client
3. Proses writing data oleh client
4. Jumlah file yang dikirim oleh server adalah 5 file
5. Apabila program client telah selesai berjalan dan program client di run lagi (server belum di close) maka folder akan dibuat lagi terpisah untuk menampung file gambar untuk client baru
6. Apabila program client belum selesai berjalan dan user membuka window cmd baru untuk run program client maka folder akan dibuat lagi terpisah untuk menampung file gambar untuk client baru
7. Apabila program server dan client ditutup lalu kedua program tersebut dijalankan kembali maka server akan me-overwrite folder yang sudah ada sebelumnya menjadi folder baru untuk menampung file gambar yang diterima client yang baru
8. Format nama folder yaitu "client[client_keberapa]" , *client_keberapa berisi angka 1, 2, dst
9. Format nama file yang terkirim ke client yaitu "new_[nama_file_asli_dari_server]"

# SEKIAN
