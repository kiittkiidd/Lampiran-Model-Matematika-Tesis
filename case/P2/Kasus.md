# Kasus P2 — Pemilihan gudang dan pengiriman dengan permintaan stokastik

Gunakan jaringan, kapasitas, biaya buka, tarif angkut, tarif penanganan, dan permintaan dasar dari [kasus P1](../P1/Kasus.md). Jalankan Low, Medium, dan High sebagai tiga instans terpisah. Pada P2, permintaan **produk A di K1** belum diketahui saat perusahaan harus memutuskan gudang mana yang dibuka. Permintaan setiap pelanggan–produk lain tetap sebesar permintaan dasar pada level tersebut.

## Keputusan yang harus dibuat

1. Sebelum permintaan K1 diketahui, pilih satu kombinasi gudang. Pilihan tersebut berlaku untuk seluruh skenario. Biaya buka dibayar sekali.
2. Setelah skenario terungkap, tentukan jumlah kiriman dari pabrik ke gudang dan dari gudang ke pelanggan. Semua kapasitas dan aturan operasi P1 berlaku di setiap skenario. Penuhi permintaan yang terjadi pada skenario tersebut.
3. Minimalkan biaya buka ditambah biaya operasi rata-rata yang dibobot dengan peluang skenario.

## Data ketidakpastian

Permintaan produk A di K1 mengikuti distribusi normal dengan rata-rata sebesar permintaan dasar P1 dan simpangan baku 1 palet. Untuk optimasi, pakai tiga skenario wakil dengan rentang di bawah batas bawah, rentang antara kedua batas, dan rentang di atas batas atas. Batas bawah adalah rata-rata dikurangi satu simpangan baku. Batas atas adalah rata-rata ditambah satu simpangan baku. Permintaan wakil setiap skenario adalah rata-rata kondisional dalam rentangnya.

| Skenario | Peluang (%) | A di K1 pada Low (palet) | A di K1 pada Medium (palet) | A di K1 pada High (palet) |
| --- | ---: | ---: | ---: | ---: |
| Sepi | 15,865525 | 3,474865 | 1,474865 | 1,474865 |
| Sedang | 68,268949 | 5 | 3 | 3 |
| Ramai | 15,865525 | 6,525135 | 4,525135 | 4,525135 |

Gunakan peluang dan pergeseran permintaan dengan presisi penuh dari [Data bersama P1 dan P2](../Data_Bersama.json). Pilih gudang yang sanggup melayani tiga skenario pada tabel. Ketiganya adalah representasi diskret untuk optimasi. Skenario Ramai memakai rata-rata rentang ekor atas.
