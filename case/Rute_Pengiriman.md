# Rute pengiriman PT XYZ per produk

## Cara membaca tabel

Setiap sel menunjukkan **tingkat pertama** yang mengizinkan rute tersebut. Low memakai sel **Low**. Medium memakai sel **Low** dan **Medium**. High memakai ketiganya. Tanda **—** berarti rute untuk produk itu tidak tersedia pada ketiga tingkat.

Pada tabel masuk, baca baris sebagai pabrik asal dan kolom sebagai gudang tujuan. Pada tabel keluar, baca baris sebagai gudang asal dan kolom sebagai zona tujuan. Kiriman melalui suatu gudang memerlukan dua rute untuk produk yang sama serta keputusan membuka gudang itu.

Sebagai contoh, minyak dari pabrik P1 melalui G1 ke K1 tersedia sejak Low. Untuk susu, rute yang sama tidak tersedia karena G1 tidak menangani susu.

## Produk A. Minyak goreng curah

### Pabrik ke gudang

| Pabrik | G1 | G2 | G3 | G4 |
| --- | :---: | :---: | :---: | :---: |
| P1 | Low | Low | — | Medium |
| P2 | Low | — | — | — |
| P3 | High | High | High | High |
| P4 | — | — | — | — |
| P5 | Medium | Low | High | Low |
| P6 | — | — | — | — |

### Gudang ke zona pelanggan

| Gudang | K1 | K2 | K3 | K4 | K5 | K6 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| G1 | Low | Low | Low | Low | Low | Low |
| G2 | Low | High | Low | Low | Low | Low |
| G3 | High | High | High | — | High | — |
| G4 | — | Low | — | Medium | — | Medium |

## Produk B. Sirup gula cair

### Pabrik ke gudang

| Pabrik | G1 | G2 | G3 | G4 |
| --- | :---: | :---: | :---: | :---: |
| P1 | Low | Medium | High | High |
| P2 | Low | Medium | Medium | Low |
| P3 | Low | High | Low | Low |
| P4 | High | High | High | High |
| P5 | — | — | — | — |
| P6 | — | — | — | — |

### Gudang ke zona pelanggan

| Gudang | K1 | K2 | K3 | K4 | K5 | K6 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| G1 | Low | Medium | Low | Medium | Low | Medium |
| G2 | Medium | — | Medium | — | High | — |
| G3 | Low | Low | Low | Low | Low | Low |
| G4 | — | Low | High | Low | High | Low |

## Produk C. Susu cair dingin

### Pabrik ke gudang

| Pabrik | G1 | G2 | G3 | G4 |
| --- | :---: | :---: | :---: | :---: |
| P1 | — | — | — | — |
| P2 | — | — | — | — |
| P3 | — | — | Low | — |
| P4 | — | Low | Low | High |
| P5 | — | — | — | — |
| P6 | — | Low | Low | High |

### Gudang ke zona pelanggan

| Gudang | K1 | K2 | K3 | K4 | K5 | K6 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| G1 | — | — | — | — | — | — |
| G2 | Low | Low | Low | Low | Low | Low |
| G3 | Low | Low | Low | Low | Low | Low |
| G4 | High | High | High | High | High | High |

[Kasus distribusi dan tabel tarif](Kasus_Dasar.md) · [Ringkasan profil](Profil_P1_P8.md) · [Halaman utama](../README.md)
