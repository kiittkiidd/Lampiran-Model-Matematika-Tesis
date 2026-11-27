# Delapan profil perencanaan

Masing-masing profil dikerjakan pada jaringan Low, Medium, dan High. Gunakan rute, kapasitas, dan data tiap wilayah dari [Kasus dasar](Kasus_Dasar.md). Tabel berikut menunjukkan perbedaan antarprofil.

| Profil | Kapan permintaan diketahui | Yang hendak diminimalkan | Penanganan di gudang |
| --- | --- | --- | --- |
| P1 | Pasti sejak awal | Biaya total | Linear |
| P2 | Setelah memilih gudang | Biaya harapan | Linear |
| P3 | Pasti sejak awal | Biaya total dan emisi total | Linear |
| P4 | Setelah memilih gudang | Biaya harapan dan emisi harapan | Linear |
| P5 | Pasti sejak awal | Biaya total | Nonlinear |
| P6 | Setelah memilih gudang | Biaya harapan | Nonlinear |
| P7 | Pasti sejak awal | Biaya total dan emisi total | Nonlinear |
| P8 | Setelah memilih gudang | Biaya harapan dan emisi harapan | Nonlinear |

## Kapan permintaan diketahui?

**P1, P3, P5, dan P7.** Seluruh angka pesanan sudah diketahui saat perencanaan. Perusahaan memilih gudang dan menyusun satu rencana pengiriman menggunakan pesanan wilayah tersebut.

**P2, P4, P6, dan P8.** Perusahaan memilih lokasi yang akan dibuka sebelum mengetahui permintaan aktual. Di setiap wilayah, hanya pesanan produk A di K1 yang belum pasti. Siapkan satu rencana pengiriman untuk masing-masing kondisi di tabel. Ketika permintaan diketahui, perusahaan menjalankan rencana yang sesuai dengan kondisi tersebut. Lokasi yang dibuka tetap sama pada ketiga kondisi. Kapasitas dan anggaran waktu harus terpenuhi untuk setiap kondisi secara terpisah.

| Kondisi | Peluang | Pesanan A di K1 (palet) | Total kebutuhan jaringan (palet) |
| --- | ---: | ---: | ---: |
| Sepi | 15,8655% | 1,474865 | 28,474865 |
| Sedang | 68,2689% | 3 | 30 |
| Ramai | 15,8655% | 4,525135 | 31,525135 |

Tiga kondisi mewakili bagian bawah, tengah, dan atas distribusi normal dengan simpangan baku 1 palet. Angka pada tabel memakai contoh rata-rata 3 palet. Untuk wilayah dengan rata-rata 3,1, tiga nilainya bergeser menjadi sekitar 1,575, 3,1, dan 4,625 palet. Peluang tetap. Satu keputusan gudang dipakai di semua kondisi pada wilayah tersebut.

Biaya harapan diperoleh dengan mengalikan biaya operasi tiap kondisi dengan peluangnya, lalu menjumlahkan hasilnya dan menambahkan biaya pembukaan gudang satu kali. Misalnya, jika biaya operasi dalam tiga kondisi sebesar 80, 100, dan 120, biaya operasi harapan adalah sekitar 100. Jika seluruh gudang terpilih memiliki biaya buka gabungan 45, biaya total harapan menjadi sekitar 145. Emisi harapan memakai cara yang sama, dengan emisi tetap gudang dihitung satu kali pada rencana yang dipilih.

## Bagaimana barang ditangani di gudang?

Kapasitas fisik dalam palet dan anggaran waktu berikut berlaku pada seluruh profil. Setiap gudang yang buka memperoleh anggaran waktunya untuk satu periode.

| Gudang | Anggaran waktu penanganan |
| --- | ---: |
| G1 | 19,2 |
| G2 | 24 |
| G3 | 21,6 |
| G4 | 16,8 |

- **Linear.** Setiap palet membutuhkan satu satuan waktu penanganan. Biaya dasar penanganan mengikuti tarif per palet untuk produk dan gudang yang bersangkutan.
- **Nonlinear.** Hitung total palet setiap produk yang disalurkan gudang. Untuk setiap produk, kuadratkan total paletnya. Tambahkan 0,025 kali hasil kuadrat ke waktu penanganan dan 0,04 kali hasil kuadrat ke biaya. Setelah itu, jumlahkan kontribusi semua produk pada gudang tersebut. Lakukan hitungan terpisah untuk setiap gudang dan kondisi permintaan.

Contohnya, G2 menyalurkan 10 palet A dan 10 palet C. Volume 20 palet tepat memenuhi kapasitas fisik G2. Secara linear, gudang memakai 20 satuan waktu. Secara nonlinear, tambahan waktu dari A sebesar 2,5 dan dari C sebesar 2,5, sehingga totalnya 25 satuan waktu. Anggaran G2 adalah 24, jadi rencana itu harus disesuaikan pada profil nonlinear. Biaya penanganan dasarnya 50, sedangkan biaya tambahannya 8 pada profil nonlinear.

## Emisi angkutan dan gudang

Emisi menggunakan satuan kilogram setara karbon dioksida (kg CO₂e). Tarif angkutan berikut berlaku per palet pada rute yang aktif untuk tiap produk.

### Pabrik ke gudang

| Pabrik | G1 | G2 | G3 | G4 |
| --- | ---: | ---: | ---: | ---: |
| P1 | 1,4 | 1,8 | 4,2 | 4,7 |
| P2 | 1,6 | 2,1 | 3,9 | 4,4 |
| P3 | 3,6 | 3,1 | 0,8 | 2,1 |
| P4 | 1,8 | 1,0 | 3,5 | 4,4 |
| P5 | 3,8 | 3,5 | 1,1 | 3,5 |
| P6 | 4,1 | 3,5 | 1,0 | 2,9 |

### Gudang ke pelanggan

| Gudang | K1 | K2 | K3 | K4 | K5 | K6 | Emisi tetap jika buka (kg CO₂e) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| G1 | 1,4 | 3,6 | 1,7 | 3,7 | 1,9 | 3,6 | 12 |
| G2 | 0,9 | 3,5 | 1,2 | 3,5 | 1,3 | 3,3 | 20 |
| G3 | 3,5 | 0,9 | 3,2 | 0,8 | 3,1 | 0,8 | 8 |
| G4 | 3,7 | 2,0 | 3,6 | 2,1 | 3,7 | 2,2 | 24 |

Satu palet yang dikirim P1 melalui G2 ke K1 menimbulkan 1,8 + 0,9 = 2,7 kg CO₂e dari angkutan. Emisi tetap G2 sebesar 20 kg CO₂e ditambahkan satu kali apabila G2 dibuka.

## Keputusan yang perlu dilaporkan

- **Profil satu tujuan.** Laporkan fasilitas terpilih, arus pengiriman, dan total biaya minimum. Untuk profil stokastik, laporkan arus tiap kondisi serta biaya harapan.
- **Profil dua tujuan.** Perusahaan ingin menyeimbangkan biaya dan emisi. Gunakan lima bobot biaya yang sama pada semua tingkat, yaitu 0,15, 0,325, 0,50, 0,675, dan 0,85. Pada setiap bobot, laporkan total biaya dan emisi untuk gabungan wilayah. [Rumus dan interpretasi bobot](../math_model_acuan/Model_Matematika.md#biaya-dan-emisi)

[Kasus dasar](Kasus_Dasar.md) · [Daftar isi](../README.md)
