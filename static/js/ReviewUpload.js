





function ReviewUpload(){
    alert("리뷰실행")
//     var storage= firebase.storage();
//     var file=document.getElementById("file-input-img").files[0];
//     var storageRef=storage.ref();
//     var thisref=storageRef.child("file.name").put(file);
//     var imgurl="";

//     thisref.on(firebase.storage.TaskEvent.STATE_CHANGED, // or 'state_changed'
//     function(snapshot) {
//     // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
//     var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
//     console.log('Upload is ' + progress + '% done');
//     switch (snapshot.state) {
//       case firebase.storage.TaskState.PAUSED: // or 'paused'
//         console.log('Upload is paused');
//         break;
//       case firebase.storage.TaskState.RUNNING: // or 'running'
//         console.log('Upload is running');
//         break;
//         }
//     }, function(error) {

//     // A full list of error codes is available at
//   // https://firebase.google.com/docs/storage/web/handle-errors
//     switch (error.code) {
//     case 'storage/unauthorized':
//       // User doesn't have permission to access the object
//     break;

//     case 'storage/canceled':
//       // User canceled the upload
//       break;
//     case 'storage/unknown':
//       // Unknown error occurred, inspect error.serverResponse
//       break;
//   }
//     }, function() {
//   // Upload completed successfully, now we can get the download URL
//     thisref.snapshot.ref.getDownloadURL().then(function(downloadURL) {
//     console.log('File available at', downloadURL);
//     imgurl=downloadURL
    

//     });
//     });


    //delivery 정보 파이어스토어에서 가죠오기
    var documentId=document.getElementById('delivery_uid').value;
    var starPoint=document.getElementById('starPoint').value;
    var text=document.getElementById('review_textarea').value;
    var docRef = db.collection("delivery").doc(documentId);
    var imgurl=document.getElementById('downloadURL').value;
  
    docRef.get().then(function(doc) {
        if (doc.exists) {
            console.log("Document data:", doc.data());
            //데이터 review 추가.
            db.collection("product").doc(doc.data().product_id).collection('review').doc(doc.data().uid).set({
                StarPoint:starPoint,
                user_uid: doc.data().uid,
                delivery_uid: doc.id,
                text: text,
                SizePoint: "",
                BrightPoint: "",
                ColorPoint: "",
                ThickPoint: "",
                timestamp: firebase.firestore.FieldValue.serverTimestamp(),
                downloadUrl:imgurl
            })
            .then(() => {
                console.log("Document written with ID: ");
                history.back();
            })
            .catch((error) => {
                console.error("Error adding document: ", error);
            });
  


        } else {
            // doc.data() will be undefined in this case
            console.log("No such document!");
        }
    }).catch(function(error) {
        console.log("Error getting document:", error);
    });
    



}
  

