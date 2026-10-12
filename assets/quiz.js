// Reusable quiz: <div class="quiz" data-answer="1" data-why="..."><div class="q">..</div><button>..</button>...<div class="why"></div></div>
// data-answer is the 0-based index of the correct button.
document.querySelectorAll('.quiz').forEach(function (quiz) {
  var answer = Number(quiz.dataset.answer);
  var why = quiz.querySelector('.why');
  quiz.querySelectorAll('button').forEach(function (btn, i) {
    btn.addEventListener('click', function () {
      if (i === answer) {
        btn.classList.add('right');
        why.textContent = '✓ Sahi. ' + (quiz.dataset.why || '');
      } else {
        btn.classList.add('wrong');
        why.textContent = '✗ Phir se socho.';
      }
    });
  });
});
