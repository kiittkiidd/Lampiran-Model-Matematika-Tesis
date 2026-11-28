# Menghitung Weighted Constraint Coupling

## 1. Apa yang dihitung?

*Weighted Constraint Coupling* (WCC) menghitung **variabel keputusan yang dipakai bersama oleh pasangan baris kendala**. Satu variabel bersama memberi bobot satu. Jika dua baris memakai tiga variabel yang sama, bobot pasangannya tiga. Cocokkan huruf **dan seluruh indeks**: <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle"> berbeda dari <img src="math_model_acuan/diagram/persamaan/eq-50e66253d5477375.svg" alt="z_{2,6,C}" width="37" height="14" align="middle">, dan <img src="math_model_acuan/diagram/persamaan/eq-25118c2b79b6e17d.svg" alt="x_{2,5,C}" width="39" height="14" align="middle"> berbeda dari <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle">.

Setiap baris kendala menjadi satu titik pada graf. Garis menghubungkan dua baris yang berbagi variabel; angka pada garis menunjukkan jumlah variabel bersama. Periksa setiap pasangan satu kali.


<p align="center"><img src="math_model_acuan/diagram/persamaan/eq-a5c59404f778b060.svg" alt="w_{rs}=\lvert S_r\cap S_s\rvert." width="129" height="25"></p>



<p align="center"><img src="math_model_acuan/diagram/persamaan/eq-3521201a6bfde71b.svg" alt="B=\sum_{r=1}^{m-1}\sum_{s=r+1}^{m}w_{rs}." width="147" height="60"></p>



<p align="center"><img src="math_model_acuan/diagram/persamaan/eq-16eaea62a468189a.svg" alt="\mathrm{WCC}=\frac{B}{B_{\mathrm{ref}}}\times100\%." width="183" height="47"></p>


| Simbol | Arti dan cara mendapatkannya |
|---|---|
| <img src="math_model_acuan/diagram/persamaan/eq-445aa3949d772c6d.svg" alt="m" width="16" height="10" align="middle"> | Jumlah baris kendala yang diperiksa. |
| <img src="math_model_acuan/diagram/persamaan/eq-ff35acc776e974da.svg" alt="S_r" width="19" height="16" align="middle"> | Himpunan variabel berbeda yang muncul pada baris <img src="math_model_acuan/diagram/persamaan/eq-640a535e9ee5fc23.svg" alt="r" width="10" height="10" align="middle">. |
| <img src="math_model_acuan/diagram/persamaan/eq-63d36148233e0986.svg" alt="w_{rs}" width="26" height="12" align="middle"> | Bobot pasangan: hitung variabel yang terdapat di kedua himpunan. |
| <img src="math_model_acuan/diagram/persamaan/eq-d10534071a7edbe1.svg" alt="B" width="15" height="13" align="middle"> | **Pembilang**: jumlahkan bobot seluruh pasangan pada tingkat yang dinilai. |
| <img src="math_model_acuan/diagram/persamaan/eq-c005b2e0ea3a3bda.svg" alt="B_{\mathrm{ref}}" width="30" height="16" align="middle"> | **Penyebut bersama**: jumlahkan bobot pasangan pada satu daftar rute pembanding yang ditetapkan untuk semua tingkat. |

**Dari mana daftar pembanding berasal?** Kasus ini memiliki empat gudang, enam zona, dan tiga produk. Semua gudang mampu menangani semua produk. Daftar pembanding mengizinkan setiap gudang mengirim setiap produk ke setiap zona: <img src="math_model_acuan/diagram/persamaan/eq-d7b7a786f959b0e6.svg" alt="4\times6\times3=72" width="103" height="15" align="middle"> rute keluar. Rute masuk mengikuti daftar High. Low, Medium, dan High hanya menggunakan sebagian dari daftar tersebut. Fasilitas tambahan tidak dibuat untuk menghitung penyebut.

Penyebut ini adalah bobot maksimum **dalam struktur rute pembanding tersebut**. Normalisasi ini ditetapkan untuk penelitian ini; persentasenya perlu dibaca bersama daftar rute dan cakupan kendala yang digunakan.

Penjumlahan <img src="math_model_acuan/diagram/persamaan/eq-d10534071a7edbe1.svg" alt="B" width="15" height="13" align="middle"> dimulai dari baris pertama dan pasangannya dengan baris sesudahnya. Untuk empat baris, urutannya adalah 1–2, 1–3, 1–4, 2–3, 2–4, dan 3–4. Dengan demikian, setiap pasangan dihitung sekali.

**NNZ dan kemungkinan hubungan.** NNZ adalah jumlah entri bukan nol. Pada matriks insidensi variabel–kendala, NNZ satu baris sama dengan banyaknya variabel berbeda yang muncul pada baris itu. Konstanta tidak dihitung. Dua baris dengan NNZ 3 dan 7 dapat berbagi paling banyak 3 variabel. Akan tetapi, batas 3 belum menyatakan bahwa ketiganya bisa cocok: asal, tujuan, produk, dan jenis keputusan juga harus sesuai. Penyebut dihitung dari **variabel yang benar-benar dapat muncul bersama dalam struktur pembanding**, bukan dengan mengalikan semua pasangan dengan satu angka NNZ.

## 2. Contoh kecil dari empat baris model sebenarnya

Ambil empat baris dari profil P1 Low. Nomor baris mengikuti model lengkap, sehingga contoh dapat ditelusuri pada [persamaan R1–R38](math_model_acuan/Persamaan_WCC.md).

| Baris | Aturan | Data yang dipakai |
|---|---|---|
| R6 | Neraca susu C di G2 | Susu masuk harus sama dengan susu keluar. |
| R27 | Pesanan susu C di K5 | Pesanan K5 sebesar 2,73 ton. |
| R32 | Kapasitas tonase G2 | Maksimal 20 ton jika G2 dibuka. |
| R36 | Waktu kerja G2 | Maksimal 22,40 jam jika G2 dibuka. |

### 2.1 Tulis persamaan dan seluruh indeksnya

Pada Low, G2 menerima susu dari P4 dan mengirimkannya ke K5 serta K6:


<p align="center"><img src="math_model_acuan/diagram/persamaan/eq-37b00332ebe5bcd1.svg" alt="\mathrm{R6}:\quad x_{4,2,C}=z_{2,5,C}+z_{2,6,C}." width="233" height="24"></p>


Pesanan susu K5 dilayani melalui G1 dan G2:


<p align="center"><img src="math_model_acuan/diagram/persamaan/eq-8470e7c81d0ae0a6.svg" alt="\mathrm{R27}:\quad z_{1,5,C}+z_{2,5,C}=2{,}73." width="233" height="24"></p>


Kapasitas tonase G2 menjumlahkan semua produk yang keluar:


<p align="center"><img src="math_model_acuan/diagram/persamaan/eq-97a0420885694952.svg" alt="\begin{aligned} \mathrm{R32}:\quad &amp;z_{2,1,A}+z_{2,2,A}+z_{2,3,B}+z_{2,4,B}\\ &amp;+z_{2,5,C}+z_{2,6,C}\le20y_2. \end{aligned}" width="289" height="50"></p>


Pada P1, setiap ton membutuhkan satu jam. Baris waktu G2 memakai kiriman yang sama:


<p align="center"><img src="math_model_acuan/diagram/persamaan/eq-ae3ea22e756710c9.svg" alt="\begin{aligned} \mathrm{R36}:\quad &amp;z_{2,1,A}+z_{2,2,A}+z_{2,3,B}+z_{2,4,B}\\ &amp;+z_{2,5,C}+z_{2,6,C}\le22{,}40y_2. \end{aligned}" width="289" height="50"></p>


<img src="math_model_acuan/diagram/persamaan/eq-7c80e0e1b67ffdbd.svg" alt="x_{4,2,C}" width="39" height="14" align="middle"> berarti ton susu dari **P4 ke G2**. <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle"> berarti ton susu dari **G2 ke K5**. <img src="math_model_acuan/diagram/persamaan/eq-23c9f2185134e5d1.svg" alt="y_2" width="17" height="13" align="middle"> adalah keputusan membuka G2. Angka 20 dan 22,40 merupakan parameter; keduanya tidak menambah bobot.

| Baris | Variabel yang muncul pada Low | NNZ insidensi |
|---|---|---:|
| R6 | <img src="math_model_acuan/diagram/persamaan/eq-f6270fe0f0c235de.svg" alt="x_{4,2,C},z_{2,5,C},z_{2,6,C}" width="123" height="14" align="middle"> | 3 |
| R27 | <img src="math_model_acuan/diagram/persamaan/eq-0dafb840ef3922e0.svg" alt="z_{1,5,C},z_{2,5,C}" width="79" height="14" align="middle"> | 2 |
| R32 | <img src="math_model_acuan/diagram/persamaan/eq-f67d77694859fe62.svg" alt="z_{2,1,A},z_{2,2,A},z_{2,3,B},z_{2,4,B},z_{2,5,C},z_{2,6,C},y_2" width="270" height="14" align="middle"> | 7 |
| R36 | Sama dengan daftar R32 | 7 |

### 2.2 Hitung pembilang: periksa keenam pasangan

Empat baris mempunyai <img src="math_model_acuan/diagram/persamaan/eq-de7865567492ec87.svg" alt="4(4-1)/2=6" width="104" height="18" align="middle"> pasangan. Mulai dari R6 dengan tiga baris sesudahnya, lalu R27 dengan dua baris sesudahnya, dan terakhir R32–R36.

| Pasangan | Variabel bersama pada Low | Bobot Low |
|---|---|---:|
| R6–R27 | <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle"> | 1 |
| R6–R32 | <img src="math_model_acuan/diagram/persamaan/eq-176c6700b69a1676.svg" alt="z_{2,5,C},z_{2,6,C}" width="79" height="14" align="middle"> | 2 |
| R6–R36 | <img src="math_model_acuan/diagram/persamaan/eq-176c6700b69a1676.svg" alt="z_{2,5,C},z_{2,6,C}" width="79" height="14" align="middle"> | 2 |
| R27–R32 | <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle"> | 1 |
| R27–R36 | <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle"> | 1 |
| R32–R36 | Keenam kiriman <img src="math_model_acuan/diagram/persamaan/eq-40c3e2b505699b72.svg" alt="z" width="10" height="10" align="middle"> pada R32 dan <img src="math_model_acuan/diagram/persamaan/eq-23c9f2185134e5d1.svg" alt="y_2" width="17" height="13" align="middle"> | 7 |
| **Jumlah pada empat baris** | <img src="math_model_acuan/diagram/persamaan/eq-5aa69473bcc366a9.svg" alt="1+2+2+1+1+7" width="148" height="15" align="middle"> | **14** |

Contoh R6–R32: keduanya memuat kiriman susu ke K5 dan K6. Variabel masuk <img src="math_model_acuan/diagram/persamaan/eq-7c80e0e1b67ffdbd.svg" alt="x_{4,2,C}" width="39" height="14" align="middle"> tidak ada pada R32. Kiriman minyak dan sirup serta <img src="math_model_acuan/diagram/persamaan/eq-23c9f2185134e5d1.svg" alt="y_2" width="17" height="13" align="middle"> tidak ada pada R6. Karena itu, bobotnya **2**, walaupun NNZ yang lebih kecil adalah 3.

### 2.3 Hitung penyebut pada empat baris yang sama

Daftar pembanding membolehkan susu dari G2 dikirim ke seluruh K1–K6. Gudang lain juga dapat melayani susu K5. Keempat aturan tetap berlaku; daftar kiriman yang boleh muncul diperluas.

| Baris | Persamaan dengan daftar rute pembanding | NNZ insidensi |
|---|---|---:|
| R6 | <img src="math_model_acuan/diagram/persamaan/eq-09cf41f891d89b38.svg" alt="x_{4,2,C}=\sum_{j=1}^{6}z_{2,j,C}" width="134" height="24" align="middle"> | 7 |
| R27 | <img src="math_model_acuan/diagram/persamaan/eq-7529c23fe011c15c.svg" alt="\sum_{g=1}^{4}z_{g,5,C}=2{,}73" width="128" height="25" align="middle"> | 4 |
| R32 | <img src="math_model_acuan/diagram/persamaan/eq-58be380f6023d400.svg" alt="\sum_{p\in\{A,B,C\}}\sum_{j=1}^{6}z_{2,j,p}\le20y_2" width="203" height="25" align="middle"> | 19 |
| R36 | <img src="math_model_acuan/diagram/persamaan/eq-91766a0606a90af5.svg" alt="\sum_{p\in\{A,B,C\}}\sum_{j=1}^{6}z_{2,j,p}\le22{,}40y_2" width="224" height="25" align="middle"> | 19 |

Penjumlahan pada R6 berarti <img src="math_model_acuan/diagram/persamaan/eq-f520d850c99061e1.svg" alt="z_{2,1,C}+z_{2,2,C}+z_{2,3,C}+z_{2,4,C}+z_{2,5,C}+z_{2,6,C}" width="310" height="16" align="middle">. Penjumlahan pada R32 mencakup enam kiriman A, enam kiriman B, dan enam kiriman C, sehingga terdapat 18 kiriman ditambah <img src="math_model_acuan/diagram/persamaan/eq-23c9f2185134e5d1.svg" alt="y_2" width="17" height="13" align="middle">.

| Pasangan | Variabel yang dapat muncul bersama pada pembanding | Bobot pembanding |
|---|---|---:|
| R6–R27 | <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle"> | 1 |
| R6–R32 | <img src="math_model_acuan/diagram/persamaan/eq-5b72bff40a4d171f.svg" alt="z_{2,1,C},z_{2,2,C},z_{2,3,C},z_{2,4,C},z_{2,5,C},z_{2,6,C}" width="248" height="14" align="middle"> | 6 |
| R6–R36 | Enam kiriman C yang sama | 6 |
| R27–R32 | <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle"> | 1 |
| R27–R36 | <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle"> | 1 |
| R32–R36 | Seluruh 18 kiriman keluar G2 dan <img src="math_model_acuan/diagram/persamaan/eq-23c9f2185134e5d1.svg" alt="y_2" width="17" height="13" align="middle"> | 19 |
| **Jumlah pada empat baris** | <img src="math_model_acuan/diagram/persamaan/eq-2eaf0f37fc624ec2.svg" alt="1+6+6+1+1+19" width="156" height="14" align="middle"> | **34** |

R6–R27 tetap berbobot satu: R6 hanya membahas G2 dan R27 hanya membahas K5. Variabel yang memenuhi kedua identitas itu hanya <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle">. NNZ 7 dan 4 tidak membuat empat kiriman bisa digunakan bersama oleh pasangan ini.

![Graf empat baris: bobot Low dan bobot pembanding](math_model_acuan/diagram/WCC_Empat_Baris.svg)

Garis hitam memperlihatkan bobot aktual Low; garis merah putus-putus memperlihatkan bobot yang dimungkinkan oleh daftar pembanding. Persilangan garis di tengah gambar bukan simpul tambahan. [Buka versi PNG](math_model_acuan/diagram/WCC_Empat_Baris.png).

Untuk **potongan empat baris ini**, persentasenya <img src="math_model_acuan/diagram/persamaan/eq-1ad0c0d5fb34f2dd.svg" alt="14/34\times100\%=41{,}18\%" width="170" height="18" align="middle">. Angka tersebut hanya menerangkan empat baris yang dipilih. WCC seluruh model menjumlahkan semua 703 pasangan, termasuk pasangan dengan baris di luar gambar.

### 2.4 Mengapa pembilang naik ketika rute ditambahkan?

Telusuri satu pasangan yang sama, **R6–R32**, dari Low ke Medium dan High. Ada enam tujuan yang diperbolehkan pada pembanding.

| Variabel susu dari G2 | Low | Medium | High | Pembanding |
|---|---:|---:|---:|---:|
| <img src="math_model_acuan/diagram/persamaan/eq-dad8cda73ef43f85.svg" alt="z_{2,1,C}" width="37" height="14" align="middle"> | 0 | **1** | 1 | 1 |
| <img src="math_model_acuan/diagram/persamaan/eq-d8fab703088bccbf.svg" alt="z_{2,2,C}" width="37" height="14" align="middle"> | 0 | **1** | 1 | 1 |
| <img src="math_model_acuan/diagram/persamaan/eq-ed158fa0601da2da.svg" alt="z_{2,3,C}" width="37" height="14" align="middle"> | 0 | **1** | 1 | 1 |
| <img src="math_model_acuan/diagram/persamaan/eq-35b41dd378893d19.svg" alt="z_{2,4,C}" width="37" height="14" align="middle"> | 0 | 0 | **1** | 1 |
| <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle"> | 1 | 1 | 1 | 1 |
| <img src="math_model_acuan/diagram/persamaan/eq-50e66253d5477375.svg" alt="z_{2,6,C}" width="37" height="14" align="middle"> | 1 | 1 | 1 | 1 |
| **Bobot pasangan** | **2** | **5** | **6** | **6** |

Angka 1 berarti variabel kiriman itu muncul pada kedua baris. Medium menambah tiga kiriman susu; bobot pasangan naik dari 2 menjadi 5. High menambah satu lagi; bobot menjadi 6. Penyebut pasangan tetap 6. R6 tetap merupakan aturan neraca, dan R32 tetap merupakan aturan kapasitas; yang berubah adalah rute yang boleh digunakan.

## 3. Perhitungan untuk seluruh model PT XYZ

### 3.1 Tetapkan baris yang diukur

| Keluarga kendala | Nomor baris | Jumlah |
|---|---|---:|
| Neraca gudang–produk | R1–R12 | <img src="math_model_acuan/diagram/persamaan/eq-8bfbae5ae6669fc8.svg" alt="4\times3=12" width="75" height="15" align="middle"> |
| Pesanan zona–produk | R13–R30 | <img src="math_model_acuan/diagram/persamaan/eq-fa000d1b42c194f0.svg" alt="6\times3=18" width="75" height="14" align="middle"> |
| Kapasitas gudang | R31–R34 | 4 |
| Waktu kerja gudang | R35–R38 | 4 |
| **Total** | **R1–R38** | **38** |

Jumlah pasangan adalah <img src="math_model_acuan/diagram/persamaan/eq-e963e466f68194ed.svg" alt="38(38-1)/2=703" width="136" height="18" align="middle">. Baris yang sama dipakai pada Low, Medium, dan High. Semua fasilitas dan produk tetap; daftar rute berubah. Karena variabel hanya disediakan untuk rute yang diizinkan, jumlah variabel kiriman juga berubah.

### 3.2 Jumlahkan kontribusi setiap variabel

Bobot seluruh pasangan dapat dihitung dengan cara lain yang memberi hasil sama. Jika satu variabel muncul pada <img src="math_model_acuan/diagram/persamaan/eq-445aa3949d772c6d.svg" alt="m" width="16" height="10" align="middle"> baris, variabel tersebut menyumbang <img src="math_model_acuan/diagram/persamaan/eq-41db94071046f741.svg" alt="m(m-1)/2" width="87" height="18" align="middle"> pasangan.

| Jenis keputusan | Baris yang memakainya | Pasangan yang dibentuk | Bobot per variabel |
|---|---|---|---:|
| Kiriman masuk <img src="math_model_acuan/diagram/persamaan/eq-00245e20aeb2a830.svg" alt="x_{igp}" width="28" height="14" align="middle"> | Satu neraca gudang–produk | Tidak ada pasangan | 0 |
| Kiriman keluar <img src="math_model_acuan/diagram/persamaan/eq-0753b7b06478fb85.svg" alt="z_{gjp}" width="27" height="14" align="middle"> | Neraca, pesanan, kapasitas, waktu | Neraca–pesanan; neraca–kapasitas; neraca–waktu; pesanan–kapasitas; pesanan–waktu; kapasitas–waktu | 6 |
| Buka gudang <img src="math_model_acuan/diagram/persamaan/eq-d26cd80ea0976736.svg" alt="y_g" width="17" height="14" align="middle"> | Kapasitas dan waktu gudang itu | Kapasitas–waktu | 1 |

Kiriman masuk tidak muncul pada batas pasokan pabrik karena kasus ini tidak membatasi pasokan pabrik. Karena hanya muncul pada satu baris yang diukur, kontribusinya nol. Kiriman itu tetap menjadi variabel model serta menimbulkan biaya dan emisi angkutan.

Contoh <img src="math_model_acuan/diagram/persamaan/eq-20f50f2c52af3966.svg" alt="z_{2,5,C}" width="37" height="14" align="middle"> muncul di R6, R27, R32, dan R36. Keempatnya membentuk enam pasangan pada tabel contoh. Satu variabel menyumbang satu pada masing-masing pasangan, sehingga total kontribusinya enam.

Empat keputusan buka menyumbang 4. Jika terdapat <img src="math_model_acuan/diagram/persamaan/eq-d57bd3051440493e.svg" alt="n_{\mathrm{out}}" width="30" height="12" align="middle"> rute keluar, total bobot adalah:


<p align="center"><img src="math_model_acuan/diagram/persamaan/eq-0ed36ff1e1ef9ec3.svg" alt="B=6n_{\mathrm{out}}+4, \qquad B_{\mathrm{ref}}=6(72)+4=436." width="342" height="25"></p>


### 3.3 Pembilang, penyebut, dan hasil

| Tingkat | Rute masuk | Rute keluar | Hitungan pembilang | Total bobot | Penyebut tetap | WCC |
|---|---:|---:|---|---:|---:|---:|
| Low | 16 | 36 | <img src="math_model_acuan/diagram/persamaan/eq-2c95dae5578e4c3f.svg" alt="6(36)+4" width="66" height="18" align="middle"> | 220 | 436 | **50,458716%** |
| Medium | 17 | 42 | <img src="math_model_acuan/diagram/persamaan/eq-3335123211c7c626.svg" alt="6(42)+4" width="66" height="18" align="middle"> | 256 | 436 | **58,715596%** |
| High | 22 | 60 | <img src="math_model_acuan/diagram/persamaan/eq-3766eaa63c7258c8.svg" alt="6(60)+4" width="66" height="18" align="middle"> | 364 | 436 | **83,486239%** |
| Pembanding | 22 | 72 | <img src="math_model_acuan/diagram/persamaan/eq-94d454d578e07111.svg" alt="6(72)+4" width="66" height="18" align="middle"> | 436 | 436 | 100% |

Sebagai contoh, Low dihitung dengan <img src="math_model_acuan/diagram/persamaan/eq-17cf4fa99a5099ec.svg" alt="220/436\times100\%" width="115" height="18" align="middle">. Medium menambah enam rute keluar, sehingga bobot bertambah <img src="math_model_acuan/diagram/persamaan/eq-19e6fbbf92618eb8.svg" alt="6\times6=36" width="75" height="14" align="middle">, dari 220 menjadi 256. High menambah 18 rute keluar dari Medium, sehingga bobot bertambah <img src="math_model_acuan/diagram/persamaan/eq-b357db16df32231d.svg" alt="18\times6=108" width="91" height="14" align="middle">, dari 256 menjadi 364. Selisih persentasenya **8,256881 poin** dan **24,770642 poin**, dihitung sebelum pembulatan.

Penambahan satu rute masuk pada Medium tidak menambah bobot pada cakupan ini karena kiriman masuk hanya muncul pada satu baris. Dengan demikian, WCC ini terutama berubah bersama jumlah rute keluar; angka WCC perlu dibaca bersama susunan jaringan dan banyak variabel.

### 3.4 Pemeriksaan seluruh pasangan

Tabel berikut mengelompokkan 703 pasangan yang sudah diperiksa satu per satu. Angka pada kolom bobot merupakan **jumlah variabel bersama**, bukan jumlah garis.

| Kelompok pasangan | Jumlah pasangan | Bobot Low | Bobot Medium | Bobot High | Bobot pembanding |
|---|---:|---:|---:|---:|---:|
| Neraca × neraca | 66 | 0 | 0 | 0 | 0 |
| Neraca × permintaan | 216 | 36 | 42 | 60 | 72 |
| Neraca × kapasitas | 48 | 36 | 42 | 60 | 72 |
| Neraca × waktu | 48 | 36 | 42 | 60 | 72 |
| Permintaan × permintaan | 153 | 0 | 0 | 0 | 0 |
| Permintaan × kapasitas | 72 | 36 | 42 | 60 | 72 |
| Permintaan × waktu | 72 | 36 | 42 | 60 | 72 |
| Kapasitas × kapasitas | 6 | 0 | 0 | 0 | 0 |
| Kapasitas × waktu | 16 | 40 | 46 | 64 | 76 |
| Waktu × waktu | 6 | 0 | 0 | 0 | 0 |
| **Total** | **703** | **220** | **256** | **364** | **436** |


Pasangan berbobot nol tetap diperiksa. Misalnya, dua baris neraca untuk gudang atau produk berbeda tidak memakai kiriman yang sama. Pada pembanding pun bobotnya nol. Pasangan tersebut menyumbang nol pada pembilang dan penyebut. Penyebut 436 adalah jumlah bobot yang diperbolehkan struktur; jumlah pasangan 703 bukan penyebut persentase ini.

Audit memakai dua metode: irisan himpunan variabel untuk seluruh pasangan, serta penjumlahan kontribusi kemunculan setiap variabel. Keduanya menghasilkan bobot yang sama.

## 4. Kesamaan WCC pada P1–P8

Pada satu tingkat rute, P1–P8 memakai identitas variabel yang sama pada **38 baris operasi per skenario**. Profil stokastik memiliki 27 salinan skenario dalam model lengkap, dengan keputusan buka bersama. Audit struktur di sini memeriksa setiap salinan secara terpisah.

Pada profil nonlinear, singkatan tonase <img src="math_model_acuan/diagram/persamaan/eq-1f4fc71f503e6ed2.svg" alt="q_{gp}" width="22" height="14" align="middle"> terlebih dahulu diganti dengan jumlah kiriman <img src="math_model_acuan/diagram/persamaan/eq-0753b7b06478fb85.svg" alt="z_{gjp}" width="27" height="14" align="middle">. Suku kuadrat memakai variabel yang sudah ada pada baris waktu; satu variabel dihitung sekali dalam daftar variabel baris itu. Nilai kiriman nol pada solusi optimal tidak menghapus variabel dari audit.

Fungsi tujuan, domain, batas emisi, pemecah seri, hubungan lintas skenario, serta variabel bantu dan baris tambahan solver berada di luar 38 baris yang diukur. Karena itu, kesamaan WCC ini berlaku pada blok operasi acuan yang dinyatakan, sedangkan waktu dan iterasi mengukur penyelesaian seluruh formulasi dan prosedur profil.

[Kasus untuk pemodel](case/Kasus_Dasar.md) · [Model matematika](math_model_acuan/Model_Matematika.md) · [Persamaan lengkap R1–R38](math_model_acuan/Persamaan_WCC.md) · [Seluruh 703 pasangan](math_model_acuan/hasil/audit/WCC_Pasangan.csv) · [Hasil verifikasi](math_model_acuan/Hasil_Verifikasi.md) · [Halaman utama](README.md)

[Sumber persamaan LaTeX](math_model_acuan/source/persamaan_sumber.tex).
