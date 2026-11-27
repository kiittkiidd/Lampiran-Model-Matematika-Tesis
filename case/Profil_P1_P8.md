# Delapan profil keputusan PT XYZ

Semua profil memakai [kasus dasar](Kasus_Dasar.md) dan dapat dijalankan pada Low, Medium, atau High. Pilih profil untuk menentukan kapan pesanan diketahui, bagaimana penanganan gudang dihitung, dan hasil apa yang diminta.

| Profil | Permintaan | Penanganan | Tujuan |
| --- | --- | --- | --- |
| P1 | Pasti | Linear | Biaya |
| P2 | Stokastik | Linear | Biaya harapan |
| P3 | Pasti | Linear | Biaya dan emisi |
| P4 | Stokastik | Linear | Biaya dan emisi harapan |
| P5 | Pasti | Nonlinear | Biaya |
| P6 | Stokastik | Nonlinear | Biaya harapan |
| P7 | Pasti | Nonlinear | Biaya dan emisi |
| P8 | Stokastik | Nonlinear | Biaya dan emisi harapan |

## Kapan pesanan diketahui?

Pada P1, P3, P5, dan P7, jumlah pesanan diketahui saat perusahaan menyusun rencana. Laporkan gudang yang dibuka dan seluruh jumlah kiriman.

Pada P2, P4, P6, dan P8, perusahaan memilih gudang **sebelum** mengetahui jumlah pesanan yang terjadi. Setelah pesanan diketahui, kiriman dapat disesuaikan. Bukaan gudang berlaku sama pada ketiga skenario. Hanya permintaan **minyak goreng di K1** yang berubah antarskenario. Semua pesanan wajib dipenuhi pada setiap skenario.

| Skenario | Peluang (dibulatkan) | Pesanan jika nilai tengah 3 ton |
| --- | ---: | ---: |
| Sepi | 15,87% | 1,475 ton |
| Sedang | 68,27% | 3,000 ton |
| Ramai | 15,87% | 4,525 ton |

Data mesin menyimpan peluang dan penyimpangan sebelum pembulatan. Biaya dan emisi harapan berarti rata-rata berbobot peluang. Biaya buka dan emisi tetap gudang dihitung satu kali. Laporkan keputusan gudang dan rencana kiriman untuk masing-masing skenario.

## Bagaimana waktu dan biaya penanganan dihitung?

Profil linear memakai tarif penanganan dasar per ton dan satu jam kerja per ton. Profil nonlinear menambahkan **0,04 satuan biaya** dan **0,025 jam**, masing-masing dikalikan kuadrat tonase satu produk yang ditangani satu gudang. Perhitungan dilakukan untuk tiap produk dan tiap gudang secara terpisah.

## Keluaran untuk profil biaya–emisi

P3, P4, P7, dan P8 meminta **sampel Pareto front**, yaitu pilihan biaya dan emisi yang memperlihatkan kompromi keduanya. Gunakan 25 batas emisi, termasuk kedua ujung rentang. Untuk setiap batas, cari biaya terendah lalu pilih emisi terendah di antara solusi dengan biaya yang sama, sesuai toleransi penyelesaian. Pada profil stokastik, batas diterapkan pada **emisi harapan**. Laporkan pasangan biaya–emisi dan gudang yang dibuka. Titik yang berulang tampil sekali pada grafik.

[Model matematika acuan](../math_model_acuan/Model_Matematika.md) · [Halaman utama](../README.md)
