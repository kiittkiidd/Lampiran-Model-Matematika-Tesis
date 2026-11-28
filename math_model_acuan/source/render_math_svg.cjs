// Rebuild formula figures: npm install --no-save mathjax-full@3.2.2
// Then: node math_model_acuan/source/render_math_svg.cjs
const fs=require('fs'),path=require('path');
const {mathjax}=require('mathjax-full/js/mathjax.js');
const {TeX}=require('mathjax-full/js/input/tex.js');
const {SVG}=require('mathjax-full/js/output/svg.js');
const {liteAdaptor}=require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler}=require('mathjax-full/js/handlers/html.js');
const {AllPackages}=require('mathjax-full/js/input/tex/AllPackages.js');
const root=path.resolve(__dirname,'../..');
const formulas=JSON.parse(fs.readFileSync(path.join(__dirname,'persamaan_sumber.json'),'utf8')).formulas;
const adaptor=liteAdaptor();RegisterHTMLHandler(adaptor);
const doc=mathjax.document('',{InputJax:new TeX({packages:AllPackages}),OutputJax:new SVG({fontCache:'local'})});
const escape=s=>s.replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
for(const r of formulas){
 const node=doc.convert(r.rendered_latex,{display:r.display,em:r.display?18:16,ex:r.display?9:8,containerWidth:860});
 const html=adaptor.outerHTML(node);
 if(/data-mml-node="merror"|Math Processing Error/.test(html))throw Error('Invalid equation '+r.id);
 let svg=html.match(/<svg[\s\S]*<\/svg>/)[0];
 const vb=svg.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number),pad=r.display?180:60,em=r.display?18:16;
 const view=[vb[0]-pad,vb[1]-pad,vb[2]+2*pad,vb[3]+2*pad];
 const width=Math.ceil(view[2]*em/1000),height=Math.ceil(view[3]*em/1000);
 if(width!==r.width||height!==r.height)throw Error('Dimension mismatch '+r.id);
 svg=svg.replace(/<svg\b[^>]*>/,`<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${width}" height="${height}" viewBox="${view.join(' ')}" role="img" aria-labelledby="formula-title" style="color:#172b4d">\n<title id="formula-title">${escape(r.rendered_latex)}</title>\n<rect x="${view[0]}" y="${view[1]}" width="${view[2]}" height="${view[3]}" fill="white"/>`);
 fs.mkdirSync(path.dirname(path.join(root,r.file)),{recursive:true});fs.writeFileSync(path.join(root,r.file),svg+'\n');
}
console.log('Generated '+formulas.length+' standalone SVG formula figures.');
