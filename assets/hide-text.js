// Reusable: adds a "Text chhupao / dikhao" button above every .card.script,
// so the learner can practise from keywords only (retrieval, not re-reading).
document.querySelectorAll('.card.script').forEach(function (card) {
  var btn = document.createElement('button');
  btn.className = 'hide-btn';
  btn.textContent = 'Text chhupao';
  btn.addEventListener('click', function () {
    var hidden = card.classList.toggle('is-hidden');
    btn.textContent = hidden ? 'Text dikhao' : 'Text chhupao';
  });
  card.parentNode.insertBefore(btn, card);
});
