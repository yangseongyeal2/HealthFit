"use strict";

function drawStar(star) {
  document.getElementById('starPoint').value=star.value
  let point = star.value;
  const del = document.querySelectorAll(`.star-draw`);

  del.forEach(function(del){
    del.classList.replace(`staron`, `staroff`);
    console.log(del);
  });

  for(let i = 0; i < point; i++) {
    del[i].classList.replace(`staroff`, `staron`);
  }
  console.log(`value:: ${point}`);
}
