# Delapan profil penelitian

Setiap tingkat Low, Medium, dan High menjalankan delapan profil pada jaringan yang sama. [Kasus dasar](Kasus_Dasar.md) · [Data lengkap](Data_Bersama.json)

| Profil | Permintaan | Tujuan | Biaya dan waktu penanganan |
| --- | --- | --- | --- |
| P1 | Pasti | Biaya | Linear |
| P2 | Stokastik | Biaya harapan | Linear |
| P3 | Pasti | Biaya dan emisi | Linear |
| P4 | Stokastik | Biaya harapan dan emisi harapan | Linear |
| P5 | Pasti | Biaya | Nonlinear |
| P6 | Stokastik | Biaya harapan | Nonlinear |
| P7 | Pasti | Biaya dan emisi | Nonlinear |
| P8 | Stokastik | Biaya harapan dan emisi harapan | Nonlinear |

## Permintaan

Satu kombinasi gudang dipilih sebelum permintaan terungkap. Setelah skenario terungkap, arus pengiriman dapat disesuaikan. Hanya permintaan produk A di K1 yang berubah. Seluruh pesanan lainnya tetap sesuai tabel kasus dasar. Tiga skenario mewakili tiga bagian distribusi normal dengan rata-rata 3 palet dan simpangan baku 1 palet. Peluang dan nilai wakil memakai presisi penuh di berkas data.

| Skenario | Peluang | Pasti (palet) | Stokastik (palet) |
| --- | ---: | ---: | ---: |
| Sepi | 15,8655% | 3 | 1,474865 |
| Sedang | 68,2689% | 3 | 3 |
| Ramai | 15,8655% | 3 | 4,525135 |

Pada profil pasti, tiga salinan arus memakai permintaan yang sama. Solusi arus terbaik dapat diulang di ketiga salinan. Untuk profil stokastik, satu pilihan gudang harus melayani setiap skenario.

## Penanganan gudang

Kapasitas fisik dan anggaran waktu gudang berlaku pada semua profil. Waktu dasar adalah satu satuan waktu per palet. Anggaran waktu G1–G4 adalah 19,2, 24, 21,6, dan 16,8. Pada profil nonlinear, volume yang lebih besar pada produk yang sama membawa waktu dan biaya tambahan kuadratik. Ini mewakili peningkatan beban penanganan ketika arus produk terkonsentrasi pada gudang yang sama. Parameter waktu dan biaya kuadratik masing-masing 0,025 dan 0,04.

## Emisi

Rencana pengiriman menimbulkan emisi angkutan per palet dan emisi operasi tetap untuk setiap gudang yang dibuka. Gunakan batas 330 kg CO₂e untuk profil biaya tunggal. Profil dua tujuan mencari biaya terendah pada beberapa batas emisi. [Model dan prosedur Pareto](../math_model_acuan/Model_Matematika.md#4-tujuan-dan-pareto)
