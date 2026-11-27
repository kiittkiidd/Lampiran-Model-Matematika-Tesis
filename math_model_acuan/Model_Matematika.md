# Model matematika acuan P1–P8

Model memilih gudang untuk dibuka dan menentukan kiriman pabrik–gudang–pelanggan. Baca [kasus dan tabel data](../case/Kasus_Dasar.md) serta [ketentuan delapan profil](../case/Profil_P1_P8.md) untuk melihat aturan bisnis yang ditulis di bawah.

## 1. Indeks dan rute

| Huruf indeks | Dibaca sebagai | Nilai yang mungkin |
| --- | --- | --- |
| i | Pabrik | P1 sampai P6 |
| g | Calon gudang | G1 sampai G4 |
| j | Pelanggan | K1 sampai K6 |
| p | Produk | A, B, atau C |
| s | Kondisi permintaan | Satu kondisi Pasti, atau tiga kondisi Sepi, Sedang, dan Ramai |

Variabel arus hanya didefinisikan pada rute aktif. Dalam setiap penjumlahan, ikutkan arus yang tersedia pada jaringan Low, Medium, atau High yang sedang dipakai. Penjumlahan atas daftar rute kosong bernilai nol.

## 2. Variabel keputusan dan domain

| Notasi | Keputusan yang diwakili | Cara membacanya |
| --- | --- | --- |
| $`x_{i,g,p,s}`$ | Palet produk yang dikirim dari pabrik ke gudang | Urutannya pabrik, gudang, produk, kondisi |
| $`z_{g,j,p,s}`$ | Palet produk yang dikirim dari gudang ke pelanggan | Urutannya gudang, pelanggan, produk, kondisi |
| $`y_g`$ | Apakah gudang dibuka | Nilai 1 berarti buka dan 0 berarti tutup |

**Domain variabel**

```math
x_{i,g,p,s}\ge 0,\qquad z_{g,j,p,s}\ge 0,\qquad y_g\in\{0,1\}.
```

Arus dapat berupa pecahan palet. Jika $`z_{2,1,A,s}=1{,}5`$, G2 mengirim 1,5 palet A ke K1 dalam kondisi tersebut. Karena $`y_g`$ hanya memakai indeks gudang, membuka G2 berlaku untuk seluruh kondisi permintaan.

| Profil | Berapa blok operasi? | Cara membaca kondisi |
| --- | ---: | --- |
| P1, P3, P5, P7 | 1 | Permintaan sudah diketahui. Peluang satu kondisi adalah 1. Indeks kondisi dapat dihilangkan saat menulis profil ini secara terpisah. |
| P2, P4, P6, P8 | 3 | Permintaan mengikuti tabel tiga kondisi. Setiap kondisi memiliki arus tersendiri dan menggunakan keputusan gudang yang sama. |

## 3. Kendala operasi

### Kapasitas pabrik

```math
\sum_{g,p} x_{i,g,p,s} \le C_i \qquad \text{untuk setiap pabrik dan kondisi}.
```

$`C_i`$ adalah batas kiriman pabrik dalam palet, yaitu 8 untuk setiap pabrik. Jumlahkan kiriman pabrik itu ke seluruh gudang dan untuk semua produk. Jika pabrik sudah mengirim 5,5 palet, sisa kapasitasnya 2,5 palet. Pada profil stokastik, pemeriksaan tersebut dilakukan untuk tiap kondisi.

### Neraca gudang untuk setiap produk

```math
\sum_i x_{i,g,p,s} = \sum_j z_{g,j,p,s}
\qquad \text{untuk setiap gudang, produk, dan kondisi}.
```

Sisi kiri menjumlahkan palet yang masuk dari semua pabrik. Sisi kanan menjumlahkan palet yang disalurkan ke semua pelanggan. Sebagai contoh, jika G2 menerima enam palet A, total A yang dikirim G2 harus enam palet. Hitung neraca A, B, dan C secara terpisah.

### Pemenuhan pesanan pelanggan

```math
\sum_g z_{g,j,p,s}=d_{j,p,s}
\qquad \text{untuk setiap pelanggan, produk, dan kondisi}.
```

$`d_{j,p,s}`$ adalah pesanan pelanggan dalam palet. Tanda sama dengan mengharuskan pesanan dipenuhi tepat. Jika K1 memesan tiga palet A, satu palet dari G1 ditambah dua palet dari G2 mencukupi. Pada kondisi Ramai, pesanan A di K1 naik menjadi sekitar 4,525 palet. Kiriman yang direncanakan untuk kondisi itu harus memenuhi jumlah yang baru.

### Kapasitas fisik gudang

```math
\sum_{j,p} z_{g,j,p,s}\le U_g y_g
\qquad \text{untuk setiap gudang dan kondisi}.
```

$`U_g`$ adalah kapasitas gudang dalam palet. Saat G2 buka, ruas kanan bernilai 20. Saat tutup, ruas kanan bernilai nol. Karena semua arus nonnegatif, gudang tutup memiliki kiriman keluar nol. Neraca per produk kemudian membuat kiriman masuknya juga nol.

### Waktu penanganan gudang

```math
Q_{g,p,s}=\sum_j z_{g,j,p,s}.
```

$`Q_{g,p,s}`$ adalah singkatan jumlah palet satu produk yang disalurkan satu gudang dalam satu kondisi. Jika G2 mengirim tiga palet A ke K1 dan dua palet A ke K2, volumenya lima palet A. Angka itu dihitung dari variabel pengiriman.

```math
\sum_p \left(Q_{g,p,s}+\beta Q_{g,p,s}^{2}\right)
\le T_g y_g
\qquad \text{untuk setiap gudang dan kondisi}.
```

$`T_g`$ adalah anggaran waktu gudang. Koefisien $`\beta`$ menentukan tambahan waktu per palet kuadrat. Pada P1–P4 nilainya nol. Pada P5–P8 nilainya 0,025. Jika G2 menyalurkan 10 palet A dan 10 palet C, waktu dasar adalah 20. Pada profil nonlinear, tambahan waktu masing-masing produk adalah 2,5, sehingga total 25 melebihi anggaran G2 sebesar 24 walaupun volume fisiknya masih 20 palet.

## 4. Biaya total

```math
\begin{aligned}
C(x,z,y)={}&\sum_g F_g y_g \\
&+\sum_s \pi_s \left[
  \sum_{i,g,p} c^{\mathrm{in}}_{i,g}x_{i,g,p,s}
  +\sum_{g,j,p}\left(c^{\mathrm{out}}_{g,j}+h_{g,p}\right)z_{g,j,p,s}
  +\alpha\sum_{g,p} Q_{g,p,s}^{2}
\right].
\end{aligned}
```

- $`F_g`$ adalah biaya membuka gudang dan dibayar sekali. Misalnya, kontribusi tetap G2 adalah 31 bila dibuka.
- Tarif $`c^{\mathrm{in}}_{i,g}`$ berlaku per palet dari pabrik ke gudang. Tarif $`c^{\mathrm{out}}_{g,j}`$ berlaku per palet dari gudang ke pelanggan. Tarif $`h_{g,p}`$ berlaku per palet produk yang disalurkan gudang. Untuk satu palet A dari pabrik P1 melalui G2 ke K1, biaya dasar arusnya 3 + 1 + 2 = 6.
- $`\alpha`$ adalah koefisien biaya tambahan. Nilainya nol untuk P1–P4 dan 0,04 untuk P5–P8. Jika suatu gudang menangani 10 palet A, biaya kuadratiknya 0,04 kali 100, yaitu 4.
- $`\pi_s`$ adalah peluang kondisi. Jumlah di dalam kurung siku dihitung per kondisi, dikalikan peluangnya, lalu dijumlahkan. Pada profil deterministik hanya ada satu kondisi dengan bobot 1.

## 5. Emisi total

```math
E(x,z,y)=\sum_g \kappa_g y_g
+\sum_s \pi_s\left[
\sum_{i,g,p}e^{\mathrm{in}}_{i,g}x_{i,g,p,s}
+\sum_{g,j,p}e^{\mathrm{out}}_{g,j}z_{g,j,p,s}
\right].
```

$`\kappa_g`$ adalah emisi tetap gudang yang dibuka. Faktor $`e^{\mathrm{in}}_{i,g}`$ dan $`e^{\mathrm{out}}_{g,j}`$ menyatakan emisi per palet pada kedua tahap angkutan. Satu palet dari pabrik P1 melalui G2 ke K1 menghasilkan 1,8 + 0,9 = 2,7 kg CO₂e dari angkutan. Bila G2 dibuka, tambahkan emisi tetap sebesar 20 kg CO₂e satu kali untuk rencana itu. Pada profil stokastik, bagian angkutan dirata-ratakan menggunakan peluang kondisi.

```math
E(x,z,y)\le \epsilon.
```

$`\epsilon`$ adalah batas emisi dalam kg CO₂e. Misalnya, pada batas 145, nilai emisi total pada profil pasti atau nilai emisi harapan pada profil stokastik harus paling banyak 145. Profil biaya tunggal menggunakan batas 330. Batas itu longgar karena emisi tetap maksimal 64, rata-rata volume pada masing-masing tahap 30 palet, dan faktor emisi angkut maksimum 4,7 dan 3,7. Dari ketiga angka itu, emisi keseluruhan paling tinggi 316 dalam data kasus.

## 6. Profil biaya tunggal

```math
\min_{x,z,y} C(x,z,y).
```

Pada P1, P2, P5, dan P6, pilih gudang dan arus dengan biaya terendah sambil memenuhi seluruh kendala dan domain. Fungsi tujuan adalah biaya total pada profil pasti dan biaya harapan pada profil stokastik.

## 7. Mencari kompromi biaya dan emisi

Pada P3, P4, P7, dan P8, jalankan model beberapa kali dengan batas emisi yang berbeda. Setiap kompromi memakai dua langkah.

```math
C^\star(\epsilon)=\min_{x,z,y} C(x,z,y)
\qquad \text{dengan } E(x,z,y)\le\epsilon.
```

Pertama, cari biaya minimum pada batas emisi yang dipilih. Semua kendala operasi dan domain tetap berlaku. Contohnya, jika batas 145 memberi biaya minimum 280, nilai 280 dipakai untuk langkah berikutnya.

```math
\min_{x,z,y} E(x,z,y)
\qquad \text{dengan } E(x,z,y)\le\epsilon
\quad \text{dan } C(x,z,y)\le C^\star(\epsilon)+\delta.
```

Kedua, cari emisi paling rendah di antara rencana dengan biaya yang masih berada dalam toleransi $`\delta`$ dari biaya terbaik. Dengan toleransi 0,0006 pada contoh sebelumnya, biaya rencana paling tinggi 280,0006.

Pada setiap tingkat jaringan, keempat profil dua tujuan memakai sembilan batas bersama. Sebelum menjalankan grid tersebut, verifikasi menghitung ujung biaya minimum dan ujung emisi minimum, masing-masing dengan satu langkah tambahan untuk memilih hasil terbaik pada tujuan kedua. Jumlahnya **4 langkah ujung + 18 langkah grid = 22 langkah optimisasi per profil dan tingkat**. Satu langkah nonlinear dapat memanggil solver beberapa kali.

## 8. Cakupan audit WCC

Satu blok operasi memiliki 6 posisi kapasitas pabrik, 11 neraca gudang–produk yang tersedia dalam jaringan acuan, 18 posisi pemenuhan pesanan, 4 kapasitas fisik gudang, dan 4 batas waktu penanganan. Totalnya **43 posisi**. Pada tingkat yang belum memakai suatu kombinasi gudang–produk, posisi neracanya kosong dan bobotnya nol.

Audit membandingkan blok yang sepadan. Pada profil stokastik, masing-masing blok diperiksa setelah indeks kondisi diselaraskan. Batas emisi agregat diperlakukan sebagai kendala lintas blok dan berada di luar cakupan WCC jaringan. [Tutorial perhitungan dan audit WCC](../Lampiran_WCC.md)

[Hasil verifikasi dan benchmark](Hasil_Verifikasi.md) · [Kembali ke daftar isi](../README.md)
