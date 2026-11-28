# Kasus distribusi PT XYZ Bahan Pangan

Dokumen ini memuat seluruh informasi untuk menyusun delapan model perencanaan distribusi. **Profil P1 menjelaskan kasus dasar secara lengkap. Profil P2–P8 merujuk pada profil sebelumnya dan menetapkan perubahan yang diterapkan.** Setiap profil dapat menggunakan jaringan Low, Medium, atau High.

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [P8](#p8)

<a id="p1"></a>

## Profil P1. Biaya minimum dengan permintaan pasti

### Perusahaan, aliran barang, dan keputusan

PT XYZ Bahan Pangan adalah perusahaan fiktif yang memasok **minyak goreng curah (A)**, **sirup gula cair (B)**, dan **susu cair dingin (C)**. Perusahaan memiliki enam pabrik P1–P6 dan empat calon gudang G1–G4 untuk melayani enam zona pelanggan K1–K6 selama **satu periode**. Sebutan Pabrik P1 menunjuk fasilitas; Profil P1 menunjuk jenis kasus pada bagian ini.

Barang dikirim melalui dua tahap: **pabrik → gudang → zona pelanggan**. Perusahaan memilih gudang yang dibuka dan menentukan berapa ton setiap produk dikirim pada setiap rute. Jumlah barang bersifat kontinu dan boleh pecahan. Pesanan 3,17 ton minyak, misalnya, dapat dipenuhi dengan 1,20 ton dari satu gudang dan 1,97 ton dari gudang lainnya jika rutenya tersedia.

Pasokan pabrik dianggap mencukupi untuk produk dan rute yang diizinkan; tidak ada batas tonase pasokan pabrik. Kapasitas penyaluran dibatasi di gudang. Keempat gudang dapat menangani ketiga produk. Produk tetap dicatat terpisah, sedangkan kapasitas tonase dan waktu kerja di setiap gudang dipakai bersama oleh seluruh produk.

### Pesanan yang harus dipenuhi

| Zona | Minyak A (ton) | Sirup B (ton) | Susu C (ton) |
| --- | --- | --- | --- |
| K1 | 3,17 | 0,88 | 1,09 |
| K2 | 2,84 | 1,16 | 0,86 |
| K3 | 1,12 | 2,79 | 1,07 |
| K4 | 0,93 | 3,24 | 0,98 |
| K5 | 1,03 | 0,97 | 2,73 |
| K6 | 0,91 | 0,96 | 3,27 |

Setiap produk mempunyai total pesanan 10 ton. Total pesanan perusahaan adalah 30 ton. Perusahaan mengetahui seluruh pesanan tersebut sebelum memilih gudang dan jumlah kiriman.

### Pembukaan dan kapasitas gudang

| Gudang | Kapasitas (ton) | Waktu tersedia (jam) | Biaya buka |
| --- | --- | --- | --- |
| G1 | 16,00 | 17,80 | 25,40 |
| G2 | 20,00 | 22,40 | 31,65 |
| G3 | 18,00 | 19,80 | 28,30 |
| G4 | 14,00 | 16,10 | 18,75 |

Membuka gudang mengaktifkan kapasitas pada tabel selama periode perencanaan. Biaya buka dibayar sekali untuk setiap gudang yang dipilih. Gudang yang ditutup tidak menerima atau mengirim barang. Kapasitas gudang yang dibuka tetap sebesar angka pada tabel; perusahaan tidak memilih tambahan kapasitas.

Pada Profil P1, menangani satu ton barang membutuhkan **satu jam kerja**, untuk setiap produk dan gudang. Jika G1 menangani 5 ton minyak, 4 ton sirup, dan 3 ton susu, pemakaian kapasitasnya 12 ton dan waktunya 12 jam. Keduanya memenuhi batas G1, yaitu 16 ton dan 17,80 jam.

Kapasitas tonase dan waktu kerja merupakan dua batas operasi yang diperiksa pada gudang yang sama. Dalam data linear ini, batas tonase sudah cukup untuk memenuhi batas waktu karena setiap ton memakai satu jam dan waktu tersedia lebih besar daripada kapasitas tonase.

### Produk yang tersedia dari pabrik

| Pabrik | Produk |
| --- | --- |
| P1 | A, B |
| P2 | A |
| P3 | A, B, C |
| P4 | B, C |
| P5 | A, C |
| P6 | B, C |

### Rute Low, Medium, dan High

Ketiga tingkat memakai pabrik, gudang, zona, produk, permintaan, kapasitas, dan tarif yang sama. Perbedaannya adalah rute per produk yang diizinkan. **Semua rute Low tersedia pada Medium; semua rute Medium tersedia pada High.** Rute yang tersedia merupakan pilihan dan boleh mempunyai jumlah kiriman nol.

![Jaringan tiga produk untuk Low, Medium, dan High](diagram/Jaringan_Low_Medium_High.svg)

Nama node yang sama pada panel A, B, dan C menunjuk fasilitas fisik yang sama. Kapasitas gudang berlaku untuk gabungan ketiga produk. Low membaca garis hijau; Medium membaca hijau dan merah putus-putus; High membaca seluruh garis. [Buka gambar PNG](diagram/Jaringan_Low_Medium_High.png).

| Tingkat | Rute pabrik–gudang–produk | Rute gudang–zona–produk |
| --- | --- | --- |
| Low | 16 | 36 |
| Medium | 17 | 42 |
| High | 22 | 60 |

**Pabrik yang diizinkan memasok setiap gudang–produk:**

| Gudang–produk | Low | Medium | High |
| --- | --- | --- | --- |
| G1–A | P1 | P1 | P1 |
| G1–B | P1 | P1 | P1 |
| G1–C | P4 | P4 | P3, P4 |
| G2–A | P1, P2 | P1, P2 | P1, P2 |
| G2–B | P4 | P4 | P4 |
| G2–C | P4 | P4 | P4 |
| G3–A | P3 | P3 | P3, P5 |
| G3–B | P3 | P3 | P3, P6 |
| G3–C | P3 | P3 | P3, P5, P6 |
| G4–A | P3, P5 | P3, P5 | P3, P5 |
| G4–B | P3, P6 | P3, P6 | P3, P6 |
| G4–C | P5, P6 | P3, P5, P6 | P3, P5, P6 |

**Zona yang diizinkan menerima kiriman setiap gudang–produk:**

| Gudang–produk | Low | Medium | High |
| --- | --- | --- | --- |
| G1–A | K1, K2 | K1, K2 | K1, K2, K3, K5 |
| G1–B | K3, K4 | K3, K4 | K1, K3, K4 |
| G1–C | K5, K6 | K5, K6 | K5, K6 |
| G2–A | K1, K2 | K1, K2, K4, K6 | K1, K2, K4, K6 |
| G2–B | K3, K4 | K2, K3, K4 | K2, K3, K4, K5, K6 |
| G2–C | K5, K6 | K1, K2, K3, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G3–A | K3, K4, K5, K6 | K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G3–B | K1, K2, K5, K6 | K1, K2, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G3–C | K1, K2, K3, K4 | K1, K2, K3, K4 | K1, K2, K3, K4, K5, K6 |
| G4–A | K3, K4, K5, K6 | K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G4–B | K1, K2, K5, K6 | K1, K2, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G4–C | K1, K2, K3, K4 | K1, K2, K3, K4 | K1, K2, K3, K4, K5, K6 |

Untuk memakai rute lengkap, kedua tahap pengiriman produk yang sama harus tersedia dan gudangnya harus dibuka. Contoh pada Low: Pabrik P4 dapat mengirim susu ke G2; G2 dapat mengirim susu itu ke K5 atau K6. Pada Medium, G2 juga dapat mengirim susu ke K1, K2, dan K3.

### Biaya angkut dan penanganan

Perusahaan membayar biaya buka gudang, biaya angkut pada kedua tahap, dan biaya penanganan dasar sekali per ton yang melewati gudang. Semua angka biaya memakai **satuan biaya sintetis** yang konsisten. Tarif angkut pada satu pasangan fasilitas berlaku per ton untuk produk yang diizinkan melalui pasangan tersebut.

Angka pada matriks tarif dipakai hanya jika rute produk itu tersedia pada tingkat yang dipilih. Izin rute ditentukan oleh dua tabel rute sebelumnya.

**Tarif angkut pabrik → gudang per ton:**

| Pabrik | G1 | G2 | G3 | G4 |
| --- | --- | --- | --- | --- |
| P1 | 2,35 | 3,42 | 6,85 | 7,64 |
| P2 | 3,18 | 2,76 | 6,43 | 5,87 |
| P3 | 6,72 | 5,48 | 2,24 | 3,36 |
| P4 | 2,68 | 2,41 | 5,96 | 6,83 |
| P5 | 5,84 | 4,73 | 4,23 | 2,17 |
| P6 | 6,13 | 5,26 | 3,04 | 2,89 |

**Tarif angkut gudang → zona per ton:**

| Gudang | K1 | K2 | K3 | K4 | K5 | K6 |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | 1,84 | 5,72 | 2,36 | 5,48 | 3,15 | 5,93 |
| G2 | 2,43 | 4,86 | 1,92 | 4,37 | 2,68 | 4,71 |
| G3 | 5,61 | 2,18 | 4,92 | 1,76 | 4,35 | 2,64 |
| G4 | 4,87 | 2,56 | 4,28 | 2,31 | 5,14 | 1,89 |

**Tarif penanganan dasar per ton:**

| Gudang | A | B | C |
| --- | --- | --- | --- |
| G1 | 1,18 | 1,74 | 2,86 |
| G2 | 1,63 | 1,29 | 2,21 |
| G3 | 1,92 | 1,46 | 1,57 |
| G4 | 1,37 | 1,88 | 1,94 |

Sebagai contoh, satu ton minyak melalui Pabrik P1 → G1 → K1 menimbulkan biaya angkut masuk 2,35, penanganan 1,18, dan angkut keluar 1,84. Jumlahnya **5,37 per ton**. Untuk 2 ton melalui rute tersebut, biaya variabelnya 10,74. Biaya buka G1 sebesar 25,40 dihitung satu kali untuk seluruh rencana yang memakai G1.

### Aturan operasi dan keluaran P1

1. Gunakan hanya produk dan rute yang diizinkan pada tingkat yang dipilih.
2. Untuk setiap produk di setiap gudang, jumlah yang diterima harus sama dengan jumlah yang dikirim keluar selama periode tersebut. Barang tidak berubah jenis saat melewati gudang.
3. Seluruh pesanan per zona dan produk dipenuhi tepat. Kiriman dapat dibagi antargudang.
4. Jumlah seluruh produk yang ditangani sebuah gudang memenuhi batas tonase dan jam kerja gudang itu. Gudang tertutup mempunyai arus masuk dan keluar nol.
5. Setiap gudang dipilih buka atau tutup. Jumlah kiriman nonnegatif dan boleh pecahan.

**Tugas P1:** susun model untuk meminimalkan jumlah biaya buka, angkut dua tahap, dan penanganan dasar. Laporkan biaya minimum, gudang yang dibuka, serta tonase kiriman per rute dan produk. Hasil perhitungan dapat disajikan dalam satuan biaya dengan empat angka desimal.

<a id="p2"></a>

## Profil P2. Biaya harapan minimum dengan permintaan stokastik

Gunakan seluruh aturan dan data P1, dengan perubahan pada **seluruh 18 pesanan zona–produk**. Setiap produk mempunyai distribusi diskret dengan tiga kondisi berikut. Angka pengali dikalikan dengan tabel pesanan dasar P1.

| Produk | Sepi: pengali; peluang | Sedang: pengali; peluang | Ramai: pengali; peluang |
| --- | --- | --- | --- |
| A | 0,70; 25,00% | 1,00; 50,00% | 1,30; 25,00% |
| B | 0,80; 20,00% | 0,95; 60,00% | 1,35; 20,00% |
| C | 0,75; 30,00% | 1,05; 50,00% | 1,25; 20,00% |

Kondisi A, B, dan C diasumsikan independen. Zona untuk produk yang sama bergerak bersama: apabila pengali A adalah 0,70, seluruh enam pesanan minyak dikalikan 0,70. Kondisi produk B dan C ditentukan oleh pengalinya masing-masing. Terdapat **27 kombinasi bersama**, yaitu 3 × 3 × 3.

Contoh ketika A sepi, B ramai, dan C sedang: peluangnya 0,25 × 0,20 × 0,50 = **0,025 atau 2,5%**. Pesanan K1 menjadi 2,219 ton A, 1,188 ton B, dan 1,1445 ton C.

Nilai harapan pengali setiap produk adalah satu. Karena itu, tabel pesanan pasti pada P1 juga merupakan nilai harapan permintaan P2. Kondisi bernama sedang mengikuti angka pada tabel dan tidak harus sama dengan nilai harapan setiap produk.

**Seluruh skenario yang digunakan:**

| Skenario | Pengali A | Pengali B | Pengali C | Peluang (%) | Total pesanan (ton) |
| --- | --- | --- | --- | --- | --- |
| 1 | 0,70 | 0,80 | 0,75 | 1,50 | 22,50 |
| 2 | 0,70 | 0,80 | 1,05 | 2,50 | 25,50 |
| 3 | 0,70 | 0,80 | 1,25 | 1,00 | 27,50 |
| 4 | 0,70 | 0,95 | 0,75 | 4,50 | 24,00 |
| 5 | 0,70 | 0,95 | 1,05 | 7,50 | 27,00 |
| 6 | 0,70 | 0,95 | 1,25 | 3,00 | 29,00 |
| 7 | 0,70 | 1,35 | 0,75 | 1,50 | 28,00 |
| 8 | 0,70 | 1,35 | 1,05 | 2,50 | 31,00 |
| 9 | 0,70 | 1,35 | 1,25 | 1,00 | 33,00 |
| 10 | 1,00 | 0,80 | 0,75 | 3,00 | 25,50 |
| 11 | 1,00 | 0,80 | 1,05 | 5,00 | 28,50 |
| 12 | 1,00 | 0,80 | 1,25 | 2,00 | 30,50 |
| 13 | 1,00 | 0,95 | 0,75 | 9,00 | 27,00 |
| 14 | 1,00 | 0,95 | 1,05 | 15,00 | 30,00 |
| 15 | 1,00 | 0,95 | 1,25 | 6,00 | 32,00 |
| 16 | 1,00 | 1,35 | 0,75 | 3,00 | 31,00 |
| 17 | 1,00 | 1,35 | 1,05 | 5,00 | 34,00 |
| 18 | 1,00 | 1,35 | 1,25 | 2,00 | 36,00 |
| 19 | 1,30 | 0,80 | 0,75 | 1,50 | 28,50 |
| 20 | 1,30 | 0,80 | 1,05 | 2,50 | 31,50 |
| 21 | 1,30 | 0,80 | 1,25 | 1,00 | 33,50 |
| 22 | 1,30 | 0,95 | 0,75 | 4,50 | 30,00 |
| 23 | 1,30 | 0,95 | 1,05 | 7,50 | 33,00 |
| 24 | 1,30 | 0,95 | 1,25 | 3,00 | 35,00 |
| 25 | 1,30 | 1,35 | 0,75 | 1,50 | 34,00 |
| 26 | 1,30 | 1,35 | 1,05 | 2,50 | 37,00 |
| 27 | 1,30 | 1,35 | 1,25 | 1,00 | 39,00 |

Seluruh skenario tersebut dipertimbangkan bersama. Daftar dan peluangnya menjadi data tetap model. Semua pesanan dalam setiap skenario dihitung dari tabel P1 dan pengali di atas. Nilai harapan total pesanan adalah 30 ton; total terendah 22,50 ton dan tertinggi 39,00 ton.

**Urutan keputusan:** perusahaan memilih gudang sebelum kondisi permintaan diketahui. Pilihan gudang tersebut berlaku sama untuk seluruh 27 skenario. Setelah kondisi diketahui, jumlah kiriman dapat disesuaikan. Setiap skenario wajib memenuhi seluruh pesanan, neraca barang, kapasitas tonase, dan waktu gudang.

**Tugas P2:** minimalkan biaya buka gudang satu kali ditambah biaya operasi rata-rata berbobot peluang. Rata-rata berbobot diperoleh dengan mengalikan biaya operasi setiap skenario dengan peluangnya, lalu menjumlahkan hasilnya. Laporkan biaya harapan, gudang yang dibuka, dan rencana kiriman untuk setiap skenario.

<a id="p3"></a>

## Profil P3. Biaya dan emisi dengan permintaan pasti

Gunakan P1 dan tambahkan **emisi sebagai tujuan kedua**. Emisi yang diperhitungkan berasal dari gudang yang dibuka serta angkutan pada kedua tahap. Emisi tetap gudang dihitung sekali per gudang yang dibuka; emisi angkutan dihitung dengan mengalikan faktor rute dengan ton yang dikirim. Satuan emisi adalah kg CO₂e.

**Emisi tetap gudang per periode:**

| Gudang | Emisi tetap (kg CO₂e) |
| --- | --- |
| G1 | 25,00 |
| G2 | 20,00 |
| G3 | 8,00 |
| G4 | 24,00 |

**Emisi pabrik → gudang, kg CO₂e per ton:**

| Pabrik | G1 | G2 | G3 | G4 |
| --- | --- | --- | --- | --- |
| P1 | 5,00 | 1,80 | 1,50 | 1,30 |
| P2 | 1,60 | 2,10 | 3,90 | 4,40 |
| P3 | 1,20 | 3,10 | 2,40 | 2,10 |
| P4 | 4,50 | 1,00 | 3,50 | 4,40 |
| P5 | 3,80 | 3,50 | 0,70 | 3,50 |
| P6 | 4,10 | 3,50 | 1,00 | 2,90 |

**Emisi gudang → zona, kg CO₂e per ton:**

| Gudang | K1 | K2 | K3 | K4 | K5 | K6 |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | 1,40 | 3,60 | 1,70 | 3,70 | 1,90 | 3,60 |
| G2 | 0,90 | 3,50 | 1,20 | 3,50 | 1,30 | 3,30 |
| G3 | 0,75 | 0,90 | 0,80 | 0,80 | 3,10 | 0,80 |
| G4 | 3,70 | 2,00 | 3,60 | 2,10 | 3,70 | 2,20 |

Sebagai contoh, satu ton minyak melalui Pabrik P1 → G1 → K1 menimbulkan emisi angkutan 5,00 + 1,40 = **6,40 kg CO₂e**. Emisi tetap G1 sebesar 25 kg CO₂e ditambahkan sekali apabila G1 dibuka.

**Tugas P3:** cari kompromi antara biaya dan emisi. Gunakan prosedur batas emisi berikut untuk menghasilkan keluaran yang dapat dibandingkan:

1. Cari titik ujung emisi minimum dan titik ujung biaya minimum. Pada ujung emisi minimum, pilih biaya terendah di antara rencana dengan emisi setara secara numerik. Pada ujung biaya minimum, pilih emisi terendah di antara rencana dengan biaya setara secara numerik.
2. Ambil **25 batas emisi berjarak sama**, termasuk kedua ujung rentang emisi dari rencana ujung tersebut. Rentang dihitung untuk profil dan tingkat rute yang sedang dinilai.
3. Untuk setiap batas emisi, cari biaya terendah yang tetap memenuhi batas tersebut. Selanjutnya pilih emisi terendah di antara rencana dengan biaya setara secara numerik dan tetap memenuhi batas emisi.
4. Gunakan toleransi kesetaraan biaya 0,00025 satuan biaya dan toleransi emisi 0,00025 kg CO₂e. Laporkan pasangan biaya–emisi, gudang terbuka, dan kiriman. Pada grafik, tampilkan setiap titik unik sekali dan keluarkan titik yang didominasi oleh titik hasil lain sesuai toleransi tersebut.

Sebuah titik didominasi apabila ada titik lain yang biaya dan emisinya sama atau lebih rendah, dengan setidaknya satu ukuran lebih rendah. Batas emisi menyatakan emisi maksimum yang diperbolehkan untuk satu rencana distribusi.

<a id="p4"></a>

## Profil P4. Biaya harapan dan emisi harapan

Gabungkan ketidakpastian permintaan P2 dengan dua tujuan dan data emisi P3. Gudang dipilih sebelum permintaan diketahui dan pilihan yang sama digunakan pada seluruh 27 skenario. Kiriman disesuaikan pada setiap skenario.

**Tugas P4:** minimalkan biaya harapan dan emisi harapan. Emisi harapan adalah emisi tetap gudang satu kali ditambah rata-rata berbobot peluang dari emisi angkutan. Terapkan 25 batas pada **emisi harapan** menggunakan prosedur P3. Pesanan, kapasitas, waktu, dan neraca harus dipenuhi pada setiap skenario. Laporkan pasangan tujuan, pilihan gudang, dan kiriman per skenario untuk setiap titik yang dilaporkan.

<a id="p5"></a>

## Profil P5. Biaya minimum dengan penanganan nonlinear

Gunakan permintaan pasti dan seluruh aturan P1, dengan perubahan biaya dan waktu penanganan pada **keempat gudang**. Biaya angkut, kapasitas tonase, jam tersedia, dan biaya buka tetap mengikuti P1.

Untuk **setiap produk di setiap gudang**, jumlahkan seluruh ton produk itu yang dikirim dari gudang ke zona-zona. Kuadratkan jumlah tersebut. Tambahkan:

- **0,04 kali kuadrat tonase** sebagai biaya penanganan tambahan.
- **0,025 kali kuadrat tonase** sebagai jam kerja tambahan.

Jumlahkan kontribusi ketiga produk pada masing-masing gudang. Kuadrat dihitung setelah seluruh kiriman satu produk dari gudang itu dijumlahkan. Tetap tambahkan biaya penanganan dasar per ton dan waktu dasar satu jam per ton.

Contoh: pada High, G3 menangani 5 ton A, 4 ton B, dan 3 ton C. Jumlah kuadrat tonase adalah 25 + 16 + 9 = **50**. Tambahan biaya adalah 0,04 × 50 = **2,00**, sedangkan tambahan waktu adalah 0,025 × 50 = **1,25 jam**. Total waktu penanganannya menjadi 12 + 1,25 = **13,25 jam**.

Contoh lain: rencana menangani 10 ton B dan 8 ton C di G3 memenuhi kapasitas fisik 18 ton. Akan tetapi, waktu nonlinear menjadi 18 + 0,025 × (100 + 64) = **22,10 jam**, melebihi waktu tersedia G3 sebesar 19,80 jam. Karena itu, rencana tersebut harus diubah agar memenuhi batas waktu.

**Tugas P5:** minimalkan biaya buka, angkut, penanganan dasar, dan tambahan penanganan kuadratik. Penuhi kapasitas tonase serta waktu nonlinear pada setiap gudang. Laporkan biaya minimum, gudang terbuka, dan kiriman per rute dan produk.

<a id="p6"></a>

## Profil P6. Biaya harapan dengan penanganan nonlinear

Gabungkan 27 skenario permintaan P2 dengan aturan penanganan kuadratik P5. Hitung tonase, kuadrat tonase, biaya penanganan, dan jam kerja **pada masing-masing skenario**. Setelah biaya skenario dihitung, kalikan dengan peluang skenario dan jumlahkan untuk memperoleh biaya operasi harapan. Tambahkan biaya buka gudang satu kali.

Pilihan gudang berlaku sama pada seluruh skenario. Pesanan, neraca, kapasitas tonase, dan waktu nonlinear dipenuhi di setiap skenario; jumlah kiriman boleh disesuaikan dengan skenario.

**Tugas P6:** minimalkan biaya harapan. Laporkan biaya harapan, gudang terbuka, dan rencana kiriman setiap skenario.

<a id="p7"></a>

## Profil P7. Biaya dan emisi dengan penanganan nonlinear

Gunakan permintaan pasti serta penanganan nonlinear P5. Tambahkan tujuan dan data emisi P3. Definisi emisi tetap mengikuti P3: emisi gudang yang dibuka dan emisi angkutan dua tahap. Tambahan biaya dan waktu kuadratik mengikuti P5 pada seluruh gudang.

**Tugas P7:** hasilkan kompromi biaya–emisi dengan 25 batas emisi dan prosedur P3. Biaya mencakup penanganan kuadratik; setiap rencana memenuhi kapasitas tonase dan waktu nonlinear. Laporkan pasangan tujuan, gudang, dan kiriman pada setiap titik yang dilaporkan.

<a id="p8"></a>

## Profil P8. Biaya harapan dan emisi harapan dengan penanganan nonlinear

Gabungkan biaya harapan dan penanganan nonlinear P6 dengan emisi harapan serta prosedur Pareto P4. Seluruh 18 pesanan mengikuti 27 skenario P2. Pilihan gudang sama pada seluruh skenario, sedangkan kiriman disesuaikan per skenario.

**Tugas P8:** terapkan 25 batas pada emisi harapan dan minimalkan biaya harapan pada setiap batas. Biaya penanganan kuadratik dihitung pada setiap skenario sebelum dirata-ratakan. Kapasitas tonase dan waktu nonlinear wajib dipenuhi di setiap skenario. Laporkan pasangan biaya harapan–emisi harapan, gudang terbuka, dan kiriman setiap skenario untuk setiap titik yang dilaporkan.

## Ringkasan penggunaan data

| Profil | Permintaan | Tujuan | Penanganan |
| --- | --- | --- | --- |
| P1 | Pasti | Biaya | Linear |
| P2 | 27 skenario | Biaya harapan | Linear |
| P3 | Pasti | Biaya dan emisi | Linear |
| P4 | 27 skenario | Biaya dan emisi harapan | Linear |
| P5 | Pasti | Biaya | Kuadratik |
| P6 | 27 skenario | Biaya harapan | Kuadratik |
| P7 | Pasti | Biaya dan emisi | Kuadratik |
| P8 | 27 skenario | Biaya dan emisi harapan | Kuadratik |

Semua profil memakai daftar fasilitas dan tabel tarif yang sama pada tingkat rute yang sama. Profil deterministik memakai satu kondisi pesanan pasti. Profil stokastik memakai 27 skenario bersama. Pada profil dua tujuan, 25 batas emisi menghasilkan sampel kompromi dan dapat memberikan kurang dari 25 titik unik.

[Halaman utama](../README.md) · [Tabel data CSV](data_tabel/) · [Model matematika acuan](../math_model_acuan/Model_Matematika.md)
