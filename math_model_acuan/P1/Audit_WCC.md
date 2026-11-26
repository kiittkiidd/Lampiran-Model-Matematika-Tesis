# Audit WCC P1

WCC dihitung dari identitas variabel lengkap sebelum presolve. Satu pasang baris menyumbang jumlah variabel yang muncul pada kedua baris. Himpunan acuan memuat 34 rute pabrik–gudang dan 66 rute gudang–pelanggan. Posisi tanpa variabel tetap tercatat. [Cara hitung lengkap](../../Lampiran_WCC.md) · [CSV pasangan](Audit_WCC_Pasangan.csv) · [Hasil solver](../Hasil_Benchmark.md)

## 39 baris dan 741 pasangan

| Tingkat | Bobot aktual | Penyebut bersama | WCC |
| --- | ---: | ---: | ---: |
| Low | 109 | 232 | 46,98% |
| Medium | 142 | 232 | 61,21% |
| High | 196 | 232 | 84,48% |

Satu variabel rute masuk muncul pada batas kapasitas pabrik dan neraca gudang–produk. Bagi total WCC, kontribusinya satu. Satu variabel rute keluar muncul pada tiga kendala dan menyumbang $3$ pasang. Variabel buka gudang hanya muncul di satu baris kapasitas pada P1.

| Tingkat | Rute masuk | Rute keluar | Pembilang |
| --- | ---: | ---: | ---: |
| Low | 16 | 31 | $16+3(31)=109$ |
| Medium | 22 | 40 | $22+3(40)=142$ |
| High | 34 | 54 | $34+3(54)=196$ |
| Acuan | 34 | 66 | $34+3(66)=232$ |

Kenaikan Low ke Medium **14,22 poin persentase**. Kenaikan Medium ke High **23,28 poin persentase**. CSV menyimpan semua 741 pasangan, termasuk pasangan berbobot nol.
