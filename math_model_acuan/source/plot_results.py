"""Publication figures from measured results and the frozen route lists."""
from pathlib import Path
import json,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
ROOT=Path(__file__).parent
COLORS={'L':'#117653','M':'#ba3a4c','H':'#252c35'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','savefig.facecolor':'white','axes.titlesize':12})

def network_figure(data,out):
    fig,axes=plt.subplots(3,1,figsize=(13,14),constrained_layout=True)
    for ax,p,title in zip(axes,'ABC',['A · Minyak goreng curah','B · Sirup gula cair','C · Susu cair dingin']):
        positions={**{('P',i):(0,5-(i-1)) for i in range(1,7)},**{('G',g):(1.3,4.5-(g-1)*1.33) for g in range(1,5)},**{('K',j):(2.6,5-(j-1)) for j in range(1,7)}}
        previous_in=set();previous_out=set()
        for level,style,width in [('L','-',1.9),('M','--',1.5),('H',':',1.3)]:
            spec=data['level'][level];rin={tuple(t) for t in spec['jalur_masuk'] if t[2]==p};rout={tuple(t) for t in spec['jalur_keluar'] if t[2]==p}
            for stage,routes,prev in [('in',rin,previous_in),('out',rout,previous_out)]:
                for a,b,_ in sorted(routes-prev):
                    src,dst=(('P',a),('G',b)) if stage=='in' else (('G',a),('K',b))
                    arrow=FancyArrowPatch(positions[src],positions[dst],arrowstyle='-|>',mutation_scale=11,shrinkA=21,shrinkB=21,color=COLORS[level],linestyle=style,linewidth=width,alpha=.83,zorder=1)
                    ax.add_patch(arrow)
            previous_in=rin;previous_out=rout
        for (kind,i),(x,y) in positions.items():
            ax.scatter([x],[y],s=1000,facecolor='#f6f8fa',edgecolor='#475569',linewidth=1.2,zorder=3)
            ax.text(x,y,f'{kind}{i}',ha='center',va='center',fontweight='bold',color='#172c40',zorder=4)
        for x,label in [(0,'PABRIK'),(1.3,'GUDANG'),(2.6,'ZONA PELANGGAN')]:ax.text(x,5.65,label,ha='center',fontsize=10,fontweight='bold',color='#475569')
        ax.set_title(title,loc='left',fontweight='bold',pad=22);ax.set_xlim(-.35,3);ax.set_ylim(-.5,5.9);ax.axis('off')
    legend=[Line2D([0],[0],color=COLORS[l],lw=2,ls=ls,label=label) for l,ls,label in [('L','-','Low: garis hijau'),('M','--','Medium: hijau + merah'),('H',':','High: hijau + merah + hitam')]]
    fig.legend(handles=legend,loc='lower center',ncol=3,bbox_to_anchor=(.5,-.015),frameon=False)
    for ext in ['png','svg']:fig.savefig(out/f'Jaringan_Low_Medium_High.{ext}',dpi=190,bbox_inches='tight')
    plt.close(fig)

def measured_figures(rows,records,out):
    fig,axes=plt.subplots(1,2,figsize=(13,4.6),layout='constrained')
    x=np.arange(1,9)
    for level in 'LMH':
        a=[next(r for r in rows if (r['profile'],r['level'])==(f'P{i}',level)) for i in x]
        y=np.array([r['solver_ms_median']/1000 for r in a]);lo=np.array([r['solver_ms_min']/1000 for r in a]);hi=np.array([r['solver_ms_max']/1000 for r in a])
        axes[0].errorbar(x,y,yerr=np.array([y-lo,hi-y]),color=COLORS[level],marker='o',markersize=4,capsize=3,lw=1.6,label={'L':'Low','M':'Medium','H':'High'}[level])
        axes[1].plot(x,[r['lp_iterations_median'] for r in a],color=COLORS[level],marker='o',markersize=4,lw=1.6,label={'L':'Low','M':'Medium','H':'High'}[level])
    axes[0].set_yscale('log');axes[0].set_ylabel('Detik · skala log');axes[0].set_title('Waktu SCIP: median dan rentang 3 ulangan')
    axes[1].set_yscale('symlog',linthresh=1);axes[1].set_ylabel('Iterasi LP · skala symlog (nol ditampilkan)');axes[1].set_title('Total iterasi LP yang dilaporkan SCIP');axes[1].legend(frameon=False,loc='upper left')
    for ax in axes:ax.set_xticks(x,[f'P{i}' for i in x]);ax.grid(axis='y',alpha=.17)
    fig.suptitle('Beban penyelesaian pada data acuan · SCIP 10.0.2 · satu thread',fontweight='bold')
    for ext in ['png','svg']:fig.savefig(out/f'Benchmark_SCIP.{ext}',dpi=220,bbox_inches='tight')
    plt.close(fig)
    fig,axes=plt.subplots(2,2,figsize=(10,8),layout='constrained')
    for ax,profile in zip(axes.flat,['P3','P4','P7','P8']):
        for level in 'LMH':
            r=next(r for r in records if (r['repeat'],r['profile'],r['level'])==(1,profile,level));pts=sorted(r['frontier'],key=lambda p:p['emission'])
            ax.scatter([p['emission'] for p in pts],[p['cost'] for p in pts],color=COLORS[level],s=22,label={'L':'Low','M':'Medium','H':'High'}[level])
        ax.set_title(profile,fontweight='bold');ax.set_xlabel('Emisi harapan (kg CO₂e)' if profile in ['P4','P8'] else 'Emisi (kg CO₂e)');ax.set_ylabel('Biaya harapan' if profile in ['P4','P8'] else 'Biaya');ax.grid(alpha=.15)
    axes[0,0].legend(frameon=False);fig.suptitle('Sampel Pareto dari 25 batas emisi per profil dan tingkat',fontweight='bold')
    for ext in ['png','svg']:fig.savefig(out/f'Pareto_SCIP.{ext}',dpi=220,bbox_inches='tight')
    plt.close(fig)

def main():
    out=ROOT/'diagram';out.mkdir(exist_ok=True);network_figure(json.loads((ROOT/'data.json').read_text()),out)
    if (ROOT/'summary.json').exists():measured_figures(json.loads((ROOT/'summary.json').read_text()),[json.loads(s) for s in (ROOT/'benchmark_runs.jsonl').read_text().splitlines()],out)
if __name__=='__main__':main()
