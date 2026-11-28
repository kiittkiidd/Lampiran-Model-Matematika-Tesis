# Penyesuaian data sebelum pembekuan

Kalibrasi mempertajam pilihan antara biaya dan emisi serta membuat perluasan rute Medium lebih bertahap. Semua pengukuran utama dilakukan ulang setelah data dan representasi SCIP ditetapkan.

## Tarif dan emisi

| Parameter | Sebelumnya | Versi acuan |
| --- | --- | --- |
| Tarif angkut P5 → G3 per ton | 3,12 | 4,23 |
| Tarif angkut P6 → G3 per ton | 2,57 | 3,04 |
| Emisi tetap G1 | 12,00 | 25,00 |
| Emisi angkut P1 → G1 per ton | 1,40 | 5,00 |
| Emisi angkut P4 → G1 per ton | 1,80 | 4,50 |
| Emisi angkut P3 → G3 per ton | 0,80 | 2,40 |
| Emisi angkut P5 → G3 per ton | 1,10 | 0,70 |

Pada High, G3 dapat memilih pemasok susu dengan tarif/emisi P3 sebesar 2,24/2,40, P6 sebesar 3,04/1,00, atau P5 sebesar 4,23/0,70. Pilihan yang lebih bersih mempunyai tarif lebih tinggi.

## Perluasan rute

Medium memakai semua rute Low dan enam rute keluar tambahan berikut.

| Gudang | Zona | Produk |
| --- | --- | --- |
| G2 | K1 | C |
| G2 | K2 | B |
| G2 | K2 | C |
| G2 | K3 | C |
| G2 | K4 | A |
| G2 | K6 | A |

Jumlah rute masuk adalah 16/17/22 dan rute keluar 36/42/60 untuk Low/Medium/High. Pada High, empat rute masuk diganti untuk menyediakan pilihan pemasok P5 dan P6 menuju G3: P5–G3 untuk A dan C, serta P6–G3 untuk B dan C. Jumlah rute masuk High tetap 22. Daftar rute lengkap tercantum pada dokumen kasus.

Permintaan dasar, distribusi dan peluang skenario, kapasitas gudang, waktu tersedia, biaya buka, tarif penanganan, serta koefisien biaya dan waktu kuadratik dipertahankan. Batas pasokan pabrik tidak digunakan dalam versi kasus yang disepakati.

## Representasi solver

Seluruh profil memakai definisi tonase yang sama. Profil nonlinear menambahkan epigraf kuadrat yang setara dengan rumus bisnis. Proyeksi ke keputusan kiriman tidak berubah. WCC tetap dihitung pada representasi bisnis acuan; solusi diperiksa kembali terhadap persamaan aslinya.
