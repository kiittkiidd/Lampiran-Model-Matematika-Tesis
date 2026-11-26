# Verifikasi, keseimbangan jaringan, dan benchmark solver

## 1. Pilihan gudang

P1 memakai permintaan pasti. Pada P2 satu kombinasi gudang dinyatakan layak jika dapat melayani ketiga skenario. Seluruh kombinasi diperiksa melalui program linear dengan keputusan lokasi tetap, lalu nilai optimum dibandingkan dengan penyelesaian MILP.

| Profil | Tingkat | Pola layak dari 16 | Pola dengan biaya ≤105% optimum | Wajib buka | Gudang optimal | Biaya optimal | Gap LP awal |
| --- | --- | ---: | ---: | --- | --- | ---: | ---: |
| P1 | Low | 6 | 4 | G2 | G1 + G2 + G4 | 299,16 | 17,43% |
| P1 | Medium | 8 | 4 | — | G1 + G3 + G4 | 277,37 | 18,86% |
| P1 | High | 10 | 2 | — | G2 + G4 | 242,95 | 13,42% |
| P2 | Low | 6 | 4 | G2 | G1 + G2 + G4 | 299,41 | 16,62% |
| P2 | Medium | 8 | 4 | — | G1 + G3 + G4 | 277,70 | 18,01% |
| P2 | High | 10 | 2 | — | G2 + G4 | 243,19 | 12,49% |

Semua pilihan layak Low tetap layak di Medium. Semua pilihan layak Medium juga tetap layak di High. G2 wajib buka pada Low karena hanya G2 yang memiliki akses produk C ke beberapa pelanggan saat itu. Penambahan rute C dari G3 pada Medium membuat G1 + G3 layak. Di High, G4 dapat menangani C untuk pelanggan di Timur dan G2 + G4 menjadi optimal. P1 dan P2 masing-masing memiliki empat pilihan yang masih berada dalam 5% dari biaya terbaik di Low dan Medium, serta dua di High. Ambang 5% dipakai untuk mendeskripsikan pilihan ekonomi yang dekat.

Gap LP awal dihitung dengan menyelesaikan formulasi yang mengizinkan setiap status buka mengambil nilai antara 0 dan 1. Persentasenya adalah selisih biaya MILP dan batas bawah LP, dibagi biaya MILP. Sebagai contoh, P2 Medium memiliki biaya 277,70 dan batas bawah LP 227,69, sehingga gap awal sekitar 18,01%. Gap ini mengukur kekuatan relaksasi sebelum teknik internal solver. Seluruh MILP verifikasi mencapai status optimal.

## 2. P3 · trade-off biaya dan emisi

| Tingkat | Batas emisi (kg CO₂e) | Emisi aktual (kg CO₂e) | Biaya | Gudang |
| --- | ---: | ---: | ---: | --- |
| Low | 134,00 | 134,00 | 319,00 | G2 + G3 |
| Low | 143,67 | 136,30 | 313,00 | G1 + G2 + G3 |
| Low | 153,35 | 136,30 | 313,00 | G1 + G2 + G3 |
| Low | 163,02 | 157,50 | 302,37 | G1 + G2 + G3 + G4 |
| Low | 172,70 | 172,70 | 299,16 | G1 + G2 + G4 |
| Medium | 124,30 | 124,30 | 287,00 | G1 + G3 |
| Medium | 129,42 | 124,30 | 287,00 | G1 + G3 |
| Medium | 134,55 | 124,30 | 287,00 | G1 + G3 |
| Medium | 139,67 | 124,30 | 287,00 | G1 + G3 |
| Medium | 144,80 | 144,80 | 277,37 | G1 + G3 + G4 |
| High | 111,50 | 111,50 | 279,00 | G2 + G3 |
| High | 122,52 | 111,80 | 278,00 | G2 + G3 |
| High | 133,55 | 133,55 | 253,12 | G2 + G3 + G4 |
| High | 144,57 | 134,60 | 252,37 | G2 + G3 + G4 |
| High | 155,60 | 155,60 | 242,95 | G2 + G4 |

Biaya terendah P3 cocok dengan biaya optimum P1 pada masing-masing tingkat. Titik dengan emisi terendah memerlukan biaya tambahan di ketiga tingkat. Pada High, beralih dari G2 + G4 ke G2 + G3 mengurangi emisi dari 155,60 menjadi 111,50 kg CO₂e dan menaikkan biaya dari 242,95 menjadi 279,00. Beberapa batas menghasilkan keputusan optimal yang sama, misalnya pada tiga batas interior Medium. Setiap titik diperiksa melalui enumerasi pola gudang dan LP. Nilai pada tabel dibulatkan, sedangkan solver memakai presisi penuh.

## 3. Waktu dan kerja solver

| Profil | Tingkat | MILP per ulangan | Median solver (ms) | P10–P90 solver (ms) | Median total (ms) | Median node |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| P1 | Low | 1 | 5,32 | 4,31–5,56 | 5,62 | 1 |
| P1 | Medium | 1 | 10,07 | 8,09–10,52 | 10,36 | 1 |
| P1 | High | 1 | 14,26 | 11,62–15,18 | 14,60 | 1 |
| P2 | Low | 1 | 11,50 | 9,36–12,04 | 11,82 | 1 |
| P2 | Medium | 1 | 21,82 | 17,71–22,42 | 22,22 | 1 |
| P2 | High | 1 | 28,00 | 22,54–28,64 | 28,37 | 5 |
| P3 | Low | 10 | 58,85 | 51,97–60,71 | 61,67 | 10 |
| P3 | Medium | 10 | 90,53 | 77,26–95,48 | 93,68 | 10 |
| P3 | High | 10 | 109,02 | 98,79–116,70 | 112,54 | 12 |

Benchmark berjalan di Linux x86-64 dengan AMD EPYC 9V74, Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 dan HiGHS. Setiap profil–tingkat menjalani 25 ulangan dengan urutan acak setelah dua putaran pemanasan. Kolom solver mengukur waktu dari awal hingga pengembalian panggilan SciPy. Kolom total juga mencakup penambahan batas, pembuatan objek untuk solver, dan pemeriksaan solusi. Matriks dasar, pembacaan berkas, enumerasi, dan audit pasangan berada di luar pengukuran tersebut. P10–P90 adalah persentil ke-10 dan ke-90 dari 25 ulangan. P3 menjalankan 10 MILP per ulangan, dua MILP untuk masing-masing titik. Node P3 dijumlahkan untuk 10 penyelesaian.

[CSV seluruh ulangan](Benchmark_Waktu.csv) · [Notebook reproduksi](Verifikasi_P1_P2_P3.ipynb) · [Buka di Google Colab](https://colab.research.google.com/github/kiittkiidd/Lampiran-Model-Matematika-Tesis/blob/main/math_model_acuan/Verifikasi_P1_P2_P3.ipynb)

## 4. Apa yang dijelaskan oleh WCC, pilihan gudang, dan waktu

Pada P2, gap LP awal naik dari 16,62% di Low ke 18,01% di Medium, lalu turun ke 12,49% di High. WCC jaringan naik pada ketiga tingkat. Ini menunjukkan bahwa kekuatan relaksasi LP dan pola keterkaitan kendala menangkap aspek yang berbeda. Catat node dan waktu secara bersamaan karena solver juga mengerjakan presolve, relaksasi, dan pembuktian optimum. Studi perbandingan solver memperhitungkan faktor algoritme dan perangkat keras. [Koch et al. (2022)](https://doi.org/10.1016/j.ejco.2022.100031)

Uji sensitivitas berikut memakai P2 Medium dengan permintaan, rute, tarif, dan skenario yang sama. Semua kapasitas gudang dikalikan faktor pada tabel. Nilai koefisien kapasitas berubah, sementara pola kemunculan variabel tetap.

| Kapasitas relatif | Bobot WCC jaringan | Pola layak dari 16 | Node MILP | Gap LP awal |
| --- | ---: | ---: | ---: | ---: |
| 90% | 142 | 7 | 1 | 16,08% |
| 100% | 142 | 8 | 1 | 18,01% |
| 110% | 142 | 8 | 1 | 19,58% |

Kapasitas 90% mengurangi jumlah pola layak dari 8 menjadi 7. Pada kapasitas 110%, jumlah pola tetap 8 dan gap LP berubah. WCC tetap 61,21% pada ketiga pengujian. Jumlah pola layak merupakan ukuran tambahan untuk keputusan buka/tutup pada kasus ini. Proporsinya dapat dilaporkan terhadap 16 pola yang mungkin. Kemampuan memperoleh angka persis bergantung pada skala enumerasi.

Evaluasi LLM dilakukan melalui eksperimen formulasi. Ukur cakupan aturan, ketepatan indeks dan domain, serta ekuivalensi semantik model. Waktu solver mengukur biaya menyelesaikan model setelah formulasi dibuat. Tiga tingkat jaringan ini memberikan kasus uji untuk mengamati hubungan antarmetrik tersebut.
