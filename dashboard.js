function mapValue(v){ if(!v||v==='NULL'||v==='-'||v==='(tidak diisi)'||v==='(coretan)')return 0; const t=v.toLowerCase(); if(t.includes('sekali'))return 5; if(t.includes('tidak'))return -1; if(t.includes('enak')||t.includes('baik')||t.includes('nyaman')||t.includes('bersih'))return 4; if(t.includes('biasa'))return 3; return 0; }

function process(){
  const summary=[]; const rowsAll=[];
  Object.entries(csvData).forEach(([gerai,data])=>{
     let total=0,count=0; let sumM=0,sumP=0,sumK=0,sumB=0;
     for(let i=1;i<data.length;i++){
        const r=data[i]; if(r.length<7)continue;
        const m=mapValue(r[3]); const p=mapValue(r[4]); const k=mapValue(r[5]); const b=mapValue(r[6]);
        sumM+=m; sumP+=p; sumK+=k; sumB+=b;
        const avg=(m+p+k+b)/4; total+=avg; count++;
        rowsAll.push({gerai,nama:r[0]||'(anonim)',alamat:r[2]||'-',makanan:r[3]||'-',pelayanan:r[4]||'-',kenyamanan:r[5]||'-',kebersihan:r[6]||'-',avg:avg.toFixed(2),komentar:r[7]||''});
     }
     summary.push({gerai,count,avg:count?total/count:0,makanan:count?sumM/count:0,pelayanan:count?sumP/count:0,kenyamanan:count?sumK/count:0,kebersihan:count?sumB/count:0});
  });
  summary.sort((a,b)=>b.avg-a.avg);
  return {summary,rowsAll};
}

function renderCards(data){const cont=document.getElementById('card-container');const totalRev=data.summary.reduce((s,g)=>s+g.count,0);const best=data.summary[0];const second=data.summary[1]||{};const third=data.summary[2]||{};
  cont.innerHTML=`
    <div class="card"><h3>Total Review</h3><div class="big">${totalRev}</div></div>
    <div class="card"><h3>🏆 Gerai #1</h3><div class="big">👑 ${best.gerai}</div><div class="tag">Skor ${best.avg.toFixed(2)}</div></div>
    ${second.gerai?`<div class="card"><h3>Peringkat #2</h3><div class="big">${second.gerai}</div><div class="tag">Skor ${second.avg.toFixed(2)}</div></div>`:''}
    ${third.gerai?`<div class="card"><h3>Peringkat #3</h3><div class="big">${third.gerai}</div><div class="tag">Skor ${third.avg.toFixed(2)}</div></div>`:''}
  `;}

function charts(data){
  const labels=data.summary.map(g=>g.gerai);
  const ctx1=document.getElementById('avgChart').getContext('2d');
  new Chart(ctx1,{type:'bar',data:{labels,datasets:[
      {label:'Makanan',data:data.summary.map(g=>g.makanan.toFixed(2)),backgroundColor:'#6366f1'},
      {label:'Pelayanan',data:data.summary.map(g=>g.pelayanan.toFixed(2)),backgroundColor:'#34d399'},
      {label:'Kenyamanan',data:data.summary.map(g=>g.kenyamanan.toFixed(2)),backgroundColor:'#fbbf24'},
      {label:'Kebersihan',data:data.summary.map(g=>g.kebersihan.toFixed(2)),backgroundColor:'#f87171'}]},
      options:{responsive:true,scales:{y:{beginAtZero:true,max:5}}}});
  const ctx2=document.getElementById('countChart').getContext('2d');
  new Chart(ctx2,{type:'pie',data:{labels,datasets:[{data:data.summary.map(g=>g.count),backgroundColor:['#6366f1','#60a5fa','#34d399','#fbbf24','#f87171','#a78bfa']}]},options:{plugins:{legend:{position:'bottom'}}}});
}

function table(rows){
  try {
    const tbody=document.querySelector('#tblReviews tbody');
    if(!tbody) { console.error('Table body not found'); return; }
    tbody.innerHTML=rows.map(r=>{
    let phoneNumber='';
    Object.entries(csvData).forEach(([gerai,data])=>{
      if(gerai===r.gerai){
        for(let i=1;i<data.length;i++){
          if(data[i][0]===r.nama){ phoneNumber=data[i][1]||''; break; }
        }
      }
    });
    const tooltipText=phoneNumber?`📞 ${phoneNumber}`:'📞 Tidak ada nomor';
    return `<tr>
      <td>${r.gerai}</td>
      <td>
        <span class="customer-name">
          ${r.nama}
          <span class="tooltip">${tooltipText}</span>
        </span>
      </td>
      <td>${r.alamat}</td>
      <td>${r.makanan}</td>
      <td>${r.pelayanan}</td>
      <td>${r.kenyamanan}</td>
      <td>${r.kebersihan}</td>
      <td style="text-align:center;font-weight:600">${r.avg}</td>
      <td>${r.komentar}</td>
    </tr>`;}).join('');

  const mobileContainer=document.getElementById('mobileComments');
  if(!mobileContainer){ console.error('Mobile container not found'); return; }
  mobileContainer.innerHTML=rows.map(r=>{
    let phoneNumber='';
    Object.entries(csvData).forEach(([gerai,data])=>{
      if(gerai===r.gerai){
        for(let i=1;i<data.length;i++){
          if(data[i][0]===r.nama){ phoneNumber=data[i][1]||''; break; }
        }
      }
    });
    const tooltipText=phoneNumber?`📞 ${phoneNumber}`:'📞 Tidak ada nomor';
    return `
      <div class="mobile-comment-card">
        <div class="mobile-comment-header">
          <div>
            <div class="mobile-comment-name">
              <span class="customer-name">
                ${r.nama}
                <span class="tooltip">${tooltipText}</span>
              </span>
            </div>
            <div class="mobile-comment-gerai">${r.gerai}</div>
          </div>
          <div class="mobile-comment-score">${r.avg}</div>
        </div>
        <div class="mobile-comment-ratings">
          <div class="mobile-rating-item"><span class="mobile-rating-label">Makanan</span><span>${r.makanan}</span></div>
          <div class="mobile-rating-item"><span class="mobile-rating-label">Pelayanan</span><span>${r.pelayanan}</span></div>
          <div class="mobile-rating-item"><span class="mobile-rating-label">Kenyamanan</span><span>${r.kenyamanan}</span></div>
          <div class="mobile-rating-item"><span class="mobile-rating-label">Kebersihan</span><span>${r.kebersihan}</span></div>
        </div>
        ${r.komentar?`<div class="mobile-comment-text">${r.komentar}</div>`:''}
        <div class="mobile-comment-address">📍 ${r.alamat}</div>
      </div>`;}).join('');
  } catch(error) { console.error('Error in table function:', error); }
}

function applyFilters(rows){
  const geraiVal=document.getElementById('filterGerai').value;
  const cat=document.getElementById('selCategory').value;
  const q=document.getElementById('txtSearch').value.toLowerCase();
  return rows.filter(r=>{
      if(geraiVal!=='all' && r.gerai!==geraiVal) return false;
      const avg=parseFloat(r.avg);
      if(cat==='positive' && avg<4) return false;
      if(cat==='critical' && avg>2.5) return false;
      if(q && !(r.nama.toLowerCase().includes(q) || r.alamat.toLowerCase().includes(q) || r.komentar.toLowerCase().includes(q))) return false;
      return true;
  });
}

window.addEventListener('DOMContentLoaded',()=>{
  const data=process();
  const sel=document.getElementById('filterGerai');
  data.summary.forEach(g=>{ const opt=document.createElement('option'); opt.value=g.gerai; opt.textContent=g.gerai; sel.appendChild(opt); });
  renderCards(data); charts(data);
  let currentRows=data.rowsAll;
  const refresh=()=>{ table(applyFilters(currentRows)); };
  refresh();
  ['filterGerai','selCategory','txtSearch'].forEach(id=>document.getElementById(id).addEventListener('input',refresh));
  console.log('Data loaded:', data.rowsAll.length, 'rows');
  document.getElementById('dataset-link').href=DATASET_URL;
  let clickCount=0; let clickTimer=null;
  document.getElementById('logo-container').addEventListener('click', function(){
    clickCount++; clearTimeout(clickTimer); clickTimer=setTimeout(()=>{clickCount=0;},3000); if(clickCount>=7){ showEasterEgg(); clickCount=0; }
  });
});

function showEasterEgg(){ document.getElementById('easter-egg').classList.add('show'); }
function closeEasterEgg(){ document.getElementById('easter-egg').classList.remove('show'); }

