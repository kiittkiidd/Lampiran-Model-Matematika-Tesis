# Profil 1 — Model acuan linear deterministik

Model memilih gudang yang dibuka dan arus pengiriman dengan biaya total minimum. Gunakan [kasus P1](../../case/P1/Kasus.md), [audit WCC](Audit_WCC.md), dan [hasil verifikasi](../Hasil_Benchmark.md).

## 1. Jaringan dan penetapan tingkat

Untuk setiap tingkat, gunakan rute masuk dan keluar pada tabel kasus. Low, Medium, dan High mempunyai fasilitas serta permintaan yang sama. Perluasan jaringan mempertahankan rute yang sudah ada. Arus pada rute baru boleh bernilai nol, sehingga solusi lama tetap layak pada tingkat berikutnya.

| Tingkat | Rute pabrik–gudang | Rute gudang–pelanggan |
| --- | ---: | ---: |
| Low | 16 | 31 |
| Medium | 22 | 40 |
| High | 34 | 54 |

## 2. Data dan notasi

| Entitas | Barat | Timur |
| --- | --- | --- |
| Pabrik | P1, P2, P4 | P3, P5, P6 |
| Gudang | G1, G2 | G3, G4 |
| Pelanggan | K1, K3, K5 | K2, K4, K6 |

| Gudang | Kapasitas gabungan (palet) | Biaya buka per periode |
| --- | ---: | ---: |
| G1 | 16 | 25 |
| G2 | 20 | 31 |
| G3 | 18 | 28 |
| G4 | 14 | 17 |

Diagram dasar memberi kapasitas 8 palet per pabrik. Formulasi ini memakai **8 palet sebagai kapasitas bersama di ketiga tingkat**. Untuk pabrik multiproduk, seluruh produk memakai kapasitas yang sama secara gabungan.

Setiap pelanggan membutuhkan lima palet, sehingga total sistem 30 palet. Untuk setiap pelanggan dan produk, permintaan $d_{jp}$ mengambil angka yang sama di Low, Medium, dan High. Tarif angkut, penanganan, dan permintaan lengkap tersedia di [kasus P1](../../case/P1/Kasus.md) dan [data bersama](../../case/Data_Bersama.json).

| Notasi | Arti |
| --- | --- |
| $i,g,j,p$ | Indeks pabrik, gudang, pelanggan, dan produk |
| $\ell$ | Tingkat L, M, atau H |
| $E_{\ell}^{\mathrm{in}}$ | Himpunan tripel $(i,g,p)$ yang diizinkan sesuai [tabel jaringan](../../case/P1/Kasus.md#jalur-masuk-dan-keluar) |
| $E_{\ell}^{\mathrm{out}}$ | Himpunan tripel $(g,j,p)$ yang diizinkan sesuai [tabel jaringan](../../case/P1/Kasus.md#jalur-masuk-dan-keluar) |
| $C_i$ | Kapasitas total pabrik $i$, dalam palet |
| $U_g,F_g$ | Kapasitas total dan biaya buka tetap gudang $g$ per periode |
| $d_{jp}$ | Permintaan pelanggan $j$ untuk produk $p$ dalam palet |

Notasi untuk tarif ketiga jenis kegiatan adalah sebagai berikut.

```math
\begin{aligned}
c_{i,g,p}^{\mathrm{in}}&\quad\text{tarif angkut per palet dari pabrik }i\text{ ke gudang }g,\\
c_{g,j,p}^{\mathrm{out}}&\quad\text{tarif angkut per palet dari gudang }g\text{ ke pelanggan }j,\\
h_{g,p}&\quad\text{tarif penanganan per palet produk }p\text{ di gudang }g.
\end{aligned}
```

| Variabel keputusan | Makna | Domain |
| --- | --- | --- |
| $x_{i,g,p}$ | Palet produk $p$ dari pabrik $i$ ke gudang $g$ | Kontinu nonnegatif pada $E_{\ell}^{\mathrm{in}}$ |
| $z_{g,j,p}$ | Palet produk $p$ dari gudang $g$ ke pelanggan $j$ | Kontinu nonnegatif pada $E_{\ell}^{\mathrm{out}}$ |
| $y_g$ | Status buka gudang $g$ | Biner, dengan 1 untuk buka dan 0 untuk tutup |

Sebagai contoh, $x_{1,2,A}$ mengukur kiriman A dari P1 ke G2 dan $z_{2,1,A}$ mengukur kiriman A dari G2 ke K1. Keduanya dihitung dalam neraca A di G2.

## 3. Fungsi tujuan dan seluruh keluarga kendala

### Fungsi tujuan — biaya buka, angkut, dan penanganan minimum

```math
\min\quad
\sum_g F_g y_g
+\sum_{(i,g,p)\in E_{\ell}^{\mathrm{in}}} c_{i,g,p}^{\mathrm{in}}x_{i,g,p}
+\sum_{(g,j,p)\in E_{\ell}^{\mathrm{out}}} c_{g,j,p}^{\mathrm{out}}z_{g,j,p}
+\sum_{(g,j,p)\in E_{\ell}^{\mathrm{out}}} h_{g,p}z_{g,j,p}.
```

Biaya buka dibayar sekali untuk tiap gudang. Biaya angkut dihitung per palet pada dua tahap pengiriman. Biaya penanganan mencakup kegiatan gudang seperti pemindahan dan penyortiran. Biaya ini dibebankan sekali per palet yang melewati gudang. Sebagai contoh, membuka G2 menambah biaya tetap 31 dan menyalurkan lima palet A dari G2 ke K1 menambah $5c_{2,1,A}^{\mathrm{out}}$ untuk angkut serta $5h_{2,A}$ untuk penanganan. Karena biaya penanganan memakai $z_{g,j,p}$ yang sudah tersedia, penambahan biaya ini mempertahankan jumlah variabel dan kendala.

### K1 — kapasitas pabrik — R1 sampai R6

```math
\sum_{(g,p):(i,g,p)\in E_{\ell}^{\mathrm{in}}} x_{i,g,p} \le C_i
\qquad \text{untuk tiap pabrik }i.
```

Untuk satu $i$ yang tetap, jumlahkan kiriman ke semua gudang dan untuk semua produk yang bisa dibuat pabrik itu. Di Low, R1 adalah $x_{1,1,A}+x_{1,2,A}+x_{1,4,A}\le 8$. Jika P1 mengirim 5 palet ke G2, masih ada 3 palet kapasitas untuk semua kiriman P1 lainnya.

### K2 — neraca arus gudang per produk — R7 sampai R17

```math
\sum_{i:(i,g,p)\in E_{\ell}^{\mathrm{in}}} x_{i,g,p}
=
\sum_{j:(g,j,p)\in E_{\ell}^{\mathrm{out}}} z_{g,j,p}
\qquad \text{untuk tiap pasangan }(g,p)\text{ dalam jaringan acuan}.
```

Untuk satu gudang dan produk, jumlah barang masuk sama dengan jumlah barang keluar pada periode yang sama. Di Low, R7 adalah $x_{1,1,A}+x_{5,1,A}=z_{1,1,A}$. Jika G1 menerima 2 palet A, dua palet itu harus dikirim ke K1. Daftar acuan berisi 11 pasangan gudang–produk. G1–C berada di luar daftar karena G1 tidak menangani C pada ketiga tingkat.

### K3 — pemenuhan permintaan pelanggan per produk — R18 sampai R35

```math
\sum_{g:(g,j,p)\in E_{\ell}^{\mathrm{out}}} z_{g,j,p}
=d_{jp}
\qquad \text{untuk tiap pasangan }(j,p).
```

Untuk satu pelanggan dan produk, kiriman dari gudang yang melayaninya harus berjumlah tepat sebesar permintaan. Di Low, R18 adalah $z_{1,1,A}+z_{2,1,A}=3$. Tiga palet A untuk K1 dapat dikirim dari G1, dari G2, atau dibagi di antara keduanya.

### K4 — kapasitas dan keputusan buka gudang — R36 sampai R39

```math
\sum_{(j,p):(g,j,p)\in E_{\ell}^{\mathrm{out}}} z_{g,j,p}
\le U_gy_g
\qquad \text{untuk tiap gudang }g.
```

Saat $y_g=0$, semua kiriman keluar nol karena variabel arus nonnegatif. K2 kemudian membuat arus masuk gudang juga nol. Saat $y_g=1$, gudang dapat menyalurkan sampai $U_g$ palet untuk seluruh produknya. Dalam contoh Low, G2 bisa menyalurkan 10 palet A dan 5 palet C, sehingga memakai 15 dari 20 palet kapasitasnya.

### Kendala domain variabel

```math
\begin{aligned}
x_{i,g,p} &\in \mathbb{R}_{\ge 0} &&\forall (i,g,p)\in E_{\ell}^{\mathrm{in}},\\
z_{g,j,p} &\in \mathbb{R}_{\ge 0} &&\forall (g,j,p)\in E_{\ell}^{\mathrm{out}},\\
y_g &\in \{0,1\} &&\forall g.
\end{aligned}
```

Arus kiriman kontinu dan nonnegatif. Keputusan buka gudang biner. Audit WCC menggunakan baris fungsional R1–R39 pada setiap blok.

Satu rencana layak Low menggunakan G2 dan G3. Kirim masing-masing 5 palet melalui jalur P1–G2–K1 (A), P5–G2–K2 (A), P2–G3–K3 (B), P3–G3–K4 (B), P4–G2–K5 (C), dan P6–G3–K6 (C). G2 dan G3 masing-masing menangani 15 palet dan setiap pabrik mengirim 5 palet.

## 4. Verifikasi solusi

Empat keputusan buka/tutup menghasilkan 16 kombinasi gudang. Tetapkan satu kombinasi, cari arus termurah dengan program linear, dan bandingkan semua pola yang layak. Notebook mencocokkan optimum enumerasi dengan optimum MILP serta mengaudit semua pasangan R1–R39.

[Notebook verifikasi](../Verifikasi_P1_P2_P3.ipynb) · [Buka di Google Colab](https://colab.research.google.com/github/kiittkiidd/Lampiran-Model-Matematika-Tesis/blob/main/math_model_acuan/Verifikasi_P1_P2_P3.ipynb)
