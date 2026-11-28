# Persamaan operasi Low, R1–R38

Seluruh baris pada halaman ini berasal dari daftar rute Low. Indeks $i,g,j,p$ berturut-turut menunjukkan pabrik, gudang, zona, dan produk. $x_{igp}$ adalah ton kiriman masuk; $z_{gjp}$ adalah ton kiriman keluar; $y_g$ memilih gudang yang dibuka. Permintaan pasti menggunakan tabel dasar. Untuk satu skenario stokastik, tambahkan indeks skenario pada setiap kiriman dan gunakan pesanan skenario tersebut.

### R1. Neraca produk A di G1


```math
\begin{aligned}
\mathrm{R1}:\quad &x_{1,1,A}=z_{1,1,A}+z_{1,2,A}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R2. Neraca produk B di G1


```math
\begin{aligned}
\mathrm{R2}:\quad &x_{1,1,B}=z_{1,3,B}+z_{1,4,B}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R3. Neraca produk C di G1


```math
\begin{aligned}
\mathrm{R3}:\quad &x_{4,1,C}=z_{1,5,C}+z_{1,6,C}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R4. Neraca produk A di G2


```math
\begin{aligned}
\mathrm{R4}:\quad &x_{1,2,A}+x_{2,2,A}=z_{2,1,A}+z_{2,2,A}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R5. Neraca produk B di G2


```math
\begin{aligned}
\mathrm{R5}:\quad &x_{4,2,B}=z_{2,3,B}+z_{2,4,B}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R6. Neraca produk C di G2


```math
\begin{aligned}
\mathrm{R6}:\quad &x_{4,2,C}=z_{2,5,C}+z_{2,6,C}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R7. Neraca produk A di G3


```math
\begin{aligned}
\mathrm{R7}:\quad &x_{3,3,A}=z_{3,3,A}+z_{3,4,A}+z_{3,5,A}+z_{3,6,A}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R8. Neraca produk B di G3


```math
\begin{aligned}
\mathrm{R8}:\quad &x_{3,3,B}=z_{3,1,B}+z_{3,2,B}+z_{3,5,B}+z_{3,6,B}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R9. Neraca produk C di G3


```math
\begin{aligned}
\mathrm{R9}:\quad &x_{3,3,C}=z_{3,1,C}+z_{3,2,C}+z_{3,3,C}+z_{3,4,C}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R10. Neraca produk A di G4


```math
\begin{aligned}
\mathrm{R10}:\quad &x_{3,4,A}+x_{5,4,A}=z_{4,3,A}+z_{4,4,A}+z_{4,5,A}+z_{4,6,A}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R11. Neraca produk B di G4


```math
\begin{aligned}
\mathrm{R11}:\quad &x_{3,4,B}+x_{6,4,B}=z_{4,1,B}+z_{4,2,B}+z_{4,5,B}+z_{4,6,B}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R12. Neraca produk C di G4


```math
\begin{aligned}
\mathrm{R12}:\quad &x_{5,4,C}+x_{6,4,C}=z_{4,1,C}+z_{4,2,C}+z_{4,3,C}+z_{4,4,C}
\end{aligned}
```

Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.

### R13. Pesanan produk A di K1


```math
\begin{aligned}
\mathrm{R13}:\quad &z_{1,1,A}+z_{2,1,A}=3{,}17
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R14. Pesanan produk B di K1


```math
\begin{aligned}
\mathrm{R14}:\quad &z_{3,1,B}+z_{4,1,B}=0{,}88
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R15. Pesanan produk C di K1


```math
\begin{aligned}
\mathrm{R15}:\quad &z_{3,1,C}+z_{4,1,C}=1{,}09
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R16. Pesanan produk A di K2


```math
\begin{aligned}
\mathrm{R16}:\quad &z_{1,2,A}+z_{2,2,A}=2{,}84
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R17. Pesanan produk B di K2


```math
\begin{aligned}
\mathrm{R17}:\quad &z_{3,2,B}+z_{4,2,B}=1{,}16
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R18. Pesanan produk C di K2


```math
\begin{aligned}
\mathrm{R18}:\quad &z_{3,2,C}+z_{4,2,C}=0{,}86
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R19. Pesanan produk A di K3


```math
\begin{aligned}
\mathrm{R19}:\quad &z_{3,3,A}+z_{4,3,A}=1{,}12
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R20. Pesanan produk B di K3


```math
\begin{aligned}
\mathrm{R20}:\quad &z_{1,3,B}+z_{2,3,B}=2{,}79
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R21. Pesanan produk C di K3


```math
\begin{aligned}
\mathrm{R21}:\quad &z_{3,3,C}+z_{4,3,C}=1{,}07
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R22. Pesanan produk A di K4


```math
\begin{aligned}
\mathrm{R22}:\quad &z_{3,4,A}+z_{4,4,A}=0{,}93
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R23. Pesanan produk B di K4


```math
\begin{aligned}
\mathrm{R23}:\quad &z_{1,4,B}+z_{2,4,B}=3{,}24
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R24. Pesanan produk C di K4


```math
\begin{aligned}
\mathrm{R24}:\quad &z_{3,4,C}+z_{4,4,C}=0{,}98
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R25. Pesanan produk A di K5


```math
\begin{aligned}
\mathrm{R25}:\quad &z_{3,5,A}+z_{4,5,A}=1{,}03
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R26. Pesanan produk B di K5


```math
\begin{aligned}
\mathrm{R26}:\quad &z_{3,5,B}+z_{4,5,B}=0{,}97
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R27. Pesanan produk C di K5


```math
\begin{aligned}
\mathrm{R27}:\quad &z_{1,5,C}+z_{2,5,C}=2{,}73
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R28. Pesanan produk A di K6


```math
\begin{aligned}
\mathrm{R28}:\quad &z_{3,6,A}+z_{4,6,A}=0{,}91
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R29. Pesanan produk B di K6


```math
\begin{aligned}
\mathrm{R29}:\quad &z_{3,6,B}+z_{4,6,B}=0{,}96
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R30. Pesanan produk C di K6


```math
\begin{aligned}
\mathrm{R30}:\quad &z_{1,6,C}+z_{2,6,C}=3{,}27
\end{aligned}
```

Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.

### R31. Batas kapasitas tonase G1


```math
\begin{aligned}
\mathrm{R31}:\quad &z_{1,1,A}+z_{1,2,A}+z_{1,3,B}+z_{1,4,B}\\
&\quad+z_{1,5,C}+z_{1,6,C}\le16y_{1}
\end{aligned}
```

Ketiga produk berbagi batas gudang yang sama. Nilai buka nol membuat seluruh arus gudang nol.

### R32. Batas kapasitas tonase G2


```math
\begin{aligned}
\mathrm{R32}:\quad &z_{2,1,A}+z_{2,2,A}+z_{2,3,B}+z_{2,4,B}\\
&\quad+z_{2,5,C}+z_{2,6,C}\le20y_{2}
\end{aligned}
```

Ketiga produk berbagi batas gudang yang sama. Nilai buka nol membuat seluruh arus gudang nol.

### R33. Batas kapasitas tonase G3


```math
\begin{aligned}
\mathrm{R33}:\quad &z_{3,1,B}+z_{3,1,C}+z_{3,2,B}+z_{3,2,C}\\
&\quad+z_{3,3,A}+z_{3,3,C}+z_{3,4,A}+z_{3,4,C}\\
&\quad+z_{3,5,A}+z_{3,5,B}+z_{3,6,A}+z_{3,6,B}\le18y_{3}
\end{aligned}
```

Ketiga produk berbagi batas gudang yang sama. Nilai buka nol membuat seluruh arus gudang nol.

### R34. Batas kapasitas tonase G4


```math
\begin{aligned}
\mathrm{R34}:\quad &z_{4,1,B}+z_{4,1,C}+z_{4,2,B}+z_{4,2,C}\\
&\quad+z_{4,3,A}+z_{4,3,C}+z_{4,4,A}+z_{4,4,C}\\
&\quad+z_{4,5,A}+z_{4,5,B}+z_{4,6,A}+z_{4,6,B}\le14y_{4}
\end{aligned}
```

Ketiga produk berbagi batas gudang yang sama. Nilai buka nol membuat seluruh arus gudang nol.

### R35. Batas waktu linear G1


```math
\begin{aligned}
\mathrm{R35}:\quad &z_{1,1,A}+z_{1,2,A}+z_{1,3,B}+z_{1,4,B}\\
&\quad+z_{1,5,C}+z_{1,6,C}\le17{,}8y_{1}
\end{aligned}
```

Ketiga produk berbagi batas gudang yang sama. Nilai buka nol membuat seluruh arus gudang nol.

### R36. Batas waktu linear G2


```math
\begin{aligned}
\mathrm{R36}:\quad &z_{2,1,A}+z_{2,2,A}+z_{2,3,B}+z_{2,4,B}\\
&\quad+z_{2,5,C}+z_{2,6,C}\le22{,}4y_{2}
\end{aligned}
```

Ketiga produk berbagi batas gudang yang sama. Nilai buka nol membuat seluruh arus gudang nol.

### R37. Batas waktu linear G3


```math
\begin{aligned}
\mathrm{R37}:\quad &z_{3,1,B}+z_{3,1,C}+z_{3,2,B}+z_{3,2,C}\\
&\quad+z_{3,3,A}+z_{3,3,C}+z_{3,4,A}+z_{3,4,C}\\
&\quad+z_{3,5,A}+z_{3,5,B}+z_{3,6,A}+z_{3,6,B}\le19{,}8y_{3}
\end{aligned}
```

Ketiga produk berbagi batas gudang yang sama. Nilai buka nol membuat seluruh arus gudang nol.

### R38. Batas waktu linear G4


```math
\begin{aligned}
\mathrm{R38}:\quad &z_{4,1,B}+z_{4,1,C}+z_{4,2,B}+z_{4,2,C}\\
&\quad+z_{4,3,A}+z_{4,3,C}+z_{4,4,A}+z_{4,4,C}\\
&\quad+z_{4,5,A}+z_{4,5,B}+z_{4,6,A}+z_{4,6,B}\le16{,}1y_{4}
\end{aligned}
```

Ketiga produk berbagi batas gudang yang sama. Nilai buka nol membuat seluruh arus gudang nol.

Pada profil nonlinear, R35–R38 menambahkan 0,025 kali jumlah kuadrat tonase setiap produk. Tonase masing-masing produk adalah jumlah kiriman yang sudah tercantum pada baris waktu, sehingga identitas variabel yang diukur WCC tetap. Fungsi biaya menambahkan kuadrat dengan koefisien 0,04.

[Penghitungan WCC](../Lampiran_WCC.md) · [Model matematika](Model_Matematika.md)
