# Hasil verifikasi P1–P8

Verifikasi mencakup **24 kombinasi** dari delapan profil dan tiga tingkat jaringan. Model memakai satu blok operasi pada P1, P3, P5, dan P7 serta tiga blok pada P2, P4, P6, dan P8. Pada model stokastik, empat keputusan buka gudang dipakai bersama oleh semua blok.

## 1. Ukuran model dan WCC

| Tingkat | WCC blok operasi P1–P8 | Variabel model pasti | Variabel model stokastik |
| --- | ---: | ---: | ---: |
| Low | 47,47% | 51 | 145 |
| Medium | 61,29% | 66 | 190 |
| High | 83,41% | 92 | 268 |

Model pasti memiliki 44 posisi baris dan model stokastik memiliki 130. Keduanya mencakup satu baris batas emisi. WCC memakai 43 posisi baris pada satu blok operasi dan memeriksa kesamaan daftar variabel di setiap posisi. Ukuran pada tabel dihitung sebelum solver menambah variabel dan baris untuk menyelesaikan bentuk nonlinear. [Audit dan definisi WCC](../Lampiran_WCC.md)

## 2. Biaya minimum

Pada profil dua tujuan, tabel mengambil ujung biaya minimum. Nilai model stokastik merupakan biaya harapan.

| Profil | Low | Medium | High |
| --- | ---: | ---: | ---: |
| P1 | 299,16 | 277,37 | 242,95 |
| P2 | 299,41 | 277,70 | 243,19 |
| P3 | 299,16 | 277,37 | 242,95 |
| P4 | 299,41 | 277,70 | 243,19 |
| P5 | 306,52 | 285,69 | 249,03 |
| P6 | 306,80 | 286,05 | 249,30 |
| P7 | 306,52 | 285,69 | 249,03 |
| P8 | 306,80 | 286,05 | 249,30 |

Setiap hasil biaya minimum diperiksa dengan enumerasi terhadap 16 pola buka dan tutup dari keempat calon gudang. Angka pola yang memenuhi kendala tersimpan pada CSV. Untuk model nonlinear, solver membuat pendekatan linear dari bawah pada suku kuadratik. Setiap titik yang dilaporkan diperiksa terhadap kendala asli. Verifikasi memakai toleransi celah 0,00025, kelayakan 0,0000002, dan pemecah seri 0,0006. [Ringkasan 24 kombinasi](hasil/Ringkasan.csv)

## 3. Kompromi biaya dan emisi

Pada setiap jaringan, P3, P4, P7, dan P8 memakai sembilan batas emisi absolut bersama. Tabel Pareto juga memuat dua titik ujung yang diperoleh khusus untuk setiap profil. Totalnya 132 hasil, dengan kemungkinan beberapa batas menghasilkan pasangan biaya dan emisi yang sama.

| Tingkat | Batas awal (kg CO₂e) | Batas akhir (kg CO₂e) | Jumlah batas |
| --- | ---: | ---: | ---: |
| Low | 136,005 | 172,842 | 9 |
| Medium | 124,368 | 144,984 | 9 |
| High | 111,615 | 155,672 | 9 |

![Titik kompromi biaya dan emisi per tingkat jaringan](hasil/Pareto.svg)

Pada P8 High, rencana dengan biaya minimum memakai G2 dan G4, dengan biaya 249,30 dan emisi 155,67 kg CO₂e. Rencana pada ujung emisi memakai G2, G3, dengan biaya 285,78 dan emisi 111,61 kg CO₂e. Garis putus-putus pada grafik membantu mengikuti urutan titik yang ditampilkan. [Nilai Pareto](hasil/Pareto.csv) · [Pilihan gudang dan arus pengiriman](hasil/Arus_Pareto.csv)

## 4. Waktu penyelesaian

Tabel memakai **median 11 pengukuran** setelah satu putaran pemanasan. Urutan 24 kombinasi diacak pada setiap putaran. Waktu mencakup pembuatan struktur solver dan penyelesaian, termasuk penyusunan dan pemeriksaan relaksasi nonlinear. Waktu enumerasi dilaporkan terpisah. Pada profil biaya tunggal, tugasnya satu langkah optimisasi. Pada profil dua tujuan, tugasnya 4 langkah titik ujung dan 18 langkah pada sembilan batas emisi bersama.

| Profil | Langkah per tingkat | Low (ms) | Medium (ms) | High (ms) |
| --- | ---: | ---: | ---: | ---: |
| P1 | 1 | 10,7 | 13,8 | 12,8 |
| P2 | 1 | 19,0 | 20,6 | 33,8 |
| P3 | 22 | 175,1 | 235,0 | 257,0 |
| P4 | 22 | 304,4 | 507,3 | 590,9 |
| P5 | 1 | 31,1 | 33,6 | 44,8 |
| P6 | 1 | 57,0 | 68,1 | 94,7 |
| P7 | 22 | 244,9 | 423,0 | 479,9 |
| P8 | 22 | 570,0 | 1.319,2 | 1.482,7 |

P8 menghabiskan waktu paling lama pada ketiga tingkat dalam pilot ini. P1 Medium sedikit lebih lama daripada P1 High. Angka waktu menunjukkan beban penyelesaian tugas yang ditetapkan pada perangkat dan konfigurasi pengujian. Sebelas ulangan mengukur variasi waktu pada keluarga kasus ini. Lingkungan pengujian memakai Linux x86-64, Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, dan HiGHS 1.8.0 dengan satu thread. [Seluruh ulangan waktu](hasil/Benchmark.csv) · [Detail waktu per langkah verifikasi](hasil/Waktu.csv)

## 5. Iterasi LP, node, dan panggilan solver

**LP** adalah *linear programming*. Ketika solver memeriksa pilihan gudang, ia bisa melonggarkan sementara keputusan buka gudang menjadi angka antara 0 dan 1. Contohnya, angka 0,5 dapat muncul dalam solusi sementara untuk menghitung batas biaya. Solusi bisnis yang dihasilkan tetap memakai 0 atau 1. **Iterasi LP** menghitung langkah numerik yang dilaporkan HiGHS ketika mengerjakan submasalah linear tersebut.

**Node** adalah simpul pada pohon pencarian *branch-and-bound*. Misalnya, jika solver perlu memisahkan keputusan G2, satu cabang menetapkan G2 tutup dan cabang lain menetapkan G2 buka. Pemeriksaan pada satu node bisa membutuhkan banyak iterasi LP. Solver juga dapat menemukan batas yang cukup untuk menyelesaikan masalah pada node awal.

Tabel menjumlahkan iterasi LP dan node pada satu pelaksanaan terpisah dari pengukuran waktu. Hitungan mencakup seluruh panggilan solver dalam langkah yang masuk benchmark. Enumerasi pemeriksaan pola gudang dihitung terpisah.

| Profil | Iterasi LP Low | Iterasi LP Medium | Iterasi LP High | Node Low | Node Medium | Node High |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| P1 | 67 | 111 | 122 | 1 | 1 | 1 |
| P2 | 184 | 265 | 566 | 1 | 1 | 5 |
| P3 | 1.317 | 2.110 | 3.207 | 24 | 26 | 28 |
| P4 | 3.243 | 6.058 | 9.468 | 22 | 34 | 32 |
| P5 | 287 | 333 | 375 | 2 | 2 | 2 |
| P6 | 669 | 846 | 1.423 | 2 | 2 | 10 |
| P7 | 2.645 | 4.292 | 6.140 | 30 | 27 | 37 |
| P8 | 7.195 | 14.300 | 18.665 | 27 | 57 | 64 |

Contohnya, P8 Low memerlukan **7.195 iterasi LP pada 27 node**, sedangkan P7 Low memakai **2.645 iterasi LP pada 30 node**. P8 Low memeriksa lebih sedikit node dengan total kerja LP yang lebih besar. Pada ketiga tingkat, P8 memiliki total iterasi LP tertinggi di antara delapan profil. Jumlah node membantu membaca pencarian, sementara iterasi LP membantu membaca pekerjaan di dalamnya.

Bentuk nonlinear dapat memanggil HiGHS lagi setelah menambahkan batas linear yang memperbaiki pendekatan. Misalnya, 22 langkah P8 High memerlukan 26 panggilan solver. Profil linear memakai satu panggilan per langkah.

| Profil nonlinear | Panggilan Low | Panggilan Medium | Panggilan High |
| --- | ---: | ---: | ---: |
| P5 | 2 | 2 | 2 |
| P6 | 2 | 2 | 2 |
| P7 | 26 | 25 | 27 |
| P8 | 27 | 27 | 26 |

WCC mengukur variabel yang dipakai bersama pada blok jaringan. Waktu dan penghitung kerja solver mencakup seluruh formulasi serta prosedur yang dipakai untuk menghasilkan keluaran. Perbandingan antara biaya tunggal dan Pareto juga mencakup perbedaan jumlah langkah. [Log iterasi LP, node, dan panggilan per langkah](hasil/Kerja_Solver.csv)

## 6. Menjalankan verifikasi

Buka [notebook di Google Colab](https://colab.research.google.com/github/kiittkiidd/Lampiran-Model-Matematika-Tesis/blob/main/math_model_acuan/Verifikasi_P1_P8.ipynb) atau [lihat notebook di GitHub](Verifikasi_P1_P8.ipynb). Untuk menjalankan dari direktori utama repositori dengan Python dan dependensi di atas, gunakan perintah berikut.

```bash
python math_model_acuan/verifikasi.py --hasil hasil_verifikasi --ulangan 11
```

Pengukuran iterasi LP membaca ringkasan HiGHS pada Linux. Waktu bergantung pada mesin yang digunakan. [Kode verifikasi](verifikasi.py) · [Kembali ke daftar isi](../README.md)
