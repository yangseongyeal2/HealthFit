function inisispay() {
    event.preventDefault();
    var IMP = window.IMP;
    var code = "imp85681890";  // FIXME: 가맹점 식별코드
    IMP.init(code);
    var productname=document.getElementById('productname').value
    var recipient=document.getElementById('recipient').value
    var username=document.getElementById('username').value
    var id=document.getElementById('id').value
    var phonenumber=document.getElementById('phonenumber').value
    //var adr=document.getElementById('adr').value
    //주소
    var zipcode=document.getElementById('sample6_postcode').value
    var address=document.getElementById('sample6_address').value
   
    var address_detail=document.getElementById('sample6_detailAddress').value
    var address_extra=document.getElementById('sample6_extraAddress').value
    var total_price=document.getElementById('total_price').value
    var brandName=document.getElementById('brandName').value
    var option=document.getElementById('option').value
    var uid=document.getElementById('uid').value
    var delivery_message=document.getElementById('delivery-message').value
    var img=document.getElementById('img').value
    var product_id=document.getElementById('product_id').value
    if (!address){
        alert("주소를 입력하십시오")
        return
    }
    // if (address_detail){
    //     alert(address_detail)
    //     address+=" "+address_detail+ " "+address_extra

    // }
    if (!delivery_message){
        alert("배송시 필요한 요구사항을 입력하시오")
       return
    }
    var url="complete"+"/"+option+"/"+total_price+"/"+username+"/"+phonenumber+"/"+address+"/"+uid+"/"+delivery_message+"/"+product_id+"/"
    // 결제요청
    IMP.request_pay({
        // name과 amount만 있어도 결제 진행가능
        pg : 'html5_inicis', // pg 사 선택
        pay_method : 'card',
        merchant_uid : 'merchant_' + new Date().getTime(),
        name : productname,
        amount : total_price,
        buyer_email : id,
        buyer_name : username,
        buyer_tel : phonenumber,
        buyer_addr : address,
        buyer_postcode : zipcode,
        m_redirect_url : 'https://127.0.0.1:8000/payments/complete/'
    }
    , function(rsp) {
        if ( rsp.success ) {
            var msg = '결제가 완료되었습니다.';
          
            msg += '고유ID : ' + rsp.imp_uid;
            msg += '상점 거래ID : ' + rsp.merchant_uid;
            msg += '결제 금액 : ' + rsp.paid_amount;
            msg += '사용자이름 : ' + rsp.buyer_name;
            msg += '사용자번호 : ' + rsp.buyer_tel;
            msg += '주소 : ' + rsp.buyer_addr;
            msg += '배송장주소 : ' + rsp.buyer_postcode;

            location.href=url

        }
        else {
            var msg = '결제에 실패하였습니다. 에러내용 : ' + rsp.error_msg
        }
        alert(msg);
    });
}
function phoneAuth(){
    //console.log("폰인증클릭");
    //var IMP = window.IMP; // 생략해도 괜찮습니다.
    IMP.init("imp85681890"); // "imp00000000" 대신 발급받은 "가맹점 식별코드"를 사용합니다.
      // IMP.certification(param, callback) 호출
//     IMP.certification({ // param
//         // merchant_uid: "ORD20180131-0000011"
//     }, function (rsp) { // callback
//         if (rsp.success) {
//             console.log("폰인증클릭");
//             jQuery.ajax({
//                 url: "https://www.myservice.com/certifications", // 서비스 웹서버
//                 method: "POST",
//                 headers: { "Content-Type": "application/json" },
//                 data: { imp_uid: rsp.imp_uid }
//               });
//     } else {
//         alert("인증에 실패하였습니다. 에러 내용: " +  rsp.error_msg);
//     }
//   });
IMP.certification({
    merchant_uid : 'merchant_' + new Date().getTime() //본인인증과 연관된 가맹점 내부 주문번호가 있다면 넘겨주세요
}, function(rsp) {
    if ( rsp.success ) {
         // 인증성공
        console.log(rsp.imp_uid);
        console.log(rsp.merchant_uid);
        
        $.ajax({
                type : 'POST',
                url : '/certifications/confirm',
                dataType : 'json',
                data : {
                    imp_uid : rsp.imp_uid
                }
         }).done(function(){
           takeResponseAndHandle(rsp)
         });
            
    } else {
         // 인증취소 또는 인증실패
        var msg = '인증에 실패하였습니다.';
        msg += '에러내용 : ' + rsp.error_msg;
 
        alert(msg);
    }
});
}