function pageClick () {

}



function paging () {
  let totlaData = 50;
  let currentPage = 2;
  const dataInPage = 5; //한 화면에 나타낼 데이터 수
  const pageCount = 5; //한 화면에 나타낼 페이지 수

  const totalPage = Math.ceil(totlaData / dataInPage); //총 페이지 수 - 50에 backend data 넣으면 됨.
  const pageGroup = Math.ceil(currentPage / pageCount); // 1 = 현재 페이지

  console.log(totalPage);
  console.log(pageGroup);

  let last =  pageGroup * pageCount;
  if(last > totalPage) {
    last = totalPage;
  }

  let first = last - (pageCount - 1); // first === -3, last === 1
  const next = last + 1; // next = 2
  const prev = first - 1; // prev = 0

  if(totalPage < 1) {
    first = last;
  }

  const pages = document.querySelector(`.pagination`);
  console.log(pages);
  console.log(first);
  console.log(last);

  if(first > 5) {
    pages.innerHTML += `<li>
    <a href="#" aria-label="Previous">
    <span aria-hidden="true">이전</span>
    </a>
    </li>`;
  }

  for(let i = first; i <= last; i++) {
    if(currentPage === i) {
      pages.innerHTML += `<li class="active"><a href="#">${i}</a></li>`;
    } else if (i > 0) {
      pages.innerHTML += `<li><a href="#">${i}</a></li>`;
    }
  }
  if(next > 5 && next < totalPage) {
    pages.innerHTML += `<li>
    <a href="#" aria-label="Next">
    <span aria-hidden="true">다음</span>
    </a>
    </li`;
  }
}

paging();