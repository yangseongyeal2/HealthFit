//어..음...이미지 추가 버튼
function imgInsert() {
  console.log(`text`);
  const browseBtn = document.querySelector('.btn-input-img');
  const realInput = document.querySelector('.file-input-img');

  browseBtn.addEventListener('click', () => {
    realInput.click();
  });
}








imgInsert();



