# Audit WCC P3

WCC dihitung dari identitas variabel lengkap sebelum presolve. Satu pasang baris menyumbang jumlah variabel yang muncul pada kedua baris. Himpunan acuan memuat 34 rute pabrik–gudang dan 66 rute gudang–pelanggan. Posisi tanpa variabel tetap tercatat. [Cara hitung lengkap](../../Lampiran_WCC.md) · [CSV pasangan](Audit_WCC_Pasangan.csv) · [Hasil solver](../Hasil_Benchmark.md)

## Jaringan dan formulasi dengan batas emisi

| Cakupan | Posisi baris | Pasangan baris | Penyebut |
| --- | ---: | ---: | ---: |
| R1–R39 untuk membandingkan jaringan | 39 | 741 | 232 |
| R1–R40 pada formulasi dengan batas emisi | 40 | 780 | 502 |

Ekspresi tujuan biaya dan emisi memakai variabel yang sudah ada. Kedua ekspresi merupakan tujuan pada model dua tujuan. Ketika batas emisi digunakan, R40 memuat semua variabel keputusan karena semua faktor emisi yang relevan positif. Akibatnya, irisan R40 dengan suatu baris operasi sama dengan himpunan variabel pada baris itu. Tambahan total bobot sama dengan jumlah koefisien keputusan bukan nol pada R1–R39. Sebagai contoh, R18 Low memuat $z_{1,1,A}$ dan $z_{2,1,A}$. Kedua variabel juga muncul di R40, sehingga pasangan R18–R40 berbobot dua.

| Tingkat | Bobot R1–R39 | Tambahan bobot R40 | Bobot R1–R40 |
| --- | ---: | ---: | ---: |
| Low | 109 | 129 | 238 |
| Medium | 142 | 168 | 310 |
| High | 196 | 234 | 430 |
| Acuan | 232 | 270 | 502 |

| Tingkat | Bobot aktual | Penyebut bersama | WCC |
| --- | ---: | ---: | ---: |
| Low | 238 | 502 | 47,41% |
| Medium | 310 | 502 | 61,75% |
| High | 430 | 502 | 85,66% |

Nilai $\epsilon$ mengubah ruas kanan R40. Selama baris R40 aktif, berbagai nilai batas emisi menghasilkan pola WCC yang sama pada satu tingkat. CSV mengikuti formulasi standar dengan batas emisi. Pemecah seri pada notebook adalah pemanggilan solver lanjutan yang memakai satu batas sementara tambahan.
