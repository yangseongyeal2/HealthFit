//hide or show subMenu
window.onscroll = function() {fixed()};

const subMenu = document.getElementById(`headbar__sub`);
console.log(subMenu);
const sticky = subMenu.offsetTop;




//파이어스토어 

var firebaseConfig = {
  apiKey: "AIzaSyAFN2apSBQwHIiGioEKyyQORxceIR22VMs",
  authDomain: "healthstore-de3c3.firebaseapp.com",
  databaseURL: "https://healthstore-de3c3-default-rtdb.firebaseio.com",
  projectId: "healthstore-de3c3",
  storageBucket: "healthstore-de3c3.appspot.com",
  messagingSenderId: "838060678239",
  appId: "1:838060678239:web:d861eca1e8639cc3a14fea",
  measurementId: "G-3T3MCBWTZ8"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

// Required for side-effects

var db = firebase.firestore();







// list.forEach(function(element){
//   console.log(element); // 0 1 2 3 4 5 6 7 8 9 10
// });




function init(data) { //0에서 4까지 리스트  savingData[0].uid 이런식으로 불러오기
  savingData = data;
 


var step;
const dataBody = document.getElementById('RecentView_list');
for (step = 0; step < data.length; step++) {
  // Runs 5 times, with values of step 0 through 4.
  var documentId=savingData[step].uid
  var docRef = db.collection("product").doc(documentId);
  docRef.get().then(function(doc) {
    if (doc.exists) {
      console.log("Document data:", doc.data());
     
      dataBody.innerHTML += `
      <li>
      <ul>
        <li><img src="${doc.data().downloadurl}" alt="product_img"></li>
        <li>${doc.data().brand}</li>
        <li>${doc.data().name}</li>
      </ul>
      </li>
      `;



    } else {
      // doc.data() will be undefined in this case
      console.log("No such document!");
    }
  }).catch(function(error) {
  console.log("Error getting document:", error);
  });

}
 
  
}



function fixed() {
  if(window.pageYOffset > sticky) {
    subMenu.classList.add(`off`);
  } else {
    subMenu.classList.remove(`off`);
  }
}

//go to top

document.getElementById(`go-top`).addEventListener(`click`, () => {
  window.scrollTo({
    top: 0,
    left: 0,
    behavior: "smooth"
  });
})