"use strict";
//어..음...이미지 추가 버튼

// function imgInsert() {
//   console.log(`text`);
//   const browseBtn = document.querySelector('.btn-input-img');
//   const realInput = document.getElementById(`file-input-img`);

//   browseBtn.addEventListener('click', () => {
//     console.log("22323");
//     realInput.click();
//   });
// }

// imgInsert();

// 미리보기 수정 샥제
// function handleFileSelect(event) {
//   let input = this;
//   console.log(input.files)
//   if (input.files && input.files.length) {
//       let reader = new FileReader();
//       this.enabled = false
//       for(let i = 0; i < input.files.length; i++) {
//         reader.onload = (function (e) {
//         console.log(`test22`);
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
let download_url_lis = [];

function readInputFile(e) {

  let sel_files = [];

  sel_files = [];

  $('#imgPreview').empty();

  let files = e.target.files;
  let fileArr = Array.prototype.slice.call(files);
  let index = 0;
  let i = 0
  //todo : 프로그래스바 시작
  fileArr.forEach(function (f) {
    console.log(`2`);
    if (!f.type.match("image/.*")) {
      alert("이미지 확장자만 업로드 가능합니다.");
      return;
    };
    if (files.length < 11) {

      console.log(`3`);
      console.log("테스트" + files[0]);
      sel_files.push(f);
      

      //스토리지에 업로드
      let storage = firebase.storage();
      //let file=document.getElementById("file-input-img").files[0];
      let files_yang = document.getElementById("file-input-img").files;
      let delivery_uid = document.getElementById('delivery_uid').value
      let user_uid = document.getElementById('user_uid').value
      let filename = delivery_uid + user_uid
      console.log("files:" + files);
      let storageRef = storage.ref();


      filename = filename + "??" + String(i)


      let thisref = storageRef.child(filename).put(files[i]);
      i++

      thisref.on(firebase.storage.TaskEvent.STATE_CHANGED, // or 'state_changed'
        function (snapshot) {
          let start = new Date().getTime();
          // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
          let progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
          
          console.log('Upload is ' + progress + '% done');
          if(progress !== 100) {
            let loading = `
              <div class="loading-img">
              <i class="fas fa-spinner fa-pulse fa-5x"></i>
              </div>
            `;
            $('#imgPreview').append(loading);
          }
          else {
            const delLoading = document.querySelector(`.loading-img`);
            delLoading.parentNode.removeChild(delLoading);

            let reader = new FileReader();
            reader.onload = function (e) {
              let html = `<li id=img_id_${index}>
              <img src=${e.target.result} data-file=${f.name} />
              <span onclick="previewDelete(${index})">삭제</span>
              </li>`;
              $('#imgPreview').append(html);
              index++;
            };
            reader.readAsDataURL(f);
          }

          
          switch (snapshot.state) {
            case firebase.storage.TaskState.PAUSED: // or 'paused'
              console.log('Upload is paused');
              break;
            case firebase.storage.TaskState.RUNNING: // or 'running'
              console.log('Upload is running');
              break;
          }
        },
        function (error) {

          // A full list of error codes is available at
          // https://firebase.google.com/docs/storage/web/handle-errors
          switch (error.code) {
            case 'storage/unauthorized':
              // User doesn't have permission to access the object
              break;

            case 'storage/canceled':
              // User canceled the upload
              break;
            case 'storage/unknown':
              // Unknown error occurred, inspect error.serverResponse
              break;
          }
        },
        function () {
          // Upload completed successfully, now we can get the download URL
          thisref.snapshot.ref.getDownloadURL().then(function (downloadURL) {

            console.log('File available at', downloadURL);
            //document.getElementById('downloadURL[]').value+=downloadURL
            // let downloadURL_reviewindex=document.getElementById('downloadURL')
            // downloadURL_reviewindex.innerHTML +=`
            // <input type="hidden" id="downloadURL${i}" name="downloadURL[] value="${downloadURL}">
            // `;
            download_url_lis.push(downloadURL);






          });
        }); //thisref.on 끝



    } //if문 끝
  }) //for each문 끝

  //todo : 프로그래스바 끝



  if (files.length > 11) {
    alert("최대 10장까지 업로드 할 수 있습니다.");
  };
}

$('#file-input-img').on('change', readInputFile);

function previewDelete(e) {
  const li = document.getElementById(`img_id_${e}`);
  li.remove();
  $("#file-input-img").val("");
}
