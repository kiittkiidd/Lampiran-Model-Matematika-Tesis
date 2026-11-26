# Kasus dasar · Pemilihan gudang dan pengiriman

Perusahaan menyalurkan minuman kemasan (A), pangan kering (B), dan produk dingin (C) dari enam pabrik melalui empat calon gudang ke enam pelanggan selama satu periode. Perusahaan memilih gudang yang dibuka dan jumlah kiriman pada setiap rute. Low, Medium, dan High memakai fasilitas dan data dasar yang sama. Perbedaan tingkat berasal dari rute yang tersedia. [Pengaturan delapan profil](Profil_P1_P8.md)

## Aturan operasi

- Setiap pabrik dapat mengirim paling banyak 8 palet gabungan pada tingkat mana pun. Jumlah kiriman boleh berupa pecahan palet.
- Gudang yang dibuka dapat menerima dan menyalurkan produk melalui rute yang aktif. Jumlah masuk harus sama dengan jumlah keluar untuk setiap produk pada setiap gudang. Gudang yang tutup memiliki arus keluar nol.
- Kapasitas gudang berlaku untuk total arus keluar seluruh produk. Biaya buka dibayar sekali untuk setiap gudang yang dipilih.
- Permintaan masing-masing produk pada setiap pelanggan harus dipenuhi tepat sebesar angka tabel. Pelanggan boleh dilayani dari beberapa gudang melalui rute yang aktif.
- Biaya angkut dibayar per palet pada setiap tahap pengiriman. Biaya penanganan dibayar sekali per palet yang disalurkan gudang. Seluruh tarif memakai satuan biaya yang sama.

| Gudang | Kapasitas (palet) | Biaya buka |
| --- | ---: | ---: |
| G1 | 16 | 25 |
| G2 | 20 | 31 |
| G3 | 18 | 28 |
| G4 | 14 | 17 |

## Jalur masuk dan keluar

Low menggunakan jaringan distribusi dasar. Pada Medium, perusahaan membuka pilihan layanan alternatif, terutama pengiriman A melalui G1 dan distribusi produk dingin C melalui G3. Pada High, penambahan akses produk dan jalur membuat G4 bisa menyalurkan C ke pelanggan wilayah Timur. Semua jalur dari tingkat sebelumnya tersedia pada tingkat berikutnya. Pesanan pelanggan sama pada ketiga tingkat.


**Pola garis**

- A · Minuman kemasan · garis penuh
- B · Pangan kering · garis putus-putus
- C · Produk dingin · garis titik-titik

Setiap panah menunjukkan satu jalur aktif untuk produk di panelnya. Kode fasilitas yang sama di beberapa panel merujuk pada lokasi fisik yang sama.

[Low](diagram/Jaringan_Low.svg) · [Medium](diagram/Jaringan_Medium.svg) · [High](diagram/Jaringan_High.svg)

![Jaringan Low dari pabrik ke calon gudang dan pelanggan, dengan panel untuk produk A, B, dan C](diagram/Jaringan_Low.svg)

<details>
<summary>Lihat diagram Medium</summary>

![Jaringan Medium dari pabrik ke calon gudang dan pelanggan, dengan panel untuk produk A, B, dan C](diagram/Jaringan_Medium.svg)

</details>

<details>
<summary>Lihat diagram High</summary>

![Jaringan High dari pabrik ke calon gudang dan pelanggan, dengan panel untuk produk A, B, dan C](diagram/Jaringan_High.svg)

</details>

Pada tabel masuk, setiap pabrik pada satu baris produk boleh memasok setiap gudang pada baris tersebut. Tabel keluar menyebut pelanggan yang dapat dilayani untuk setiap gudang dan produk. Tanda — berarti jalur belum tersedia.

| Tingkat | Produk | Pabrik pemasok | Gudang penerima |
| --- | --- | --- | --- |
| Low | A | P1, P5 | G1, G2, G4 |
| Low | B | P2, P3 | G1, G3, G4 |
| Low | C | P4, P6 | G2, G3 |
| Medium | A | P1, P5 | G1, G2, G4 |
| Medium | B | P1, P2, P3 | G1, G2, G3, G4 |
| Medium | C | P4, P6 | G2, G3 |
| High | A | P1, P3, P5 | G1, G2, G3, G4 |
| High | B | P1, P2, P3, P4 | G1, G2, G3, G4 |
| High | C | P4, P6 | G2, G3, G4 |

| Gudang | Produk | Low | Medium | High |
| --- | --- | --- | --- | --- |
| G1 | A | K1 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G1 | B | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G2 | A | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G2 | B | — | — | K1, K3, K5 |
| G2 | C | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G3 | A | — | — | K1, K3, K5 |
| G3 | B | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G3 | C | K2, K4 | K1, K2, K3, K4, K5, K6 | K1, K2, K3, K4, K5, K6 |
| G4 | A | K2 | K2 | K2, K4, K6 |
| G4 | B | K2, K4, K6 | K2, K4, K6 | K1, K2, K3, K4, K5, K6 |
| G4 | C | — | — | K2, K4, K6 |

## Permintaan per pelanggan

Semua angka dalam palet dan berlaku untuk seluruh tingkat.

| Pelanggan | A | B | C | Total |
| --- | ---: | ---: | ---: | ---: |
| K1 | 3 | 1 | 1 | 5 |
| K2 | 3 | 1 | 1 | 5 |
| K3 | 1 | 3 | 1 | 5 |
| K4 | 1 | 3 | 1 | 5 |
| K5 | 1 | 1 | 3 | 5 |
| K6 | 1 | 1 | 3 | 5 |
| **Total** | 10 | 10 | 10 | 30 |

## Tarif per palet

Tarif angkut berlaku untuk seluruh produk pada satu pasangan lokasi. Pemakaian tarif tetap mengikuti jalur aktif pada level yang dipilih. Data tarif benchmark bersifat sintetis.

### Angkut pabrik ke gudang

| Pabrik | G1 | G2 | G3 | G4 |
| --- | ---: | ---: | ---: | ---: |
| P1 | 2 | 3 | 7 | 8 |
| P2 | 3 | 4 | 7 | 8 |
| P3 | 7 | 6 | 2 | 3 |
| P4 | 2 | 2 | 7 | 8 |
| P5 | 7 | 6 | 3 | 2 |
| P6 | 7 | 6 | 2 | 3 |

### Angkut gudang ke pelanggan

| Gudang | K1 | K2 | K3 | K4 | K5 | K6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| G1 | 2 | 7 | 2 | 7 | 3 | 7 |
| G2 | 1 | 7 | 2 | 7 | 2 | 6 |
| G3 | 7 | 2 | 7 | 2 | 6 | 2 |
| G4 | 7 | 1,79 | 6 | 2 | 7 | 2 |

### Penanganan di gudang

| Gudang | A | B | C |
| --- | ---: | ---: | ---: |
| G1 | 1 | 1 | — |
| G2 | 2 | 2 | 3 |
| G3 | 2 | 1 | 2 |
| G4 | 1 | 1 | 3 |

Salinan data dalam format terstruktur tersedia di [Data bersama P1–P8](Data_Bersama.json).
