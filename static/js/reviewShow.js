"use strict";
let savingReviewShow = null;

function detailReviewInit(e){
  savingReviewShow = e;
  console.log(savingReviewShow);
  drawReviewShow(savingReviewShow);
}

function drawReviewShow(data) {
  const painter = document.querySelector(`.details__review--wrap`);
  console.log(data.length);


  for(let i = 0; i < data.length; i++) {
    painter.innerHTML += 
    `
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
  
}

function detailDrawStar(data) {
  let point = "";
  console.log(`point:${data.point}`);
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

function detailDrawImg(data) {
  let img ="";
  if(data.reviewImg) {
    img += `<img src="${data.reviewImg}" alt="userReviewImg"></img>`;
  }
  return img;
}
