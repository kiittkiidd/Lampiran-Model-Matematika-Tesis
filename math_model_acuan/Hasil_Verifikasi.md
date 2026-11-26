# Hasil verifikasi P1–P8

## Kelayakan dan optimum biaya

Seluruh 24 kombinasi memiliki solusi layak. Optimum biaya dibandingkan dengan hasil enumerasi 16 pola buka gudang. Pada profil dua tujuan, kolom biaya di bawah adalah optimum biaya sebelum batas emisi diperketat.

| Profil | Biaya Low | Biaya Medium | Biaya High | Pola layak Low → Medium → High |
| --- | ---: | ---: | ---: | ---: |
| P1 | 299,16 | 277,37 | 242,95 | 6 → 8 → 10 |
| P2 | 299,41 | 277,70 | 243,19 | 6 → 8 → 10 |
| P3 | 299,16 | 277,37 | 242,95 | 6 → 8 → 10 |
| P4 | 299,41 | 277,70 | 243,19 | 6 → 8 → 10 |
| P5 | 306,52 | 285,69 | 249,03 | 6 → 8 → 10 |
| P6 | 306,80 | 286,05 | 249,30 | 5 → 8 → 10 |
| P7 | 306,52 | 285,69 | 249,03 | 6 → 8 → 10 |
| P8 | 306,80 | 286,05 | 249,30 | 5 → 8 → 10 |

Pada Low, bentuk waktu nonlinear dapat mengurangi pola lokasi yang mampu melayani skenario Ramai. Pada P6 dan P8 terdapat lima pola layak. P2 dan P4 masing-masing memiliki enam. Keempat profil tetap memakai graf kendala dan WCC yang sama di Low.

## Pareto biaya dan emisi

Keempat profil dua tujuan memakai sembilan batas absolut bersama per tingkat. Tambahkan dua titik ujung per profil untuk melihat rentang lengkap yang dicapai masing-masing profil. CSV menyimpan 132 hasil dari 108 pengujian batas bersama dan 24 titik ujung. Beberapa pengujian menghasilkan pasangan biaya–emisi yang sama.

| Tingkat | Batas awal (kg CO₂e) | Batas akhir (kg CO₂e) | Jumlah batas |
| --- | ---: | ---: | ---: |
| Low | 136,005 | 172,842 | 9 |
| Medium | 124,368 | 144,984 | 9 |
| High | 111,615 | 155,672 | 9 |

![Titik biaya dan emisi pada Low, Medium, dan High](hasil/Pareto.svg)

Garis putus-putus menghubungkan titik yang ditampilkan sebagai panduan baca. Untuk P8 High, titik ujung biaya memakai G2 + G4 dengan biaya 249,30 dan emisi 155,67 kg CO₂e. Titik ujung emisi memakai G2 + G3 dengan biaya 285,78 dan emisi 111,61 kg CO₂e.

[CSV nilai Pareto](hasil/Pareto.csv) · [Arus dan keputusan lokasi](hasil/Arus_Pareto.csv)

## Pemeriksaan numerik

Model nonlinear memiliki suku kuadratik konveks. Untuk setiap submasalah, sistem menambahkan garis singgung sebagai batas bawah bagi suku kuadrat. Solusi kemudian diperiksa pada bentuk kuadratik asli. Untuk setiap nilai optimum, CSV waktu menyimpan nilai solusi dan batas bawah. Selisih terbesar yang tercatat adalah 0,00024089 satuan fungsi tujuan. Toleransi internal selisih adalah 0,00025, toleransi kelayakan 0,0000002, dan toleransi pemecah seri 0,0006. Titik Pareto dan optimum dilaporkan secara numerik sesuai toleransi tersebut.

Enumerasi memeriksa pilihan gudang secara eksplisit. Jumlah pola yang masih layak diperiksa sebelum uji Pareto. Pada masing-masing batas bersama, enumerasi membandingkan biaya minimum dan pemeriksaan seri emisi. Baris dan variabel tambahan dari relaksasi digunakan oleh solver. Audit WCC mengikuti formulasi acuan.

## Waktu pada uji verifikasi

Tabel berisi total durasi penyelesaian per profil dan tingkat pada satu pelaksanaan. Waktu pengukuran mencakup pembentukan model solver dan langkah penyelesaian utama. Waktu enumerasi terpisah tersedia di CSV ringkasan. Profil dua tujuan mencakup empat langkah titik ujung dan 18 langkah grid bersama. CSV waktu mencatat waktu solver, waktu total, jumlah panggilan solver, dan node untuk setiap langkah. Lingkungan memakai Linux x86-64, Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, dan HiGHS.

| Profil | Langkah per tingkat | Low (ms) | Medium (ms) | High (ms) |
| --- | ---: | ---: | ---: | ---: |
| P1 | 1 | 20,0 | 22,8 | 29,7 |
| P2 | 1 | 20,6 | 19,8 | 33,7 |
| P3 | 22 | 391,7 | 518,6 | 675,9 |
| P4 | 22 | 474,7 | 508,7 | 944,4 |
| P5 | 1 | 71,0 | 67,2 | 89,4 |
| P6 | 1 | 47,5 | 68,5 | 86,6 |
| P7 | 22 | 724,7 | 1355,6 | 4482,0 |
| P8 | 22 | 511,7 | 1271,5 | 1348,8 |

[Waktu per langkah](hasil/Waktu.csv) · [Ringkasan 24 kombinasi](hasil/Ringkasan.csv) · [Notebook verifikasi](Verifikasi_P1_P8.ipynb) · [Buka di Google Colab](https://colab.research.google.com/github/kiittkiidd/Lampiran-Model-Matematika-Tesis/blob/p1-p8-validasi/math_model_acuan/Verifikasi_P1_P8.ipynb)
