# Menghitung Weighted Constraint Coupling

Untuk setiap pasangan kendala, hitung **berapa variabel berindeks yang benar-benar muncul di kedua baris** dan **berapa yang paling banyak bisa muncul di kedua baris berdasarkan rute yang diizinkan rancangan**. Jumlah pertama masuk ke pembilang. Jumlah kedua masuk ke penyebut. Dua variabel cocok jika huruf dan seluruh indeksnya sama.

## 1. Pembilang dan penyebut dari kasus PT XYZ

Ambil **R8–R36** dari model distribusi PT XYZ.

| R | Kendala | Variabel yang dapat dipakai |
| --- | --- | --- |
| R8 | Neraca sirup di G1 | Kiriman sirup masuk ke G1 dan kiriman sirup keluar dari G1 |
| R36 | Kapasitas tonase G1 | Semua kiriman keluar dari G1 dan keputusan membuka G1 |

### Pembilang. Variabel yang benar-benar muncul di kedua baris pada Low

Dalam notasi $`z_{g,j,p}`$, indeks $`g`$ adalah gudang, $`j`$ adalah zona tujuan, dan $`p`$ adalah produk. Jadi $`z_{1,3,B}`$ berarti kiriman sirup (produk B) dari G1 ke K3. Variabel $`x_{i,g,p}`$ adalah kiriman dari pabrik ke gudang dan $`y_1`$ adalah keputusan membuka G1.

Persamaan Low memuat rute yang tersedia pada tingkat tersebut.

```math
\begin{aligned}
\mathrm{R8}\quad &x_{1,1,B}+x_{2,1,B}+x_{3,1,B}\\
&\quad = z_{1,1,B}+z_{1,3,B}+z_{1,5,B}
\end{aligned}
```

```math
\begin{aligned}
\mathrm{R36}\quad &z_{1,1,A}+z_{1,1,B}+z_{1,2,A}+z_{1,3,A}\\
&{}+z_{1,3,B}+z_{1,4,A}+z_{1,5,A}+z_{1,5,B}\\
&{}+z_{1,6,A}\\
&\quad \le 16y_1
\end{aligned}
```

Cocokkan variabel pada kedua ruas. **Hanya tiga yang sama**, yaitu $`z_{1,1,B}`$, $`z_{1,3,B}`$, dan $`z_{1,5,B}`$. Ketiganya adalah kiriman sirup dari G1 ke K1, K3, dan K5. Bobot aktual pasangan R8–R36 adalah **3**.

### Penyebut. Variabel yang bisa muncul di kedua baris

R8 membatasi produk ke sirup. R36 membatasi asal kiriman ke G1. Karena itu, variabel yang bisa menghubungkan keduanya hanya berbentuk $`z_{1,j,B}`$. Dalam daftar kemungkinan yang sama untuk semua tingkat, G1 boleh mengirim sirup ke keenam zona. Cocokkan indeksnya satu per satu. Angka 1 berarti variabel tersedia pada kedua baris.

| Rute sirup | Variabel | Muncul di kedua baris pada Low | Bisa muncul di kedua baris menurut rancangan |
| --- | --- | ---: | ---: |
| G1 → K1 | $`z_{1,1,B}`$ | 1 | 1 |
| G1 → K2 | $`z_{1,2,B}`$ | 0 | 1 |
| G1 → K3 | $`z_{1,3,B}`$ | 1 | 1 |
| G1 → K4 | $`z_{1,4,B}`$ | 0 | 1 |
| G1 → K5 | $`z_{1,5,B}`$ | 1 | 1 |
| G1 → K6 | $`z_{1,6,B}`$ | 0 | 1 |
| **Bobot pasangan R8–R36** | | **3** | **6** |

**Cara memakai NNZ.** NNZ adalah jumlah koefisien bukan nol pada satu baris linear. Pada daftar rute lengkap, R8 dapat memuat 10 variabel (4 kiriman masuk dan 6 kiriman keluar). R36 dapat memuat 13 variabel (6 kiriman minyak, 6 kiriman sirup, dan 1 keputusan buka gudang). Dari NNZ saja, batas atasnya adalah **min(10, 13) = 10**. Pencocokan indeks memperketat batas itu menjadi **6**. Keempat variabel kiriman masuk di R8 memang dapat muncul di R8, tetapi aturan tonase R36 hanya memuat kiriman keluar dan keputusan buka gudang.

<details>
<summary>Lihat R8 dan R36 dengan semua rute yang mungkin</summary>

```math
\begin{aligned}
\mathrm{R8}\quad &x_{1,1,B}+x_{2,1,B}+x_{3,1,B}+x_{4,1,B}\\
&\quad = z_{1,1,B}+z_{1,2,B}+z_{1,3,B}+z_{1,4,B}\\
&\qquad {}+z_{1,5,B}+z_{1,6,B}
\end{aligned}
```

```math
\begin{aligned}
\mathrm{R36}\quad &z_{1,1,A}+z_{1,2,A}+z_{1,3,A}+z_{1,4,A}\\
&{}+z_{1,5,A}+z_{1,6,A}+z_{1,1,B}+z_{1,2,B}\\
&{}+z_{1,3,B}+z_{1,4,B}+z_{1,5,B}+z_{1,6,B}\\
&\quad \le 16y_1
\end{aligned}
```

</details>

Dengan demikian, pasangan yang sama menyumbang **3 ke pembilang Low** dan **6 ke penyebut**. Pasangan lain dihitung dengan cara yang sama.

## 2. Kendala dan hubungan pada model lengkap Low

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

```math
\begin{aligned}
\mathrm{R1}\quad &x_{1,1,A}+x_{1,1,B}+x_{1,2,A} \le 8
\end{aligned}
```

**R2 · Kapasitas pabrik P2**

```math
\begin{aligned}
\mathrm{R2}\quad &x_{2,1,A}+x_{2,1,B}+x_{2,4,B} \le 8
\end{aligned}
```

**R3 · Kapasitas pabrik P3**

```math
\begin{aligned}
\mathrm{R3}\quad &x_{3,1,B}+x_{3,3,B}+x_{3,3,C}+x_{3,4,B} \le 8
\end{aligned}
```

**R4 · Kapasitas pabrik P4**

```math
\begin{aligned}
\mathrm{R4}\quad &x_{4,2,C}+x_{4,3,C} \le 8
\end{aligned}
```

**R5 · Kapasitas pabrik P5**

```math
\begin{aligned}
\mathrm{R5}\quad &x_{5,2,A}+x_{5,4,A} \le 8
\end{aligned}
```

**R6 · Kapasitas pabrik P6**

```math
\begin{aligned}
\mathrm{R6}\quad &x_{6,2,C}+x_{6,3,C} \le 8
\end{aligned}
```

</details>

<details>
<summary>R7–R17 · Neraca gudang–produk</summary>

**R7 · Neraca minyak di G1**

```math
\begin{aligned}
\mathrm{R7}\quad &x_{1,1,A}+x_{2,1,A}\\
&\quad = z_{1,1,A}+z_{1,2,A}+z_{1,3,A}+z_{1,4,A}\\
&\qquad {}+z_{1,5,A}+z_{1,6,A}
\end{aligned}
```

**R8 · Neraca sirup di G1**

```math
\begin{aligned}
\mathrm{R8}\quad &x_{1,1,B}+x_{2,1,B}+x_{3,1,B}\\
&\quad = z_{1,1,B}+z_{1,3,B}+z_{1,5,B}
\end{aligned}
```

**R9 · Neraca minyak di G2**

```math
\begin{aligned}
\mathrm{R9}\quad &x_{1,2,A}+x_{5,2,A}\\
&\quad = z_{2,1,A}+z_{2,3,A}+z_{2,4,A}+z_{2,5,A}\\
&\qquad {}+z_{2,6,A}
\end{aligned}
```

**R10 · Neraca sirup di G2**

```math
\begin{aligned}
\mathrm{R10}\quad &0\\
&\quad = 0
\end{aligned}
```

**R11 · Neraca susu di G2**

```math
\begin{aligned}
\mathrm{R11}\quad &x_{4,2,C}+x_{6,2,C}\\
&\quad = z_{2,1,C}+z_{2,2,C}+z_{2,3,C}+z_{2,4,C}\\
&\qquad {}+z_{2,5,C}+z_{2,6,C}
\end{aligned}
```

**R12 · Neraca minyak di G3**

```math
\begin{aligned}
\mathrm{R12}\quad &0\\
&\quad = 0
\end{aligned}
```

**R13 · Neraca sirup di G3**

```math
\begin{aligned}
\mathrm{R13}\quad &x_{3,3,B}\\
&\quad = z_{3,1,B}+z_{3,2,B}+z_{3,3,B}+z_{3,4,B}\\
&\qquad {}+z_{3,5,B}+z_{3,6,B}
\end{aligned}
```

**R14 · Neraca susu di G3**

```math
\begin{aligned}
\mathrm{R14}\quad &x_{3,3,C}+x_{4,3,C}+x_{6,3,C}\\
&\quad = z_{3,1,C}+z_{3,2,C}+z_{3,3,C}+z_{3,4,C}\\
&\qquad {}+z_{3,5,C}+z_{3,6,C}
\end{aligned}
```

**R15 · Neraca minyak di G4**

```math
\begin{aligned}
\mathrm{R15}\quad &x_{5,4,A}\\
&\quad = z_{4,2,A}
\end{aligned}
```

**R16 · Neraca sirup di G4**

```math
\begin{aligned}
\mathrm{R16}\quad &x_{2,4,B}+x_{3,4,B}\\
&\quad = z_{4,2,B}+z_{4,4,B}+z_{4,6,B}
\end{aligned}
```

**R17 · Neraca susu di G4**

```math
\begin{aligned}
\mathrm{R17}\quad &0\\
&\quad = 0
\end{aligned}
```

</details>

<details>
<summary>R18–R35 · Pesanan zona–produk</summary>

**R18 · Pesanan minyak di K1**

```math
\begin{aligned}
\mathrm{R18}\quad &z_{1,1,A}+z_{2,1,A} = 3
\end{aligned}
```

**R19 · Pesanan sirup di K1**

```math
\begin{aligned}
\mathrm{R19}\quad &z_{1,1,B}+z_{3,1,B} = 1
\end{aligned}
```

**R20 · Pesanan susu di K1**

```math
\begin{aligned}
\mathrm{R20}\quad &z_{2,1,C}+z_{3,1,C} = 1
\end{aligned}
```

**R21 · Pesanan minyak di K2**

```math
\begin{aligned}
\mathrm{R21}\quad &z_{1,2,A}+z_{4,2,A} = 3
\end{aligned}
```

**R22 · Pesanan sirup di K2**

```math
\begin{aligned}
\mathrm{R22}\quad &z_{3,2,B}+z_{4,2,B} = 1
\end{aligned}
```

**R23 · Pesanan susu di K2**

```math
\begin{aligned}
\mathrm{R23}\quad &z_{2,2,C}+z_{3,2,C} = 1
\end{aligned}
```

**R24 · Pesanan minyak di K3**

```math
\begin{aligned}
\mathrm{R24}\quad &z_{1,3,A}+z_{2,3,A} = 1
\end{aligned}
```

**R25 · Pesanan sirup di K3**

```math
\begin{aligned}
\mathrm{R25}\quad &z_{1,3,B}+z_{3,3,B} = 3
\end{aligned}
```

**R26 · Pesanan susu di K3**

```math
\begin{aligned}
\mathrm{R26}\quad &z_{2,3,C}+z_{3,3,C} = 1
\end{aligned}
```

**R27 · Pesanan minyak di K4**

```math
\begin{aligned}
\mathrm{R27}\quad &z_{1,4,A}+z_{2,4,A} = 1
\end{aligned}
```

**R28 · Pesanan sirup di K4**

```math
\begin{aligned}
\mathrm{R28}\quad &z_{3,4,B}+z_{4,4,B} = 3
\end{aligned}
```

**R29 · Pesanan susu di K4**

```math
\begin{aligned}
\mathrm{R29}\quad &z_{2,4,C}+z_{3,4,C} = 1
\end{aligned}
```

**R30 · Pesanan minyak di K5**

```math
\begin{aligned}
\mathrm{R30}\quad &z_{1,5,A}+z_{2,5,A} = 1
\end{aligned}
```

**R31 · Pesanan sirup di K5**

```math
\begin{aligned}
\mathrm{R31}\quad &z_{1,5,B}+z_{3,5,B} = 1
\end{aligned}
```

**R32 · Pesanan susu di K5**

```math
\begin{aligned}
\mathrm{R32}\quad &z_{2,5,C}+z_{3,5,C} = 3
\end{aligned}
```

**R33 · Pesanan minyak di K6**

```math
\begin{aligned}
\mathrm{R33}\quad &z_{1,6,A}+z_{2,6,A} = 1
\end{aligned}
```

**R34 · Pesanan sirup di K6**

```math
\begin{aligned}
\mathrm{R34}\quad &z_{3,6,B}+z_{4,6,B} = 1
\end{aligned}
```

**R35 · Pesanan susu di K6**

```math
\begin{aligned}
\mathrm{R35}\quad &z_{2,6,C}+z_{3,6,C} = 3
\end{aligned}
```

</details>

<details>
<summary>R36–R39 · Kapasitas tonase gudang</summary>

**R36 · Kapasitas tonase G1**

```math
\begin{aligned}
\mathrm{R36}\quad &z_{1,1,A}+z_{1,1,B}+z_{1,2,A}+z_{1,3,A}\\
&{}+z_{1,3,B}+z_{1,4,A}+z_{1,5,A}+z_{1,5,B}\\
&{}+z_{1,6,A}\\
&\quad \le 16y_1
\end{aligned}
```

**R37 · Kapasitas tonase G2**

```math
\begin{aligned}
\mathrm{R37}\quad &z_{2,1,A}+z_{2,1,C}+z_{2,2,C}+z_{2,3,A}\\
&{}+z_{2,3,C}+z_{2,4,A}+z_{2,4,C}+z_{2,5,A}\\
&{}+z_{2,5,C}+z_{2,6,A}+z_{2,6,C}\\
&\quad \le 20y_2
\end{aligned}
```

**R38 · Kapasitas tonase G3**

```math
\begin{aligned}
\mathrm{R38}\quad &z_{3,1,B}+z_{3,1,C}+z_{3,2,B}+z_{3,2,C}\\
&{}+z_{3,3,B}+z_{3,3,C}+z_{3,4,B}+z_{3,4,C}\\
&{}+z_{3,5,B}+z_{3,5,C}+z_{3,6,B}+z_{3,6,C}\\
&\quad \le 18y_3
\end{aligned}
```

**R39 · Kapasitas tonase G4**

```math
\begin{aligned}
\mathrm{R39}\quad &z_{4,2,A}+z_{4,2,B}+z_{4,4,B}+z_{4,6,B} \le 14y_4
\end{aligned}
```

</details>

<details>
<summary>R40–R43 · Batas waktu kerja gudang</summary>

**R40 · Batas waktu kerja G1**

```math
\begin{aligned}
\mathrm{R40}\quad &z_{1,1,A}+z_{1,1,B}+z_{1,2,A}+z_{1,3,A}\\
&{}+z_{1,3,B}+z_{1,4,A}+z_{1,5,A}+z_{1,5,B}\\
&{}+z_{1,6,A}\\
&\quad \le 19{,}2y_1
\end{aligned}
```

**R41 · Batas waktu kerja G2**

```math
\begin{aligned}
\mathrm{R41}\quad &z_{2,1,A}+z_{2,1,C}+z_{2,2,C}+z_{2,3,A}\\
&{}+z_{2,3,C}+z_{2,4,A}+z_{2,4,C}+z_{2,5,A}\\
&{}+z_{2,5,C}+z_{2,6,A}+z_{2,6,C}\\
&\quad \le 24y_2
\end{aligned}
```

**R42 · Batas waktu kerja G3**

```math
\begin{aligned}
\mathrm{R42}\quad &z_{3,1,B}+z_{3,1,C}+z_{3,2,B}+z_{3,2,C}\\
&{}+z_{3,3,B}+z_{3,3,C}+z_{3,4,B}+z_{3,4,C}\\
&{}+z_{3,5,B}+z_{3,5,C}+z_{3,6,B}+z_{3,6,C}\\
&\quad \le 21{,}6y_3
\end{aligned}
```

**R43 · Batas waktu kerja G4**

```math
\begin{aligned}
\mathrm{R43}\quad &z_{4,2,A}+z_{4,2,B}+z_{4,4,B}+z_{4,6,B} \le 16{,}8y_4
\end{aligned}
```

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

## 3. Hitung seluruh pembilang dan penyebut

### Tetapkan semua rute yang mungkin untuk penyebut

Daftar yang dipakai untuk menghitung kemungkinan bersama pada setiap pasangan disebut **acuan bersama**. Daftar ini memakai 43 kendala yang sama dan mencakup semua rute pada Low, Medium, dan High.

- **Rute masuk.** Ada 35 kombinasi pabrik, gudang, dan produk yang diizinkan rancangan. Daftarnya mengikuti rute masuk High.
- **Rute keluar.** Untuk setiap pasangan gudang–produk yang menerima kiriman pada daftar tersebut, semua zona boleh menjadi tujuan. Ada 11 pasangan gudang–produk dan 6 zona, sehingga terdapat 66 kombinasi gudang, zona, dan produk.

Untuk setiap pasangan kendala, cocokkan variabel dari dua persamaan Low untuk memperoleh bobot aktual. Ulangi pada dua persamaan yang memuat semua rute dalam daftar acuan untuk memperoleh bobot maksimum menurut rancangan. Misalnya, R36 dan R40 memakai kesembilan variabel kiriman keluar G1 dan $`y_1`$ pada Low, sehingga bobot aktualnya 10. Di acuan, tiga rute sirup tambahan dapat muncul di kedua baris, sehingga bobot maksimumnya 13.

<details>
<summary>Lihat seluruh persamaan R1–R43 dengan daftar rute maksimum</summary>

<details>
<summary>R1–R6 · Kapasitas pabrik</summary>

**R1 · Kapasitas pabrik P1**

```math
\begin{aligned}
\mathrm{R1}\quad &x_{1,1,A}+x_{1,1,B}+x_{1,2,A}+x_{1,2,B}\\
&{}+x_{1,3,B}+x_{1,4,A}+x_{1,4,B}\\
&\quad \le 8
\end{aligned}
```

**R2 · Kapasitas pabrik P2**

```math
\begin{aligned}
\mathrm{R2}\quad &x_{2,1,A}+x_{2,1,B}+x_{2,2,B}+x_{2,3,B}\\
&{}+x_{2,4,B}\\
&\quad \le 8
\end{aligned}
```

**R3 · Kapasitas pabrik P3**

```math
\begin{aligned}
\mathrm{R3}\quad &x_{3,1,A}+x_{3,1,B}+x_{3,2,A}+x_{3,2,B}\\
&{}+x_{3,3,A}+x_{3,3,B}+x_{3,3,C}+x_{3,4,A}\\
&{}+x_{3,4,B}\\
&\quad \le 8
\end{aligned}
```

**R4 · Kapasitas pabrik P4**

```math
\begin{aligned}
\mathrm{R4}\quad &x_{4,1,B}+x_{4,2,B}+x_{4,2,C}+x_{4,3,B}\\
&{}+x_{4,3,C}+x_{4,4,B}+x_{4,4,C}\\
&\quad \le 8
\end{aligned}
```

**R5 · Kapasitas pabrik P5**

```math
\begin{aligned}
\mathrm{R5}\quad &x_{5,1,A}+x_{5,2,A}+x_{5,3,A}+x_{5,4,A} \le 8
\end{aligned}
```

**R6 · Kapasitas pabrik P6**

```math
\begin{aligned}
\mathrm{R6}\quad &x_{6,2,C}+x_{6,3,C}+x_{6,4,C} \le 8
\end{aligned}
```

</details>

<details>
<summary>R7–R17 · Neraca gudang–produk</summary>

**R7 · Neraca minyak di G1**

```math
\begin{aligned}
\mathrm{R7}\quad &x_{1,1,A}+x_{2,1,A}+x_{3,1,A}+x_{5,1,A}\\
&\quad = z_{1,1,A}+z_{1,2,A}+z_{1,3,A}+z_{1,4,A}\\
&\qquad {}+z_{1,5,A}+z_{1,6,A}
\end{aligned}
```

**R8 · Neraca sirup di G1**

```math
\begin{aligned}
\mathrm{R8}\quad &x_{1,1,B}+x_{2,1,B}+x_{3,1,B}+x_{4,1,B}\\
&\quad = z_{1,1,B}+z_{1,2,B}+z_{1,3,B}+z_{1,4,B}\\
&\qquad {}+z_{1,5,B}+z_{1,6,B}
\end{aligned}
```

**R9 · Neraca minyak di G2**

```math
\begin{aligned}
\mathrm{R9}\quad &x_{1,2,A}+x_{3,2,A}+x_{5,2,A}\\
&\quad = z_{2,1,A}+z_{2,2,A}+z_{2,3,A}+z_{2,4,A}\\
&\qquad {}+z_{2,5,A}+z_{2,6,A}
\end{aligned}
```

**R10 · Neraca sirup di G2**

```math
\begin{aligned}
\mathrm{R10}\quad &x_{1,2,B}+x_{2,2,B}+x_{3,2,B}+x_{4,2,B}\\
&\quad = z_{2,1,B}+z_{2,2,B}+z_{2,3,B}+z_{2,4,B}\\
&\qquad {}+z_{2,5,B}+z_{2,6,B}
\end{aligned}
```

**R11 · Neraca susu di G2**

```math
\begin{aligned}
\mathrm{R11}\quad &x_{4,2,C}+x_{6,2,C}\\
&\quad = z_{2,1,C}+z_{2,2,C}+z_{2,3,C}+z_{2,4,C}\\
&\qquad {}+z_{2,5,C}+z_{2,6,C}
\end{aligned}
```

**R12 · Neraca minyak di G3**

```math
\begin{aligned}
\mathrm{R12}\quad &x_{3,3,A}+x_{5,3,A}\\
&\quad = z_{3,1,A}+z_{3,2,A}+z_{3,3,A}+z_{3,4,A}\\
&\qquad {}+z_{3,5,A}+z_{3,6,A}
\end{aligned}
```

**R13 · Neraca sirup di G3**

```math
\begin{aligned}
\mathrm{R13}\quad &x_{1,3,B}+x_{2,3,B}+x_{3,3,B}+x_{4,3,B}\\
&\quad = z_{3,1,B}+z_{3,2,B}+z_{3,3,B}+z_{3,4,B}\\
&\qquad {}+z_{3,5,B}+z_{3,6,B}
\end{aligned}
```

**R14 · Neraca susu di G3**

```math
\begin{aligned}
\mathrm{R14}\quad &x_{3,3,C}+x_{4,3,C}+x_{6,3,C}\\
&\quad = z_{3,1,C}+z_{3,2,C}+z_{3,3,C}+z_{3,4,C}\\
&\qquad {}+z_{3,5,C}+z_{3,6,C}
\end{aligned}
```

**R15 · Neraca minyak di G4**

```math
\begin{aligned}
\mathrm{R15}\quad &x_{1,4,A}+x_{3,4,A}+x_{5,4,A}\\
&\quad = z_{4,1,A}+z_{4,2,A}+z_{4,3,A}+z_{4,4,A}\\
&\qquad {}+z_{4,5,A}+z_{4,6,A}
\end{aligned}
```

**R16 · Neraca sirup di G4**

```math
\begin{aligned}
\mathrm{R16}\quad &x_{1,4,B}+x_{2,4,B}+x_{3,4,B}+x_{4,4,B}\\
&\quad = z_{4,1,B}+z_{4,2,B}+z_{4,3,B}+z_{4,4,B}\\
&\qquad {}+z_{4,5,B}+z_{4,6,B}
\end{aligned}
```

**R17 · Neraca susu di G4**

```math
\begin{aligned}
\mathrm{R17}\quad &x_{4,4,C}+x_{6,4,C}\\
&\quad = z_{4,1,C}+z_{4,2,C}+z_{4,3,C}+z_{4,4,C}\\
&\qquad {}+z_{4,5,C}+z_{4,6,C}
\end{aligned}
```

</details>

<details>
<summary>R18–R35 · Pesanan zona–produk</summary>

**R18 · Pesanan minyak di K1**

```math
\begin{aligned}
\mathrm{R18}\quad &z_{1,1,A}+z_{2,1,A}+z_{3,1,A}+z_{4,1,A} = 3
\end{aligned}
```

**R19 · Pesanan sirup di K1**

```math
\begin{aligned}
\mathrm{R19}\quad &z_{1,1,B}+z_{2,1,B}+z_{3,1,B}+z_{4,1,B} = 1
\end{aligned}
```

**R20 · Pesanan susu di K1**

```math
\begin{aligned}
\mathrm{R20}\quad &z_{2,1,C}+z_{3,1,C}+z_{4,1,C} = 1
\end{aligned}
```

**R21 · Pesanan minyak di K2**

```math
\begin{aligned}
\mathrm{R21}\quad &z_{1,2,A}+z_{2,2,A}+z_{3,2,A}+z_{4,2,A} = 3
\end{aligned}
```

**R22 · Pesanan sirup di K2**

```math
\begin{aligned}
\mathrm{R22}\quad &z_{1,2,B}+z_{2,2,B}+z_{3,2,B}+z_{4,2,B} = 1
\end{aligned}
```

**R23 · Pesanan susu di K2**

```math
\begin{aligned}
\mathrm{R23}\quad &z_{2,2,C}+z_{3,2,C}+z_{4,2,C} = 1
\end{aligned}
```

**R24 · Pesanan minyak di K3**

```math
\begin{aligned}
\mathrm{R24}\quad &z_{1,3,A}+z_{2,3,A}+z_{3,3,A}+z_{4,3,A} = 1
\end{aligned}
```

**R25 · Pesanan sirup di K3**

```math
\begin{aligned}
\mathrm{R25}\quad &z_{1,3,B}+z_{2,3,B}+z_{3,3,B}+z_{4,3,B} = 3
\end{aligned}
```

**R26 · Pesanan susu di K3**

```math
\begin{aligned}
\mathrm{R26}\quad &z_{2,3,C}+z_{3,3,C}+z_{4,3,C} = 1
\end{aligned}
```

**R27 · Pesanan minyak di K4**

```math
\begin{aligned}
\mathrm{R27}\quad &z_{1,4,A}+z_{2,4,A}+z_{3,4,A}+z_{4,4,A} = 1
\end{aligned}
```

**R28 · Pesanan sirup di K4**

```math
\begin{aligned}
\mathrm{R28}\quad &z_{1,4,B}+z_{2,4,B}+z_{3,4,B}+z_{4,4,B} = 3
\end{aligned}
```

**R29 · Pesanan susu di K4**

```math
\begin{aligned}
\mathrm{R29}\quad &z_{2,4,C}+z_{3,4,C}+z_{4,4,C} = 1
\end{aligned}
```

**R30 · Pesanan minyak di K5**

```math
\begin{aligned}
\mathrm{R30}\quad &z_{1,5,A}+z_{2,5,A}+z_{3,5,A}+z_{4,5,A} = 1
\end{aligned}
```

**R31 · Pesanan sirup di K5**

```math
\begin{aligned}
\mathrm{R31}\quad &z_{1,5,B}+z_{2,5,B}+z_{3,5,B}+z_{4,5,B} = 1
\end{aligned}
```

**R32 · Pesanan susu di K5**

```math
\begin{aligned}
\mathrm{R32}\quad &z_{2,5,C}+z_{3,5,C}+z_{4,5,C} = 3
\end{aligned}
```

**R33 · Pesanan minyak di K6**

```math
\begin{aligned}
\mathrm{R33}\quad &z_{1,6,A}+z_{2,6,A}+z_{3,6,A}+z_{4,6,A} = 1
\end{aligned}
```

**R34 · Pesanan sirup di K6**

```math
\begin{aligned}
\mathrm{R34}\quad &z_{1,6,B}+z_{2,6,B}+z_{3,6,B}+z_{4,6,B} = 1
\end{aligned}
```

**R35 · Pesanan susu di K6**

```math
\begin{aligned}
\mathrm{R35}\quad &z_{2,6,C}+z_{3,6,C}+z_{4,6,C} = 3
\end{aligned}
```

</details>

<details>
<summary>R36–R39 · Kapasitas tonase gudang</summary>

**R36 · Kapasitas tonase G1**

```math
\begin{aligned}
\mathrm{R36}\quad &z_{1,1,A}+z_{1,2,A}+z_{1,3,A}+z_{1,4,A}\\
&{}+z_{1,5,A}+z_{1,6,A}+z_{1,1,B}+z_{1,2,B}\\
&{}+z_{1,3,B}+z_{1,4,B}+z_{1,5,B}+z_{1,6,B}\\
&\quad \le 16y_1
\end{aligned}
```

**R37 · Kapasitas tonase G2**

```math
\begin{aligned}
\mathrm{R37}\quad &z_{2,1,A}+z_{2,2,A}+z_{2,3,A}+z_{2,4,A}\\
&{}+z_{2,5,A}+z_{2,6,A}+z_{2,1,B}+z_{2,2,B}\\
&{}+z_{2,3,B}+z_{2,4,B}+z_{2,5,B}+z_{2,6,B}\\
&{}+z_{2,1,C}+z_{2,2,C}+z_{2,3,C}+z_{2,4,C}\\
&{}+z_{2,5,C}+z_{2,6,C}\\
&\quad \le 20y_2
\end{aligned}
```

**R38 · Kapasitas tonase G3**

```math
\begin{aligned}
\mathrm{R38}\quad &z_{3,1,A}+z_{3,2,A}+z_{3,3,A}+z_{3,4,A}\\
&{}+z_{3,5,A}+z_{3,6,A}+z_{3,1,B}+z_{3,2,B}\\
&{}+z_{3,3,B}+z_{3,4,B}+z_{3,5,B}+z_{3,6,B}\\
&{}+z_{3,1,C}+z_{3,2,C}+z_{3,3,C}+z_{3,4,C}\\
&{}+z_{3,5,C}+z_{3,6,C}\\
&\quad \le 18y_3
\end{aligned}
```

**R39 · Kapasitas tonase G4**

```math
\begin{aligned}
\mathrm{R39}\quad &z_{4,1,A}+z_{4,2,A}+z_{4,3,A}+z_{4,4,A}\\
&{}+z_{4,5,A}+z_{4,6,A}+z_{4,1,B}+z_{4,2,B}\\
&{}+z_{4,3,B}+z_{4,4,B}+z_{4,5,B}+z_{4,6,B}\\
&{}+z_{4,1,C}+z_{4,2,C}+z_{4,3,C}+z_{4,4,C}\\
&{}+z_{4,5,C}+z_{4,6,C}\\
&\quad \le 14y_4
\end{aligned}
```

</details>

<details>
<summary>R40–R43 · Batas waktu kerja gudang</summary>

**R40 · Batas waktu kerja G1**

```math
\begin{aligned}
\mathrm{R40}\quad &z_{1,1,A}+z_{1,2,A}+z_{1,3,A}+z_{1,4,A}\\
&{}+z_{1,5,A}+z_{1,6,A}+z_{1,1,B}+z_{1,2,B}\\
&{}+z_{1,3,B}+z_{1,4,B}+z_{1,5,B}+z_{1,6,B}\\
&\quad \le 19{,}2y_1
\end{aligned}
```

**R41 · Batas waktu kerja G2**

```math
\begin{aligned}
\mathrm{R41}\quad &z_{2,1,A}+z_{2,2,A}+z_{2,3,A}+z_{2,4,A}\\
&{}+z_{2,5,A}+z_{2,6,A}+z_{2,1,B}+z_{2,2,B}\\
&{}+z_{2,3,B}+z_{2,4,B}+z_{2,5,B}+z_{2,6,B}\\
&{}+z_{2,1,C}+z_{2,2,C}+z_{2,3,C}+z_{2,4,C}\\
&{}+z_{2,5,C}+z_{2,6,C}\\
&\quad \le 24y_2
\end{aligned}
```

**R42 · Batas waktu kerja G3**

```math
\begin{aligned}
\mathrm{R42}\quad &z_{3,1,A}+z_{3,2,A}+z_{3,3,A}+z_{3,4,A}\\
&{}+z_{3,5,A}+z_{3,6,A}+z_{3,1,B}+z_{3,2,B}\\
&{}+z_{3,3,B}+z_{3,4,B}+z_{3,5,B}+z_{3,6,B}\\
&{}+z_{3,1,C}+z_{3,2,C}+z_{3,3,C}+z_{3,4,C}\\
&{}+z_{3,5,C}+z_{3,6,C}\\
&\quad \le 21{,}6y_3
\end{aligned}
```

**R43 · Batas waktu kerja G4**

```math
\begin{aligned}
\mathrm{R43}\quad &z_{4,1,A}+z_{4,2,A}+z_{4,3,A}+z_{4,4,A}\\
&{}+z_{4,5,A}+z_{4,6,A}+z_{4,1,B}+z_{4,2,B}\\
&{}+z_{4,3,B}+z_{4,4,B}+z_{4,5,B}+z_{4,6,B}\\
&{}+z_{4,1,C}+z_{4,2,C}+z_{4,3,C}+z_{4,4,C}\\
&{}+z_{4,5,C}+z_{4,6,C}\\
&\quad \le 16{,}8y_4
\end{aligned}
```

</details>

</details>

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

```math
\mathrm{WCC}_{\mathrm{Low}}
=\frac{\text{total bobot aktual Low}}{\text{total bobot maksimum menurut daftar rute}}\times 100\%
=\frac{236}{435}\times 100\%
\approx 54{,}25\%.
```

## 4. Ringkasan hasil

| Tingkat | Rute masuk | Rute keluar | Pembilang | Penyebut tetap | WCC |
| --- | ---: | ---: | ---: | ---: | ---: |
| Low | 16 | 36 | 236 | 435 | **54,25%** |
| Medium | 21 | 43 | 283 | 435 | **65,06%** |
| High | 35 | 57 | 381 | 435 | **87,59%** |

Ketiga tingkat menggunakan 43 aturan operasi yang sama. Variabel kiriman bertambah ketika daftar rute bertambah. Pada satu tingkat, WCC operasi sama untuk P1–P8. Audit memeriksa skenario stokastik satu per satu. Batas emisi, domain variabel, pemilihan emisi saat biaya sama, dan garis singgung solver berada di luar 43 baris yang dihitung.

[Model matematika](math_model_acuan/Model_Matematika.md) · [Data rute](case/Data_Bersama.json) · [Audit 24 kombinasi](math_model_acuan/hasil/WCC.csv) · [Halaman utama](README.md)
