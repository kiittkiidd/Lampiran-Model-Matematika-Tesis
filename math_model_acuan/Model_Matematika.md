# Model matematika acuan

Kasus memilih gudang dan membagi kiriman dari pabrik ke gudang dan dari gudang ke pelanggan. Operasi tiap wilayah berjalan secara lokal. Perusahaan menjumlahkan biaya dan emisi seluruh wilayah aktif. [Kasus dan tabel data](../case/Kasus_Dasar.md)

## Variabel dan kondisi permintaan

Untuk satu wilayah, indeks i, g, j, p, dan s masing-masing menunjukkan pabrik, gudang, pelanggan, produk, dan kondisi permintaan. Variabel arus hanya dibuat untuk rute yang aktif.

| Variabel | Arti |
| --- | --- |
| x | Palet produk p dari pabrik i menuju gudang g pada kondisi s |
| z | Palet produk p dari gudang g menuju pelanggan j pada kondisi s |
| y | Keputusan membuka gudang g. Nilainya 1 atau 0 dan berlaku untuk seluruh kondisi wilayah tersebut |

Arus x dan z boleh pecahan dan nonnegatif. Pada profil pasti, terdapat satu kondisi berbobot 1. Pada profil stokastik, tiga blok arus memiliki keputusan gudang yang sama. [Peluang masing-masing kondisi](../case/Profil_P1_P8.md#kapan-permintaan-diketahui)

## Kendala operasi per wilayah

Gunakan hanya variabel pada rute aktif di setiap penjumlahan.

1. **Kapasitas pabrik.**

```math
\sum_{g,p}x_{i,g,p,s}\le C_i.
```

Jika pabrik mengirim 5,5 palet dari kapasitas 8, kapasitas tersisa 2,5 palet pada kondisi itu.

2. **Neraca barang di gudang.**

```math
\sum_i x_{i,g,p,s}=\sum_j z_{g,j,p,s}.
```

Hitung neraca per produk. Enam palet A yang masuk ke G2 harus sama dengan enam palet A yang keluar dari G2.

3. **Pemenuhan pesanan.**

```math
\sum_g z_{g,j,p,s}=d_{j,p,s}.
```

Jika pelanggan perlu tiga palet produk A, beberapa gudang bisa membagi pesanan, misalnya satu dan dua palet.

4. **Kapasitas fisik gudang.**

```math
\sum_{j,p}z_{g,j,p,s}\le U_g y_g.
```

Saat gudang G2 dibuka, kapasitasnya 20 palet. Saat ditutup, ruas kanan nol. Neraca membuat arus masuk dan keluar sama-sama nol.

5. **Anggaran waktu penanganan.**

```math
Q_{g,p,s}=\sum_j z_{g,j,p,s},\qquad
\sum_p\left(Q_{g,p,s}+\beta Q_{g,p,s}^2\right)\le T_g y_g.
```

Q adalah volume produk yang ditangani. Koefisien beta adalah nol pada profil linear dan 0,025 pada profil nonlinear. Jika G2 menyalurkan masing-masing 10 palet A dan C, kebutuhan waktunya 20 unit pada profil linear dan 25 unit pada profil nonlinear.

## Biaya dan emisi

```math
\begin{aligned}
C_r &= \sum_g F_g y_g +
 \sum_s \pi_s\left(\sum_{i,g,p}c^{\mathrm{in}}_{i,g}x_{i,g,p,s}
 + \sum_{g,j,p}(c^{\mathrm{out}}_{g,j}+h_{g,p})z_{g,j,p,s}
 +\alpha\sum_{g,p} Q_{g,p,s}^2\right),\\
E_r &= \sum_g \kappa_g y_g +
 \sum_s \pi_s\left(\sum_{i,g,p}e^{\mathrm{in}}_{i,g}x_{i,g,p,s}
 + \sum_{g,j,p}e^{\mathrm{out}}_{g,j}z_{g,j,p,s}\right).
\end{aligned}
```

Untuk wilayah r, biaya terdiri dari biaya buka F, tarif angkut dan penanganan, serta biaya tambahan padatnya penanganan. Nilai alpha adalah nol pada profil linear dan 0,04 pada profil nonlinear. Emisi terdiri dari emisi tetap gudang yang dibuka dan emisi angkutan. Bobot kondisi pi dipakai pada biaya dan emisi operasional.

Untuk profil biaya tunggal, minimalkan jumlah C di seluruh wilayah. Untuk profil dua tujuan, selesaikan lima optimisasi berikut dengan bobot lambda tetap.

```math
\min\ \sum_r\left(\lambda\frac{C_r}{300}+(1-\lambda)\frac{E_r}{150}\right),\qquad
\lambda\in\{0.15,0.325,0.5,0.675,0.85\}.
```

Pembagi 300 dan 150 adalah skala tetap biaya dan emisi. Bobot 0,85 memberi prioritas lebih besar pada biaya setelah dinormalisasi. Penyampelan dengan bobot positif menargetkan titik Pareto yang didukung pembobotan. Titik efisien lain bisa berada di antara atau di luar lima hasil tersebut, terutama ketika ada keputusan biner. [Das & Dennis, 1997](https://doi.org/10.1007/BF01197559)

## Penyelesaian dan verifikasi

Himpunan kendala wilayah terpisah. Untuk setiap bobot, minimum jumlah fungsi wilayah sama dengan jumlah minimum fungsi tiap wilayah. Menggabungkan solusi lokal menghasilkan rencana tingkat perusahaan dan menjumlahkan batas bawahnya. Jadi kode memecahkan satu model per wilayah aktif dan menggabungkan hasilnya. Ini adalah **pemecahan eksak menurut struktur wilayah**, dengan toleransi numerik solver.

Untuk suku kuadratik konveks, kode membatasi fungsi kuadrat dari bawah dengan garis singgung. Kode kemudian memeriksa solusi pada persamaan kuadratik asli, memeriksa pilihan gudang biner, dan membandingkan nilai solusi dengan batas bawah sebelum menerimanya. [Bonami dkk., 2008](https://doi.org/10.1016/j.disopt.2006.10.011)

**Presolve** adalah pemeriksaan awal HiGHS yang menyederhanakan persamaan sebelum pencarian. Misalnya, variabel yang nilainya sudah pasti bisa digantikan nilainya. Model awal dan solusi yang dikembalikan tetap mengikuti aturan bisnis yang sama. Pengujian operasi perusahaan memakai konfigurasi presolve bawaan HiGHS di semua tingkat. [Panduan HiGHS](https://ergo-code.github.io/HiGHS/dev/guide/further/#presolve)

[Baca perhitungan WCC](../Lampiran_WCC.md) · [Hasil benchmark](Hasil_Verifikasi.md)
