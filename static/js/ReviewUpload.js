





function ReviewUpload(){
  

    var documentId=document.getElementById('delivery_uid').value;
    var starPoint=document.getElementById('starPoint').value;
    var text=document.getElementById('review_textarea').value;
    var docRef = db.collection("delivery").doc(documentId);
    //var imgurl=document.getElementById('downloadURL10').value;
    //var imglist=document.getElementsByName('downloadURL[]').value;
   // console.log("이미지리스트:"+imgurl)
  
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
                downloadUrl:download_url_lis
            })
            .then(() => {
                console.log("Document written with ID: ");
                //history.back();
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
  

