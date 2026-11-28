"""Expand every canonical Low equation directly from the route data."""
from pathlib import Path
import json,itertools
ROOT=Path(__file__).parent

def variable(name,t):return name+'_{'+','.join(map(str,t))+'}'
def summation(terms,chunk=4):
 if not terms:return '0'
 return '+'.join(terms[:chunk])+''.join('\\\\\n&\\quad+'+'+'.join(terms[i:i+chunk]) for i in range(chunk,len(terms),chunk))
def block(label,lhs,rhs,relation='='):
 return '\n```math\n\\begin{aligned}\n'+label+':\\quad &' +lhs+relation+rhs+'\n\\end{aligned}\n```\n\n'
def main():
 d=json.loads((ROOT/'data.json').read_text());a=d['level']['L'];rin=sorted(map(tuple,a['jalur_masuk']));rout=sorted(map(tuple,a['jalur_keluar']));s='# Persamaan operasi Low, R1–R38\n\nSeluruh baris pada halaman ini berasal dari daftar rute Low. Indeks $i,g,j,p$ berturut-turut menunjukkan pabrik, gudang, zona, dan produk. $x_{igp}$ adalah ton kiriman masuk; $z_{gjp}$ adalah ton kiriman keluar; $y_g$ memilih gudang yang dibuka. Permintaan pasti menggunakan tabel dasar. Untuk satu skenario stokastik, tambahkan indeks skenario pada setiap kiriman dan gunakan pesanan skenario tersebut.\n\n'
 n=0
 for g,p in itertools.product(range(1,5),'ABC'):
  n+=1;xs=[variable('x',t) for t in rin if t[1:]==(g,p)];zs=[variable('z',t) for t in rout if (t[0],t[2])==(g,p)];s+=f'### R{n}. Neraca produk {p} di G{g}\n\n';s+=block(f'\\mathrm{{R{n}}}',summation(xs),summation(zs));s+='Jumlah yang diterima untuk produk dan gudang ini harus sama dengan jumlah yang dikirim keluar.\n\n'
 for j,p in itertools.product(range(1,7),'ABC'):
  n+=1;zs=[variable('z',t) for t in rout if t[1:]==(j,p)];rhs=str(a['permintaan_dasar'][f'{j},{p}']).replace('.','{,}');s+=f'### R{n}. Pesanan produk {p} di K{j}\n\n';s+=block(f'\\mathrm{{R{n}}}',summation(zs),rhs);s+='Semua kiriman produk ini menuju zona yang sama dijumlahkan untuk memenuhi pesanannya.\n\n'
 for family,key in [('kapasitas tonase','kapasitas_gudang'),('waktu linear',None)]:
  for g in range(1,5):
   n+=1;zs=[variable('z',t) for t in rout if t[0]==g];value=d[key][g-1] if key else d['kontrol_profil']['waktu_gudang'][g-1];rhs=str(value).replace('.','{,}')+variable('y',(g,));s+=f'### R{n}. Batas {family} G{g}\n\n';s+=block(f'\\mathrm{{R{n}}}',summation(zs),rhs,'\\le');s+='Ketiga produk berbagi batas gudang yang sama. Nilai buka nol membuat seluruh arus gudang nol.\n\n'
 assert n==38
 s+='Pada profil nonlinear, R35–R38 menambahkan 0,025 kali jumlah kuadrat tonase setiap produk. Tonase masing-masing produk adalah jumlah kiriman yang sudah tercantum pada baris waktu, sehingga identitas variabel yang diukur WCC tetap. Fungsi biaya menambahkan kuadrat dengan koefisien 0,04.\n\n[Penghitungan WCC](../Lampiran_WCC.md) · [Model matematika](Model_Matematika.md)\n';(ROOT/'Persamaan_WCC.md').write_text(s)
if __name__=='__main__':main()
