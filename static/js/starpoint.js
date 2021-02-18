"use strict";

function drawStar(star) {
  let point = star.value;
  const del = document.querySelectorAll(`.star-draw`);

  del.forEach(function(del){
    console.log(del);
    del.classList.add(`staroff`)
    del.classList.remove(`staron`);
  });

  for(let i = 0; i < point; i++) {
    del[i].classList.add(`staron`);
  }
  console.log(`value:: ${point}`);
}
