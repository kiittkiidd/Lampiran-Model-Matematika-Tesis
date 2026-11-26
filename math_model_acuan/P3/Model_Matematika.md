# Profil 3 — Model acuan linear deterministik dengan dua tujuan

Pilih lokasi gudang dan alokasi pengiriman untuk menyeimbangkan biaya dan emisi. P3 menggunakan permintaan pasti, jaringan, tarif, dan kapasitas P1 untuk masing-masing tingkat. [Kasus P3](../../case/P3/Kasus.md) · [Audit WCC](Audit_WCC.md) · [Hasil verifikasi dan waktu](../Hasil_Benchmark.md)

## 1. Notasi dan keputusan

| Simbol | Makna |
| --- | --- |
| $x_{i,g,p}$ | Palet produk $p$ yang dikirim dari pabrik $i$ ke gudang $g$ |
| $z_{g,j,p}$ | Palet produk $p$ yang dikirim dari gudang $g$ ke pelanggan $j$ |
| $y_g$ | Bernilai 1 jika gudang $g$ dibuka dan 0 jika tutup |
| $\kappa_g$ | Emisi tetap saat gudang $g$ beroperasi pada periode ini |
| $e_{ig}^{\mathrm{in}}$ | Emisi angkut satu palet dari pabrik $i$ ke gudang $g$ |
| $e_{gj}^{\mathrm{out}}$ | Emisi angkut satu palet dari gudang $g$ ke pelanggan $j$ |
| $E_{\ell}^{\mathrm{in}}, E_{\ell}^{\mathrm{out}}$ | Himpunan rute masuk dan keluar pada tingkat $\ell$ |

Sebagai contoh, $x_{1,2,A}=2$ berarti dua palet A dikirim dari P1 ke G2. Penetapan satu $y_g$ berlaku untuk seluruh produk.

## 2. Dua fungsi tujuan

Biaya total memakai persamaan P1.

```math
\begin{aligned}
C(x,z,y) ={}& \sum_g F_g y_g
+ \sum_{(i,g,p)\in E_{\ell}^{\mathrm{in}}} c_{i,g,p}^{\mathrm{in}} x_{i,g,p} \\
&+ \sum_{(g,j,p)\in E_{\ell}^{\mathrm{out}}}
(c_{g,j,p}^{\mathrm{out}}+h_{g,p}) z_{g,j,p}.
\end{aligned}
```

Sebagai contoh, membuka G2 menambah biaya tetap 31. Jika G2 mengirim dua palet A ke K1, biaya tambahan angkut dan penanganannya $2(1+2)=6$.

Emisi total menjumlahkan emisi tetap gudang dan emisi angkut.

```math
\begin{aligned}
E(x,z,y) ={}& \sum_g \kappa_g y_g
+ \sum_{(i,g,p)\in E_{\ell}^{\mathrm{in}}} e_{ig}^{\mathrm{in}} x_{i,g,p} \\
&+ \sum_{(g,j,p)\in E_{\ell}^{\mathrm{out}}} e_{gj}^{\mathrm{out}} z_{g,j,p}.
\end{aligned}
```

Membuka G2 menyumbang 20 kg CO₂e. Memindahkan dua palet A dari P1 melalui G2 ke K1 menyumbang tambahan $2(1{,}8+0{,}9)=5{,}4$ kg CO₂e. Kedua ekspresi memakai variabel arus dan lokasi yang telah ada di P1.

## 3. Kendala operasi dan domain

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

Saat $y_g=0$, semua kiriman keluar nol karena variabel arus nonnegatif. K2 kemudian membuat arus masuk gudang juga nol. Saat $y_g=1$, gudang dapat menyalurkan sampai $U_g$ palet untuk seluruh produknya. Contoh di Low. G2 menyalurkan 10 palet A dan 10 palet C. Seluruh arus itu memakai 20 dari 20 palet kapasitas G2.

### Kendala domain variabel

```math
\begin{aligned}
x_{i,g,p} &\in \mathbb{R}_{\ge 0} &&\forall (i,g,p)\in E_{\ell}^{\mathrm{in}},\\
z_{g,j,p} &\in \mathbb{R}_{\ge 0} &&\forall (g,j,p)\in E_{\ell}^{\mathrm{out}},\\
y_g &\in \{0,1\} &&\forall g.
\end{aligned}
```

Arus kiriman kontinu dan nonnegatif. Keputusan buka gudang biner. Audit WCC menggunakan baris fungsional R1–R39 pada jaringan.

Contoh rencana pengiriman Low yang memenuhi R1–R39 adalah membuka G2 dan G3. Kelayakannya untuk suatu batas emisi juga bergantung pada R40. [Rincian kiriman per pelanggan](../P1/Model_Matematika.md#contoh-rencana-pengiriman-low)

## 4. Menemukan alternatif biaya dan emisi

Untuk satu batas emisi $\epsilon$, selesaikan MILP berikut.

```math
\begin{aligned}
\min \quad & C(x,z,y) \\
\text{dengan} \quad & \text{kendala R1 sampai R39 dan domain variabel}, \\
& E(x,z,y) \le \epsilon \qquad \text{(R40)}.
\end{aligned}
```

Jika $\epsilon=145$, model mencari biaya paling rendah di antara rencana yang emisinya paling banyak 145 kg CO₂e. Untuk menyusun lima titik per tingkat, cari dahulu emisi minimum dan biaya minimum. Pada ujung biaya minimum, pilih emisi terendah di antara solusi dengan biaya minimum. Gunakan emisi dari kedua ujung sebagai batas rentang. Ambil batas pada 0%, 25%, 50%, 75%, dan 100% dari rentang tersebut. Pada tiga titik interior, pilih emisi terendah di antara solusi dengan biaya minimum pada batas itu. Pada ujung emisi minimum, pilih biaya terendah. Notebook memakai toleransi numerik $10^{-7}$ pada batas pemecah seri.

Lima titik ini adalah pilihan untuk memeriksa trade-off. Arus kontinu dapat menghasilkan titik lain di antara batas yang diuji. Periksa tiap optimum dengan enumerasi 16 pola gudang dan LP arus untuk tiap pola.

## 5. WCC jaringan dan WCC formulasi batas emisi

Gunakan R1–R39 untuk membandingkan jaringan P1–P3 pada skala yang sama. Dalam formulasi $\epsilon$-constraint, R40 adalah kendala fungsional tambahan. [Audit P3](Audit_WCC.md) melaporkan penghitungan yang mencakup R40.

[Notebook verifikasi](../Verifikasi_P1_P2_P3.ipynb) · [Buka di Google Colab](https://colab.research.google.com/github/kiittkiidd/Lampiran-Model-Matematika-Tesis/blob/main/math_model_acuan/Verifikasi_P1_P2_P3.ipynb)
