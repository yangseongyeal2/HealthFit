




function ReviewUpload(){
    alert("리뷰실행")
    var storage= firebase.storage();
    var file=document.getElementById("file-input-img").files[0];
    var storageRef=storage.ref();
    var thisref=storageRef.child(file.name).put(file);
    thisref.on('state_changed',function(snapshot){
        console.log("file Uploaded successfully");
    },
    function(error){
        console.log("error")
    },
    function(){
        var downloadURL=thisref.snapshot.downloadURL;
        console.log("got url")
        
    });

}