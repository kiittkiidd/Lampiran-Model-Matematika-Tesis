# Kasus distribusi multiwilayah

Perusahaan menyalurkan minuman kemasan (A), pangan kering (B), dan produk dingin (C) melalui jaringan gudang. Setiap wilayah memiliki enam pabrik, empat calon gudang, dan enam pelanggan. Perusahaan memilih gudang dan menentukan jumlah kiriman untuk satu periode.

Setiap pabrik dan gudang melayani wilayahnya sendiri. Pelanggan suatu wilayah dilayani oleh fasilitas di wilayah tersebut. Keputusan di tiap wilayah diambil dengan aturan operasi yang sama. Biaya dan emisi perusahaan diperoleh dengan menjumlahkan hasil dari wilayah yang dilayani.

## Cakupan wilayah

![Cakupan wilayah. Low melayani wilayah 01. Medium melayani 01–04. High melayani 01–12. Wilayah 01 selalu memakai rute Low, wilayah 02–04 memakai rute Medium, dan wilayah 05–12 memakai rute High. Dua contoh kiriman menunjukkan P1 ke G2 ke K1 terpisah di wilayah 01 dan 02.](diagram/Diagram_Cakupan_Wilayah.svg)

Baca gambar dari atas. **Low** merencanakan satu wilayah. **Medium** tetap melayani wilayah 01 dan menambah 02–04. **High** mencakup keempat wilayah itu dan menambah 05–12. Warna menunjukkan tipe rute di dalam wilayah. Karena itu, kotak 01 tetap biru pada ketiga tingkat.

Bagian bawah menunjukkan contoh pengiriman produk A. **01–G2 dan 02–G2 adalah dua gudang berbeda.** Di sebelah kiri, kiriman berjalan dari pabrik 01–P1 ke gudang 01–G2 lalu ke pelanggan 01–K1. Di sebelah kanan, pesanan 02–K1 dipenuhi dari fasilitas wilayah 02. Perusahaan menjumlahkan biaya dan emisi dari wilayah yang masuk dalam rencana.

## Data permintaan dan biaya

**Instans** berarti satu paket angka yang mendeskripsikan seluruh wilayah, misalnya angka pesanan dan ongkos kirim pada paket 8201. Dalam paket yang sama, data Wilayah 01 sama untuk Low, Medium, dan High. Pengujian memakai sepuluh paket data dengan kode 8201–8210.

Tabel berikut adalah data dasar per wilayah. Untuk tiap paket dan wilayah, kode pembangkit memberi perubahan hingga 5% pada biaya buka dan hingga 3% pada tarif angkut. Permintaan berubah sedikit antarpelanggan dengan total per produk tetap. Pembangkit mengurangi rata-rata variasi per produk dari setiap perubahan agar totalnya tetap sama. Kapasitas, rute yang diizinkan, dan faktor emisi ditetapkan oleh desain. Semua profil memakai input wilayah yang sama. [Data dasar](Data_Bersama.json) · [Kode pembangkit](../math_model_acuan/benchmark_wilayah.py)

## Aturan operasi

- **Kapasitas pabrik.** Masing-masing pabrik dapat mengirim paling banyak 8 palet, dijumlahkan untuk seluruh gudang dan produk. Kiriman boleh berupa pecahan palet. Contohnya, pabrik yang telah mengirim 5,5 palet dapat mengirim hingga 2,5 palet lagi.
- **Pembukaan gudang.** Setiap lokasi dipilih untuk dibuka atau ditutup. Lokasi yang dipilih membayar biaya buka satu kali dan bisa menyalurkan barang dalam batas kapasitas fisik dan waktu penanganannya. Lokasi yang ditutup memiliki arus masuk dan keluar sebesar nol.
- **Keseimbangan gudang.** Untuk setiap gudang dan produk, semua barang yang masuk disalurkan di periode yang sama. Jika G2 menerima enam palet A, G2 menyalurkan tepat enam palet A. Barang masuk seluruhnya berasal dari pabrik dalam jaringan.
- **Pemenuhan pesanan.** Jumlah palet yang diterima setiap pelanggan untuk setiap produk harus tepat sebesar pesanannya. Pesanan bisa dibagi ke beberapa gudang. Contohnya, K1 dapat menerima satu palet A dari G1 dan dua palet A dari G2 untuk memenuhi tiga palet A.
- **Tarif.** Biaya angkut dikenakan pada kedua tahap. Setiap palet dikenai biaya penanganan sekali di gudang yang menyalurkannya. Semua tarif dan biaya tetap memakai satuan biaya yang sama.

Sebagai contoh, menggunakan tarif dasar jaringan lokal Low, satu palet A dapat bergerak dari pabrik P1 ke G2 lalu ke K1. Biaya angkutnya 3 pada tahap pertama dan 1 pada tahap kedua. Biaya penanganan dasar di G2 adalah 2, sehingga biaya dasar rute itu 6 per palet. Biaya buka G2 dihitung satu kali untuk seluruh arusnya. Profil nonlinear juga mengenakan biaya tambahan berdasarkan volume produk yang ditangani gudang.

| Gudang | Kapasitas (palet) | Biaya buka |
| --- | ---: | ---: |
| G1 | 16 | 25 |
| G2 | 20 | 31 |
| G3 | 18 | 28 |
| G4 | 14 | 17 |

## Rincian rute dalam satu wilayah

Jaringan lokal Low menyediakan 16 rute masuk dan 31 rute keluar. Jaringan lokal Medium menyediakan 22 rute masuk dan 40 rute keluar, termasuk layanan A dari G1 ke K2–K6 dan layanan C dari G3 ke K1, K3, K5, dan K6. High menyediakan 34 rute masuk dan 54 rute keluar, termasuk penyaluran C melalui G4 ke K2, K4, dan K6. Rute yang sudah tersedia ikut dibawa ke tingkat berikutnya. Satu rute dihitung untuk satu produk. Tabel rute dan diagram di bawah menunjukkan jaringan lokal untuk satu wilayah.


**Pola garis**

- A · Minuman kemasan · garis penuh
- B · Pangan kering · garis putus-putus
- C · Produk dingin · garis titik-titik

Setiap panah menunjukkan satu jalur aktif untuk produk di panelnya. Kode fasilitas yang sama di beberapa panel merujuk pada lokasi fisik yang sama.

<details>
<summary>Lihat diagram rute di dalam satu wilayah</summary>

**Wilayah 01 · rute lokal Low**

![Rute produk A, B, dan C di satu wilayah dengan tipe Low](diagram/Jaringan_Low.svg)

**Wilayah 02–04 · rute lokal Medium**

![Rute produk A, B, dan C di satu wilayah dengan tipe Medium](diagram/Jaringan_Medium.svg)

**Wilayah 05–12 · rute lokal High**

![Rute produk A, B, dan C di satu wilayah dengan tipe High](diagram/Jaringan_High.svg)

</details>

Pada tabel masuk, setiap pabrik pada satu baris produk boleh memasok setiap gudang pada baris tersebut. Tabel keluar menyebut pelanggan yang dapat dilayani untuk setiap gudang dan produk. Tanda — berarti jalur belum tersedia.

| Tingkat | Produk | Pabrik pemasok | Gudang penerima |
| --- | --- | --- | --- |
| Low | A | P1, P5 | G1, G2, G4 |
| Low | B | P2, P3 | G1, G3, G4 |
| Low | C | P4, P6 | G2, G3 |
| Medium | A | P1, P5 | G1, G2, G4 |
| Medium | B | P1, P2, P3 | G1, G2, G3, G4 |
| Medium | C | P4, P6 | G2, G3 |
| High | A | P1, P3, P5 | G1, G2, G3, G4 |
| High | B | P1, P2, P3, P4 | G1, G2, G3, G4 |
| High | C | P4, P6 | G2, G3, G4 |

| Gudang | Produk | Low | Medium | High |
| --- | --- | --- | --- | --- |
| G1 | A | K1 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G1 | B | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G2 | A | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G2 | B | — | — | K1, K3, K5 |
| G2 | C | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G3 | A | — | — | K1, K3, K5 |
| G3 | B | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G3 | C | K2, K4 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G4 | A | K2 | K2 | K2, K4, K6 |
| G4 | B | K2, K4, K6 | K2, K4, K6 | K1, K2, K3, K4, K5, K6 |
| G4 | C | — | — | K2, K4, K6 |

## Permintaan per pelanggan

Tabel dalam palet menunjukkan permintaan dasar sebelum perubahan antarwilayah. Pada profil deterministik seluruh permintaan wilayah diketahui. Pada profil stokastik pesanan A di K1 memiliki [tiga kondisi](Profil_P1_P8.md#kapan-permintaan-diketahui) di sekitar angka permintaan wilayahnya.

| Pelanggan | A | B | C | Total |
| --- | ---: | ---: | ---: | ---: |
| K1 | 3 | 1 | 1 | 5 |
| K2 | 3 | 1 | 1 | 5 |
| K3 | 1 | 3 | 1 | 5 |
| K4 | 1 | 3 | 1 | 5 |
| K5 | 1 | 1 | 3 | 5 |
| K6 | 1 | 1 | 3 | 5 |
| **Total** | 10 | 10 | 10 | 30 |

## Tarif per palet

Tarif angkut berlaku untuk seluruh produk pada satu pasangan lokasi. Pemakaian tarif tetap mengikuti jalur aktif pada level yang dipilih. Data tarif benchmark bersifat sintetis.

### Angkut pabrik ke gudang

| Pabrik | G1 | G2 | G3 | G4 |
| --- | ---: | ---: | ---: | ---: |
| P1 | 2 | 3 | 7 | 8 |
| P2 | 3 | 4 | 7 | 8 |
| P3 | 7 | 6 | 2 | 3 |
| P4 | 2 | 2 | 7 | 8 |
| P5 | 7 | 6 | 3 | 2 |
| P6 | 7 | 6 | 2 | 3 |

### Angkut gudang ke pelanggan

| Gudang | K1 | K2 | K3 | K4 | K5 | K6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| G1 | 2 | 7 | 2 | 7 | 3 | 7 |
| G2 | 1 | 7 | 2 | 7 | 2 | 6 |
| G3 | 7 | 2 | 7 | 2 | 6 | 2 |
| G4 | 7 | 1,79 | 6 | 2 | 7 | 2 |

### Penanganan di gudang

| Gudang | A | B | C |
| --- | ---: | ---: | ---: |
| G1 | 1 | 1 | — |
| G2 | 2 | 2 | 3 |
| G3 | 2 | 1 | 2 |
| G4 | 1 | 1 | 3 |

[Data dasar](Data_Bersama.json) · [Delapan profil](Profil_P1_P8.md) · [Kembali ke daftar isi](../README.md)
