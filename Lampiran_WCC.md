# Menghitung Weighted Constraint Coupling

Weighted Constraint Coupling atau **WCC** mengukur seberapa banyak aturan model menggunakan keputusan yang sama. Satu keputusan yang muncul di dua aturan memberi bobot satu pada pasangan aturan itu. Jika dua keputusan muncul bersama di kedua aturan, bobot pasangannya dua.

## Contoh dari jaringan PT XYZ

Ambil keputusan **ton minyak dari P1 ke G1**. Keputusan ini muncul di kendala kapasitas P1 dan kendala neraca minyak G1. Jadi pasangan kedua aturan mendapat bobot satu dari kiriman tersebut.

Lalu ambil keputusan **ton minyak dari G1 ke K1**. Keputusan ini muncul pada neraca minyak G1, pesanan minyak K1, kapasitas tonase G1, dan batas waktu G1. Empat aturan membentuk enam pasangan, sehingga kiriman tersebut memberi bobot enam pada hitungan total.

Secara umum, jika keputusan $v$ muncul pada $`m_v`$ baris yang diperiksa, kontribusinya adalah

$$
\binom{m_v}{2}.
$$

Masukkan hanya kemunculan yang mempunyai koefisien tidak nol. Misalnya, kapasitas pabrik P1 dan pesanan di K1 tidak berbagi variabel secara langsung, karena masing-masing memakai tahap kiriman yang berlainan.

## Menghitung angka Low–Medium–High

Audit memakai 43 baris operasi dalam satu kondisi permintaan sebelum penyederhanaan solver. Baris ini mencakup kapasitas pabrik, keseimbangan barang, pemenuhan pesanan, kapasitas gudang, dan waktu kerja gudang.

| Jenis keputusan | Baris yang memakainya | Bobot per keputusan |
| --- | --- | ---: |
| Buka gudang | Kapasitas dan waktu kerja gudang | 1 |
| Kiriman pabrik → gudang | Kapasitas pabrik dan neraca gudang–produk | 1 |
| Kiriman gudang → zona | Neraca gudang–produk, pesanan, kapasitas gudang, dan waktu kerja | 6 |

Untuk Low ada 4 pilihan buka gudang, 16 rute masuk, dan 36 rute keluar. Bobot totalnya $4+16+6(36)=236$.

Acuan bersama menggunakan 35 rute masuk High dan mengizinkan seluruh 6 zona bagi 11 pasangan gudang–produk yang kompatibel. Maka acuan memiliki 66 rute keluar dan berbobot $4+35+6(66)=435$.

| Tingkat | Rute masuk | Rute keluar | Bobot | WCC |
| --- | ---: | ---: | ---: | ---: |
| Low | 16 | 36 | 236 | 54,25% |
| Medium | 21 | 43 | 283 | 65,06% |
| High | 35 | 57 | 381 | 87,59% |

Hitung WCC dengan membagi bobot tingkat oleh 435. Untuk Low, $236/435\times100\%=54{,}25\%$.

WCC tabel ini sama untuk P1–P8 pada tingkat rute yang sama. Profil stokastik memakai satu salinan struktur operasi per skenario dalam audit ini. Pada profil nonlinear, suku kuadrat memakai kiriman yang sudah muncul pada baris waktu. Kendala tambahan batas emisi ε, pemilihan emisi saat biaya sama, domain variabel, serta garis singgung solver berada di luar 43 baris operasi yang diukur.

[Model matematika](math_model_acuan/Model_Matematika.md) · [Hasil validasi](math_model_acuan/Hasil_Verifikasi.md) · [Halaman utama](README.md)
