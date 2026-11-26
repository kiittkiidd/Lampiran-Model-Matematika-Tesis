# Audit WCC P2

WCC dihitung dari identitas variabel lengkap sebelum presolve. Satu pasang baris menyumbang jumlah variabel yang muncul pada kedua baris. Himpunan acuan memuat 34 rute pabrik–gudang dan 66 rute gudang–pelanggan. Posisi tanpa variabel tetap tercatat. [Cara hitung lengkap](../../Lampiran_WCC.md) · [CSV pasangan](Audit_WCC_Pasangan.csv) · [Hasil solver](../Hasil_Benchmark.md)

## WCC jaringan

Pada satu blok skenario, himpunan variabel bersama identik dengan P1 setelah indeks skenario melekat pada variabel arus. Tiga tingkat menggunakan penyebut 232 dan menghasilkan 46,98%, 61,21%, serta 84,48%. Ini adalah ukuran jaringan yang digunakan pada perbandingan lintas profil.

## WCC tiga skenario

P2 mempunyai 117 posisi baris dan 6.786 pasangan. Variabel arus untuk Sepi, Sedang, dan Ramai memiliki identitas berbeda. Satu $y_g$ muncul pada tiga baris kapasitas gudang $g$, satu per skenario. Tiga baris tersebut membentuk tiga pasangan yang masing-masing berbobot satu. Empat gudang menyumbang $4(3)=12$ bobot lintas blok. Maka bobot total menjadi $3B_{\mathrm{jaringan}}+12$ dan penyebutnya $3(232)+12=708$.

| Tingkat | Bobot aktual | Penyebut bersama | WCC |
| --- | ---: | ---: | ---: |
| Low | 339 | 708 | 47,88% |
| Medium | 438 | 708 | 61,86% |
| High | 600 | 708 | 84,75% |

Contoh pasangan lintas blok adalah `Sepi:R37` dengan `Ramai:R37`. Keduanya memakai $y_2$ sehingga bobotnya satu. Variabel arus tetap berbeda karena indeks skenarionya berbeda. CSV mencatat seluruh pasangan, baik di dalam blok maupun lintas skenario.
