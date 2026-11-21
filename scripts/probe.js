<script>
window.addEventListener('load', function(){ setTimeout(function(){
  document.querySelectorAll('textarea').forEach(function(t){ t.value='test'; t.dispatchEvent(new Event('input',{bubbles:true})); });
  document.querySelectorAll('input[type=radio]').forEach(function(r){ if(!document.querySelector('input[name="'+r.name+'"]:checked')){ r.checked=true; r.dispatchEvent(new Event('change',{bubbles:true})); }});
  var btns=[].slice.call(document.querySelectorAll('button.show, .card button'));
  btns.forEach(function(b){ b.click(); });
  document.title='RESULT answers='+document.querySelectorAll('.answer').length+' stillHidden='+document.querySelectorAll('.answer[hidden]').length;
 },300); });
window.onerror=function(m){ document.title='JSERROR '+m; };
</script>
