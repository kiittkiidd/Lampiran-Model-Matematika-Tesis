# Profil 1 — Model matematika lokasi gudang dan alokasi kiriman

Perusahaan memilih calon gudang yang dibuka dan menentukan kiriman produk dari pabrik ke gudang lalu ke pelanggan. Model ini menggunakan satu periode, permintaan deterministik, dan satu tujuan biaya minimum. Ketiga tingkat memakai jaringan distribusi Profil 1 yang terdiri atas enam pabrik, empat calon gudang, enam pelanggan, dan tiga produk.

## 1. Kasus dan jaringan

Produk A adalah minuman kemasan, B pangan kering, dan C produk dingin. Untuk setiap tingkat dan produk, setiap pabrik pada tabel dapat memasok setiap gudang yang tercantum. Pada Low dan Medium, setiap gudang dalam satu baris produk dapat memasok setiap pelanggan pada baris yang sama. Pada High, jalur keluar dibentuk dengan aturan wilayah yang dijelaskan di bawah. Satu gudang fisik memiliki satu keputusan buka, satu kapasitas gabungan untuk semua produk, dan satu biaya buka.

| Tingkat | Produk | Pabrik yang dapat memasok | Gudang yang dapat menangani | Pelanggan yang membutuhkan | Jalur masuk | Jalur keluar |
| --- | --- | --- | --- | --- | ---: | ---: |
| L | A | P1, P5 | G1, G2, G4 | K1, K2 | 6 | 6 |
| L | B | P2, P3 | G1, G3, G4 | K3, K4 | 6 | 6 |
| L | C | P4, P6 | G2, G3 | K5, K6 | 4 | 4 |
| M | A | P1, P5 | G1, G2, G4 | K1, K2, K5, K6 | 6 | 12 |
| M | B | P1, P2, P3 | G1, G2, G3, G4 | K1, K2, K3, K4 | 12 | 16 |
| M | C | P4, P6 | G2, G3 | K3, K4, K5, K6 | 4 | 8 |
| H | A | P1, P3, P5 | G1, G2, G3, G4 | K1, K2, K3, K4, K5, K6 | 12 | 18 |
| H | B | P1, P2, P3, P4 | G1, G2, G3, G4 | K1, K2, K3, K4, K5, K6 | 16 | 20 |
| H | C | P4, P6 | G2, G3, G4 | K1, K2, K3, K4, K5, K6 | 6 | 13 |

Contoh Low untuk A. P1 dan P5 dapat mengirim A ke G1, G2, dan G4, sehingga ada $2\times3=6$ jalur masuk A. Ketiga gudang itu dapat memasok A ke K1 dan K2, sehingga ada $3\times2=6$ jalur keluar A. Setiap jalur membentuk satu variabel arus dengan indeks produk lengkap.

### Jalur keluar High dan cakupan acuan

Cakupan acuan adalah seluruh kombinasi pabrik, gudang, dan pelanggan yang kompatibel pada baris High di tabel produk. Dengan cakupan ini ada 34 jalur masuk dan 66 jalur keluar. Acuan ditetapkan untuk mengukur kapasitas hubungan pada skala bersama.

High menggunakan semua 34 jalur masuk. Untuk jalur keluar, High mempertahankan seluruh 36 jalur Medium, termasuk jalur lintas wilayah yang sudah ada. Dari rute kompatibel yang masih tersedia, High menambah 15 jalur keluar dengan gudang dan pelanggan di wilayah yang sama. Hasilnya 51 jalur keluar. Semua pelanggan tetap dapat menerima A, B, dan C.

| Gudang | Produk | Pelanggan dari jalur Medium | Pelanggan dari jalur baru sewilayah | Total jalur High |
| --- | --- | --- | --- | ---: |
| G1 | A | K1, K2, K5, K6 | K3 | 5 |
| G1 | B | K1, K2, K3, K4 | K5 | 5 |
| G2 | A | K1, K2, K5, K6 | K3 | 5 |
| G2 | B | K1, K2, K3, K4 | K5 | 5 |
| G2 | C | K3, K4, K5, K6 | K1 | 5 |
| G3 | A | — | K2, K4, K6 | 3 |
| G3 | B | K1, K2, K3, K4 | K6 | 5 |
| G3 | C | K3, K4, K5, K6 | K2 | 5 |
| G4 | A | K1, K2, K5, K6 | K4 | 5 |
| G4 | B | K1, K2, K3, K4 | K6 | 5 |
| G4 | C | — | K2, K4, K6 | 3 |

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

Setiap pelanggan membutuhkan total 5 palet per periode, sehingga total sistem adalah 30 palet. Di Low, K1 dan K2 masing-masing meminta 5 palet A, K3 dan K4 masing-masing 5 palet B, dan K5 dan K6 masing-masing 5 palet C. Pada Medium dan High, $d_{jp}^{(\ell)}$ adalah permintaan per pelanggan dan produk. Total setiap pelanggan tetap 5 palet. Produk yang tercantum di tabel jaringan mempunyai permintaan positif dan pasangan pelanggan–produk di luar tabel mempunyai permintaan nol.

Tarif per jalur dan pembagian 5 palet per produk pada Medium dan High masih berupa parameter. Perhitungan WCC memakai rute dan kemunculan variabel yang sudah ditetapkan. Perhitungan optimum biaya memerlukan tarif per jalur pada ketiga tingkat dan pembagian permintaan pada Medium dan High.

| Notasi | Arti |
| --- | --- |
| $i,g,j,p$ | Indeks pabrik, gudang, pelanggan, dan produk |
| $\ell$ | Tingkat L, M, atau H |
| $E_{\ell}^{\mathrm{in}}$ | Himpunan tripel $(i,g,p)$ yang diizinkan sesuai tabel jaringan |
| $E_{\ell}^{\mathrm{out}}$ | Himpunan tripel $(g,j,p)$ yang diizinkan sesuai tabel jaringan |
| $C_i$ | Kapasitas total pabrik $i$, dalam palet |
| $U_g,F_g$ | Kapasitas total dan biaya buka tetap gudang $g$ per periode |
| $c_{igp}^{\mathrm{in}},c_{gjp}^{\mathrm{out}}$ | Tarif per palet pada jalur masuk dan keluar |
| $d_{jp}^{(\ell)}$ | Permintaan pelanggan $j$ untuk produk $p$ pada tingkat $\ell$, dalam palet |

| Variabel keputusan | Makna | Domain |
| --- | --- | --- |
| $x_{i,g,p}$ | Palet produk $p$ dari pabrik $i$ ke gudang $g$ | Kontinu nonnegatif pada $E_{\ell}^{\mathrm{in}}$ |
| $z_{g,j,p}$ | Palet produk $p$ dari gudang $g$ ke pelanggan $j$ | Kontinu nonnegatif pada $E_{\ell}^{\mathrm{out}}$ |
| $y_g$ | Status buka gudang $g$ | Biner, dengan 1 untuk buka dan 0 untuk tutup |

Sebagai contoh, $x_{1,2,A}$ mengukur kiriman A dari P1 ke G2 dan $z_{2,1,A}$ mengukur kiriman A dari G2 ke K1. Keduanya dihitung dalam neraca A di G2.

## 3. Fungsi tujuan dan seluruh keluarga kendala

### Fungsi tujuan — biaya buka dan angkut minimum

```math
\min\quad
\sum_g F_g y_g
+\sum_{(i,g,p)\in E_{\ell}^{\mathrm{in}}} c_{igp}^{\mathrm{in}}x_{i,g,p}
+\sum_{(g,j,p)\in E_{\ell}^{\mathrm{out}}} c_{gjp}^{\mathrm{out}}z_{g,j,p}.
```

Biaya buka dibayar sekali untuk tiap gudang. Biaya angkut dihitung per palet pada dua tahap pengiriman. Misalnya, membuka G2 menambah 31 satuan biaya tetap dan mengirim 5 palet pada satu jalur menambah lima kali tarif jalur itu.

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

Untuk satu gudang dan produk, jumlah barang masuk sama dengan jumlah barang keluar pada periode yang sama. Di Low, R7 adalah $x_{1,1,A}+x_{5,1,A}=z_{1,1,A}+z_{1,2,A}$. Jika G1 menerima 5 palet A, total A yang dikirim dari G1 ke K1 dan K2 juga 5 palet. Daftar acuan berisi 11 pasangan gudang–produk. G1–C berada di luar daftar karena G1 tidak menangani C pada ketiga tingkat.

### K3 — pemenuhan permintaan pelanggan per produk — R18 sampai R35

```math
\sum_{g:(g,j,p)\in E_{\ell}^{\mathrm{out}}} z_{g,j,p}
=d_{jp}^{(\ell)}
\qquad \text{untuk tiap pasangan }(j,p).
```

Untuk satu pelanggan dan produk, kiriman dari gudang yang melayaninya harus berjumlah tepat sebesar permintaan. Di Low, R18 adalah $z_{1,1,A}+z_{2,1,A}+z_{4,1,A}=5$. Lima palet A untuk K1 dapat dipenuhi seluruhnya dari G2 atau melalui pembagian di antara beberapa gudang yang diizinkan. Pasangan tanpa permintaan dan tanpa jalur menghasilkan $0=0$ pada daftar audit.

### K4 — kapasitas dan keputusan buka gudang — R36 sampai R39

```math
\sum_{(j,p):(g,j,p)\in E_{\ell}^{\mathrm{out}}} z_{g,j,p}
\le U_gy_g
\qquad \text{untuk tiap gudang }g.
```

Saat $y_g=0$, semua kiriman keluar nol karena variabel arus nonnegatif. K2 kemudian membuat arus masuk gudang juga nol. Saat $y_g=1$, gudang dapat menyalurkan sampai $U_g$ palet untuk seluruh produknya. Dalam contoh Low, G2 bisa menyalurkan 10 palet A dan 5 palet C, sehingga memakai 15 dari 20 palet kapasitasnya.

### Domain

```math
x_{i,g,p}\ge 0,\qquad z_{g,j,p}\ge 0,\qquad y_g\in\{0,1\}.
```

Satu rencana layak Low menggunakan G2 dan G3. Kirim masing-masing 5 palet melalui jalur P1–G2–K1 (A), P5–G2–K2 (A), P2–G3–K3 (B), P3–G3–K4 (B), P4–G2–K5 (C), dan P6–G3–K6 (C). G2 dan G3 masing-masing menangani 15 palet dan setiap pabrik mengirim 5 palet.

## 4. WCC model utama

Untuk audit, 39 posisi baris memiliki ID yang sama untuk ketiga tingkat. Daftar ini memuat 6 batas kapasitas pabrik, 11 neraca gudang–produk, 18 persamaan pelanggan–produk, dan 4 batas kapasitas gudang. Posisi yang berupa $0=0$ mempunyai NNZ nol dan irisan kosong. Jumlah baris dengan variabel aktif dilaporkan terpisah.

Untuk tiap baris $r$, $S_r^{(\ell)}$ memuat variabel dengan koefisien selain nol setelah indeks dijabarkan. $U_r^{\mathrm{ref}}$ memuat variabel yang diizinkan muncul pada baris tersebut oleh cakupan jalur acuan. Identitas variabel mencakup jenis arus dan seluruh indeks. Fungsi tujuan dan deklarasi domain berada di luar daftar baris fungsional.

```math
\begin{aligned}
B_\ell &=\sum_{(r,s)\in P}\lvert S_r^{(\ell)}\cap S_s^{(\ell)}\rvert,\\
D_{\mathrm{ref}} &=\sum_{(r,s)\in P}\lvert U_r^{\mathrm{ref}}\cap U_s^{\mathrm{ref}}\rvert,\\
\mathrm{WCC}_\ell &=100\%\times\frac{B_\ell}{D_{\mathrm{ref}}}.
\end{aligned}
```

$P$ mencatat setiap pasangan dua baris berbeda sekali. Cakupan acuan adalah jaringan kompatibilitas penuh pada bagian 1, dengan 34 jalur masuk dan 66 jalur keluar. Ketiga tingkat adalah bagian dari cakupan ini. High menggunakan 34 jalur masuk dan 51 jalur keluar, dengan bobot aktual 187 dari batas total 232.

| Tingkat | Jalur masuk | Jalur keluar | Variabel | Baris dengan variabel | NNZ | Pasangan berbobot positif | Total bobot aktual | WCC |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| L | 16 | 16 | 36 | 24 | 84 | 56 | 64 | 27,59% |
| M | 22 | 36 | 62 | 31 | 156 | 103 | 130 | 56,03% |
| H | 34 | 51 | 89 | 39 | 225 | 147 | 187 | 80,60% |

Penyebut bersama adalah **232**. Satu variabel kiriman masuk muncul di dua kendala dan menyumbang 1 poin bobot. Satu variabel kiriman keluar muncul di tiga kendala dan menyumbang 3 poin. Empat variabel buka gudang masing-masing muncul pada satu baris kapasitas. Penjabaran lengkap R1–R39, contoh perhitungan pasangan, dan audit 741 pasangan ada di lampiran. [Lampiran WCC](Tutorial_Weighted_Constraint_Coupling.md)
