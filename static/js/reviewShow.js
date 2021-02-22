"use strict";
let savingReviewShow = null;

function detailReviewInit(e){
  savingReviewShow = e;
  drawReviewShow(savingReviewShow);
}

function drawReviewShow(data) {
  const painter = document.querySelector(`.details__review--wrap`);
  

  let str = "";
  for(let i = 0; i < data.length; i++) {
    str += `
      <article>

        <div class="details__review__userinfo">

          <div class="details__review__userinfo__nickname">
            <span>${data[i].nickname}</span>
          </div>

          <div class="details__review__userinfo__info">

            <span>
              ${detailDrawStar(data[i])}
            </span>

            <span>${data[i].time}</span>

          </div>

          <div class="details__review__delivery__info">
            <span>${data[i].productName}, ${data[i].productOption}</span>
          </div>

          <div class="details__review__product-img">
            ${detailDrawImg(data[i])}
          </div>

          <div class="details__review__text">
            <pre>${data[i].reviewText}</pre>
          </div>

        </div>

      </article>
    `;
    
  }
  painter.innerHTML += str;
  
}
// 별점에 맞는 별 그리는 함수
function detailDrawStar(data) {
  let point = "";
  for(let i = 0; i < data.point; i++) {
    point += 
    `
      <span class="star-draw staron">
      <i class="fas fa-star fa-2x"></i>
      </span>
    `;
  }
  for(let i = 5; i > data.point; i--) {
    point += 
    `
      <span class="star-draw staroff">
      <i class="fas fa-star fa-2x"></i>
      </span>
    `;
  }
  return point;
}

//유저가 업로드한 이미지를 저장하는 함수
function detailDrawImg(data) {
  let img = "";
  let array = data.reviewImg;
  console.log(`array : ${array}`);
    
  array.forEach(element => {
    console.log(`이미지 경로: ${element}`);
    img += `<img src="${element}" alt="userReviewImg"></img>`;  
  });
  return img;
}
