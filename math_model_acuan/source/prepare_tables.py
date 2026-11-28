from pathlib import Path
import csv,json
from itertools import product
ROOT=Path(__file__).parent
d=json.loads((ROOT/'data.json').read_text());out=ROOT/'data_tabel';out.mkdir(exist_ok=True)
def write(name,header,rows):
 with (out/name).open('w',newline='') as f:
  w=csv.writer(f);w.writerow(header);w.writerows(rows)
write('Gudang.csv',['Gudang','Kapasitas_ton','Waktu_jam','Biaya_buka','Emisi_buka_kg_CO2e','Penanganan_A','Penanganan_B','Penanganan_C'],[[f'G{g}',d['kapasitas_gudang'][g-1],d['kontrol_profil']['waktu_gudang'][g-1],d['biaya_buka_gudang'][g-1],d['P3']['emisi_tetap_gudang'][g-1],*d['tarif_penanganan_per_ton'][g-1]] for g in range(1,5)])
write('Permintaan_Dasar.csv',['Zona','A_ton','B_ton','C_ton'],[[f'K{j}',*[d['level']['L']['permintaan_dasar'][f'{j},{p}'] for p in 'ABC']] for j in range(1,7)])
for key,name,index,nrows,ncols,prefix in [('tarif_masuk_per_ton','Tarif_Masuk.csv','Pabrik',6,4,'G'),('tarif_keluar_per_ton','Tarif_Keluar.csv','Gudang',4,6,'K')]:write(name,[index,*[f'{prefix}{k}' for k in range(1,ncols+1)]],[[f'{"P" if index=="Pabrik" else "G"}{i}',*d[key][i-1]] for i in range(1,nrows+1)])
for key,name,index,nrows,ncols,prefix in [('emisi_masuk_per_ton','Emisi_Masuk.csv','Pabrik',6,4,'G'),('emisi_keluar_per_ton','Emisi_Keluar.csv','Gudang',4,6,'K')]:write(name,[index,*[f'{prefix}{k}' for k in range(1,ncols+1)]],[[f'{"P" if index=="Pabrik" else "G"}{i}',*d['P3'][key][i-1]] for i in range(1,nrows+1)])
write('Distribusi_Produk.csv',['Produk','Kondisi','Pengali','Peluang'],[[p,lab,*v] for p in 'ABC' for lab,v in zip(['Sepi','Sedang','Ramai'],d['P2']['distribusi_produk'][p])])
write('Skenario.csv',['Skenario','Pengali_A','Pengali_B','Pengali_C','Peluang'],[[i,*[s['pengali'][p] for p in 'ABC'],s['peluang']] for i,s in enumerate(d['P2']['skenario'],1)])
write('Rute_Masuk.csv',['Tingkat','Pabrik','Gudang','Produk'],[[l,f'P{i}',f'G{g}',p] for l in 'LMH' for i,g,p in d['level'][l]['jalur_masuk']])
write('Rute_Keluar.csv',['Tingkat','Gudang','Zona','Produk'],[[l,f'G{g}',f'K{j}',p] for l in 'LMH' for g,j,p in d['level'][l]['jalur_keluar']])
write('Kompatibilitas_Pabrik.csv',['Pabrik','Produk'],[[f'P{i}',','.join(v)] for i,v in d['produk_pabrik'].items()])
print('Readable input tables',len(list(out.glob('*.csv'))))
