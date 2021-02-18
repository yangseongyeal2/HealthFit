//어..음...이미지 추가 버튼
function imgInsert() {
  console.log(`text`);
  const browseBtn = document.querySelector('.btn-input-img');
  const realInput = document.querySelector('.file-input-img');

  browseBtn.addEventListener('click', () => {
    console.log("이쁜버튼클릭")
    realInput.click();
  });
}



// 미리보기 수정 샥제
// function handleFileSelect(event) {
  
//   let input = this;
//   console.log(input.files)
//   if (input.files && input.files.length) {
//       let reader = new FileReader();
//       this.enabled = false
//       for(let i = 0; i < input.files.length; i++) {
//         reader.onload = (function (e) {
//         console.log("test22");
//         console.log(e)
//             $("#imgPreview").html(['<img class="thumb" src="', e.target.result, '" title="', escape(e.name), '"/>'].join(''))
//         });
//         reader.readAsDataURL(input.files[0]);
//       }
//   }
// }

// $('.file-input-img').change(handleFileSelect);

// $('.file-edit-icon').on('click', '.preview-de', function () {
//   $("#preview").empty()
//   $("#file").val("");
// });

// $('.preview-edit').click( function() {
// $("#file").click();
// } );

function readInputFile(e){
  let sel_files = [];

  sel_files = [];
  $('#imgPreview').empty();

  let files = e.target.files;
  let fileArr = Array.prototype.slice.call(files);
  let index = 0;

  fileArr.forEach(function(f){
    if(!f.type.match("image/.*")){
        alert("이미지 확장자만 업로드 가능합니다.");
          return;
      };
      if(files.length < 11){
        sel_files.push(f);
          let reader = new FileReader();
          reader.onload = function(e){
            let html = <a id=img_id_${index}><img src=${e.target.result} data-file=${f.name} /></a>;
              $('#imgPreview').append(html);
              index++;
          };
          reader.readAsDataURL(f);
      }
  })
  if(files.length > 11){
    alert("최대 10장까지 업로드 할 수 있습니다.");
  };
}

$('.file-input-img').on('change',readInputFile)







imgInsert();



