# Profil 2 — Model acuan stokastik dua tahap

P2 menggunakan jaringan dan biaya dari P1. Permintaan A di K1 baru terungkap setelah keputusan membuka gudang dibuat. Jalankan tiga instans Low, Medium, dan High. Model berbentuk MILP untuk tiga skenario diskret. [Kasus P2](../../case/P2/Kasus.md) · [Kasus dan data bersama](../../case/P1/Kasus.md) · [Audit WCC dan hasil optimasi](Audit_WCC.md)

## 1. Parameter dan tahap keputusan

Gunakan indeks pabrik $i$, gudang $g$, pelanggan $j$, produk $p$, level $\ell$, dan skenario $s$. Himpunan jalur masuk $E_{\ell}^{\mathrm{in}}$ dan keluar $E_{\ell}^{\mathrm{out}}$ sama seperti P1 di level yang bersesuaian. Kapasitas pabrik adalah $C_i$, kapasitas gudang $U_g$, dan biaya buka $F_g$. Ketiga tarif per palet didefinisikan sebagai berikut.

```math
\begin{aligned}
c_{i,g,p}^{\mathrm{in}}&\quad\text{tarif angkut per palet dari pabrik }i\text{ ke gudang }g,\\
c_{g,j,p}^{\mathrm{out}}&\quad\text{tarif angkut per palet dari gudang }g\text{ ke pelanggan }j,\\
h_{g,p}&\quad\text{tarif penanganan per palet produk }p\text{ di gudang }g.
\end{aligned}
```

| Tahap | Variabel | Keputusan |
| --- | --- | --- |
| Sebelum permintaan diketahui | $y_g$ biner | Buka atau tutup gudang $g$. Nilainya satu untuk semua skenario. |
| Setelah skenario diketahui | $x^s_{i,g,p}$ kontinu nonnegatif | Kiriman dari pabrik $i$ ke gudang $g$ pada skenario $s$. |
| Setelah skenario diketahui | $z^s_{g,j,p}$ kontinu nonnegatif | Kiriman dari gudang $g$ ke pelanggan $j$ pada skenario $s$. |

### Dari distribusi ke skenario

Misalkan $\mu=d_{1,A}=3$ dari P1 dan $\sigma=1$ palet. Pada normal baku, $q=\Phi(-1)=0{,}1586552539\ldots$ adalah peluang satu ekor dan $a=\phi(1)/q=1{,}5251352762\ldots$ adalah nilai absolut rata-rata kondisional ekor. $\Phi$ dan $\phi$ menyatakan fungsi distribusi kumulatif dan fungsi kepadatan normal baku.

| Skenario | Peluang $\pi_s$ | Permintaan A di K1 |
| --- | ---: | --- |
| Sepi | $q$ | $\mu-a\sigma$ |
| Sedang | $1-2q$ | $\mu$ |
| Ramai | $q$ | $\mu+a\sigma$ |

Tuliskan permintaan skenario sebagai $d_{jp}^{\ell,s}$. Hanya $d_{1,A}^{\ell,s}$ yang berubah. Simetri skenario membuat rata-rata tertimbang permintaan tetap tepat $\mu$. Data lengkap memakai presisi penuh dari [Data bersama](../../case/Data_Bersama.json). Model mengharuskan pemenuhan untuk tiga titik skenario yang ditetapkan. Rata-rata kondisional ekor atas mewakili permintaan Ramai pada model diskret.

## 2. Fungsi tujuan

```math
\begin{aligned}
\min\quad &\sum_g F_g y_g + \sum_s \pi_s\,O_s(x^s,z^s),\\
O_s(x^s,z^s)
&=\sum_{(i,g,p)\in E_{\ell}^{\mathrm{in}}}c_{i,g,p}^{\mathrm{in}}x^s_{i,g,p}\\
&\quad +\sum_{(g,j,p)\in E_{\ell}^{\mathrm{out}}}
(c_{g,j,p}^{\mathrm{out}}+h_{g,p})z^s_{g,j,p}.
\end{aligned}
```

$O_s$ adalah biaya operasi dalam skenario $s$. Biaya buka masuk sekali karena gudang dipilih satu kali. Biaya angkut masuk, angkut keluar, dan penanganan masuk ke rata-rata tertimbang biaya operasi.

## 3. Kendala pada tiap skenario

Setiap skenario memakai R1–R39 dari P1. Variabel arus mendapat indeks skenario dan setiap baris kapasitas gudang merujuk pada $y_g$ yang sama.

**R1–R6 · kapasitas pabrik**

```math
\sum_{(g,p):(i,g,p)\in E_{\ell}^{\mathrm{in}}}x_{i,g,p}^s \le C_i
\qquad \forall i,s.
```

Total kiriman gabungan semua produk dari pabrik $i$ dibatasi untuk setiap skenario.

**R7–R17 · neraca gudang–produk**

```math
\sum_{i:(i,g,p)\in E_{\ell}^{\mathrm{in}}} x^s_{i,g,p}
=
\sum_{j:(g,j,p)\in E_{\ell}^{\mathrm{out}}}z^s_{g,j,p}
\qquad \forall (g,p),s.
```

Untuk setiap pasangan gudang–produk pada daftar acuan, jumlah yang masuk harus sama dengan jumlah yang keluar di skenario yang sama.

**R18–R35 · pemenuhan permintaan**

```math
\sum_{g:(g,j,p)\in E_{\ell}^{\mathrm{out}}}z^s_{g,j,p}
=d_{jp}^{\ell,s}
\qquad \forall j,p,s.
```

Sebagai contoh, R18 di Low memuat $z^s_{1,1,A}+z^s_{2,1,A}=d_{1,A}^{L,s}$. Ruas kanannya sekitar 1,474865, 3, atau 4,525135 palet. Daftar jalurnya sama pada ketiga skenario.

**R36–R39 · kapasitas dan buka gudang**

```math
\sum_{(j,p):(g,j,p)\in E_{\ell}^{\mathrm{out}}}z^s_{g,j,p}
\le U_gy_g
\qquad \forall g,s.
```

Jika $y_g=0$, kiriman keluar gudang tersebut nol pada semua skenario. Jika $y_g=1$, kapasitas $U_g$ berlaku di masing-masing skenario. Biaya buka dan keputusan $y_g$ tetap dimodelkan sekali.

### Kendala domain variabel

```math
\begin{aligned}
x^s_{i,g,p} &\in \mathbb{R}_{\ge 0} &&\forall (i,g,p)\in E_{\ell}^{\mathrm{in}},\ \forall s,\\
z^s_{g,j,p} &\in \mathbb{R}_{\ge 0} &&\forall (g,j,p)\in E_{\ell}^{\mathrm{out}},\ \forall s,\\
y_g &\in \{0,1\} &&\forall g.
\end{aligned}
```

Arus kiriman kontinu dan nonnegatif. Keputusan buka gudang biner. Audit WCC menggunakan baris fungsional R1–R39 pada setiap blok. Indeks skenario berlaku untuk arus. Satu keputusan buka per gudang berlaku pada semua skenario.

## 4. Cara memeriksa hasil

Dengan satu pola buka gudang yang tetap, arus paling murah dapat dihitung lewat satu program linear per skenario. Jumlahkan biaya buka dan biaya operasi berbobot peluang. Ulangi untuk seluruh 16 pola buka gudang, lalu pilih pola layak dengan biaya minimum. Notebook juga menyelesaikan MILP gabungan dengan satu set $y_g$ dan mencocokkan nilai optimum kedua metode. [Notebook verifikasi P1–P3](../Verifikasi_P1_P2_P3.ipynb) · [Buka di Google Colab](https://colab.research.google.com/github/kiittkiidd/Lampiran-Model-Matematika-Tesis/blob/main/math_model_acuan/Verifikasi_P1_P2_P3.ipynb)
