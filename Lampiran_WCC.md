# WCC jaringan

Weighted Constraint Coupling (WCC) mengukur keterhubungan kendala melalui variabel yang dipakai bersama. Ambil kapasitas gudang G3 dan permintaan pelanggan K2. Jika keduanya memakai variabel kiriman G3 ke K2, variabel itu menyumbang satu bobot hubungan. Dua kendala yang mempunyai dua variabel bersama mendapat bobot dua.

## Blok yang diperiksa

Audit memakai kendala operasi **satu wilayah dan satu kondisi**. Ada 43 posisi kendala. Posisi neraca yang kosong mempunyai himpunan variabel kosong. Model deterministik memakai satu kondisi. Pada profil stokastik, audit memeriksa apakah setiap kondisi memiliki himpunan variabel yang sama setelah label kondisi diselaraskan. Struktur arus yang masuk ke suku kuadratik sudah muncul pada kendala waktu linear. Ini menjaga WCC operasi tetap sama di P1–P8 pada tingkat jaringan yang sama.

### Cara menghitung

1. Untuk setiap pasangan kendala, hitung variabel yang sama-sama dipakai.
2. Jumlahkan bobot pasangan itu. Cara ekuivalennya, variabel yang muncul di k kendala menyumbang k(k−1)/2.
3. Bagi bobot aktual dengan bobot acuan untuk wilayah aktif. Satu wilayah dengan seluruh rute acuan mempunyai bobot 434. Bobot itu diperoleh dari 4 keputusan gudang, 34 rute masuk, dan 66 rute keluar. Masing-masing keputusan gudang dan rute masuk menyumbang satu pasangan. Setiap rute keluar menyumbang enam karena muncul di empat kendala.
4. Kalikan hasil pembagian dengan 100%.

| Lingkup | Bobot aktual | Bobot acuan wilayah aktif | WCC operasi P1–P8 |
| --- | ---: | ---: | ---: |
| Low · 1 wilayah | 206 | 434 | 47,47% |
| Medium · 4 wilayah | 206 + 3 × 266 = 1.004 | 1.736 | 57,83% |
| High · 12 wilayah | 1.004 + 8 × 362 = 3.900 | 5.208 | 74,88% |

Contohnya, Medium berisi Wilayah 01 dengan bobot 206 dan tiga wilayah lain dengan bobot 266 per wilayah. Pembaginya adalah 4 × 434. Angka WCC menyatakan kepadatan hubungan terhadap rute yang diizinkan di wilayah aktif. **Bobot total** menunjukkan jumlah hubungan berbobot yang harus ditangani di seluruh wilayah.

Ukuran ini mengaudit **graf operasi per kondisi**. Jumlah variabel dan kendala masing-masing formulasi lengkap tetap bergantung pada jumlah kondisi dan wilayah. Pembobotan biaya–emisi dilakukan di fungsi tujuan, dan kode memasukkan garis singgung hanya saat penyelesaian solver.

[Model matematika](math_model_acuan/Model_Matematika.md) · [Kode audit WCC](math_model_acuan/benchmark_wilayah.py)
