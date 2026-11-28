"""Write the final benchmark CSVs, report, and two figures from the raw JSONL."""
from argparse import ArgumentParser
from collections import defaultdict
import csv
from itertools import product
import json
from pathlib import Path
from statistics import median

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from inti_solver import PROFILES
from solver import PAKET_FINAL

LEVELS = dict(L='Low', M='Medium', H='High')
COLORS = dict(L='#17714E', M='#AF3344', H='#22262C')

def number(value, decimal=0):
    return f'{value:,.{decimal}f}'.translate(str.maketrans({',':'.','.':','}))

def write_csv(path, headers, records):
    with path.open('w',encoding='utf-8',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(headers)
        writer.writerows(records)

def figures(out, data, summary):
    plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','axes.spines.top':False,
                         'axes.spines.right':False,'axes.titleweight':'bold','axes.labelcolor':'#273849',
                         'xtick.color':'#273849','ytick.color':'#273849'})
    fig,axes=plt.subplots(1,2,figsize=(10,3.6),layout='constrained')
    fig.suptitle('Beban penyelesaian menurut profil dan rute',x=.03,ha='left',weight='bold',color='#192c3c')
    for ax,measure,title,ylabel in zip(axes,('median_ms','lp'),('Waktu total','Iterasi LP'),('Detik · skala log','Iterasi · skala log')):
        for l in LEVELS:
            ax.plot(list(PROFILES),[summary[p,l][measure]/(1000 if measure=='median_ms' else 1) for p in PROFILES],
                    label=LEVELS[l],color=COLORS[l],marker='o',markersize=4,linewidth=1.5)
        ax.set(title=title,ylabel=ylabel,yscale='log')
        ax.grid(axis='y',alpha=.18)
    axes[1].legend(frameon=False,loc='upper left',ncol=1)
    fig.savefig(out/'Beban_Solver.svg',metadata={'Date':None})
    plt.close(fig)

    fig,axes=plt.subplots(2,2,figsize=(10,6.8),layout='constrained')
    fig.suptitle('Sampel Pareto biaya dan emisi · paket 10101',x=.03,ha='left',weight='bold',color='#192c3c')
    for ax,p in zip(axes.flat,('P3','P4','P7','P8')):
        for l in LEVELS:
            points=data[p,l,10101]['frontier']
            ax.scatter([t['emission'] for t in points],[t['cost'] for t in points],
                       label=LEVELS[l],color=COLORS[l],alpha=.8,s=22,edgecolors='white',linewidths=.35)
        stoch,_,_=PROFILES[p]
        ax.set(title=p,xlabel='Emisi harapan (kg CO₂e)' if stoch else 'Emisi (kg CO₂e)',
               ylabel='Biaya harapan' if stoch else 'Biaya')
        ax.grid(alpha=.15)
    axes[0,0].legend(frameon=False,fontsize=9)
    fig.savefig(out/'Pareto_Contoh.svg',metadata={'Date':None})
    plt.close(fig)

def main():
    ap=ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,nargs='+',required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    rows=[json.loads(line) for path in args.input for line in path.read_text().splitlines() if line.strip()]
    data={(r['profile'],r['level'],r['seed']):r for r in rows}
    assert len(rows)==len(data)==480 and data.keys()==set(product(PROFILES,LEVELS,PAKET_FINAL))
    versions={row['solver'] for row in rows}
    assert len(versions)==1
    repeats={len(row['times']) for row in rows}
    assert len(repeats)==1 and repeats<={3,6}
    repeats=repeats.pop()
    for r in rows:
        multi=PROFILES[r['profile']][1]
        assert len(r['points'])==(25 if multi else 1)
        assert abs(median(r['times'])-r['median_ms'])<1e-8
        assert all(p['emission']<=p.get('epsilon',float('inf'))+2e-7 for p in r['points'])
        assert all(-2e-7<=p['gap']<=(.00025 if PROFILES[r['profile']][2] else 1e-7) for p in r['points'])
    out=args.output
    out.mkdir(parents=True,exist_ok=True)
    measures=('median_ms','lp','calls','nodes')
    groups=defaultdict(list)
    for p,l,s in product(PROFILES,LEVELS,PAKET_FINAL):groups[p,l].append(data[p,l,s])
    summary={(p,l):{**{key:median(r[key] for r in g) for key in measures},
               'points':median(len(r['frontier']) for r in g)} for (p,l),g in groups.items()}
    strict={(p,key):sum(data[p,'L',s][key]<data[p,'M',s][key]<data[p,'H',s][key] for s in PAKET_FINAL)
               for p in PROFILES for key in ('median_ms','lp')}
    write_csv(out/'Ringkasan.csv',['Profil','Tingkat','Paket','Median waktu (ms)','Median iterasi LP',
              'Median panggilan','Median simpul','Median titik berbeda','Paket urut waktu L<M<H','Paket urut LP L<M<H'],
              [(p,LEVELS[l],len(PAKET_FINAL),*(v[k] for k in measures),v['points'],strict[p,'median_ms'],strict[p,'lp'])
               for (p,l),v in summary.items()])
    ordered=[data[p,l,s] for p,l,s in product(PROFILES,LEVELS,PAKET_FINAL)]
    write_csv(out/'Pengukuran.csv',['Profil','Tingkat','Paket','HiGHS','Iterasi LP','Panggilan','Simpul',
              'Panggilan ulang','Titik berbeda','Median waktu (ms)',*(f'Ulangan {i} (ms)' for i in range(1,repeats+1))],
            [(r['profile'],LEVELS[r['level']],r['seed'],r['solver'],r['lp'],r['calls'],r['nodes'],
              r['retries'],len(r['frontier']),f"{r['median_ms']:.5f}",*(f'{x:.5f}' for x in r['times'])) for r in ordered])
    write_csv(out/'Titik_Tujuan.csv',['Profil','Tingkat','Paket','Nomor batas','Batas emisi','Biaya','Emisi',
              'Gudang dibuka','Celah tujuan','Titik ditampilkan'],
              [(r['profile'],r['level'],r['seed'],i+1 if 'epsilon' in q else '',
              f"{q['epsilon']:.7f}" if 'epsilon' in q else '',f"{q['cost']:.7f}",f"{q['emission']:.7f}",
              ' '.join(f'G{g}' for g in q['warehouses']),f"{q['gap']:.8g}",int(q in r['frontier']))
              for r in ordered for i,q in enumerate(r['points'])])
    figures(out,data,summary)
    text=['# Hasil validasi jaringan PT XYZ','',
      'Pengujian mencakup **480 kombinasi** dari 20 paket data, delapan profil, dan tiga tingkat rute. '
      'Satu paket memvariasikan biaya buka, tarif angkut, dan pembagian pesanan antar zona. '
      'Total permintaan dasar setiap produk tetap. '
      'Dalam tiap paket, permintaan, kapasitas, dan tarif yang sama dipakai pada Low, Medium, dan High. '
      f'Kolom waktu mengambil median dari {repeats} ulangan untuk tiap paket, lalu median dari 20 paket. '
      'Kolom iterasi LP mengambil median dari 20 penghitungan terpisah.', '',
      '| Profil | Waktu Low → Medium → High (detik) | Iterasi LP Low → Medium → High | Paket urut waktu | Paket urut iterasi |',
      '| --- | ---: | ---: | ---: | ---: |']
    for p in PROFILES:
        tm=' → '.join(number(summary[p,l]['median_ms']/1000,3) for l in LEVELS)
        lp=' → '.join(number(summary[p,l]['lp'],1 if summary[p,l]['lp']%1 else 0) for l in LEVELS)
        text.append(f'| {p} | {tm} | {lp} | {strict[p,"median_ms"]}/20 | {strict[p,"lp"]}/20 |')
    for metric,title in [('median_ms','waktu'),('lp','iterasi LP')]:
        passes=sum(summary[p,'L'][metric]<summary[p,'M'][metric]<summary[p,'H'][metric] for p in PROFILES)
        strict_total=sum(strict[p,metric] for p in PROFILES)
        text+=['',f'Median {title} naik secara ketat pada **{passes}/8 profil**. Pada tingkat paket individual, urutan itu terjadi pada **{strict_total}/160 perbandingan**.']
    text+=['','Satu perbandingan memeriksa tiga tingkat dalam satu paket dan satu profil. '
      'Hasil ini menunjukkan pola pada jaringan dan paket yang diuji. Setiap tingkat menambah pilihan rute sekaligus menaikkan WCC. '
      'Waktu dan iterasi LP juga mencerminkan jumlah skenario dan prosedur Pareto yang dikerjakan oleh tiap profil.',
      '', '![Perbandingan waktu dan iterasi LP pada ketiga tingkat](hasil/Beban_Solver.svg)','',
      '## Sampel Pareto','',
      'P3, P4, P7, dan P8 memakai 25 batas ε per kombinasi. '
      'Batas tersebut berjarak sama di antara dua ujung rentang emisi untuk kombinasi yang sedang diselesaikan. '
      'Grafik menampilkan satu paket contoh (10101). '
      'Setiap titik mewakili satu pasangan biaya dan emisi yang lolos pemeriksaan. '
      'Batas ε yang memberikan titik sama tetap tercatat di CSV.', '',
      '![Sampel Pareto pada empat profil multiobjektif](hasil/Pareto_Contoh.svg)','',
      'Sebagai contoh terpisah, gunakan data dasar High dengan permintaan pasti dan penanganan linear. '
      'Solusi biaya terendah membuka G2 dan G4 dengan biaya 242,95 dan emisi 155,60 kg CO₂e. '
      'Salah satu solusi yang lebih mengutamakan emisi membuka G2 dan G3 dengan biaya 259,00 dan emisi 96,00 kg CO₂e.', '',
      '## Nilai alternatif fasilitas dan rute','',
      '- Pada setiap tingkat, penutupan satu fasilitas dari 10 fasilitas diuji satu per satu. '
      'P1 tetap dapat memenuhi pesanan, dan P6 tetap dapat memenuhi pesanan di ketiga skenario.',
      '- Pada P1, setiap pesanan zona–produk bisa dipenuhi sepenuhnya dari minimal dua pilihan gudang pada Low dan Medium serta tiga pada High. '
      'Setiap pilihan diuji bergantian sambil tetap memenuhi semua pesanan lain.',
      '- Untuk setiap kombinasi rute dan tingkat, CSV mencatat dua kondisi uji. Pada kondisi pertama, menutup rute menaikkan nilai tujuan '
      'atau membuat pesanan mustahil dipenuhi. Pada kondisi kedua, mewajibkan sedikitnya satu ton pada rute itu menaikkan nilai tujuan. '
      'Totalnya **208 kombinasi rute dan tingkat**.', '',
      'Audit rute membandingkan biaya minimum atau skor gabungan berbobot. Skor gabungan menjumlahkan biaya dibagi 300 dan emisi dibagi 150 '
      'setelah masing-masing dikalikan bobotnya. Kedua pembagi adalah skala tetap pada uji rute. '
      'Pada benchmark Pareto, P3, P4, P7, dan P8 memakai batas ε seperti pada model matematika.', '',
      '## Cara pengukuran dan menjalankan ulang','',
      f'Pengujian memakai Linux, Python 3.12, SciPy 1.17.0, dan HiGHS {next(iter(versions))} dengan satu thread per penyelesaian. '
      f'Setiap kombinasi mempunyai {repeats} ulangan waktu setelah satu pemanasan. '
      'Urutan tingkat diseimbangkan antarulangan di setiap paket, dan data serta model operasi disiapkan sebelum pencatatan waktu. '
      'Waktu mencakup seluruh penyelesaian, pemilihan solusi jika biaya sama, dan pemeriksaan solusi. '
      'Iterasi LP dihitung dari laporan solver pada lintasan terpisah, termasuk panggilan tambahan jika solusi perlu diperiksa ulang.', '',
      'Profil satu tujuan menyelesaikan biaya minimum. Profil dua tujuan mencakup penentuan dua ujung dan seluruh 25 batas ε. '
      'P5 sampai P8 memeriksa bentuk kuadrat asli dengan toleransi kelayakan 0,0000002 dan celah tujuan absolut maksimum 0,00025. '
      f'Tercatat **{sum(r["retries"] for r in rows)} panggilan ulang numerik** pada seluruh benchmark.', '',
      '[Jalankan di Google Colab](https://colab.research.google.com/github/kiittkiidd/Lampiran-Model-Matematika-Tesis/blob/main/math_model_acuan/Verifikasi_P1_P8.ipynb) · [Notebook di repo](Verifikasi_P1_P8.ipynb)', '',
      'Contoh lokal untuk Python 3.12 di Linux, dari direktori utama repo.', '',
      '~~~bash','python -m pip install -r requirements.txt',
      'OPENBLAS_NUM_THREADS=1 python math_model_acuan/benchmark.py --paket 10101 --profil P3 --output contoh.jsonl','~~~','',
      'Untuk benchmark lengkap, hilangkan opsi paket dan profil. Gunakan path keluaran baru untuk pengujian baru. '
      'Waktu absolut bergantung pada lingkungan. Paket final memakai kode 10101–10110 dan 10301–10310. '
      'Paket tersebut dipisahkan dari paket yang dipakai untuk memilih rancangan rute.', '',
      'Untuk membuat ulang tabel dan gambar dari benchmark lengkap, jalankan perintah berikut.', '',
      '~~~bash','python math_model_acuan/ringkas.py --input benchmark_lengkap.jsonl --output cek/hasil','~~~','',
      '## Data pemeriksaan','',
      '[Median dan urutan per profil](hasil/Ringkasan.csv) · [Pengukuran per paket](hasil/Pengukuran.csv) · '
      '[Biaya dan emisi pada setiap batas](hasil/Titik_Tujuan.csv) · [Audit WCC](hasil/WCC.csv) · '
      '[Audit per fasilitas dan zona](hasil/Audit_Fasilitas_Dan_Zona.json) · [Audit per rute](hasil/Audit_Per_Rute.csv)','',
      '[Model matematika](Model_Matematika.md) · [Halaman utama](../README.md)']
    (out.parent/'Hasil_Verifikasi.md').write_text('\n'.join(text)+'\n',encoding='utf-8')
    print('kombinasi',len(rows),'batas Pareto',sum(len(r['points']) for r in rows if PROFILES[r['profile']][1]),
          'ulang numerik',sum(r['retries'] for r in rows))
    print('\n'.join(text[:21]))

if __name__=='__main__':
    main()
