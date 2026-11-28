# Kasus distribusi PT XYZ Bahan Pangan

Delapan profil menggunakan jaringan distribusi yang sama. **P1** memuat kasus dasar secara lengkap. **P2–P8** merujuk pada profil sebelumnya dan menjelaskan perubahan yang perlu diterapkan. Setiap profil dapat dijalankan pada salah satu tingkat rute **Low**, **Medium**, atau **High**.

**Cakupan model.** Pada profil stokastik, **hanya pesanan minyak goreng di zona K1** yang berubah antarskenario. Pada profil nonlinear, **biaya dan waktu penanganan di gudang** bergantung pada kuadrat tonase. Keenam pabrik masing-masing memakai batas pasokan linear sebesar 8 ton.

[P1](#p1-minimisasi-biaya-dengan-permintaan-pasti) · [P2](#p2-minimisasi-biaya-harapan) · [P3](#p3-biaya-dan-emisi) · [P4](#p4-biaya-harapan-dan-emisi-harapan) · [P5](#p5-minimisasi-biaya-dengan-penanganan-nonlinear) · [P6](#p6-biaya-harapan-dengan-penanganan-nonlinear) · [P7](#p7-biaya-dan-emisi-dengan-penanganan-nonlinear) · [P8](#p8-biaya-harapan-dan-emisi-harapan-dengan-penanganan-nonlinear)

## P1. Minimisasi biaya dengan permintaan pasti

PT XYZ Bahan Pangan adalah perusahaan fiktif yang memasok **minyak goreng curah (A)**, **sirup gula cair (B)**, dan **susu cair dingin (C)**. Perusahaan memiliki enam pabrik dan empat calon gudang untuk melayani enam zona pelanggan selama satu periode. Barang melewati dua tahap pengiriman, yaitu **pabrik → gudang** dan **gudang → zona pelanggan**.

Perusahaan menentukan **gudang mana yang dibuka** dan **berapa ton setiap produk dikirim melalui tiap rute**. Sebagai contoh, zona K1 dapat menerima **1,25 ton minyak dari G1** dan **1,75 ton dari G2** untuk memenuhi pesanannya sebesar **3 ton**. Jumlah kiriman boleh pecahan.

### Rute Low, Medium, dan High

![Rute pabrik–gudang–zona untuk tiga produk. Warna menunjukkan tingkat saat rute pertama kali tersedia.](diagram/Jaringan_Low_Medium_High.svg)

| Tingkat | Panah yang dibaca | Pabrik → gudang | Gudang → zona |
| --- | --- | ---: | ---: |
| Low | Hijau penuh | 16 | 36 |
| Medium | Hijau + merah putus-putus | 21 | 43 |
| High | Hijau + merah putus-putus + hitam bertitik | 35 | 57 |

Ikuti panah untuk **produk yang sama** pada kedua tahap. Untuk minyak goreng, misalnya, **P1 → G1 → K1** tersedia sejak Low. Rute lengkap memerlukan kedua panah pada tingkat yang dipilih serta gudang yang dibuka. Pabrik, gudang, zona, permintaan, tarif, dan kapasitas pada kasus dasar sama di ketiga tingkat. [Lihat daftar rute per produk](Rute_Pengiriman.md#cara-membaca-tabel)

### Aturan pengiriman

1. **Pabrik.** Setiap pabrik dapat memasok maksimal 8 ton. Ketiga produk berbagi batas tersebut.
2. **Gudang.** Gudang yang dibuka dapat menerima dan mengirim barang sampai batas tonase dan waktu penanganannya. Barang yang diterima harus diteruskan ke zona pelanggan dalam periode yang sama, per produk. Gudang yang ditutup memiliki arus masuk dan keluar nol.
3. **Zona pelanggan.** Pesanan per produk harus dipenuhi tepat. Kiriman dapat dibagi ke beberapa gudang yang melayani produk dan zona tersebut.
4. **Tarif.** Perusahaan membayar biaya buka gudang satu kali. Biaya angkut dibayar pada kedua tahap, dan biaya penanganan dikenakan sekali per ton yang melewati gudang. Semua angka biaya memakai satuan biaya sintetis.

| Calon gudang | Kapasitas (ton) | Waktu tersedia (jam) | Biaya buka |
| --- | ---: | ---: | ---: |
| G1 | 16 | 19,20 | 25 |
| G2 | 20 | 24,00 | 31 |
| G3 | 18 | 21,60 | 28 |
| G4 | 14 | 16,80 | 17 |

### Tarif angkut dan penanganan

Seluruh biaya memakai satuan biaya sintetis. Tarif angkut ditentukan oleh pasangan lokasi dan berlaku untuk semua produk yang boleh memakai jalur tersebut. Gunakan [daftar rute per produk](Rute_Pengiriman.md) untuk melihat jalur yang tersedia.

**Angkut dari pabrik ke gudang · biaya per ton**

| Pabrik | G1 | G2 | G3 | G4 |
| --- | ---: | ---: | ---: | ---: |
| P1 | 2 | 3 | 7 | 8 |
| P2 | 3 | 4 | 7 | 8 |
| P3 | 7 | 6 | 2 | 3 |
| P4 | 2 | 2 | 7 | 8 |
| P5 | 7 | 6 | 3 | 2 |
| P6 | 7 | 6 | 2 | 3 |

**Angkut dari gudang ke zona pelanggan · biaya per ton**

| Gudang | K1 | K2 | K3 | K4 | K5 | K6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| G1 | 2 | 7 | 2 | 7 | 3 | 7 |
| G2 | 1 | 7 | 2 | 7 | 2 | 6 |
| G3 | 7 | 2 | 7 | 2 | 6 | 2 |
| G4 | 7 | 1,79 | 6 | 2 | 7 | 2 |

**Penanganan di gudang · biaya per ton**

| Gudang | Minyak (A) | Sirup (B) | Susu (C) |
| --- | ---: | ---: | ---: |
| G1 | 1 | 1 | — |
| G2 | 2 | 2 | 3 |
| G3 | 2 | 1 | 2 |
| G4 | 1 | 1 | 3 |

Tanda **—** berarti produk tersebut tidak ditangani oleh gudang. Biaya buka gudang pada tabel sebelumnya dibayar sekali.

Untuk minyak goreng dari **P1 lewat G1 ke K1**, tarif dasar per ton adalah 2 untuk angkut masuk, 1 untuk penanganan, dan 2 untuk angkut keluar. Jumlahnya **5 per ton**. Biaya membuka G1, jika dipilih, dihitung terpisah.

### Kapasitas fisik dan waktu penanganan

Kapasitas tonase mengukur **berapa banyak barang** yang dapat ditangani. Batas waktu mengukur **berapa jam kerja** yang tersedia. Pada data uji, untuk tiap ton kapasitas tersedia 1,2 jam. Karena itu, G3 yang berkapasitas 18 ton mempunyai waktu 21,60 jam.

Pada P1, waktu penanganan dihitung secara linear. Setiap ton membutuhkan satu jam. Menangani 18 ton di G3 memerlukan 18 jam, sehingga memenuhi kedua batas.

### Permintaan dasar

| Zona | Minyak goreng (ton) | Sirup gula (ton) | Susu dingin (ton) |
| --- | ---: | ---: | ---: |
| K1 | 3 | 1 | 1 |
| K2 | 3 | 1 | 1 |
| K3 | 1 | 3 | 1 |
| K4 | 1 | 3 | 1 |
| K5 | 1 | 1 | 3 |
| K6 | 1 | 1 | 3 |

**Keputusan dan keluaran.** Perusahaan mengetahui seluruh pesanan sebelum menentukan gudang yang dibuka dan jumlah kiriman. Carilah biaya total terendah yang mencakup biaya buka gudang, biaya angkut pada kedua tahap, dan biaya penanganan. Laporkan biaya total, gudang yang dibuka, dan jumlah kiriman pada setiap rute dan produk.

## P2. Minimisasi biaya harapan

Gunakan [P1](#p1-minimisasi-biaya-dengan-permintaan-pasti) dengan perubahan pada permintaan minyak goreng di K1. Pesanan itu dapat berada pada salah satu dari tiga skenario. **Sebanyak 17 kombinasi zona–produk lainnya memakai angka yang sama pada ketiga skenario.** Contohnya, pesanan sirup K1 selalu 1 ton dan pesanan minyak K2 selalu 3 ton pada data dasar.

| Skenario | Peluang (dibulatkan) | Pesanan minyak K1 jika rata-ratanya 3 ton |
| --- | ---: | ---: |
| Sepi | 15,87% | 1,475 ton |
| Sedang | 68,27% | 3,000 ton |
| Ramai | 15,87% | 4,525 ton |

Skenario dibentuk dari tiga bagian distribusi normal dengan simpangan baku 1 ton. Bagian bawah berada di bawah rata-rata dikurangi 1 ton, bagian tengah berada dalam rentang satu simpangan baku di sekitar rata-rata, dan bagian atas berada di atas rata-rata ditambah 1 ton. Peluang setiap skenario adalah peluang bagiannya. Pesanan pada tabel adalah rata-rata dalam bagian itu. Tabel menampilkan angka yang dibulatkan. Solver menggunakan nilai sebelum pembulatan.

Pada benchmark, volume permintaan dasar bisa berbeda dari satu paket data ke paket lain. Setelah satu paket dipilih, hanya pesanan minyak K1 yang berubah di antara ketiga skenarionya.

**Keputusan dan keluaran.** Tentukan gudang yang dibuka sebelum skenario diketahui. Gunakan keputusan buka yang sama di ketiga skenario, lalu sesuaikan jumlah kiriman setelah permintaan diketahui. Penuhi seluruh pesanan di setiap skenario. Minimalkan biaya buka gudang ditambah rata-rata berbobot peluang dari biaya angkut dan penanganan. Laporkan biaya harapan, gudang yang dibuka, dan rencana kiriman per skenario.

## P3. Biaya dan emisi

Gunakan [P1](#p1-minimisasi-biaya-dengan-permintaan-pasti) dan tambahkan emisi sebagai tujuan kedua. Hitung emisi dalam kg CO₂e dari setiap gudang yang dibuka dan dari angkutan pada kedua tahap pengiriman.

### Faktor emisi

**Bukaan gudang · kg CO₂e per gudang yang dibuka**

| Gudang | Emisi tetap |
| --- | ---: |
| G1 | 12 |
| G2 | 20 |
| G3 | 8 |
| G4 | 24 |

**Angkut dari pabrik ke gudang · kg CO₂e per ton**

| Pabrik | G1 | G2 | G3 | G4 |
| --- | ---: | ---: | ---: | ---: |
| P1 | 1,4 | 1,8 | 1,5 | 1,3 |
| P2 | 1,6 | 2,1 | 3,9 | 4,4 |
| P3 | 1,2 | 3,1 | 0,8 | 2,1 |
| P4 | 1,8 | 1 | 3,5 | 4,4 |
| P5 | 3,8 | 3,5 | 1,1 | 3,5 |
| P6 | 4,1 | 3,5 | 1 | 2,9 |

**Angkut dari gudang ke zona pelanggan · kg CO₂e per ton**

| Gudang | K1 | K2 | K3 | K4 | K5 | K6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| G1 | 1,4 | 3,6 | 1,7 | 3,7 | 1,9 | 3,6 |
| G2 | 0,9 | 3,5 | 1,2 | 3,5 | 1,3 | 3,3 |
| G3 | 0,75 | 0,9 | 0,8 | 0,8 | 3,1 | 0,8 |
| G4 | 3,7 | 2 | 3,6 | 2,1 | 3,7 | 2,2 |

Sebagai contoh, satu ton minyak dari pabrik P1 melalui G1 ke K1 menghasilkan **1,4 + 1,4 = 2,8 kg CO₂e** dari angkutan. Jika G1 dibuka, tambahkan **12 kg CO₂e** satu kali untuk bukaan gudang.

### Prosedur Pareto

**Keputusan dan keluaran.** Cari kompromi antara biaya dan emisi. Tentukan 25 batas emisi berjarak sama, mulai dari emisi minimum hingga emisi pada solusi biaya terendah. Pada setiap ujung rentang, gunakan tujuan lain sebagai pemecah seri. Untuk setiap batas, cari biaya minimum, lalu pilih emisi terendah di antara solusi dengan biaya yang sama sesuai toleransi penyelesaian. Laporkan pasangan biaya–emisi dan gudang yang dibuka. Pada grafik Pareto, tampilkan titik yang tidak didominasi dan tampilkan setiap titik tersebut satu kali.

## P4. Biaya harapan dan emisi harapan

Gabungkan skenario dan keputusan buka gudang dari [P2](#p2-minimisasi-biaya-harapan) dengan tujuan emisi dan prosedur Pareto dari [P3](#p3-biaya-dan-emisi).

**Keputusan dan keluaran.** Hitung biaya harapan seperti pada P2. Hitung emisi harapan dengan menjumlahkan emisi tetap gudang yang dibuka dan rata-rata berbobot peluang dari emisi angkutan. Terapkan 25 batas pada emisi harapan. Pada setiap batas, minimalkan biaya harapan. Laporkan pasangan biaya harapan–emisi harapan, gudang yang dibuka, dan rencana kiriman per skenario untuk setiap solusi yang dilaporkan.

## P5. Minimisasi biaya dengan penanganan nonlinear

Gunakan [P1](#p1-minimisasi-biaya-dengan-permintaan-pasti) dengan biaya dan waktu penanganan gudang yang bertambah secara kuadratik. Aturan ini berlaku di keempat gudang untuk produk yang dapat ditangani. Hitung kuadrat tonase setiap produk secara terpisah pada setiap gudang. Pabrik tetap memiliki satu batas pasokan linear sebesar 8 ton untuk gabungan semua produk. Kalikan dengan **0,04** untuk mendapatkan tambahan biaya dan dengan **0,025** untuk mendapatkan tambahan jam kerja. Jumlahkan tambahannya dengan biaya penanganan dasar dan waktu dasar satu jam per ton. Terapkan batas tonase dan batas waktu pada setiap gudang.

Sebagai contoh, G3 menangani 10 ton sirup dan 8 ton susu. Waktunya adalah $18+0{,}025(10^2+8^2)=22{,}10$ jam. Volume 18 ton memenuhi kapasitas fisik G3, sedangkan waktu penanganannya melampaui batas 21,60 jam.

**Keputusan dan keluaran.** Minimalkan biaya total dengan tambahan biaya penanganan tersebut. Laporkan biaya total, gudang yang dibuka, dan jumlah kiriman pada setiap rute dan produk.

## P6. Biaya harapan dengan penanganan nonlinear

Gabungkan skenario permintaan dari [P2](#p2-minimisasi-biaya-harapan) dengan penanganan nonlinear dari [P5](#p5-minimisasi-biaya-dengan-penanganan-nonlinear).

**Keputusan dan keluaran.** Untuk setiap skenario, hitung tambahan biaya dan jam kerja dari tonase yang ditangani pada skenario itu. Periksa batas waktu di setiap gudang untuk ketiga skenario. Rata-ratakan biaya angkut dan penanganan dengan peluang skenario, lalu tambahkan biaya buka gudang satu kali. Laporkan biaya harapan minimum, gudang yang dibuka, dan rencana kiriman per skenario.

## P7. Biaya dan emisi dengan penanganan nonlinear

Gabungkan penanganan nonlinear dari [P5](#p5-minimisasi-biaya-dengan-penanganan-nonlinear) dengan tujuan emisi dan prosedur Pareto dari [P3](#p3-biaya-dan-emisi). Gunakan permintaan pasti dari P1.

**Keputusan dan keluaran.** Pada setiap batas emisi, minimalkan biaya total yang memuat tambahan biaya penanganan kuadratik. Periksa batas tonase dan waktu penanganan. Laporkan pasangan biaya–emisi dan gudang yang dibuka seperti pada P3.

## P8. Biaya harapan dan emisi harapan dengan penanganan nonlinear

Gunakan [P6](#p6-biaya-harapan-dengan-penanganan-nonlinear) untuk skenario permintaan, biaya harapan, dan batas waktu penanganan. Tambahkan emisi harapan dan prosedur Pareto dari [P4](#p4-biaya-harapan-dan-emisi-harapan).

**Keputusan dan keluaran.** Pada setiap batas emisi harapan, minimalkan biaya harapan dengan biaya penanganan kuadratik. Untuk setiap solusi, gunakan kombinasi gudang terbuka yang sama pada ketiga skenario. Hitung rencana kiriman dan periksa batas waktu penanganan di setiap skenario. Laporkan pasangan biaya harapan–emisi harapan, gudang yang dibuka, dan rencana kiriman per skenario untuk setiap solusi yang dilaporkan.

[Daftar rute per produk](Rute_Pengiriman.md) · [Ringkasan profil](Profil_P1_P8.md) · [Model matematika acuan](../math_model_acuan/Model_Matematika.md) · [Halaman utama](../README.md)
