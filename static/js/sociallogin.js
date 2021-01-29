


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


function naverLogin() { // 네이버 로그인
    //alert("네이버로그인클릭");
    console.log("네이버로그인클릭");
    params = {
        response_type: 'code',
        client_id:'gyHDnkTYKAXVqlUIyVLp',
        //redirect_uri: location.origin + '/naver/callback/',
        redirect_uri: 'http://3.35.247.69/naver/callback/',
        state: document.querySelector('[name=csrfmiddlewaretoken]').value
    }
    url = buildUrl('https://nid.naver.com/oauth2.0/authorize', params);
    location.replace(url);
}
function buildQuery(params) {
    return Object.keys(params).map(function (key) {return key + '=' + encodeURIComponent(params[key])}).join('&')
}
function buildUrl(baseUrl, queries) {
    return baseUrl + '?' + buildQuery(queries)
}


function KakaoLogin(){
    window.Kakao.init('869c59081a7f71a8abe022de7f7c522f');
    console.log(Kakao.isInitialized());
    window.Kakao.Auth.login({
        scope:'profile,account_email',
        success: function(authObj){
            console.log(authObj);
            
            window.Kakao.API.request({
                url:'/v2/user/me',
                success: res=>{
                    const kakao_account =res.kakao_account;
                    document.getElementById("kaemail").value=kakao_account.email;
                    console.log(kakao_account.email);
                }
            })
        }
    })
}
function google_login(){
    //alert("구글로그인클릭");
    var provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth()
    .signInWithPopup(provider)
    .then((result) => {
        /** @type {firebase.auth.OAuthCredential} */
        var credential = result.credential;
        console.log("크레댄셜:");
        console.log(credential);

    // This gives you a Google Access Token. You can use it to access the Google API.
        var token = credential.accessToken;
        console.log("토큰:");
        console.log(token);
       
    // The signed-in user info.
        var user = result.user;
        console.log("유저:");
        console.log(user);
        console.log(user.uid);
        console.log(typeof(user.displayName));
        //window.location.href = 'http://127.0.0.1:8000/google/'+user.uid+'/'+user.displayName;
        //window.location.href = 'http://127.0.0.1:8000/google/'+user.uid;
        window.location.href = 'http://3.35.247.69/google/'+user.uid
        
    // ...
    }).catch((error) => {
    // Handle Errors here.
    var errorCode = error.code;
    console.log(errorCode);
    var errorMessage = error.message;
    console.log(errorMessage);
    // The email of the user's account used.
    var email = error.email;
    console.log(email);
    // The firebase.auth.AuthCredential type that was used.
    var credential = error.credential;
    console.log(credential);
    // ...
  });
}



//   window.fbAsyncInit = function() {
//     FB.init({
//       appId      : '118661006732967',
//       cookie     : true,
//       xfbml      : true,
//       version    : 'v9.0'
//     });
      
//     FB.AppEvents.logPageView();   
      
//   };

//   (function(d, s, id){
//      var js, fjs = d.getElementsByTagName(s)[0];
//      if (d.getElementById(id)) {return;}
//      js = d.createElement(s); js.id = id;
//      js.src = "https://connect.facebook.net/en_US/sdk.js";
//      fjs.parentNode.insertBefore(js, fjs);
//    }(document, 'script', 'facebook-jssdk'));
function facebook_login(){
    var provider = new firebase.auth.FacebookAuthProvider();
    firebase
  .auth()
  .signInWithPopup(provider)
  .then((result) => {
    /** @type {firebase.auth.OAuthCredential} */
    var credential = result.credential;

    // The signed-in user info.
    var user = result.user;

    // This gives you a Facebook Access Token. You can use it to access the Facebook API.
    var accessToken = credential.accessToken;

    // ...
  })
  .catch((error) => {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
    // The email of the user's account used.
    var email = error.email;
    // The firebase.auth.AuthCredential type that was used.
    var credential = error.credential;

    // ...
  });

}


