(function(){
  requestAnimationFrame(()=>document.documentElement.classList.add('loaded'));

  /* nav */
  const nav=document.getElementById('nav'), burger=document.getElementById('burger');
  burger.addEventListener('click',()=>{const o=nav.classList.toggle('open');burger.setAttribute('aria-expanded',o);burger.setAttribute('aria-label',o?'Close menu':'Open menu')});
  nav.querySelectorAll('.links a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');burger.setAttribute('aria-expanded','false')}));
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');burger.setAttribute('aria-expanded','false');burger.focus()}});
  const navLinks=[...nav.querySelectorAll('.links a')];
  const secIO=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){navLinks.forEach(l=>l.classList.toggle('active',l.getAttribute('href')==='#'+e.target.id))}}),{rootMargin:'-45% 0px -50% 0px'});
  document.querySelectorAll('main section[id]').forEach(s=>secIO.observe(s));

  /* reveal */
  const rvIO=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');rvIO.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});
  document.querySelectorAll('.rv').forEach((el,i)=>{el.style.transitionDelay=((i%3)*70)+'ms';rvIO.observe(el)});

  /* timeline progress */
  const tl=document.getElementById('timeline'), tlp=document.getElementById('tlp');
  function tlUpdate(){const r=tl.getBoundingClientRect();const p=Math.min(1,Math.max(0,(innerHeight*.6-r.top)/r.height));tlp.style.height=(p*(r.height-12))+'px'}
  addEventListener('scroll',tlUpdate,{passive:true});addEventListener('resize',tlUpdate);tlUpdate();
})();
