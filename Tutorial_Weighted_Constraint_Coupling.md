# Tutorial Weighted Constraint Coupling (WCC)

Weighted Constraint Coupling (WCC) mengukur keterkaitan antarbaris kendala berdasarkan **jumlah variabel keputusan yang dipakai bersama**. Misalnya, aturan kapasitas gudang dan aturan minimum kiriman sama-sama membatasi pengiriman A dan B ke Pelanggan 1. Kedua keputusan itu menghubungkan sepasang kendala, sehingga garisnya berbobot **2**. Pasangan lain yang hanya berbagi pengiriman A mendapat bobot **1**. Bobot ini membuat perbedaan kedua pasangan terlihat pada graf.

Untuk menghitungnya, jabarkan dulu indeks pada setiap kendala. Satu rumus yang berlaku untuk dua pelanggan menghasilkan dua baris, dan setiap keputusan pengiriman dikenali lewat nama variabel beserta seluruh indeksnya.

## 1. Kasus dan kendala

Gudang 1 mengirim produk A dan B ke dua pelanggan. Kedua produk dihitung dalam satuan paket. Gudang dapat menangani paling banyak **20 paket**. Produk A memerlukan penanganan dingin, dengan kapasitas **12 paket A** yang termasuk dalam kapasitas total gudang. Pelanggan 1 harus menerima sedikitnya **7 paket**, dan pelanggan 2 sedikitnya **6 paket**. Dalam contoh ini, kedua pelanggan dapat menerima kombinasi A dan B.

### Variabel keputusan

Notasi $x_{g,j,p}$ berarti jumlah paket produk $p$ yang dikirim dari gudang $g$ ke pelanggan $j$. Urutan indeksnya adalah **gudang, pelanggan, produk**. Karena hanya ada satu gudang, indeks pertama selalu 1.

| Variabel | Keputusan yang dicatat |
| --- | --- |
| $x_{1,1,A}$ | Paket A dari Gudang 1 ke Pelanggan 1 |
| $x_{1,1,B}$ | Paket B dari Gudang 1 ke Pelanggan 1 |
| $x_{1,2,A}$ | Paket A dari Gudang 1 ke Pelanggan 2 |
| $x_{1,2,B}$ | Paket B dari Gudang 1 ke Pelanggan 2 |

Sebagai contoh, $x_{1,1,A}=4$ dan $x_{1,2,A}=2$ berarti Gudang 1 mengirim empat paket A ke Pelanggan 1 dan dua paket A ke Pelanggan 2. Perbedaan pada indeks pelanggan membuat keduanya menjadi variabel yang berbeda, walaupun keduanya memakai huruf $x$ dan produk A yang sama.

### Empat baris kendala

**R1. Kapasitas total gudang**

```math
x_{1,1,A}+x_{1,1,B}+x_{1,2,A}+x_{1,2,B} \le 20
```

Keempat pengiriman memakai kapasitas gudang. Jika pengiriman pada urutan di atas adalah 4, 3, 2, dan 4 paket, kapasitas yang terpakai adalah $4+3+2+4=13$ paket.

**R2. Kapasitas penanganan dingin untuk produk A**

```math
x_{1,1,A}+x_{1,2,A} \le 12
```

Kendala ini menjumlahkan pengiriman produk A ke kedua pelanggan. Pada pengiriman yang sama, kapasitas dingin yang terpakai adalah $4+2=6$ paket A.

**R3 dan R4. Jumlah minimum paket untuk setiap pelanggan**

Kedua baris berasal dari satu rumus. Indeks $j$ menunjukkan pelanggan, $p$ menunjukkan produk, dan $d_j$ adalah jumlah paket minimum untuk pelanggan $j$.

```math
\sum_{p\in\{A,B\}} x_{1,j,p} \ge d_j, \qquad j\in\{1,2\}
```

Masukkan $j=1$ dan $d_1=7$ untuk memperoleh **R3**.

```math
x_{1,1,A}+x_{1,1,B} \ge 7
```

Pelanggan 1 menerima $4+3=7$ paket pada contoh pengiriman tadi.

Masukkan $j=2$ dan $d_2=6$ untuk memperoleh **R4**.

```math
x_{1,2,A}+x_{1,2,B} \ge 6
```

Pelanggan 2 menerima $2+4=6$ paket. Semua variabel pengiriman bernilai nonnegatif. Graf tutorial ini memakai empat baris kendala fungsional R1–R4. Nonnegativitas dicatat sebagai domain variabel.

## 2. Bandingkan keenam pasangan baris satu per satu

Pertama, tandai variabel yang muncul pada setiap baris. Tanda ✓ berarti variabel dengan **nama dan seluruh indeks tersebut** muncul pada baris itu.

| Baris | $x_{1,1,A}$ | $x_{1,1,B}$ | $x_{1,2,A}$ | $x_{1,2,B}$ |
| --- | :---: | :---: | :---: | :---: |
| R1 · Kapasitas total | ✓ | ✓ | ✓ | ✓ |
| R2 · Kapasitas dingin | ✓ | | ✓ | |
| R3 · Minimum Pelanggan 1 | ✓ | ✓ | | |
| R4 · Minimum Pelanggan 2 | | | ✓ | ✓ |

Selanjutnya, ambil dua baris dan hitung kolom yang memiliki ✓ di **kedua** baris. Contohnya, R1 dan R2 sama-sama memiliki ✓ pada kolom $x_{1,1,A}$ dan $x_{1,2,A}$. Jadi bobot pasangan R1–R2 adalah $1+1=2$.

| Pasangan | Variabel yang sama persis di kedua baris | Bobot garis |
| --- | --- | ---: |
| R1–R2 | $x_{1,1,A}$ dan $x_{1,2,A}$ | 2 |
| R1–R3 | $x_{1,1,A}$ dan $x_{1,1,B}$ | 2 |
| R1–R4 | $x_{1,2,A}$ dan $x_{1,2,B}$ | 2 |
| R2–R3 | $x_{1,1,A}$ | 1 |
| R2–R4 | $x_{1,2,A}$ | 1 |
| R3–R4 | Tidak ada. Indeks pelanggan pada R3 adalah 1 dan pada R4 adalah 2. | 0 |

Perhatikan R3–R4. Kedua baris menyebut produk A dan B. Namun, $x_{1,1,A}$ masuk ke R3, sedangkan $x_{1,2,A}$ masuk ke R4. Untuk produk B, perbedaan indeks pelanggannya juga sama. Karena tidak ada kolom yang ditandai pada kedua baris, bobotnya **0**.

## 3. Gambar graf kendala

Setiap lingkaran mewakili satu baris kendala. Garis muncul jika dua baris memakai sedikitnya satu variabel yang sama. Angka pada garis menunjukkan jumlah variabel yang digunakan bersama. R3 dan R4 tidak memiliki garis langsung.

```mermaid
flowchart TB
    R1((R1)) ---|2| R3((R3))
    R1 ---|2| R2((R2))
    R1 ---|2| R4((R4))
    R3 ---|1| R2
    R4 ---|1| R2
```

## 4. Dari mana rumus bobot berasal?

### 4.1 Hitung satu pasangan dulu

Ambil **R1 dan R2**. Baca kedua baris dan beri **1** untuk setiap variabel yang muncul di keduanya, atau **0** jika variabel itu hanya muncul di salah satu baris.

| Variabel | Ada di R1? | Ada di R2? | Sumbangan ke bobot R1–R2 |
| --- | :---: | :---: | ---: |
| $x_{1,1,A}$ | Ya | Ya | 1 |
| $x_{1,1,B}$ | Ya | Tidak | 0 |
| $x_{1,2,A}$ | Ya | Ya | 1 |
| $x_{1,2,B}$ | Ya | Tidak | 0 |
| **Total** | | | **2** |

Inilah asal angka **2** pada garis R1–R2. Nilai pengirimannya, misalnya empat paket A ke Pelanggan 1, digunakan untuk memeriksa kapasitas pada model. Untuk menghitung bobot, kemunculan variabel pengiriman tersebut menyumbang **1** ke pasangan R1–R2.

Dalam notasi matematika, $S_r$ adalah daftar variabel pada baris R yang bernomor $r$. Jadi $S_1$ berisi empat variabel pengiriman pada R1. $S_2$ berisi dua variabel pengiriman produk A pada R2. Simbol $\cap$ berarti mengambil anggota yang ada di kedua daftar.

```math
S_1 \cap S_2 = \{x_{1,1,A},\ x_{1,2,A}\}
```

Hasilnya berisi dua anggota. Jika $R_r$ dan $R_s$ adalah dua baris yang sedang dibandingkan, $w_{rs}$ adalah bobot garis penghubungnya. Tanda $\lvert\,\cdot\,\rvert$ pada rumus berikut berarti menghitung banyaknya anggota.

```math
w_{rs} = \lvert S_r \cap S_s \rvert
```

### 4.2 Jumlahkan bobot seluruh pasangan

R1 membentuk tiga pasangan dengan R2, R3, dan R4. Setelah itu, R2 membentuk dua pasangan baru dengan R3 dan R4. Terakhir, tersisa R3–R4. Jadi ada **3 + 2 + 1 = 6 pasangan**, masing-masing dihitung sekali. Huruf $B$ menyatakan total bobot keenam pasangan.

```math
B = w_{12}+w_{13}+w_{14}+w_{23}+w_{24}+w_{34}
```

Masukkan bobot dari tabel pasangan di bagian 2 sesuai urutan. R3–R4 ikut diperiksa dengan bobot 0.

```math
B = 2 + 2 + 2 + 1 + 1 + 0 = 8
```

Angka **8** berasal dari penjumlahan lima label pada graf. Dalam contoh ini, ada empat variabel pengiriman, dan satu variabel bisa menyumbang bobot ke lebih dari satu pasangan. Misalnya, $x_{1,1,A}$ muncul di R1, R2, dan R3. Variabel ini menyumbang satu ke R1–R2, satu ke R1–R3, dan satu ke R2–R3. Kita bisa memeriksa hasil 8 dengan menghitung dari sisi variabel.

| Variabel | Baris tempat variabel muncul | Pasangan yang mendapat tambahan 1 | Sumbangan |
| --- | --- | --- | ---: |
| $x_{1,1,A}$ | R1, R2, R3 | R1–R2, R1–R3, R2–R3 | 3 |
| $x_{1,1,B}$ | R1, R3 | R1–R3 | 1 |
| $x_{1,2,A}$ | R1, R2, R4 | R1–R2, R1–R4, R2–R4 | 3 |
| $x_{1,2,B}$ | R1, R4 | R1–R4 | 1 |
| **Total** | | | **8** |

Untuk model yang lebih besar, $P$ menyatakan daftar semua pasangan baris berbeda, dengan setiap pasangan dicatat sekali. Simbol $\sum$ menyingkat penjumlahan bobot pada daftar itu.

```math
B = \sum_{(r,s) \in P} w_{rs}
```

## 5. Dari mana penyebut persentase WCC berasal?

### 5.1 Tentukan jaringan yang menjadi patokan

Persentase menjawab pertanyaan **“Total bobot versi ini mencapai berapa persen dari bobot jaringan acuan?”** Dalam tutorial ini, jaringan acuan adalah versi yang mengizinkan **A dan B ke kedua pelanggan**. Keempat kombinasi pengiriman tersedia, dan bentuk empat baris kendalanya sudah ditulis pada bagian 1.

Terapkan penghitungan yang sama pada jaringan acuan. Dari langkah 4.2, total bobotnya adalah **2 + 2 + 2 + 1 + 1 + 0 = 8**. Karena itulah penyebutnya **8**. Kita menulis $B_{\mathrm{ref}}$ untuk total bobot khusus jaringan acuan, dan $B$ untuk total bobot versi yang sedang dinilai.

```math
\mathrm{WCC}_{\mathrm{ref}} = \frac{B}{B_{\mathrm{ref}}} \times 100\%
```

Di sini ada dua angka dengan peran berbeda. **6** adalah banyaknya pasangan baris yang diperiksa. **8** adalah jumlah bobot keenam pasangan pada jaringan acuan. Karena persentase yang kita cari membandingkan *total bobot dengan total bobot*, nilai pembaginya adalah 8.

Untuk jaringan acuan sendiri, pembilang dan penyebut sama-sama 8. Maka $8\div8=1$, lalu $1\times100\%=100\%$. Artinya jaringan itu mencapai seluruh **bobot jaringan acuan**. R3–R4 tetap berbobot 0.

### 5.2 Uji satu perubahan dan hitung ulang keenam pasangan

Sekarang anggap Pelanggan 2 hanya menerima A. Kombinasi $x_{1,2,B}$ dihapus dari jaringan, beserta sukunya pada R1 dan R4. R1 menjumlahkan tiga pengiriman, dan R4 menjadi $x_{1,2,A}\ge6$. R2 dan R3 memakai daftar variabel yang sama seperti sebelumnya.

| Pasangan | Bobot acuan | Variabel bersama setelah perubahan | Bobot setelah perubahan |
| --- | ---: | --- | ---: |
| R1–R2 | 2 | $x_{1,1,A}$ dan $x_{1,2,A}$ | 2 |
| R1–R3 | 2 | $x_{1,1,A}$ dan $x_{1,1,B}$ | 2 |
| R1–R4 | 2 | $x_{1,2,A}$ | 1 |
| R2–R3 | 1 | $x_{1,1,A}$ | 1 |
| R2–R4 | 1 | $x_{1,2,A}$ | 1 |
| R3–R4 | 0 | Tidak ada | 0 |
| **Total** | **8** | | **7** |

Jumlahkan kolom terakhir dan gunakan acuan yang sama. Angka 7 berasal dari jaringan setelah perubahan, dan angka 8 dari jaringan acuan.

```math
B = 2 + 2 + 1 + 1 + 1 + 0 = 7
```

```math
\mathrm{WCC}_{\mathrm{ref}} = \frac{7}{8} \times 100\% = 87{,}5\%
```

Secara aritmetika, $7\div8=0{,}875$. Kalikan dengan 100% untuk memperoleh **87,5%**. Kelima garis masih ada karena R1–R4 tetap berbagi $x_{1,2,A}$. Label garis itulah yang berubah dari 2 menjadi 1. WCC menangkap bobot yang hilang ketika Pelanggan 2 hanya menerima produk A.

## 6. Terapkan pada model lain

1. Tetapkan baris kendala fungsional yang dihitung pada formulasi sebelum *presolve*. Fungsi tujuan dan deklarasi domain berada di luar graf ini.
2. Jabarkan rumus berindeks menjadi baris terpisah. Catat nama dan **seluruh indeks** variabel pada setiap baris. Untuk baris linear, gabungkan suku sejenis terlebih dahulu. Catat satu kali setiap variabel dengan koefisien akhir bukan nol.
3. Periksa setiap pasangan baris sekali. Beri satu poin untuk setiap variabel berindeks lengkap yang muncul di kedua baris. Jumlahkan seluruh bobot pasangan untuk memperoleh $B$.
4. Jika hasil dilaporkan dalam persen, tetapkan satu jaringan acuan dengan $B_{\mathrm{ref}}>0$. Gunakan aturan penghitungan yang sama untuk memperoleh bobotnya dan pakai **penyebut yang sama** pada seluruh versi pembanding.

Kesamaan WCC dengan penyebut yang sama menunjukkan kesamaan **total bobot**. Jika yang ingin dipastikan juga mencakup kesamaan garis serta variabel yang menghubungkannya, periksa daftar variabel bersama **pada setiap pasangan baris**.
