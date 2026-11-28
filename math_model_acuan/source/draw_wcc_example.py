"""Draw exact row-intersection weights for four rows of the Low model."""
from pathlib import Path
import csv,itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
rows={}
with (ROOT/'hasil/audit/WCC_Baris.csv').open() as f:
 for r in csv.DictReader(f):
  rows[r['Tingkat'],r['Baris']]=set(r['Variabel'].split('; ')) if r['Variabel'] else set()
labels=['R6','R27','R32','R36'];pos={'R6':(0,1),'R27':(1,1),'R32':(0,0),'R36':(1,0)}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig,axes=plt.subplots(1,2,figsize=(10.5,4.6),layout='constrained')
for ax,level,title,color,style in zip(axes,['L','REF'],['Low · bobot 14 pada 6 pasangan','Daftar pembanding · bobot 34'],['#263445','#bc344b'],['-','--']):
 for a,b in itertools.combinations(labels,2):
  w=len(rows[level,a]&rows[level,b]);x1,y1=pos[a];x2,y2=pos[b];ax.plot([x1,x2],[y1,y2],color=color,lw=1.8,ls=style,zorder=1)
  fraction=.34 if (a,b)==('R6','R36') else .35 if (a,b)==('R27','R32') else .5
  x=x1+fraction*(x2-x1);y=y1+fraction*(y2-y1)
  ax.text(x,y,str(w),ha='center',va='center',fontweight='bold',color=color,bbox=dict(facecolor='white',edgecolor='none',pad=3),zorder=5)
 for label,(x,y) in pos.items():
  ax.scatter([x],[y],s=1900,color='#f4f7fa',edgecolor='#263445',lw=1.4,zorder=3);ax.text(x,y,label,ha='center',va='center',fontweight='bold',zorder=4)
 ax.set_xlim(-.2,1.2);ax.set_ylim(-.2,1.2);ax.set_aspect('equal');ax.axis('off');ax.set_title(title,fontweight='bold')
fig.suptitle('Empat baris yang sama · angka pada garis = variabel bersama',fontweight='bold')
fig.supxlabel('R6: neraca susu G2    R27: pesanan susu K5    R32: kapasitas G2    R36: waktu G2',fontsize=10)
out=ROOT/'diagram';out.mkdir(exist_ok=True)
for ext in ['svg','png']:fig.savefig(out/f'WCC_Empat_Baris.{ext}',dpi=200,bbox_inches='tight')
plt.close(fig)
