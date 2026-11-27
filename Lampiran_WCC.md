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

<details>
<summary>Lihat persamaan, indeks, dan NNZ untuk contoh sirup G1</summary>

| R | Kendala | Isi kendala |
| --- | --- | --- |
| R8 | Neraca sirup di gudang G1 | Ton sirup yang masuk ke G1 sama dengan ton sirup yang keluar. |
| R36 | Kapasitas tonase gudang G1 | Total kiriman minyak dan sirup dari G1 paling banyak 16 ton saat gudang dibuka. |

$`x_{i,g,p}`$ adalah kiriman dari pabrik $`i`$ ke gudang $`g`$ untuk produk $`p`$. $`z_{g,j,p}`$ adalah kiriman dari gudang $`g`$ ke zona $`j`$ untuk produk $`p`$. A berarti minyak dan B berarti sirup. $`y_1`$ adalah keputusan buka G1, dengan nilai 1 jika buka dan 0 jika tutup. Contohnya, $`z_{1,4,B}`$ adalah kiriman sirup dari G1 ke K4.

### Persamaan R8 dan R36

**Low. Rute sirup ke K1, K3, dan K5**

R8 ditampilkan pada [contoh persamaan di atas](#contoh-persamaan-r8-pada-low). R36 menghitung seluruh kiriman keluar dari G1.

$$
\begin{aligned}
\mathrm{R36}\quad &z_{1,1,A}+z_{1,2,A}+z_{1,3,A}\\
&{}+z_{1,4,A}+z_{1,5,A}+z_{1,6,A}\\
&{}+z_{1,1,B}+z_{1,3,B}+z_{1,5,B}\\
&\quad \le 16y_1
\end{aligned}
$$

**Medium. Rute sirup ke K1 sampai K6**

Suku **tebal** menunjukkan tiga rute sirup yang baru tersedia dari G1 ke **K2, K4, dan K6** pada Medium. Ketiga suku itu muncul pada R8 dan R36.

$$
\begin{aligned}
\mathrm{R8}\quad &x_{1,1,B}+x_{2,1,B}+x_{3,1,B}\\
&\quad = z_{1,1,B}+\boldsymbol{z_{1,2,B}}+z_{1,3,B}\\
&\qquad {}+\boldsymbol{z_{1,4,B}}+z_{1,5,B}+\boldsymbol{z_{1,6,B}}
\end{aligned}
$$

$$
\begin{aligned}
\mathrm{R36}\quad &z_{1,1,A}+z_{1,2,A}+z_{1,3,A}\\
&{}+z_{1,4,A}+z_{1,5,A}+z_{1,6,A}\\
&{}+z_{1,1,B}+\boldsymbol{z_{1,2,B}}+z_{1,3,B}\\
&{}+\boldsymbol{z_{1,4,B}}+z_{1,5,B}+\boldsymbol{z_{1,6,B}}\\
&\quad \le 16y_1
\end{aligned}
$$

**Daftar rute pembanding untuk penyebut**

Daftar pembanding ditetapkan sekali dan diterapkan pada Low, Medium, dan High. Satu entri menentukan **rute dan produknya**, misalnya pabrik P3 → gudang G1 untuk sirup. Dalam ilustrasi dengan pabrik P1, P2, dan P3, jika Low mengizinkan P1 dan P2 mengirim sirup ke G1, sedangkan daftar pembanding juga mengizinkan **P3 → G1 untuk sirup**, maka suku $`x_{3,1,B}`$ ikut masuk ke persamaan pembanding.

Daftar pembanding pada kasus PT XYZ dibentuk dari dua tahap pengiriman.

| Tahap | Aturan pembentukan daftar pembanding | Hasil |
| --- | --- | ---: |
| Pabrik → gudang | Ambil semua rute masuk yang diizinkan pada High. | **35** rute masuk |
| Gudang → zona | Dari 35 rute masuk itu, temukan 11 pasangan gudang–produk yang bisa menerima kiriman. Untuk tiap pasangan, izinkan kiriman ke semua enam zona. | **11 × 6 = 66** rute keluar |

Pada **R8 dalam kasus asli**, sirup dapat masuk ke G1 dari P1, P2, dan P3 pada Low maupun Medium. Daftar pembanding juga memuat **P4 → G1 untuk sirup** karena rute itu tersedia di High. Suku $`x_{4,1,B}`$ ditebalkan di bawah untuk menunjukkan tambahannya pada R8. R36 hanya memuat kiriman keluar dan keputusan buka gudang, sehingga suku tersebut muncul pada satu baris dan menyumbang **0** ke bobot pasangan R8–R36. [Data rute kasus PT XYZ](case/Data_Bersama.json)

$$
\begin{aligned}
\mathrm{R8}\quad &x_{1,1,B}+x_{2,1,B}+x_{3,1,B}\\
&{}+\boldsymbol{x_{4,1,B}}\\
&\quad = z_{1,1,B}+z_{1,2,B}+z_{1,3,B}\\
&\qquad {}+z_{1,4,B}+z_{1,5,B}+z_{1,6,B}
\end{aligned}
$$

$$
\begin{aligned}
\mathrm{R36}\quad &z_{1,1,A}+z_{1,2,A}+z_{1,3,A}\\
&{}+z_{1,4,A}+z_{1,5,A}+z_{1,6,A}\\
&{}+z_{1,1,B}+z_{1,2,B}+z_{1,3,B}\\
&{}+z_{1,4,B}+z_{1,5,B}+z_{1,6,B}\\
&\quad \le 16y_1
\end{aligned}
$$

### Daftar indeks yang bisa muncul di kedua kendala

R8 dan R36 bisa berbagi variabel kiriman sirup dari G1 ke zona mana pun. Karena itu, yang perlu diperiksa berbentuk $`z_{1,j,B}`$. Daftar kemungkinan mengizinkan keenam zona, jadi ada **enam indeks yang mungkin sama**. Angka **1** berarti indeks itu tertulis pada kedua persamaan. Angka **0** berarti tidak muncul bersama.

| Rute sirup | Variabel berindeks | Aktual di Low | Aktual di Medium | Mungkin di kedua baris |
| --- | --- | ---: | ---: | ---: |
| G1 → K1 | $`z_{1,1,B}`$ | 1 | 1 | 1 |
| **G1 → K2** | $`\boldsymbol{z_{1,2,B}}`$ | 0 | **1** | 1 |
| G1 → K3 | $`z_{1,3,B}`$ | 1 | 1 | 1 |
| **G1 → K4** | $`\boldsymbol{z_{1,4,B}}`$ | 0 | **1** | 1 |
| G1 → K5 | $`z_{1,5,B}`$ | 1 | 1 | 1 |
| **G1 → K6** | $`\boldsymbol{z_{1,6,B}}`$ | 0 | **1** | 1 |
| **Jumlah bobot R8–R36** | | **3** | **6** | **6** |

<details>
<summary>Periksa semua variabel lain pada persamaan R8 dan R36</summary>

Pada setiap sel, angka pertama menandai kemunculan di R8 dan angka kedua menandai kemunculan di R36. Semua variabel di bawah menyumbang 0 karena tidak tertulis pada kedua baris.

| Variabel yang diperiksa | Low · R8 × R36 | Medium · R8 × R36 | Daftar kemungkinan · R8 × R36 |
| --- | ---: | ---: | ---: |
| $`x_{1,1,B}`$ | 1 × 0 = 0 | 1 × 0 = 0 | 1 × 0 = 0 |
| $`x_{2,1,B}`$ | 1 × 0 = 0 | 1 × 0 = 0 | 1 × 0 = 0 |
| $`x_{3,1,B}`$ | 1 × 0 = 0 | 1 × 0 = 0 | 1 × 0 = 0 |
| $`x_{4,1,B}`$ | 0 × 0 = 0 | 0 × 0 = 0 | 1 × 0 = 0 |
| $`z_{1,1,A}`$ | 0 × 1 = 0 | 0 × 1 = 0 | 0 × 1 = 0 |
| $`z_{1,2,A}`$ | 0 × 1 = 0 | 0 × 1 = 0 | 0 × 1 = 0 |
| $`z_{1,3,A}`$ | 0 × 1 = 0 | 0 × 1 = 0 | 0 × 1 = 0 |
| $`z_{1,4,A}`$ | 0 × 1 = 0 | 0 × 1 = 0 | 0 × 1 = 0 |
| $`z_{1,5,A}`$ | 0 × 1 = 0 | 0 × 1 = 0 | 0 × 1 = 0 |
| $`z_{1,6,A}`$ | 0 × 1 = 0 | 0 × 1 = 0 | 0 × 1 = 0 |
| $`y_1`$ | 0 × 1 = 0 | 0 × 1 = 0 | 0 × 1 = 0 |

</details>

**Cek dengan NNZ.** Dalam daftar kemungkinan, R8 berisi 10 variabel dan R36 berisi 13 variabel. Dari banyaknya koefisien bukan nol saja, batas atasnya adalah $`\min(10,13)=10`$. Setelah indeks diperiksa, hanya enam kiriman sirup dari G1 yang bisa tertulis pada kedua kendala. Kiriman masuk hanya tertulis pada R8. Kiriman minyak dan keputusan buka gudang hanya tertulis pada R36. Jadi bobot maksimum menurut daftar kemungkinan untuk pasangan ini adalah **6**.

### Apa yang bertambah dari Low ke Medium?

Medium menambahkan tiga indeks yang sama pada kedua persamaan, yaitu $`z_{1,2,B}`$, $`z_{1,4,B}`$, dan $`z_{1,6,B}`$. Setiap indeks dihitung sekali untuk pasangan R8–R36.

| Sumbangan pasangan R8–R36 | Low | Medium | Perubahan |
| --- | ---: | ---: | ---: |
| Pembilang | 3 | 3 + 3 = **6** | **+3** |
| Penyebut | 6 | **6** | **0** |

Enam indeks untuk penyebut sudah tersedia di daftar kemungkinan sebelum memilih tingkat. Saat rute ke K2, K4, dan K6 ditambahkan ke Medium, yang berubah adalah kolom aktual pada tabel.

</details>

<details>
<summary>Lihat 43 persamaan pada Low dan pada daftar pembanding</summary>

### Daftar kendala R1–R43

Di model lengkap, nomor berikut mengikuti urutan 43 baris operasi sebelum penyederhanaan solver. Produk A adalah minyak goreng, B adalah sirup, dan C adalah susu. Buka kelompok yang ingin diperiksa untuk melihat setiap persamaan beserta indeksnya.

| Baris | Kendala |
| --- | --- |
| R1–R6 | Kapasitas P1–P6 |
| R7–R17 | Neraca per gudang dan produk. G1 menangani A dan B, G2–G4 masing-masing menangani A, B, dan C. |
| R18–R35 | Pesanan K1–K6, masing-masing untuk A, B, dan C |
| R36–R39 | Kapasitas tonase G1–G4 |
| R40–R43 | Batas waktu kerja G1–G4 dalam bentuk linear P1 |

<details>
<summary>R1–R6 · Kapasitas pabrik</summary>

**R1 · Kapasitas pabrik P1**

$$
\begin{aligned}
\mathrm{R1}\quad &x_{1,1,A}+x_{1,1,B}+x_{1,2,A} \le 8
\end{aligned}
$$

**R2 · Kapasitas pabrik P2**

$$
\begin{aligned}
\mathrm{R2}\quad &x_{2,1,A}+x_{2,1,B}+x_{2,4,B} \le 8
\end{aligned}
$$

**R3 · Kapasitas pabrik P3**

$$
\begin{aligned}
\mathrm{R3}\quad &x_{3,1,B}+x_{3,3,B}+x_{3,3,C}+x_{3,4,B} \le 8
\end{aligned}
$$

**R4 · Kapasitas pabrik P4**

$$
\begin{aligned}
\mathrm{R4}\quad &x_{4,2,C}+x_{4,3,C} \le 8
\end{aligned}
$$

**R5 · Kapasitas pabrik P5**

$$
\begin{aligned}
\mathrm{R5}\quad &x_{5,2,A}+x_{5,4,A} \le 8
\end{aligned}
$$

**R6 · Kapasitas pabrik P6**

$$
\begin{aligned}
\mathrm{R6}\quad &x_{6,2,C}+x_{6,3,C} \le 8
\end{aligned}
$$

</details>

<details>
<summary>R7–R17 · Neraca gudang–produk</summary>

**R7 · Neraca minyak di G1**

$$
\begin{aligned}
\mathrm{R7}\quad &x_{1,1,A}+x_{2,1,A}\\
&\quad = z_{1,1,A}+z_{1,2,A}+z_{1,3,A}+z_{1,4,A}\\
&\qquad {}+z_{1,5,A}+z_{1,6,A}
\end{aligned}
$$

**R8 · Neraca sirup di G1**

$$
\begin{aligned}
\mathrm{R8}\quad &x_{1,1,B}+x_{2,1,B}+x_{3,1,B}\\
&\quad = z_{1,1,B}+z_{1,3,B}+z_{1,5,B}
\end{aligned}
$$

**R9 · Neraca minyak di G2**

$$
\begin{aligned}
\mathrm{R9}\quad &x_{1,2,A}+x_{5,2,A}\\
&\quad = z_{2,1,A}+z_{2,3,A}+z_{2,4,A}+z_{2,5,A}\\
&\qquad {}+z_{2,6,A}
\end{aligned}
$$

**R10 · Neraca sirup di G2**

$$
\begin{aligned}
\mathrm{R10}\quad &0\\
&\quad = 0
\end{aligned}
$$

**R11 · Neraca susu di G2**

$$
\begin{aligned}
\mathrm{R11}\quad &x_{4,2,C}+x_{6,2,C}\\
&\quad = z_{2,1,C}+z_{2,2,C}+z_{2,3,C}+z_{2,4,C}\\
&\qquad {}+z_{2,5,C}+z_{2,6,C}
\end{aligned}
$$

**R12 · Neraca minyak di G3**

$$
\begin{aligned}
\mathrm{R12}\quad &0\\
&\quad = 0
\end{aligned}
$$

**R13 · Neraca sirup di G3**

$$
\begin{aligned}
\mathrm{R13}\quad &x_{3,3,B}\\
&\quad = z_{3,1,B}+z_{3,2,B}+z_{3,3,B}+z_{3,4,B}\\
&\qquad {}+z_{3,5,B}+z_{3,6,B}
\end{aligned}
$$

**R14 · Neraca susu di G3**

$$
\begin{aligned}
\mathrm{R14}\quad &x_{3,3,C}+x_{4,3,C}+x_{6,3,C}\\
&\quad = z_{3,1,C}+z_{3,2,C}+z_{3,3,C}+z_{3,4,C}\\
&\qquad {}+z_{3,5,C}+z_{3,6,C}
\end{aligned}
$$

**R15 · Neraca minyak di G4**

$$
\begin{aligned}
\mathrm{R15}\quad &x_{5,4,A}\\
&\quad = z_{4,2,A}
\end{aligned}
$$

**R16 · Neraca sirup di G4**

$$
\begin{aligned}
\mathrm{R16}\quad &x_{2,4,B}+x_{3,4,B}\\
&\quad = z_{4,2,B}+z_{4,4,B}+z_{4,6,B}
\end{aligned}
$$

**R17 · Neraca susu di G4**

$$
\begin{aligned}
\mathrm{R17}\quad &0\\
&\quad = 0
\end{aligned}
$$

</details>

<details>
<summary>R18–R35 · Pesanan zona–produk</summary>

**R18 · Pesanan minyak di K1**

$$
\begin{aligned}
\mathrm{R18}\quad &z_{1,1,A}+z_{2,1,A} = 3
\end{aligned}
$$

**R19 · Pesanan sirup di K1**

$$
\begin{aligned}
\mathrm{R19}\quad &z_{1,1,B}+z_{3,1,B} = 1
\end{aligned}
$$

**R20 · Pesanan susu di K1**

$$
\begin{aligned}
\mathrm{R20}\quad &z_{2,1,C}+z_{3,1,C} = 1
\end{aligned}
$$

**R21 · Pesanan minyak di K2**

$$
\begin{aligned}
\mathrm{R21}\quad &z_{1,2,A}+z_{4,2,A} = 3
\end{aligned}
$$

**R22 · Pesanan sirup di K2**

$$
\begin{aligned}
\mathrm{R22}\quad &z_{3,2,B}+z_{4,2,B} = 1
\end{aligned}
$$

**R23 · Pesanan susu di K2**

$$
\begin{aligned}
\mathrm{R23}\quad &z_{2,2,C}+z_{3,2,C} = 1
\end{aligned}
$$

**R24 · Pesanan minyak di K3**

$$
\begin{aligned}
\mathrm{R24}\quad &z_{1,3,A}+z_{2,3,A} = 1
\end{aligned}
$$

**R25 · Pesanan sirup di K3**

$$
\begin{aligned}
\mathrm{R25}\quad &z_{1,3,B}+z_{3,3,B} = 3
\end{aligned}
$$

**R26 · Pesanan susu di K3**

$$
\begin{aligned}
\mathrm{R26}\quad &z_{2,3,C}+z_{3,3,C} = 1
\end{aligned}
$$

**R27 · Pesanan minyak di K4**

$$
\begin{aligned}
\mathrm{R27}\quad &z_{1,4,A}+z_{2,4,A} = 1
\end{aligned}
$$

**R28 · Pesanan sirup di K4**

$$
\begin{aligned}
\mathrm{R28}\quad &z_{3,4,B}+z_{4,4,B} = 3
\end{aligned}
$$

**R29 · Pesanan susu di K4**

$$
\begin{aligned}
\mathrm{R29}\quad &z_{2,4,C}+z_{3,4,C} = 1
\end{aligned}
$$

**R30 · Pesanan minyak di K5**

$$
\begin{aligned}
\mathrm{R30}\quad &z_{1,5,A}+z_{2,5,A} = 1
\end{aligned}
$$

**R31 · Pesanan sirup di K5**

$$
\begin{aligned}
\mathrm{R31}\quad &z_{1,5,B}+z_{3,5,B} = 1
\end{aligned}
$$

**R32 · Pesanan susu di K5**

$$
\begin{aligned}
\mathrm{R32}\quad &z_{2,5,C}+z_{3,5,C} = 3
\end{aligned}
$$

**R33 · Pesanan minyak di K6**

$$
\begin{aligned}
\mathrm{R33}\quad &z_{1,6,A}+z_{2,6,A} = 1
\end{aligned}
$$

**R34 · Pesanan sirup di K6**

$$
\begin{aligned}
\mathrm{R34}\quad &z_{3,6,B}+z_{4,6,B} = 1
\end{aligned}
$$

**R35 · Pesanan susu di K6**

$$
\begin{aligned}
\mathrm{R35}\quad &z_{2,6,C}+z_{3,6,C} = 3
\end{aligned}
$$

</details>

<details>
<summary>R36–R39 · Kapasitas tonase gudang</summary>

**R36 · Kapasitas tonase G1**

$$
\begin{aligned}
\mathrm{R36}\quad &z_{1,1,A}+z_{1,1,B}+z_{1,2,A}+z_{1,3,A}\\
&{}+z_{1,3,B}+z_{1,4,A}+z_{1,5,A}+z_{1,5,B}\\
&{}+z_{1,6,A}\\
&\quad \le 16y_1
\end{aligned}
$$

**R37 · Kapasitas tonase G2**

$$
\begin{aligned}
\mathrm{R37}\quad &z_{2,1,A}+z_{2,1,C}+z_{2,2,C}+z_{2,3,A}\\
&{}+z_{2,3,C}+z_{2,4,A}+z_{2,4,C}+z_{2,5,A}\\
&{}+z_{2,5,C}+z_{2,6,A}+z_{2,6,C}\\
&\quad \le 20y_2
\end{aligned}
$$

**R38 · Kapasitas tonase G3**

$$
\begin{aligned}
\mathrm{R38}\quad &z_{3,1,B}+z_{3,1,C}+z_{3,2,B}+z_{3,2,C}\\
&{}+z_{3,3,B}+z_{3,3,C}+z_{3,4,B}+z_{3,4,C}\\
&{}+z_{3,5,B}+z_{3,5,C}+z_{3,6,B}+z_{3,6,C}\\
&\quad \le 18y_3
\end{aligned}
$$

**R39 · Kapasitas tonase G4**

$$
\begin{aligned}
\mathrm{R39}\quad &z_{4,2,A}+z_{4,2,B}+z_{4,4,B}+z_{4,6,B} \le 14y_4
\end{aligned}
$$

</details>

<details>
<summary>R40–R43 · Batas waktu kerja gudang</summary>

**R40 · Batas waktu kerja G1**

$$
\begin{aligned}
\mathrm{R40}\quad &z_{1,1,A}+z_{1,1,B}+z_{1,2,A}+z_{1,3,A}\\
&{}+z_{1,3,B}+z_{1,4,A}+z_{1,5,A}+z_{1,5,B}\\
&{}+z_{1,6,A}\\
&\quad \le 19{,}2y_1
\end{aligned}
$$

**R41 · Batas waktu kerja G2**

$$
\begin{aligned}
\mathrm{R41}\quad &z_{2,1,A}+z_{2,1,C}+z_{2,2,C}+z_{2,3,A}\\
&{}+z_{2,3,C}+z_{2,4,A}+z_{2,4,C}+z_{2,5,A}\\
&{}+z_{2,5,C}+z_{2,6,A}+z_{2,6,C}\\
&\quad \le 24y_2
\end{aligned}
$$

**R42 · Batas waktu kerja G3**

$$
\begin{aligned}
\mathrm{R42}\quad &z_{3,1,B}+z_{3,1,C}+z_{3,2,B}+z_{3,2,C}\\
&{}+z_{3,3,B}+z_{3,3,C}+z_{3,4,B}+z_{3,4,C}\\
&{}+z_{3,5,B}+z_{3,5,C}+z_{3,6,B}+z_{3,6,C}\\
&\quad \le 21{,}6y_3
\end{aligned}
$$

**R43 · Batas waktu kerja G4**

$$
\begin{aligned}
\mathrm{R43}\quad &z_{4,2,A}+z_{4,2,B}+z_{4,4,B}+z_{4,6,B} \le 16{,}8y_4
\end{aligned}
$$

</details>

### Contoh pasangan dari persamaan Low

| Pasangan | Kendala yang dibandingkan | Variabel bersama di Low | Bobot Low |
| --- | --- | --- | ---: |
| R1–R8 | Kapasitas P1 dan neraca sirup G1 | $`x_{1,1,B}`$ | 1 |
| R1–R19 | Kapasitas P1 dan pesanan sirup K1 | Tidak ada | 0 |
| R8–R19 | Neraca sirup G1 dan pesanan sirup K1 | $`z_{1,1,B}`$ | 1 |
| R8–R36 | Neraca sirup dan tonase G1 | $`z_{1,1,B}`$, $`z_{1,3,B}`$, $`z_{1,5,B}`$ | 3 |
| R8–R40 | Neraca sirup dan waktu kerja G1 | $`z_{1,1,B}`$, $`z_{1,3,B}`$, $`z_{1,5,B}`$ | 3 |
| R19–R36 | Pesanan sirup K1 dan tonase G1 | $`z_{1,1,B}`$ | 1 |
| R19–R40 | Pesanan sirup K1 dan waktu kerja G1 | $`z_{1,1,B}`$ | 1 |
| R36–R40 | Tonase dan waktu kerja G1 | $`z_{1,j,A}`$ untuk K1–K6, $`z_{1,j,B}`$ untuk K1, K3, K5, $`y_1`$ | 10 |

Contohnya, R36 dan R40 memuat daftar kiriman keluar G1 yang sama. Dari persamaan keduanya, cocokkan enam variabel kiriman minyak dan tiga variabel kiriman sirup. Cocokkan pula $`y_1`$ pada kedua ruas kanan. Koefisien $`y_1`$ berbeda, yaitu 16 dan 19,2, tetapi identitas variabelnya sama. Bobot pasangan ini adalah **6 + 3 + 1 = 10**.



Empat puluh tiga baris menghasilkan **43 × 42 ÷ 2 = 903 pasangan**. Jumlahkan bobot setiap pasangan satu kali, termasuk pasangan berbobot nol. Total bobot Low adalah **236**. Tabel pada Bagian 3 merangkum penjumlahannya, dan CSV mencantumkan indeks lengkap untuk setiap pasangan. [Rincian 903 pasangan](math_model_acuan/hasil/Audit_WCC_Pasangan.csv)

<details>
<summary>Lihat seluruh persamaan R1–R43 dengan daftar rute maksimum</summary>

<details>
<summary>R1–R6 · Kapasitas pabrik</summary>

**R1 · Kapasitas pabrik P1**

$$
\begin{aligned}
\mathrm{R1}\quad &x_{1,1,A}+x_{1,1,B}+x_{1,2,A}+x_{1,2,B}\\
&{}+x_{1,3,B}+x_{1,4,A}+x_{1,4,B}\\
&\quad \le 8
\end{aligned}
$$

**R2 · Kapasitas pabrik P2**

$$
\begin{aligned}
\mathrm{R2}\quad &x_{2,1,A}+x_{2,1,B}+x_{2,2,B}+x_{2,3,B}\\
&{}+x_{2,4,B}\\
&\quad \le 8
\end{aligned}
$$

**R3 · Kapasitas pabrik P3**

$$
\begin{aligned}
\mathrm{R3}\quad &x_{3,1,A}+x_{3,1,B}+x_{3,2,A}+x_{3,2,B}\\
&{}+x_{3,3,A}+x_{3,3,B}+x_{3,3,C}+x_{3,4,A}\\
&{}+x_{3,4,B}\\
&\quad \le 8
\end{aligned}
$$

**R4 · Kapasitas pabrik P4**

$$
\begin{aligned}
\mathrm{R4}\quad &x_{4,1,B}+x_{4,2,B}+x_{4,2,C}+x_{4,3,B}\\
&{}+x_{4,3,C}+x_{4,4,B}+x_{4,4,C}\\
&\quad \le 8
\end{aligned}
$$

**R5 · Kapasitas pabrik P5**

$$
\begin{aligned}
\mathrm{R5}\quad &x_{5,1,A}+x_{5,2,A}+x_{5,3,A}+x_{5,4,A} \le 8
\end{aligned}
$$

**R6 · Kapasitas pabrik P6**

$$
\begin{aligned}
\mathrm{R6}\quad &x_{6,2,C}+x_{6,3,C}+x_{6,4,C} \le 8
\end{aligned}
$$

</details>

<details>
<summary>R7–R17 · Neraca gudang–produk</summary>

**R7 · Neraca minyak di G1**

$$
\begin{aligned}
\mathrm{R7}\quad &x_{1,1,A}+x_{2,1,A}+x_{3,1,A}+x_{5,1,A}\\
&\quad = z_{1,1,A}+z_{1,2,A}+z_{1,3,A}+z_{1,4,A}\\
&\qquad {}+z_{1,5,A}+z_{1,6,A}
\end{aligned}
$$

**R8 · Neraca sirup di G1**

$$
\begin{aligned}
\mathrm{R8}\quad &x_{1,1,B}+x_{2,1,B}+x_{3,1,B}+x_{4,1,B}\\
&\quad = z_{1,1,B}+z_{1,2,B}+z_{1,3,B}+z_{1,4,B}\\
&\qquad {}+z_{1,5,B}+z_{1,6,B}
\end{aligned}
$$

**R9 · Neraca minyak di G2**

$$
\begin{aligned}
\mathrm{R9}\quad &x_{1,2,A}+x_{3,2,A}+x_{5,2,A}\\
&\quad = z_{2,1,A}+z_{2,2,A}+z_{2,3,A}+z_{2,4,A}\\
&\qquad {}+z_{2,5,A}+z_{2,6,A}
\end{aligned}
$$

**R10 · Neraca sirup di G2**

$$
\begin{aligned}
\mathrm{R10}\quad &x_{1,2,B}+x_{2,2,B}+x_{3,2,B}+x_{4,2,B}\\
&\quad = z_{2,1,B}+z_{2,2,B}+z_{2,3,B}+z_{2,4,B}\\
&\qquad {}+z_{2,5,B}+z_{2,6,B}
\end{aligned}
$$

**R11 · Neraca susu di G2**

$$
\begin{aligned}
\mathrm{R11}\quad &x_{4,2,C}+x_{6,2,C}\\
&\quad = z_{2,1,C}+z_{2,2,C}+z_{2,3,C}+z_{2,4,C}\\
&\qquad {}+z_{2,5,C}+z_{2,6,C}
\end{aligned}
$$

**R12 · Neraca minyak di G3**

$$
\begin{aligned}
\mathrm{R12}\quad &x_{3,3,A}+x_{5,3,A}\\
&\quad = z_{3,1,A}+z_{3,2,A}+z_{3,3,A}+z_{3,4,A}\\
&\qquad {}+z_{3,5,A}+z_{3,6,A}
\end{aligned}
$$

**R13 · Neraca sirup di G3**

$$
\begin{aligned}
\mathrm{R13}\quad &x_{1,3,B}+x_{2,3,B}+x_{3,3,B}+x_{4,3,B}\\
&\quad = z_{3,1,B}+z_{3,2,B}+z_{3,3,B}+z_{3,4,B}\\
&\qquad {}+z_{3,5,B}+z_{3,6,B}
\end{aligned}
$$

**R14 · Neraca susu di G3**

$$
\begin{aligned}
\mathrm{R14}\quad &x_{3,3,C}+x_{4,3,C}+x_{6,3,C}\\
&\quad = z_{3,1,C}+z_{3,2,C}+z_{3,3,C}+z_{3,4,C}\\
&\qquad {}+z_{3,5,C}+z_{3,6,C}
\end{aligned}
$$

**R15 · Neraca minyak di G4**

$$
\begin{aligned}
\mathrm{R15}\quad &x_{1,4,A}+x_{3,4,A}+x_{5,4,A}\\
&\quad = z_{4,1,A}+z_{4,2,A}+z_{4,3,A}+z_{4,4,A}\\
&\qquad {}+z_{4,5,A}+z_{4,6,A}
\end{aligned}
$$

**R16 · Neraca sirup di G4**

$$
\begin{aligned}
\mathrm{R16}\quad &x_{1,4,B}+x_{2,4,B}+x_{3,4,B}+x_{4,4,B}\\
&\quad = z_{4,1,B}+z_{4,2,B}+z_{4,3,B}+z_{4,4,B}\\
&\qquad {}+z_{4,5,B}+z_{4,6,B}
\end{aligned}
$$

**R17 · Neraca susu di G4**

$$
\begin{aligned}
\mathrm{R17}\quad &x_{4,4,C}+x_{6,4,C}\\
&\quad = z_{4,1,C}+z_{4,2,C}+z_{4,3,C}+z_{4,4,C}\\
&\qquad {}+z_{4,5,C}+z_{4,6,C}
\end{aligned}
$$

</details>

<details>
<summary>R18–R35 · Pesanan zona–produk</summary>

**R18 · Pesanan minyak di K1**

$$
\begin{aligned}
\mathrm{R18}\quad &z_{1,1,A}+z_{2,1,A}+z_{3,1,A}+z_{4,1,A} = 3
\end{aligned}
$$

**R19 · Pesanan sirup di K1**

$$
\begin{aligned}
\mathrm{R19}\quad &z_{1,1,B}+z_{2,1,B}+z_{3,1,B}+z_{4,1,B} = 1
\end{aligned}
$$

**R20 · Pesanan susu di K1**

$$
\begin{aligned}
\mathrm{R20}\quad &z_{2,1,C}+z_{3,1,C}+z_{4,1,C} = 1
\end{aligned}
$$

**R21 · Pesanan minyak di K2**

$$
\begin{aligned}
\mathrm{R21}\quad &z_{1,2,A}+z_{2,2,A}+z_{3,2,A}+z_{4,2,A} = 3
\end{aligned}
$$

**R22 · Pesanan sirup di K2**

$$
\begin{aligned}
\mathrm{R22}\quad &z_{1,2,B}+z_{2,2,B}+z_{3,2,B}+z_{4,2,B} = 1
\end{aligned}
$$

**R23 · Pesanan susu di K2**

$$
\begin{aligned}
\mathrm{R23}\quad &z_{2,2,C}+z_{3,2,C}+z_{4,2,C} = 1
\end{aligned}
$$

**R24 · Pesanan minyak di K3**

$$
\begin{aligned}
\mathrm{R24}\quad &z_{1,3,A}+z_{2,3,A}+z_{3,3,A}+z_{4,3,A} = 1
\end{aligned}
$$

**R25 · Pesanan sirup di K3**

$$
\begin{aligned}
\mathrm{R25}\quad &z_{1,3,B}+z_{2,3,B}+z_{3,3,B}+z_{4,3,B} = 3
\end{aligned}
$$

**R26 · Pesanan susu di K3**

$$
\begin{aligned}
\mathrm{R26}\quad &z_{2,3,C}+z_{3,3,C}+z_{4,3,C} = 1
\end{aligned}
$$

**R27 · Pesanan minyak di K4**

$$
\begin{aligned}
\mathrm{R27}\quad &z_{1,4,A}+z_{2,4,A}+z_{3,4,A}+z_{4,4,A} = 1
\end{aligned}
$$

**R28 · Pesanan sirup di K4**

$$
\begin{aligned}
\mathrm{R28}\quad &z_{1,4,B}+z_{2,4,B}+z_{3,4,B}+z_{4,4,B} = 3
\end{aligned}
$$

**R29 · Pesanan susu di K4**

$$
\begin{aligned}
\mathrm{R29}\quad &z_{2,4,C}+z_{3,4,C}+z_{4,4,C} = 1
\end{aligned}
$$

**R30 · Pesanan minyak di K5**

$$
\begin{aligned}
\mathrm{R30}\quad &z_{1,5,A}+z_{2,5,A}+z_{3,5,A}+z_{4,5,A} = 1
\end{aligned}
$$

**R31 · Pesanan sirup di K5**

$$
\begin{aligned}
\mathrm{R31}\quad &z_{1,5,B}+z_{2,5,B}+z_{3,5,B}+z_{4,5,B} = 1
\end{aligned}
$$

**R32 · Pesanan susu di K5**

$$
\begin{aligned}
\mathrm{R32}\quad &z_{2,5,C}+z_{3,5,C}+z_{4,5,C} = 3
\end{aligned}
$$

**R33 · Pesanan minyak di K6**

$$
\begin{aligned}
\mathrm{R33}\quad &z_{1,6,A}+z_{2,6,A}+z_{3,6,A}+z_{4,6,A} = 1
\end{aligned}
$$

**R34 · Pesanan sirup di K6**

$$
\begin{aligned}
\mathrm{R34}\quad &z_{1,6,B}+z_{2,6,B}+z_{3,6,B}+z_{4,6,B} = 1
\end{aligned}
$$

**R35 · Pesanan susu di K6**

$$
\begin{aligned}
\mathrm{R35}\quad &z_{2,6,C}+z_{3,6,C}+z_{4,6,C} = 3
\end{aligned}
$$

</details>

<details>
<summary>R36–R39 · Kapasitas tonase gudang</summary>

**R36 · Kapasitas tonase G1**

$$
\begin{aligned}
\mathrm{R36}\quad &z_{1,1,A}+z_{1,2,A}+z_{1,3,A}+z_{1,4,A}\\
&{}+z_{1,5,A}+z_{1,6,A}+z_{1,1,B}+z_{1,2,B}\\
&{}+z_{1,3,B}+z_{1,4,B}+z_{1,5,B}+z_{1,6,B}\\
&\quad \le 16y_1
\end{aligned}
$$

**R37 · Kapasitas tonase G2**

$$
\begin{aligned}
\mathrm{R37}\quad &z_{2,1,A}+z_{2,2,A}+z_{2,3,A}+z_{2,4,A}\\
&{}+z_{2,5,A}+z_{2,6,A}+z_{2,1,B}+z_{2,2,B}\\
&{}+z_{2,3,B}+z_{2,4,B}+z_{2,5,B}+z_{2,6,B}\\
&{}+z_{2,1,C}+z_{2,2,C}+z_{2,3,C}+z_{2,4,C}\\
&{}+z_{2,5,C}+z_{2,6,C}\\
&\quad \le 20y_2
\end{aligned}
$$

**R38 · Kapasitas tonase G3**

$$
\begin{aligned}
\mathrm{R38}\quad &z_{3,1,A}+z_{3,2,A}+z_{3,3,A}+z_{3,4,A}\\
&{}+z_{3,5,A}+z_{3,6,A}+z_{3,1,B}+z_{3,2,B}\\
&{}+z_{3,3,B}+z_{3,4,B}+z_{3,5,B}+z_{3,6,B}\\
&{}+z_{3,1,C}+z_{3,2,C}+z_{3,3,C}+z_{3,4,C}\\
&{}+z_{3,5,C}+z_{3,6,C}\\
&\quad \le 18y_3
\end{aligned}
$$

**R39 · Kapasitas tonase G4**

$$
\begin{aligned}
\mathrm{R39}\quad &z_{4,1,A}+z_{4,2,A}+z_{4,3,A}+z_{4,4,A}\\
&{}+z_{4,5,A}+z_{4,6,A}+z_{4,1,B}+z_{4,2,B}\\
&{}+z_{4,3,B}+z_{4,4,B}+z_{4,5,B}+z_{4,6,B}\\
&{}+z_{4,1,C}+z_{4,2,C}+z_{4,3,C}+z_{4,4,C}\\
&{}+z_{4,5,C}+z_{4,6,C}\\
&\quad \le 14y_4
\end{aligned}
$$

</details>

<details>
<summary>R40–R43 · Batas waktu kerja gudang</summary>

**R40 · Batas waktu kerja G1**

$$
\begin{aligned}
\mathrm{R40}\quad &z_{1,1,A}+z_{1,2,A}+z_{1,3,A}+z_{1,4,A}\\
&{}+z_{1,5,A}+z_{1,6,A}+z_{1,1,B}+z_{1,2,B}\\
&{}+z_{1,3,B}+z_{1,4,B}+z_{1,5,B}+z_{1,6,B}\\
&\quad \le 19{,}2y_1
\end{aligned}
$$

**R41 · Batas waktu kerja G2**

$$
\begin{aligned}
\mathrm{R41}\quad &z_{2,1,A}+z_{2,2,A}+z_{2,3,A}+z_{2,4,A}\\
&{}+z_{2,5,A}+z_{2,6,A}+z_{2,1,B}+z_{2,2,B}\\
&{}+z_{2,3,B}+z_{2,4,B}+z_{2,5,B}+z_{2,6,B}\\
&{}+z_{2,1,C}+z_{2,2,C}+z_{2,3,C}+z_{2,4,C}\\
&{}+z_{2,5,C}+z_{2,6,C}\\
&\quad \le 24y_2
\end{aligned}
$$

**R42 · Batas waktu kerja G3**

$$
\begin{aligned}
\mathrm{R42}\quad &z_{3,1,A}+z_{3,2,A}+z_{3,3,A}+z_{3,4,A}\\
&{}+z_{3,5,A}+z_{3,6,A}+z_{3,1,B}+z_{3,2,B}\\
&{}+z_{3,3,B}+z_{3,4,B}+z_{3,5,B}+z_{3,6,B}\\
&{}+z_{3,1,C}+z_{3,2,C}+z_{3,3,C}+z_{3,4,C}\\
&{}+z_{3,5,C}+z_{3,6,C}\\
&\quad \le 21{,}6y_3
\end{aligned}
$$

**R43 · Batas waktu kerja G4**

$$
\begin{aligned}
\mathrm{R43}\quad &z_{4,1,A}+z_{4,2,A}+z_{4,3,A}+z_{4,4,A}\\
&{}+z_{4,5,A}+z_{4,6,A}+z_{4,1,B}+z_{4,2,B}\\
&{}+z_{4,3,B}+z_{4,4,B}+z_{4,5,B}+z_{4,6,B}\\
&{}+z_{4,1,C}+z_{4,2,C}+z_{4,3,C}+z_{4,4,C}\\
&{}+z_{4,5,C}+z_{4,6,C}\\
&\quad \le 16{,}8y_4
\end{aligned}
$$

</details>

</details>

</details>

<details>
<summary>Lihat penjumlahan bobot dan rincian 12 rute baru</summary>

### Jumlahkan bobot, lalu bagi

| Kelompok pasangan | Jumlah pasangan | Bobot aktual Low | Bobot maksimum menurut daftar rute |
| --- | ---: | ---: | ---: |
| Kapasitas pabrik × neraca | 66 | 16 | 35 |
| Neraca × pesanan | 198 | 36 | 66 |
| Neraca × tonase | 44 | 36 | 66 |
| Neraca × waktu | 44 | 36 | 66 |
| Pesanan × tonase | 72 | 36 | 66 |
| Pesanan × waktu | 72 | 36 | 66 |
| Tonase × waktu | 16 | 40 | 70 |
| Kelompok lain | 391 | 0 | 0 |
| **Total** | **903** | **236** | **435** |

Setiap rute masuk menyumbang satu ke pasangan kapasitas pabrik–neraca. Setiap rute keluar menyumbang satu pada tiap kelompok dari neraca–pesanan sampai tonase–waktu. Pada kelompok tonase–waktu, empat keputusan buka gudang juga menyumbang empat. Itu sebabnya, misalnya, bobot kelompok tonase–waktu pada Low adalah 36 + 4 = 40.

$$
\mathrm{WCC}_{\mathrm{Low}}
=\frac{\text{total bobot aktual Low}}{\text{total bobot maksimum menurut daftar rute}}\times 100\%
=\frac{236}{435}\times 100\%
\approx 54{,}25\%.
$$

### Dari tambahan 3 pada satu pasangan ke tambahan 47 pada seluruh model

Low memiliki 16 rute masuk dan 36 rute keluar. Medium memiliki 21 rute masuk dan 43 rute keluar. Tabel menunjukkan **semua 12 variabel rute yang bertambah**. Nomor R merujuk pada daftar persamaan dalam lampiran teknis di atas.

| Variabel baru di Medium | Rute dan produk | Kendala yang memuatnya | Tambahan bobot seluruh pasangan |
| --- | --- | --- | ---: |
| $`x_{1,2,B}`$ | P1 → G2, B | R1, R10 | 1 |
| $`x_{1,4,A}`$ | P1 → G4, A | R1, R15 | 1 |
| $`x_{2,2,B}`$ | P2 → G2, B | R2, R10 | 1 |
| $`x_{2,3,B}`$ | P2 → G3, B | R2, R13 | 1 |
| $`x_{5,1,A}`$ | P5 → G1, A | R5, R7 | 1 |
| $`z_{1,2,B}`$ | G1 → K2, B | R8, R22, R36, R40 | 6 |
| $`z_{1,4,B}`$ | G1 → K4, B | R8, R28, R36, R40 | 6 |
| $`z_{1,6,B}`$ | G1 → K6, B | R8, R34, R36, R40 | 6 |
| $`z_{2,1,B}`$ | G2 → K1, B | R10, R19, R37, R41 | 6 |
| $`z_{2,3,B}`$ | G2 → K3, B | R10, R25, R37, R41 | 6 |
| $`z_{4,4,A}`$ | G4 → K4, A | R15, R27, R39, R43 | 6 |
| $`z_{4,6,A}`$ | G4 → K6, A | R15, R33, R39, R43 | 6 |
| **Total** | **5 rute masuk + 7 rute keluar** | | **47** |

Misalnya, $`z_{1,2,B}`$ muncul pada R8 (neraca sirup G1), R22 (pesanan sirup K2), R36 (tonase G1), dan R40 (waktu kerja G1). Variabel itu menambah satu bobot pada masing-masing dari enam pasangan berikut.

| R8 dengan baris lain | R22 dengan baris lain | Pasangan terakhir |
| --- | --- | --- |
| R8–R22, R8–R36, R8–R40 | R22–R36, R22–R40 | R36–R40 |

Setiap rute masuk baru muncul pada dua kendala, sehingga menambah satu bobot. Setiap rute keluar baru muncul pada empat kendala, sehingga menambah enam bobot. Jadi pembilang seluruh model naik sebanyak **5 × 1 + 7 × 6 = 47**, dari **236** menjadi **283**. Penyebut seluruh model tetap **435**. Tambahan tiga bobot pada R8–R36 sudah termasuk di dalam 47.

</details>

<details>
<summary>Lihat cakupan audit</summary>

Ketiga tingkat menggunakan 43 aturan operasi yang sama. Variabel kiriman bertambah ketika daftar rute bertambah. Pada satu tingkat, WCC operasi sama untuk P1–P8. Audit memeriksa skenario stokastik satu per satu. Batas emisi, domain variabel, pemilihan emisi saat biaya sama, dan garis singgung solver berada di luar 43 baris yang dihitung.

</details>

[Gambar jaringan PT XYZ](case/Kasus_Dasar.md) · [Rincian 903 pasangan](math_model_acuan/hasil/Audit_WCC_Pasangan.csv) · [Model matematika](math_model_acuan/Model_Matematika.md) · [Data rute](case/Data_Bersama.json) · [Audit 24 kombinasi](math_model_acuan/hasil/WCC.csv) · [Halaman utama](README.md)
