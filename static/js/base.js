window.onscroll = function() {fixed()};

const subMenu = document.getElementById(`headbar__sub`);
console.log(subMenu);
const sticky = subMenu.offsetTop;

function fixed() {
  if(window.pageYOffset > sticky) {
    subMenu.classList.add(`off`);
  } else {
    subMenu.classList.remove(`off`);
  }
}