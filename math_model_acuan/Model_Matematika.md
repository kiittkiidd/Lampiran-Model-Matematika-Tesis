# Model matematika acuan PT XYZ Bahan Pangan

Perusahaan memilih gudang yang dibuka dan membagi kiriman dari pabrik ke zona pelanggan melalui gudang selama satu periode. Pilih dahulu tingkat rute Low, Medium, atau High dari [kasus dasar](../case/Kasus_Dasar.md).

## 1. Notasi dan keputusan P1

| Simbol | Arti |
| --- | --- |
| $i,g,j,p$ | Pabrik, gudang, zona pelanggan, dan produk. |
| $`\mathcal R_{\mathrm{in}},\mathcal R_{\mathrm{out}}`$ | Daftar rute pabrik–gudang dan gudang–zona yang diizinkan, masing-masing dengan kode produk. |
| $`U_i,V_g,T_g`$ | Kapasitas pabrik dalam ton, kapasitas gudang dalam ton, dan waktu kerja gudang dalam jam. |
| $`d_{jp}`$ | Permintaan produk $p$ di zona $j$, dalam ton. |
| $`F_g,c^{\mathrm{in}}_{ig},c^{\mathrm{out}}_{gj},h_{gp}`$ | Biaya buka gudang, tarif angkut masuk per ton, tarif angkut keluar per ton, dan tarif penanganan per ton. |
| $`y_g\in\{0,1\}`$ | Keputusan membuka gudang $g$. Nilai 1 berarti buka. |
| $`x_{igp}\geq0`$ | Ton produk $p$ yang dikirim dari pabrik $i$ ke gudang $g$. |
| $`z_{gjp}\geq0`$ | Ton produk $p$ yang dikirim dari gudang $g$ ke zona $j$. |

Arus hanya dibentuk untuk setiap rute yang diizinkan. Semua penjumlahan arus menggunakan aturan itu. Sebagai singkatan, $`q_{gp}=\sum_j z_{gjp}`$ adalah tonase produk $p$ yang ditangani di gudang $g$.

## 2. Biaya dan kendala P1

**Tujuan biaya.** Pilih rencana dengan jumlah biaya buka, biaya angkut dua tahap, dan biaya penanganan paling rendah.

$$
\min C =
\sum_g F_g y_g
+\sum_{(i,g,p)\in\mathcal R_{\mathrm{in}}}c^{\mathrm{in}}_{ig}x_{igp}
+\sum_{(g,j,p)\in\mathcal R_{\mathrm{out}}}c^{\mathrm{out}}_{gj}z_{gjp}
+\sum_{g,p}h_{gp}q_{gp}.
$$

Contoh P1 → G1 → K1 untuk produk A dikenai biaya angkut dan penanganan $2+1+2=5$ per ton. Biaya tetap G1 sebesar 25 dibayar sekali jika dibuka.

**Kapasitas pabrik.** Seluruh produk yang dikirim satu pabrik berbagi kapasitas.

$$
\sum_{g,p}x_{igp}\le U_i
\quad\text{untuk setiap pabrik } i.
$$

Nilai $`U_i=8`$ ton. Jika P1 memasok 5,5 ton minyak, sisa kapasitasnya untuk semua kiriman adalah 2,5 ton.

**Keseimbangan barang di gudang.** Setiap produk yang masuk harus dikirim ke zona pada periode yang sama.

$$
\underbrace{\sum_i x_{igp}}_{\text{total masuk}} = \underbrace{q_{gp}}_{\text{tonase ditangani}} = \underbrace{\sum_j z_{gjp}}_{\text{total keluar}}
$$

Persamaan ini berlaku untuk setiap pasangan gudang dan produk yang kompatibel. Panah masuk dari pabrik dan panah keluar ke zona dihubungkan oleh $`q_{gp}`$, singkatan untuk total arus keluar. Saat $`q_{gp}`$ diganti dengan definisinya, persamaan langsung menunjukkan **total masuk = total keluar** untuk produk yang sama di gudang yang sama.

Jika G2 menerima 6 ton minyak, total kiriman minyak dari G2 juga harus 6 ton. Pada pasangan yang belum memiliki rute di suatu tingkat, penjumlahan kosong bernilai nol.

**Pemenuhan pesanan.** Seluruh permintaan dilayani tepat sesuai jumlah yang diminta.

$$
\sum_g z_{gjp}=d_{jp}
\quad\text{untuk setiap zona } j \text{ dan produk } p.
$$

Jika K1 memesan 3 ton minyak, G1 dapat mengirim 1,25 ton dan G2 mengirim 1,75 ton.

**Kapasitas tonase gudang.** Barang hanya bisa disalurkan melalui gudang yang dibuka dan totalnya dibatasi.

$$
\sum_p q_{gp}\le V_g y_g
\quad\text{untuk setiap gudang } g.
$$

Jika G2 dibuka, batasnya 20 ton. Jika ditutup, arus keluar menjadi nol dan aturan keseimbangan membuat arus masuk juga nol.

**Waktu penanganan linear.** Setiap ton memerlukan satu jam kerja.

$$
\sum_p q_{gp}\le T_g y_g
\quad\text{untuk setiap gudang } g.
$$

Data menetapkan $`T_g=1{,}2V_g`$. G3 yang menangani 18 ton memerlukan 18 jam dan memiliki 21,60 jam tersedia. Karena itu, pada profil linear, pemenuhan kapasitas tonase sekaligus memenuhi batas waktu. Baris waktu dicatat dalam formulasi operasi dan diganti dengan bentuk kuadratik di profil nonlinear.

## 3. Perubahan pada profil nonlinear

Hitung volume per produk di tiap gudang terlebih dahulu. Setiap gudang dapat memiliki jumlah ton berbeda untuk A, B, dan C.

$$
C_{\mathrm{NL}}=C+0{,}04\sum_{g,p}q_{gp}^{2}.
$$

Koefisien 0,04 mengubah kuadrat tonase menjadi tambahan biaya penanganan. Delapan ton satu produk memberi tambahan $0{,}04(8^2)=2{,}56$ satuan biaya.

$$
\sum_p(q_{gp}+0{,}025q_{gp}^2)\le T_g y_g
\quad\text{untuk setiap gudang } g.
$$

Koefisien 0,025 mengubah kuadrat tonase menjadi jam tambahan. Sepuluh ton sirup dan delapan ton susu di G3 memerlukan $18+0{,}025(10^2+8^2)=22{,}10$ jam, melebihi batas 21,60 jam. Batas tonase tetap 18 ton.

## 4. Perubahan pada profil stokastik

Perusahaan memilih $`y_g`$ sebelum mengetahui permintaan. Setelah skenario $s$ diketahui, perusahaan mengatur $`x_{igps}`$ dan $`z_{gjps}`$ sesuai kebutuhan. Semua kendala operasi berlaku pada masing-masing skenario, dengan $`q_{gps}=\sum_j z_{gjps}`$ dan permintaan $`d_{jps}`$. Contoh K1 memiliki tiga kemungkinan pesanan minyak, yaitu sekitar 1,475, 3,000, dan 4,525 ton jika nilai tengahnya 3 ton.

$$
C_{\mathrm{stoch}}=
\sum_g F_g y_g+\sum_s\pi_s C_s^{\mathrm{operasi}}.
$$

$`\pi_s`$ adalah peluang skenario, dan $`C_s^{\mathrm{operasi}}`$ mencakup angkut dan penanganan. Biaya buka dibayar sekali. Pada P6 dan P8, biaya dan waktu kuadratik masing-masing dihitung dari tonase skenario bersangkutan.

## 5. Perubahan pada profil multiobjektif

Emisi dihitung dalam kilogram setara karbon dioksida (kg CO₂e).

$$
E=
\sum_g e_g^{\mathrm{tetap}}y_g
+\sum_{(i,g,p)\in\mathcal R_{\mathrm{in}}} e^{\mathrm{in}}_{ig}x_{igp}
+\sum_{(g,j,p)\in\mathcal R_{\mathrm{out}}} e^{\mathrm{out}}_{gj}z_{gjp}.
$$

$`e_g^{\mathrm{tetap}}`$ adalah emisi gudang yang dibuka. Faktor $`e^{\mathrm{in}}_{ig}`$ dan $`e^{\mathrm{out}}_{gj}`$ adalah emisi angkutan per ton. Untuk P4 dan P8, emisi angkutan dirata-ratakan berbobot peluang skenario dan emisi tetap gudang ditambahkan satu kali.

P3, P4, P7, dan P8 mencari kompromi biaya dan emisi dengan metode **ε-constraint**. Untuk setiap batas emisi $\varepsilon$, selesaikan

$$
\min C\qquad\text{dengan}\qquad E\le\varepsilon.
$$

Gunakan bentuk biaya dan emisi yang sesuai dengan profil. Sebagai contoh, $\varepsilon=120$ berarti rencana biaya terendah harus menghasilkan emisi maksimal 120 kg CO₂e. Pada profil stokastik, batas ini berlaku untuk emisi harapan.

Cari dua solusi ujung dengan menyelesaikan tujuan biaya dan tujuan emisi secara bergantian. Pada masing-masing ujung, gunakan tujuan lainnya untuk memilih di antara solusi dengan nilai tujuan utama yang sama sesuai toleransi. Emisi terendah $`E_{\min}`$ dan emisi pada solusi biaya terendah $`E_C`$ menentukan 25 batas.

$$
\varepsilon_k=E_{\min}+\frac{k}{24}(E_C-E_{\min}),
\qquad k=0,\ldots,24.
$$

Kedua ujung ikut dihitung. Pada setiap batas interior, pilih biaya minimum terlebih dahulu, lalu emisi terendah di antara solusi dengan biaya yang sama sesuai toleransi. CSV menyimpan seluruh batas. Grafik menampilkan sampel titik berbeda yang tidak didominasi pada toleransi pencatatan.

Untuk P7 dan P8, kode membangun batas bawah suku kuadrat dengan garis singgung. Biaya dan waktu dihitung kembali dari suku kuadrat asli, dan hasil hanya diterima saat memenuhi toleransi kelayakan dan celah terhadap batas bawah solver. [Metode pengujian dan hasil](Hasil_Verifikasi.md)

[Halaman utama](../README.md)
