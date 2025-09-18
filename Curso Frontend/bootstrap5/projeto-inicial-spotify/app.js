// Interações dinâmicas do projeto
(function(){
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Reveal on scroll
  const revealEls = document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries)=>{
      entries.forEach(en=>{
        if(en.isIntersecting){
          en.target.classList.add('on');
          io.unobserve(en.target);
        }
      });
    },{threshold:0.15});
    revealEls.forEach(el=>io.observe(el));
  } else {
    revealEls.forEach(el=>el.classList.add('on'));
  }

  // Scroll progress bar
  const progress = document.getElementById('scroll-progress');
  function updateProgress(){
    const h = document.documentElement;
    const scrolled = (h.scrollTop)/(h.scrollHeight - h.clientHeight) * 100;
    if(progress) progress.style.width = scrolled + '%';
  }
  window.addEventListener('scroll', updateProgress, {passive:true});
  updateProgress();

  // Botão voltar ao topo
  const btnTopo = document.getElementById('btn-topo');
  function toggleBtnTopo(){
    if(!btnTopo) return;
    if(window.scrollY > 300){ btnTopo.classList.add('visivel'); } else { btnTopo.classList.remove('visivel'); }
  }
  window.addEventListener('scroll', toggleBtnTopo, {passive:true});
  if(btnTopo){
    btnTopo.addEventListener('click', ()=> window.scrollTo({top:0, behavior: prefersReduced ? 'auto':'smooth'}));
  }
  toggleBtnTopo();

  // Contador animado
  const contadorEl = document.getElementById('contador-musicas');
  function animateCount(el, end, dur=1600){
    const start = 0; const t0 = performance.now();
    function tick(t){
      const p = Math.min(1,(t-t0)/dur);
      const val = Math.floor(start + (end-start)*p);
      el.textContent = val.toLocaleString('pt-BR');
      if(p<1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  if(contadorEl){ animateCount(contadorEl, 50000000); }

  // Service Worker update toast
  let newWorker;
  const toast = document.getElementById('toast-update');
  const btnAtualizar = document.getElementById('btn-atualizar');
  if(navigator.serviceWorker){
    navigator.serviceWorker.addEventListener('controllerchange', ()=>{
      // reload autom. após ativação
      window.location.reload();
    });
    navigator.serviceWorker.getRegistration().then(reg=>{
      if(!reg) return;
      reg.addEventListener('updatefound', ()=>{
        newWorker = reg.installing;
        if(newWorker){
          newWorker.addEventListener('statechange', ()=>{
            if(newWorker.state === 'installed' && navigator.serviceWorker.controller){
              if(toast){ toast.classList.add('mostrar'); }
            }
          });
        }
      });
    });
  }
  if(btnAtualizar){
    btnAtualizar.addEventListener('click', ()=>{
      if(newWorker){ newWorker.postMessage({action:'skipWaiting'}); }
    });
  }

  // Scroll Spy
  const sections = document.querySelectorAll('section[id], footer#footer');
  const navLinks = Array.from(document.querySelectorAll('.navbar-nav .nav-link'));
  if('IntersectionObserver' in window) {
    const spy = new IntersectionObserver((entries)=>{
      entries.forEach(en=>{
        if(en.isIntersecting){
          const id = en.target.getAttribute('id');
          navLinks.forEach(a=> a.classList.toggle('active', a.getAttribute('href') === '#'+id));
        }
      });
    },{threshold:0.5});
    sections.forEach(s=>spy.observe(s));
  } else {
    window.addEventListener('scroll', ()=>{
      const y = window.scrollY + window.innerHeight/2;
      let current;
      sections.forEach(s=>{ if(s.offsetTop <= y) current = s.id; });
      if(current){ navLinks.forEach(a=> a.classList.toggle('active', a.getAttribute('href') === '#'+current)); }
    }, {passive:true});
  }
})();
