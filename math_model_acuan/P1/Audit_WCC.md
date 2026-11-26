# Audit WCC dan verifikasi optimasi P1

[CSV pasangan](Audit_WCC_Pasangan.csv) · [Notebook verifikasi P1 dan P2](../Verifikasi_P1_P2.ipynb) · [Buka di Google Colab](https://colab.research.google.com/github/kiittkiidd/Lampiran-Model-Matematika-Tesis/blob/main/math_model_acuan/Verifikasi_P1_P2.ipynb)

## 1. Pasangan baris dan WCC

CSV memuat seluruh 741 pasangan dari 39 posisi baris R1–R39. Untuk setiap pasangan, berkas mencatat batas bobot dan variabel yang mungkin dipakai bersama pada acuan, lalu bobot dan variabel bersama yang muncul pada Low, Medium, dan High. Format kolomnya sama dengan CSV P2. Identitas baris P1 berlaku untuk satu model deterministik per tingkat. Pada P2, akhiran skenario menandai blok model lengkap.

| Tingkat | Variabel | Baris aktif | Penyebut | Bobot | WCC |
| --- | ---: | ---: | ---: | ---: | ---: |
| Low | 36 | 24 | 232 | 64 | 27,59% |
| Medium | 51 | 31 | 232 | 97 | 41,81% |
| High | 89 | 39 | 232 | 187 | 80,60% |

Cara menelusuri persamaan, pasangan berbobot nol, dan pembagi dijelaskan di [Lampiran WCC](../../Lampiran_WCC.md).

## 2. Hasil optimasi

| Tingkat | Gudang yang dibuka | Biaya total minimum |
| --- | --- | ---: |
| Low | G1, G3, G4 | 263,95 |
| Medium | G2, G3, G4 | 264,37 |
| High | G2, G4 | 242,95 |

Notebook membandingkan hasil MILP dengan enumerasi 16 pilihan gudang. Ia juga mencocokkan variabel bersama pada tiap pasangan terhadap CSV P1. [Data bersama](../../case/Data_Bersama.json)
