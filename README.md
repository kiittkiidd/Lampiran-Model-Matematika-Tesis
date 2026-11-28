# Lampiran Model Matematika Tesis

**Versi 1.0.0-SCIP · 28 November 2026**

Kasus PT XYZ Bahan Pangan mempelajari pemilihan gudang dan distribusi tiga produk cair melalui pabrik → gudang → zona pelanggan dalam satu periode. Delapan profil menggabungkan permintaan pasti/stokastik, penanganan linear/nonlinear, serta satu/dua tujuan. Setiap profil mempunyai pilihan rute Low, Medium, dan High.

## Mulai membaca

| Kebutuhan | Halaman |
|---|---|
| Menyusun model sendiri dari kasus | **[Kasus lengkap P1–P8](case/Kasus_Dasar.md)** |
| Memeriksa formulasi | [Model matematika dan penjelasan persamaan](math_model_acuan/Model_Matematika.md) |
| Memahami dan menghitung WCC | [Tutorial WCC, contoh berindeks, dan graf](Lampiran_WCC.md) |
| Melihat hasil optimisasi dan benchmark | [Hasil verifikasi, waktu, iterasi, dan Pareto](math_model_acuan/Hasil_Verifikasi.md) |
| Menjalankan ulang | [Notebook](math_model_acuan/Reproduksi.ipynb) · [Buka di Colab](https://colab.research.google.com/github/kiittkiidd/Lampiran-Model-Matematika-Tesis/blob/main/math_model_acuan/Reproduksi.ipynb) |

Dokumen kasus memuat seluruh tabel input dan aturan bisnis. Pemodel dapat mulai dari dokumen tersebut sebelum membandingkan hasilnya dengan model acuan. JSON dan kode disediakan untuk reproduksi; angka input juga tersedia dalam tabel pada halaman kasus dan [CSV](case/data_tabel/).

## Jaringan dan profil

Jumlah fasilitas tetap: enam pabrik, empat gudang, dan enam zona pelanggan. Low mengizinkan 36 rute keluar, Medium 42, dan High 60. Semua rute Low tersedia pada Medium dan High.

| Profil | Permintaan | Penanganan | Tujuan |
|---|---|---|---|
| P1 | Pasti | Linear | Biaya |
| P2 | 27 skenario | Linear | Biaya harapan |
| P3 | Pasti | Linear | Biaya dan emisi |
| P4 | 27 skenario | Linear | Biaya dan emisi harapan |
| P5 | Pasti | Kuadratik | Biaya |
| P6 | 27 skenario | Kuadratik | Biaya harapan |
| P7 | Pasti | Kuadratik | Biaya dan emisi |
| P8 | 27 skenario | Kuadratik | Biaya dan emisi harapan |

WCC pada 38 baris operasi per skenario adalah **50,46% / 58,72% / 83,49%** untuk Low/Medium/High. Cakupan yang sama digunakan pada seluruh profil; formulasi stokastik lengkap tetap memuat 27 skenario. Penjelasan pembilang, penyebut bersama 436, dan audit 703 pasangan tersedia pada tutorial.

## Menjalankan model

SCIP adalah solver default. Build yang diuji memakai SCIP 10.0.2, PySCIPOpt 6.3.0, SoPlex 8.0.2, dan Ipopt 3.14.19. Tidak diperlukan lisensi akademik berbayar.

```bash
python -m pip install -r math_model_acuan/source/requirements.txt
python math_model_acuan/source/solve.py --profile P1 --level L --output hasil_P1_L.json
```

Gunakan P1–P8 dan L/M/H. Profil satu tujuan menjalankan satu optimisasi; profil Pareto menjalankan 50 optimisasi untuk 25 batas emisi. Notebook menyediakan instalasi, pemilihan profil, pemeriksaan solusi, dan penyimpanan keluaran.

Pemeriksaan hasil acuan tersimpan:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python math_model_acuan/source/verify.py
```

## Hasil dan rekaman versi

[Ringkasan 24 kombinasi](math_model_acuan/hasil/Ringkasan.csv) · [Seluruh 72 pengukuran](math_model_acuan/hasil/Benchmark.csv) · [Pekerjaan per langkah](math_model_acuan/hasil/Waktu_dan_Iterasi_Per_Langkah.csv) · [Pasangan biaya–emisi](math_model_acuan/hasil/Pareto.csv)

Data mentah kiriman tersimpan sebagai JSONL terkompresi gzip agar ukuran repositori tetap ringkas. Pembaca verifikasi membuka berkas itu secara otomatis. Catatan [penyesuaian data](math_model_acuan/hasil/Perubahan_Data.md), [checksum versi](math_model_acuan/hasil/MANIFEST.json), dan hasil sensitivitas tersedia bersama audit.

Seluruh gambar adalah SVG/PNG statis. Data, kode optimisasi, dan hasil utama sama dengan versi yang diuji. Pengukuran utama memakai median tiga ulangan setelah pemanasan; hasil variasi permintaan dilaporkan terpisah.
