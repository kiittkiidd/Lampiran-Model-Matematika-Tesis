# Cara menghitung WCC di PT XYZ

Bayangkan gudang G1 akan mengirim sirup ke K1. **Rute yang sama tertulis di dua aturan.**

| Aturan | Apa yang diperiksa? |
| --- | --- |
| **R8 · Aturan sirup** | Jumlah sirup yang masuk ke G1 harus sama dengan jumlah sirup yang dikirim keluar dari G1. |
| **R36 · Aturan gudang** | Semua barang yang dikirim keluar dari G1, termasuk sirup, ikut memakai batas 16 ton. |

Sirup **G1 → K1** muncul di kedua aturan. Jadi, saat membandingkan dua aturan ini, rute G1 → K1 mendapat **1 poin**. Kiriman sirup ke tujuan lain diperiksa dengan cara yang sama.

## 1. Hitung poin untuk dua aturan ini

PT XYZ punya enam zona tujuan, K1 sampai K6. **Low** membolehkan gudang G1 mengirim sirup ke tiga zona. **Medium** menambah tiga zona. Untuk membandingkan keduanya, penelitian memakai **daftar pembanding** yang berisi keenam zona.

| Tujuan kiriman sirup dari G1 | Low | Medium | Daftar pembanding |
| --- | ---: | ---: | ---: |
| K1 | 1 | 1 | 1 |
| **K2** | 0 | **1** | 1 |
| K3 | 1 | 1 | 1 |
| **K4** | 0 | **1** | 1 |
| K5 | 1 | 1 | 1 |
| **K6** | 0 | **1** | 1 |
| **Jumlah poin** | **3** | **6** | **6** |

**1** berarti rute itu tertulis di kedua aturan. **0** berarti rute itu belum tersedia di tingkat tersebut. Lihat baris **K2**. Pada Low, G1 belum boleh mengirim sirup ke K2, jadi poinnya 0. Pada Medium, rute itu ditambahkan dan tertulis di kedua aturan, jadi poinnya 1. Tiga tujuan yang ditebalkan memberi **3 poin tambahan**.

Untuk **dua aturan ini**, Low mendapat **3 dari 6 poin atau 50%**, dan Medium mendapat **6 dari 6 poin atau 100%**. Bagi poin yang didapat dengan poin pembanding. Untuk Low, hitung **3 ÷ 6**. Untuk Medium, hitung **6 ÷ 6**. Angka pembaginya sama.

## 2. Dari mana daftar pembanding berasal?

Dalam contoh tadi, daftar pembanding memuat K1 sampai K6 karena **G1 dapat menerima sirup** dan rancangan pembanding mengizinkan sirup dari G1 dikirim ke semua zona. Untuk jaringan lengkap, daftar pembanding disusun sekali dengan cara berikut.

1. **Dari pabrik ke gudang**, ambil 35 rute masuk dari High. Setiap rute mencatat pabrik, gudang tujuan, dan produknya.
2. **Dari gudang ke pelanggan**, lihat produk apa saja yang bisa diterima tiap gudang berdasarkan 35 rute tadi. Ada 11 pasangan gudang–produk. Izinkan setiap pasangan mengirim ke 6 zona. Hasilnya **11 × 6 = 66 rute keluar**.

Contohnya, rute **pabrik P4 → G1 untuk sirup** tersedia pada High, sehingga ikut dalam 35 rute masuk pembanding. Di tahap keluar, **G1 → K2 untuk sirup** sudah masuk daftar pembanding sejak awal, termasuk ketika yang sedang dihitung adalah Low. Itulah sebabnya poin yang didapat bisa bertambah dari Low ke Medium sementara poin pembandingnya tetap.

## 3. Hitung poin untuk seluruh jaringan

Jaringan lengkap punya **43 aturan**. Kita memeriksa tiap pasangan aturan satu kali. Jika satu rute tertulis di dua aturan, rute itu mendapat **1 poin**. Jika satu rute tertulis di empat aturan, rute itu bisa ditemukan pada **6 pasangan** dan mendapat **6 poin**. Cara menghitung enam pasangan itu adalah **3 + 2 + 1**. Pasangkan aturan pertama dengan tiga sisanya, aturan kedua dengan dua sisanya, lalu aturan ketiga dengan aturan keempat.

| Yang dihitung | Poin per variabel | Low | Medium | Daftar pembanding |
| --- | ---: | ---: | ---: | ---: |
| Rute pabrik → gudang | 1 | 16 × 1 | 21 × 1 | 35 × 1 |
| Rute gudang → pelanggan | 6 | 36 × 6 | 43 × 6 | 66 × 6 |
| Keputusan buka gudang | 1 | 4 × 1 | 4 × 1 | 4 × 1 |
| **Jumlah poin** | | **236** | **283** | **435** |

Contoh cara membaca tabel. Satu rute gudang → pelanggan muncul di empat aturan, yaitu aturan barang masuk dan keluar, pesanan pelanggan, batas tonase, dan batas waktu kerja. Enam pasangan aturan memakai rute itu. Karena Low punya 36 rute jenis ini, sumbangannya **36 × 6 = 216 poin**. Tambahkan 16 poin dari rute pabrik dan 4 poin dari keputusan membuka gudang. Hasilnya **236 poin**. Dengan cara yang sama, daftar pembanding mendapat **35 + 396 + 4 = 435 poin**.

## 4. Ubah poin menjadi persentase

**WCC** (*Weighted Constraint Coupling*) adalah poin yang didapat dibagi poin pembanding, lalu dinyatakan dalam persen. Untuk seluruh jaringan, daftar pembanding selalu memberi **435 poin**.

| Tingkat | Poin yang didapat | Poin pembanding | WCC |
| --- | ---: | ---: | ---: |
| Low | 236 | 435 | **54,25%** |
| Medium | 283 | 435 | **65,06%** |
| High | 381 | 435 | **87,59%** |

Dari Low ke Medium, ada **5 rute pabrik baru** yang masing-masing memberi 1 poin dan **7 rute gudang baru** yang masing-masing memberi 6 poin. Jadi, seluruh jaringan bertambah **5 + 42 = 47 poin**. Tiga poin dari contoh sirup G1 sudah termasuk dalam 47 poin itu.

## Contoh persamaan R8 pada Low

Gudang G1 boleh mengirim sirup ke K1, K3, dan K5. Persamaan R8 menyatakan **total sirup yang masuk = total sirup yang keluar**.

$$
\begin{aligned}
\mathrm{R8}\quad &x_{1,1,B}+x_{2,1,B}+x_{3,1,B}\\
&\quad = z_{1,1,B}+z_{1,3,B}+z_{1,5,B}
\end{aligned}
$$

## Lampiran teknis

[Lihat persamaan R1–R43, indeks rute, dan hitungan lengkap](math_model_acuan/Persamaan_WCC.md).

[Gambar jaringan PT XYZ](case/Kasus_Dasar.md) · [Rincian 903 pasangan](math_model_acuan/hasil/Audit_WCC_Pasangan.csv) · [Model matematika](math_model_acuan/Model_Matematika.md) · [Data rute](case/Data_Bersama.json) · [Audit 24 kombinasi](math_model_acuan/hasil/WCC.csv) · [Halaman utama](README.md)
