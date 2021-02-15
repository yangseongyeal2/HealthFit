//hide or show subMenu
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

//go to top

document.getElementById(`go-top`).addEventListener(`click`, () => {
  window.scrollTo({
    top: 0,
    left: 0,
    behavior: "smooth"
  });
})