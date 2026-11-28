# Model matematika acuan P1–P8

Model ini memakai data pada [Kasus](../case/Kasus_Dasar.md). Jumlah barang diukur dalam ton dan boleh pecahan. Gudang dipilih untuk satu periode. Setiap produk yang diterima gudang harus dikirim kembali dalam periode tersebut.

| Profil | Banyak skenario | Koefisien biaya kuadratik α | Koefisien waktu kuadratik β | Tujuan |
|---|---:|---:|---:|---|
| P1 | 1 | 0 | 0 | Biaya |
| P2 | 27 | 0 | 0 | Biaya harapan |
| P3 | 1 | 0 | 0 | Biaya dan emisi |
| P4 | 27 | 0 | 0 | Biaya dan emisi harapan |
| P5 | 1 | 0,04 | 0,025 | Biaya |
| P6 | 27 | 0,04 | 0,025 | Biaya harapan |
| P7 | 1 | 0,04 | 0,025 | Biaya dan emisi |
| P8 | 27 | 0,04 | 0,025 | Biaya dan emisi harapan |

Profil pasti menggunakan peluang satu pada satu kondisi permintaan. Profil stokastik menggunakan peluang dan pesanan dari dokumen kasus. Rute yang diizinkan pada satu tingkat sama untuk semua profil dan skenario.

## 1. Indeks, parameter, dan keputusan

| Simbol | Arti |
|---|---|
| <img src="diagram/persamaan/eq-3924da6c6c6887a6.svg" alt="i" width="8" height="13" align="middle"> | Pabrik P1–P6 |
| <img src="diagram/persamaan/eq-7e524a7302e1d9a3.svg" alt="R^{\mathrm{in}},R^{\mathrm{out}}" width="62" height="19" align="middle"> | Himpunan rute pabrik–gudang–produk dan gudang–zona–produk yang diizinkan pada tingkat L/M/H |
| <img src="diagram/persamaan/eq-10e36d9b3f540053.svg" alt="\alpha,\beta" width="29" height="17" align="middle"> | Koefisien tambahan biaya dan jam kerja kuadratik pada tabel profil |
| <img src="diagram/persamaan/eq-23009c376bb95b17.svg" alt="g" width="10" height="13" align="middle"> | Gudang G1–G4 |
| <img src="diagram/persamaan/eq-68fa4ad2d7561e59.svg" alt="j" width="9" height="16" align="middle"> | Zona pelanggan K1–K6 |
| <img src="diagram/persamaan/eq-e4bd8005f58b3d95.svg" alt="p" width="10" height="13" align="middle"> | Produk A, B, atau C |
| <img src="diagram/persamaan/eq-b7c4deb092eb7e51.svg" alt="s" width="10" height="10" align="middle"> | Kondisi permintaan; satu kondisi pada profil pasti dan 27 skenario pada profil stokastik |
| <img src="diagram/persamaan/eq-c4d441f388584f0e.svg" alt="\pi_s" width="18" height="12" align="middle"> | Peluang skenario; bernilai satu pada profil pasti |
| <img src="diagram/persamaan/eq-9a8eb14ced6400b8.svg" alt="d_{jps}" width="28" height="18" align="middle"> | Pesanan produk <img src="diagram/persamaan/eq-e4bd8005f58b3d95.svg" alt="p" width="10" height="13" align="middle"> di zona <img src="diagram/persamaan/eq-68fa4ad2d7561e59.svg" alt="j" width="9" height="16" align="middle"> pada skenario <img src="diagram/persamaan/eq-b7c4deb092eb7e51.svg" alt="s" width="10" height="10" align="middle"> |
| <img src="diagram/persamaan/eq-6c3a42dc84aeac00.svg" alt="V_g,T_g" width="42" height="18" align="middle"> | Kapasitas tonase dan jam kerja gudang <img src="diagram/persamaan/eq-23009c376bb95b17.svg" alt="g" width="10" height="13" align="middle"> |
| <img src="diagram/persamaan/eq-f26ede7eb59ffc69.svg" alt="F_g" width="19" height="18" align="middle"> | Biaya membuka gudang <img src="diagram/persamaan/eq-23009c376bb95b17.svg" alt="g" width="10" height="13" align="middle"> |
| <img src="diagram/persamaan/eq-2b2ae609fd609cf7.svg" alt="c^{\mathrm{in}}_{ig},c^{\mathrm{out}}_{gj}" width="52" height="23" align="middle"> | Tarif angkut masuk dan keluar per ton |
| <img src="diagram/persamaan/eq-62a914a47ed38e7b.svg" alt="h_{gp}" width="24" height="18" align="middle"> | Biaya penanganan dasar per ton |
| <img src="diagram/persamaan/eq-b089f8fb83a9e76b.svg" alt="e_g^F,e^{\mathrm{in}}_{ig},e^{\mathrm{out}}_{gj}" width="77" height="23" align="middle"> | Emisi tetap gudang dan emisi angkutan per ton |
| <img src="diagram/persamaan/eq-d26cd80ea0976736.svg" alt="y_g" width="17" height="14" align="middle"> | Keputusan buka gudang: 1 berarti buka, 0 berarti tutup |
| <img src="diagram/persamaan/eq-b2fdff9ebb764674.svg" alt="x_{igps}" width="33" height="14" align="middle"> | Kiriman produk <img src="diagram/persamaan/eq-e4bd8005f58b3d95.svg" alt="p" width="10" height="13" align="middle"> dari pabrik <img src="diagram/persamaan/eq-3924da6c6c6887a6.svg" alt="i" width="8" height="13" align="middle"> ke gudang <img src="diagram/persamaan/eq-23009c376bb95b17.svg" alt="g" width="10" height="13" align="middle"> pada skenario <img src="diagram/persamaan/eq-b7c4deb092eb7e51.svg" alt="s" width="10" height="10" align="middle"> |
| <img src="diagram/persamaan/eq-d7bdd5cb0ed4a4f2.svg" alt="z_{gjps}" width="32" height="14" align="middle"> | Kiriman produk <img src="diagram/persamaan/eq-e4bd8005f58b3d95.svg" alt="p" width="10" height="13" align="middle"> dari gudang <img src="diagram/persamaan/eq-23009c376bb95b17.svg" alt="g" width="10" height="13" align="middle"> ke zona <img src="diagram/persamaan/eq-68fa4ad2d7561e59.svg" alt="j" width="9" height="16" align="middle"> pada skenario <img src="diagram/persamaan/eq-b7c4deb092eb7e51.svg" alt="s" width="10" height="10" align="middle"> |

Variabel kiriman hanya disediakan untuk rute yang diizinkan pada tingkat yang dipilih. Keputusan <img src="diagram/persamaan/eq-d26cd80ea0976736.svg" alt="y_g" width="17" height="14" align="middle"> dipakai bersama pada seluruh skenario. Setiap jumlah kiriman memiliki indeks skenarionya sendiri. Contoh <img src="diagram/persamaan/eq-d9d42646709eb6a0.svg" alt="x_{1,2,A,s}" width="47" height="14" align="middle"> dibaca ton minyak dari Pabrik P1 ke G2 pada skenario <img src="diagram/persamaan/eq-b7c4deb092eb7e51.svg" alt="s" width="10" height="10" align="middle">; <img src="diagram/persamaan/eq-b8df615b14bee623.svg" alt="z_{1,2,A,s}" width="46" height="14" align="middle"> dibaca ton minyak dari G1 ke K2 pada skenario yang sama. Huruf dan semua indeks menentukan identitas keputusan.

Tonase produk di gudang ditulis dengan singkatan berikut:


<p align="center"><img src="diagram/persamaan/eq-4caf660d7c845ba8.svg" alt="q_{gps}:=\sum_{j:(g,j,p)\in R^{\mathrm{out}}}z_{gjps}." width="181" height="50"></p>


<img src="diagram/persamaan/eq-c6fac57b4e73ac71.svg" alt="q_{gps}" width="27" height="14" align="middle"> adalah jumlah semua kiriman keluar untuk satu produk dari satu gudang. Pada representasi acuan, simbol ini merupakan singkatan penjumlahan. Contohnya, jika G1 mengirim 1,20 ton dan 0,80 ton minyak ke dua zona, tonase minyak di G1 adalah 2,00 ton.

## 2. Fungsi biaya dan emisi

Biaya total adalah biaya membuka gudang sekali, ditambah biaya operasi yang dirata-ratakan menurut peluang skenario.


<p align="center"><img src="diagram/persamaan/eq-6985f348df95c75b.svg" alt="C=\sum_g F_g y_g+ \sum_s\pi_s\left[ \sum_{(i,g,p)\in R^{\mathrm{in}}}c^{\mathrm{in}}_{ig}x_{igps} +\sum_{(g,j,p)\in R^{\mathrm{out}}}c^{\mathrm{out}}_{gj}z_{gjps} +\sum_{g,p}h_{gp}q_{gps} +\alpha\sum_{g,p}q_{gps}^{2}\right]." width="288" height="218"></p>


Gunakan <img src="diagram/persamaan/eq-5f165748abcddf56.svg" alt="\alpha=0" width="42" height="14" align="middle"> pada profil linear dan <img src="diagram/persamaan/eq-dfa7349853e20714.svg" alt="\alpha=0{,}04" width="62" height="16" align="middle"> pada profil nonlinear. Karena jumlah peluang satu, biaya operasi pada profil pasti adalah biaya dari satu kondisi yang diketahui. Sebagai contoh, tonase 5, 4, dan 3 ton di satu gudang memberikan tambahan biaya nonlinear sebesar <img src="diagram/persamaan/eq-aa4f24a21bae1b9f.svg" alt="0{,}04(25+16+9)=2" width="152" height="18" align="middle">.

Emisi total menghitung emisi tetap gudang satu kali dan emisi angkutan sesuai peluang skenario.


<p align="center"><img src="diagram/persamaan/eq-8dac50c042abeded.svg" alt="E=\sum_g e_g^F y_g+ \sum_s\pi_s\left[ \sum_{(i,g,p)\in R^{\mathrm{in}}}e^{\mathrm{in}}_{ig}x_{igps} +\sum_{(g,j,p)\in R^{\mathrm{out}}}e^{\mathrm{out}}_{gj}z_{gjps}\right]." width="245" height="173"></p>


Pada profil stokastik, <img src="diagram/persamaan/eq-269b432f796e73cc.svg" alt="C" width="15" height="14" align="middle"> dan <img src="diagram/persamaan/eq-5864a2ca82e50724.svg" alt="E" width="15" height="13" align="middle"> adalah biaya harapan dan emisi harapan. Pada profil satu tujuan, minimalkan <img src="diagram/persamaan/eq-269b432f796e73cc.svg" alt="C" width="15" height="14" align="middle">. Pada profil dua tujuan, cari kompromi antara <img src="diagram/persamaan/eq-269b432f796e73cc.svg" alt="C" width="15" height="14" align="middle"> dan <img src="diagram/persamaan/eq-5864a2ca82e50724.svg" alt="E" width="15" height="13" align="middle"> dengan prosedur pada Bagian 4.

## 3. Kendala operasi

### Keseimbangan setiap produk di setiap gudang


<p align="center"><img src="diagram/persamaan/eq-114bdc32f5b6ce1a.svg" alt="\sum_{i:(i,g,p)\in R^{\mathrm{in}}}x_{igps} =\sum_{j:(g,j,p)\in R^{\mathrm{out}}}z_{gjps}, \qquad \forall g,p,s." width="350" height="50"></p>


Kedua ruas menyatakan produk yang sama di gudang dan skenario yang sama. Jika G1 menerima 2 ton sirup, seluruh kiriman sirup keluar G1 harus berjumlah 2 ton. Ada 12 baris per skenario: empat gudang dikalikan tiga produk.

### Pemenuhan pesanan


<p align="center"><img src="diagram/persamaan/eq-d8484168760fc413.svg" alt="\sum_{g:(g,j,p)\in R^{\mathrm{out}}}z_{gjps}=d_{jps}, \qquad \forall j,p,s." width="272" height="50"></p>


Pesanan boleh dibagi antargudang. Pesanan 3,17 ton minyak di K1 dapat dipenuhi, misalnya, dengan 1,20 ton dari satu gudang dan 1,97 ton dari gudang lainnya jika kedua rutenya diizinkan. Ada 18 baris per skenario: enam zona dikalikan tiga produk.

### Kapasitas tonase gudang


<p align="center"><img src="diagram/persamaan/eq-80c6a49fc9d1e680.svg" alt="\sum_p q_{gps}\le V_g y_g, \qquad \forall g,s." width="206" height="47"></p>


Jumlah seluruh produk berbagi kapasitas gudang. Jika G1 dibuka, batasnya 16 ton; jika ditutup, ruas kanan nol. Karena semua kiriman nonnegatif dan barang masuk sama dengan barang keluar, penutupan gudang juga membuat arus masuknya nol. Ada empat baris per skenario.

### Waktu penanganan gudang


<p align="center"><img src="diagram/persamaan/eq-085c091ef3143db2.svg" alt="\sum_p q_{gps}+\beta\sum_p q_{gps}^{2}\le T_g y_g, \qquad \forall g,s." width="299" height="47"></p>


Gunakan <img src="diagram/persamaan/eq-57602d2f79bdee5e.svg" alt="\beta=0" width="41" height="17" align="middle"> pada profil linear dan <img src="diagram/persamaan/eq-17addaa5ae549cf2.svg" alt="\beta=0{,}025" width="69" height="17" align="middle"> pada profil nonlinear. Waktu dasar satu jam per ton. Untuk 5 ton minyak, 4 ton sirup, dan 3 ton susu, waktu linear 12 jam; waktu nonlinear <img src="diagram/persamaan/eq-4e98520bfad22885.svg" alt="12+0{,}025(25+16+9)=13{,}25" width="224" height="18" align="middle"> jam. Aturan berlaku pada seluruh empat gudang dan seluruh skenario.

Pada profil linear, waktu tersedia lebih besar daripada kapasitas tonase, sehingga batas tonase juga cukup untuk memenuhi batas waktu. Kedua baris tetap dicatat sebagai dua aturan fisik yang dibedakan. Pada profil nonlinear, tambahan waktu kuadratik dapat membuat batas waktu aktif.

### Domain keputusan


<p align="center"><img src="diagram/persamaan/eq-5fb583a8ccd54b31.svg" alt="\begin{aligned} y_g&amp;\in\{0,1\} &amp;&amp;\forall g,\\ x_{igps}&amp;\ge0 &amp;&amp;\forall (i,g,p)\in R^{\mathrm{in}},s,\\ z_{gjps}&amp;\ge0 &amp;&amp;\forall (g,j,p)\in R^{\mathrm{out}},s. \end{aligned}" width="286" height="78"></p>


Keputusan gudang biner, sedangkan kiriman dapat pecahan. Penghitungan WCC menggunakan 38 baris operasi per skenario: 12 neraca, 18 permintaan, empat kapasitas, dan empat waktu. Domain dicatat terpisah dari 38 baris tersebut.

## 4. Profil dua tujuan dan 25 batas emisi

Untuk setiap batas emisi <img src="diagram/persamaan/eq-cc52deca71b2deea.svg" alt="\varepsilon" width="10" height="10" align="middle">, selesaikan:


<p align="center"><img src="diagram/persamaan/eq-b29d26548587c25d.svg" alt="\min C\qquad\text{dengan kendala operasi dan }E\le\varepsilon." width="360" height="23"></p>


Setelah biaya minimum pada langkah tersebut diperoleh, pilih emisi minimum di antara rencana yang biayanya berada dalam toleransi biaya yang ditetapkan:


<p align="center"><img src="diagram/persamaan/eq-01ddac2da318bf29.svg" alt="\min E\qquad\text{dengan kendala operasi, }E\le\varepsilon, \quad C\le C^{\star}_{\varepsilon}+\delta_C." width="458" height="25"></p>


<img src="diagram/persamaan/eq-8cad4135cea4703e.svg" alt="\delta_C=0{,}00025" width="93" height="17" align="middle"> adalah toleransi pemecah seri dalam satuan biaya. Toleransi selisih objektif pada penyelesaian biaya adalah 0,00025 satuan biaya; pada penyelesaian emisi adalah 0,00025 kg CO2e. Batas celah absolut SCIP pada profil linear ditetapkan lebih ketat, yaitu <img src="diagram/persamaan/eq-a886a0ce44f2e9a4.svg" alt="10^{-8}" width="34" height="17" align="middle">; pada profil nonlinear sebesar 0,00025. Seluruh hasil harus memenuhi batas pemeriksaan 0,00025 pada tujuan yang sedang diminimalkan.

Empat langkah awal menghitung biaya minimum, emisi minimum, rencana biaya minimum dekat ujung emisi minimum, serta emisi minimum dekat ujung biaya minimum. Ambil 25 batas berjarak sama di antara emisi kedua rencana ujung itu. Pada 23 batas interior, lakukan masing-masing dua langkah di atas. Jumlahnya 50 langkah optimisasi per profil dan tingkat. Rentang batas dihitung untuk masing-masing profil dan tingkat; jumlah batas serta prosedurnya sama. Pada profil stokastik, batas diterapkan pada emisi harapan dan seluruh skenario tetap diselesaikan dalam satu model dengan keputusan gudang bersama.

Titik biaya–emisi yang sama ditampilkan sekali. Titik yang didominasi dikeluarkan dari grafik Pareto. Toleransi numerik dinyatakan dalam konfigurasi yang dibekukan.

## 5. Representasi internal SCIP

SCIP menangani keputusan biner dan kontinu secara bersama. Implementasi menggunakan variabel bantu tonase pada seluruh profil:


<p align="center"><img src="diagram/persamaan/eq-972dfdc202411477.svg" alt="\widehat q_{gps}=\sum_j z_{gjps}." width="126" height="48"></p>


Variabel bantu ditentukan sepenuhnya oleh kiriman. Menggantikan <img src="diagram/persamaan/eq-e4a35c47d62b71fe.svg" alt="\widehat q" width="10" height="18" align="middle"> dengan ruas kanannya mengembalikan persamaan acuan. Pada profil nonlinear, setiap kuadrat tonase diberi variabel bantu berikut:


<p align="center"><img src="diagram/persamaan/eq-c594e6bca4b67874.svg" alt="v_{gps}\ge\widehat q_{gps}^{2}." width="93" height="30"></p>


Tambahan biaya menjadi <img src="diagram/persamaan/eq-eb954a6e26267505.svg" alt="0{,}04\sum_s\pi_s\sum_{g,p}v_{gps}" width="139" height="21" align="middle"> dan tambahan jam kerja menjadi <img src="diagram/persamaan/eq-a3c652ab533d0849.svg" alt="0{,}025\sum_p v_{gps}" width="94" height="21" align="middle">. Seluruh fungsi tujuan dan batas lain kemudian linear terhadap variabel bantu ini; hubungan kuadrat berada pada pertidaksamaan di atas.

Representasi ini setara dalam keputusan bisnis. Setiap rencana asli dapat diperluas dengan memilih <img src="diagram/persamaan/eq-809300ee2215c1ea.svg" alt="v_{gps}=q_{gps}^{2}" width="74" height="22" align="middle">. Sebaliknya, jika suatu rencana memenuhi batas dengan <img src="diagram/persamaan/eq-f8824c9bd7955215.svg" alt="v_{gps}\ge q_{gps}^{2}" width="74" height="22" align="middle">, menggantinya dengan kuadrat sebenarnya tidak menambah biaya atau jam kerja. Pada minimisasi biaya, koefisien positif mendorong nilai bantu ke batas kuadratnya. Pada pemilihan emisi dengan batas biaya, proyeksi rencana ke kiriman asli tetap memenuhi biaya serta waktu asli. Biaya dan waktu yang dilaporkan selalu dihitung ulang dari kuadrat tonase sebenarnya.

Batas atas kiriman diturunkan dari kendala acuan. Kiriman keluar tidak melampaui pesanan tujuan. Tonase produk di gudang tidak melampaui kapasitas gudang dan total pesanan produk tersebut. Setiap batas mengikuti nonnegativitas, neraca, pesanan, dan kapasitas yang sudah berlaku.

WCC dihitung pada representasi acuan sebelum variabel bantu dan presolve. Pemeriksaan solusi menghitung ulang neraca, kapasitas, waktu, biaya, dan emisi langsung dari kiriman asli. Data, kode, konfigurasi, dan hasil pengukuran dicatat dengan checksum pada versi yang dibekukan.

[Kasus untuk pemodel](../case/Kasus_Dasar.md) · [Tutorial WCC](../Lampiran_WCC.md) · [Persamaan Low R1–R38](Persamaan_WCC.md) · [Hasil verifikasi](Hasil_Verifikasi.md)

[Sumber persamaan LaTeX](source/persamaan_sumber.tex).
