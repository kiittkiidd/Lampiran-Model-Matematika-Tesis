# Audit WCC dan verifikasi optimasi P2

## 1. Satu blok skenario terhadap P1

Pada setiap level, satu blok skenario P2 menggunakan R1–R39 dan rute yang sama dengan P1. Setelah indeks skenario diabaikan pada satu blok, variabel bersama pada tiap pasangan persis sama. Peluang dan besarnya permintaan hanya memengaruhi fungsi tujuan atau ruas kanan.

| Tingkat | Bobot satu blok | Penyebut | WCC per blok |
| --- | ---: | ---: | ---: |
| L | 64 | 232 | 27,59% |
| M | 97 | 232 | 41,81% |
| H | 187 | 232 | 80,60% |

## 2. Formulasi lengkap tiga skenario

Tiga blok masing-masing menyumbang bobot yang sama. Di antara dua blok, hanya pasangan kendala kapasitas gudang yang merujuk pada gudang yang sama berbagi satu variabel $y_g$. Ada tiga pasangan skenario dan empat gudang, sehingga total tambahan adalah $3\times4=12$ poin. Penyebut acuan graf lengkap mengikuti aturan yang sama, yaitu $3\times232+12=708$.

```math
B_{\mathrm{penuh}}=3B_{\mathrm{blok}}+12.
```

Tiga blok menyediakan 117 posisi R1–R39 pada setiap level, dengan $117\cdot116/2=6.786$ pasangan posisi. Posisi dengan baris $0=0$ mempunyai NNZ nol.

| Tingkat | Variabel | Baris aktif | NNZ | Pasangan positif | Bobot penuh | Penyebut | WCC penuh |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| L | 100 | 72 | 252 | 180 | 204 | 708 | 28,81% |
| M | 145 | 93 | 369 | 255 | 303 | 708 | 42,80% |
| H | 259 | 117 | 675 | 453 | 573 | 708 | 80,93% |

## 3. Hasil optimasi dengan tarif benchmark

MILP gabungan dan enumerasi 16 pola gudang memberikan biaya minimum yang sama pada keenam instans P1 dan P2. Pola gudang P1 dihitung dari permintaan rata-rata, kemudian dievaluasi lagi pada tiga skenario P2 dengan biaya operasi optimal per skenario.

| Tingkat | Gudang P1 | Biaya P1 | Gudang P2 | Biaya ekspektasian minimum P2 | Biaya jika memakai pilihan P1 dalam P2 |
| --- | --- | ---: | --- | ---: | ---: |
| L | G1, G3, G4 | 263,9500 | G1, G3, G4 | 263,9500 | 263,9500 |
| M | G2, G3, G4 | 264,3700 | G2, G3, G4 | 264,4533 | 264,4533 |
| H | G2, G4 | 242,9500 | G2, G3 | 243,0833 | 243,1920 |

Pada High, P1 membuka G2 dan G4. P2 memilih G2 dan G3. Memakai keputusan P2 pada tiga skenario menghemat sekitar **0,1087 satuan biaya ekspektasian** dibanding memakai pilihan P1 pada skenario yang sama. Ini selisih untuk dataset sintetis yang ditetapkan.

| Tingkat | Pola gudang layak di P2 | Biaya buka optimum | Operasi Sepi | Operasi Sedang | Operasi Ramai |
| --- | ---: | ---: | ---: | ---: | ---: |
| L | 10 | 70,0000 | 186,3243 | 193,9500 | 201,5757 |
| M | 2 | 76,0000 | 179,2192 | 188,3700 | 198,0459 |
| H | 6 | 59,0000 | 174,8492 | 184,0000 | 193,6759 |

Rincian data ada di [Data bersama](../../case/Data_Bersama.json). Jalankan [Verifikasi.py](Verifikasi.py) dengan Python 3, NumPy, dan SciPy untuk menghitung ulang WCC dan nilai optimum.
