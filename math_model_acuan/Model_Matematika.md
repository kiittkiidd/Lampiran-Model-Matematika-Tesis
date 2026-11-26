# Model matematika acuan P1–P8

Untuk tiap tingkat, delapan profil memakai indeks variabel, domain, dan posisi kendala yang sama. Gunakan [kasus dasar](../case/Kasus_Dasar.md) dan [matriks profil](../case/Profil_P1_P8.md).

## 1. Indeks dan keputusan

| Notasi | Makna |
| --- | --- |
| $i,g,j,p,s$ | Pabrik, gudang, pelanggan, produk, skenario |
| $A^{\mathrm{in}},A^{\mathrm{out}}$ | Himpunan rute aktif pada tingkat yang dipilih |
| $x_{i,g,p,s}$ | Palet produk dari pabrik $i$ ke gudang $g$ pada skenario $s$ |
| $z_{g,j,p,s}$ | Palet produk dari gudang $g$ ke pelanggan $j$ pada skenario $s$ |
| $y_g$ | Biner. Satu berarti gudang $g$ dibuka untuk semua skenario |
| $d_{j,p,s}$ | Pesanan per pelanggan, produk, dan skenario |
| $C_i,U_g,T_g$ | Kapasitas pabrik, kapasitas fisik gudang, dan anggaran waktu gudang |

Arus pada rute aktif boleh pecahan. Sebagai contoh, $z_{2,1,A,3}=2$ berarti G2 mengirim dua palet A ke K1 pada skenario Ramai. Keputusan membuka G2 tetap sama pada ketiga skenario.

```math
x_{i,g,p,s} \in \mathbb{R}_{\ge 0},\qquad
z_{g,j,p,s} \in \mathbb{R}_{\ge 0},\qquad
y_g \in \{0,1\}.
```

## 2. Kendala operasi

Untuk ringkasnya, penjumlahan berikut hanya menggunakan variabel pada rute aktif. Ada 39 posisi kendala pada setiap skenario. Sebelas posisi neraca mengikuti kombinasi gudang–produk pada jaringan acuan. Bila satu kombinasi belum aktif pada tingkat tertentu, posisinya berupa $0=0$.

### Kapasitas pabrik

```math
\sum_{g,p}x_{i,g,p,s}\le C_i\qquad \forall i,s.
```

Setiap pabrik menyediakan delapan palet gabungan. Apabila lima palet dikirim ke G2, pabrik masih dapat mengirim total tiga palet ke gudang lain pada skenario itu.

### Neraca gudang dan produk

```math
\sum_i x_{i,g,p,s}= \sum_j z_{g,j,p,s}\qquad \forall (g,p),s.
```

Jika G2 menerima enam palet A, jumlah A yang dikirim G2 ke semua pelanggan harus enam palet. Neraca dihitung per produk.

### Pemenuhan pesanan

```math
\sum_g z_{g,j,p,s}=d_{j,p,s}\qquad \forall j,p,s.
```

Jika K1 memesan tiga palet A, satu palet dari G1 dan dua palet dari G2 sudah memenuhi pesanan. Pada profil stokastik, nilai pesanan A di K1 mengikuti skenario.

### Kapasitas fisik gudang

```math
\sum_{j,p}z_{g,j,p,s}\le U_g y_g\qquad \forall g,s.
```

Jika G2 buka, ia dapat menyalurkan sampai 20 palet pada setiap skenario. Jika G2 tutup, arus keluar nol dan neraca membuat arus masuk nol juga.

## 3. Batas emisi dan waktu penanganan

Definisikan volume produk melalui gudang $g$ pada skenario $s$ sebagai singkatan ekspresi $Q_{g,p,s}=\sum_j z_{g,j,p,s}$. Angka ini dihitung dari arus keluar. Daftar variabel keputusan tetap terdiri dari $x,z,y$.

### Batas emisi · R118

```math
\begin{aligned}
E(x,z,y)
={}& \sum_g \kappa_g y_g+
\sum_s\pi_s\left(\sum_{i,g,p}e^{\mathrm{in}}_{i,g}x_{i,g,p,s}
+\sum_{g,j,p}e^{\mathrm{out}}_{g,j}z_{g,j,p,s}\right),\\
E(x,z,y) &\le \epsilon.
\end{aligned}
```

$\kappa_g$ adalah emisi tetap gudang. Faktor emisi angkut masuk $e^{\mathrm{in}}_{i,g}$ dan keluar $e^{\mathrm{out}}_{g,j}$ memakai kg CO₂e per palet. $\pi_s$ adalah peluang skenario. Jika $\epsilon=145$, emisi harapan seluruh jaringan paling banyak 145 kg CO₂e. Pada profil pasti, ketiga skenario menggunakan pesanan identik dan salah satu solusi optimal dapat memakai arus identik.

Batas 330 untuk tujuan tunggal berlaku longgar. Emisi tetap maksimum adalah 64 kg CO₂e. Tarif emisi angkut masuk dan keluar tertinggi masing-masing 4,7 dan 3,7. Dengan 30 palet harapan dan dua tahap angkut, batas analitis emisi adalah $64+30(4{,}7+3{,}7)=316$ kg CO₂e.

### Anggaran waktu penanganan · R119–R130

```math
\sum_p \left(Q_{g,p,s}+\beta Q_{g,p,s}^2\right)
\le T_g y_g\qquad \forall g,s.
```

$\beta$ bernilai 0 pada P1–P4 dan 0,025 pada P5–P8. Menangani 10 palet A dan 10 palet C di G2 memakai 20 satuan waktu pada bentuk linear dan 25 pada bentuk nonlinear. Dengan anggaran G2 sebesar 24, konsentrasi kiriman itu hanya layak pada bentuk linear.

## 4. Tujuan dan Pareto

```math
\begin{aligned}
C(x,z,y)={}&\sum_g F_g y_g+\sum_s\pi_s\Bigg[
\sum_{i,g,p}c^{\mathrm{in}}_{i,g}x_{i,g,p,s}
+\sum_{g,j,p}(c^{\mathrm{out}}_{g,j}+h_{g,p})z_{g,j,p,s}\\
&\qquad+\alpha\sum_{g,p} Q_{g,p,s}^{2}\Bigg].
\end{aligned}
```

$F_g$ adalah biaya tetap buka, $c^{\mathrm{in}}_{i,g}$ dan $c^{\mathrm{out}}_{g,j}$ tarif angkut, serta $h_{g,p}$ tarif penanganan per palet. Koefisien $\alpha$ bernilai 0 pada profil linear dan 0,04 pada profil nonlinear. Jika sebuah gudang menangani 10 palet A, suku kuadratik untuk produk itu menambah 4 satuan biaya sebelum dibobot peluang.

Untuk profil biaya tunggal, minimalkan $C$ dengan batas emisi 330. Untuk P3, P4, P7, dan P8, hitung titik Pareto dengan prosedur berikut.

1. Cari ujung emisi minimum dan ujung biaya minimum. Pilih nilai terbaik bagi tujuan kedua dalam toleransi yang dicatat.
2. Pada tiap tingkat, tentukan sembilan batas absolut yang berlaku untuk seluruh profil dua tujuan. Awal rentang mengikuti emisi minimum tertinggi, dengan margin numerik. Akhir rentang mengikuti emisi tertinggi dari solusi biaya minimum, dengan margin yang sama.
3. Pada setiap batas, minimalkan biaya. Setelah itu, minimalkan emisi dengan biaya yang dibatasi di sekitar optimum sebelumnya.
4. Simpan batas, emisi aktual, biaya, gudang terpilih, dan waktu penyelesaian. Pisahkan titik ujung masing-masing profil dan sembilan pengujian bersama. Hasil merupakan titik Pareto yang diperoleh dalam toleransi solver.

## 5. Pengukuran WCC

Audit menghitung 130 posisi kendala sebelum presolve dan sebelum langkah pemecah seri. Pada baris nonlinear, suatu variabel tercatat ketika nilai baris bergantung padanya. Suku linier waktu mempertahankan semua variabel arus yang juga dipakai oleh suku kuadratik. Koefisien kuadratik biaya berada dalam fungsi tujuan. [Lampiran WCC](../Lampiran_WCC.md) · [Hasil verifikasi](Hasil_Verifikasi.md)
