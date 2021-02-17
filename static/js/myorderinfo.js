"use strict";
const dataInPage = 5; //한 화면에 나타낼 리스트 수
const pageCount = 5; //한 화면에 나타낼 페이지 수
let totalleng=0; //데이터의 갯수
//오브젝트 저장하기 위한 전역변수
let savingPage = null;

function pagingInit(data) {
  savingPage = data;
  console.log(savingPage);
  paging(1, savingPage);
}


function paintingData(currentPage, totalData) {
  
  let start = 5 * (currentPage - 1);
  let end = start + pageCount;

  if(end > totalData.length) {
    end = totalData.length;
  }

  const dataBody = document.querySelector(`tbody`);
  while (dataBody.hasChildNodes()) {
    dataBody.removeChild(dataBody.firstChild);
  }
  
  for (start; start < end; start++) {
    console.log(`forstart : ${start}`);
    console.log(totalData[start].state);

    dataBody.innerHTML += `
    <tr>
    <td>${totalData[start].timestamp}</td>
    <td><img src="${totalData[start].image}" alt="test"></td>
    <td>${totalData[start].name}</td>
    <td>${totalData[start].option}</td>
    <td>${totalData[start].price}</td>
    <td>${totalData[start].state}</td>
    <td>취소/교환/반품</td>
    <td><span id="tableReview" class="review--off">후기작성</span></td>
    </tr>
    `;

    if(totalData[start].state === "배송완료") {
      const tableReview = document.getElementById(`tableReview`);
      tableReview.setAttribute(`class`, `review--on`);
    }
  }
}

function paging(currentPage, totalData) {
  const totalPage = Math.ceil(totalData.length / dataInPage); //총 페이지 수
  const pageGroup = Math.ceil(currentPage / pageCount); // 1 = 현재 페이지 1 = 1~5, 2 = 6~10

  let last = pageGroup * pageCount; //현재 페이지의 마지막 번호

  if (last > totalPage) {
    last = totalPage;
  }

  let first = last - (pageCount - 1); // 현재 페이지의 시작 번호
  const next = last + 1; // 현재 페이지의 다음 번호
  // const prev = first - 1;

  if (totalPage < 1) { //
    first = last;
  }

  const pages = document.getElementById(`paging`);

  //페이지 이동 시 삭제 후 다시 그리기 위한 while
  while (pages.hasChildNodes()) {
    pages.removeChild(pages.firstChild);
  }


  if (first > 5) { //시작 페이지가 5 이상일 경우
    pages.innerHTML += `<li>
  <a href="#" aria-label="Previous" onclick="prevClick(${currentPage})">
  <span aria-hidden="true">이전</span>
  </a>
  </li>`;
  }

  for (let i = first; i <= last; i++) {
    if (currentPage === i) { // 현재 페이지에 active 부여
      pages.innerHTML += `<li id="page/${i}" class = "active"><a href="#">${i}</a></li>`;
      paintingData(i, totalData);
    } else if (i > 0) { // 현재 페이지 외 다른 페이지 PAINTING
      pages.innerHTML += `<li id="page/${i}" onclick="pageClick(${i})"><a href="#">${i}</a></li>`;
    }
  }
  if (next > 5 && next < totalPage) { //
    pages.innerHTML += `<li>
  <a href="#" aria-label="Next" onclick="nextClick(${currentPage})">
  <span aria-hidden="true">다음</span>
  </a>
  </li>`;
  }
}



function pageClick(currentNumber) { //100에 DB DATA
  paging(currentNumber, savingPage);
}
//1 = 1~5 2 = 6~10
//1=1, 2=6, 3=11, 4=16, 5=21
function prevClick(pageNumber) {
  const prev = Math.ceil((pageNumber - 5) / pageCount);
  const movePage = 1 + (5 * (prev - 1));
  console.log(movePage);
  paging(movePage, savingPage);
}

function nextClick(pageNumber) {
  const next = Math.ceil((pageNumber + 5) / pageCount);
  const movePage = 1 + (5 * (next - 1));
  // console.log(movePage);
  paging(movePage, savingPage);
}