
mtotal=0
stotal=0
ltotal=0
xltotal=0
xxltotal=0;
let mySet = new Set();

function paintOption(size) {
   
    var sizevalue=size.value
    if (!mySet.has(sizevalue)){


    const paint = document.getElementById(`optionList`);

    const ul = document.createElement(`ul`);
    ul.setAttribute(`class`, `optionListAlign`);
    var ulid="ulid"+sizevalue
    ul.setAttribute(`id`,`${ulid}`)

    paint.appendChild(ul);

    // nameList li 
    const nameList = document.createElement(`li`);
    //nameList.setAttribute(`class`, `optionListAlign product-item`);
    ul.appendChild(nameList);
    const productName = document.createElement(`div`);
    let nameId = document.getElementById(`product_name`).value;
    const nameText = document.createTextNode(`${nameId}`);

    nameList.appendChild(productName);
    productName.appendChild(nameText);
    // productName CSS 작성해야됨@@

    const optionSize = document.createElement(`div`);
    const sizeText = document.createTextNode(`${size.value}`);

    nameList.appendChild(optionSize);
    optionSize.appendChild(sizeText);
    //nameList li END

    //countList li 
    const countList = document.createElement(`li`);
    ul.appendChild(countList);

    const counter = document.createElement(`input`);
    counter.setAttribute(`type`, `text`);
    var gaesuID="amount_"+sizevalue
    counter.setAttribute(`name`, `${gaesuID}`);
    var amountid="amountId"+sizevalue
    counter.setAttribute(`id`, `${amountid}`);
    
    counter.setAttribute(`onchange`, `amountprice(this,'${sizevalue}')`);
    counter.setAttribute(`min`, `1`);
    countList.appendChild(counter);

    const closeBtn = document.createElement(`i`);
    closeBtn.setAttribute(`class`, `fa fa-trash fa-lg`);
    closeBtn.setAttribute(`aria-hidden`, `true`);
    // closeBtn.setAttribute(`style`, `cursor: pointer;`);
    closeBtn.setAttribute(`onclick`, `cancel('${sizevalue}')`);
    countList.appendChild(closeBtn);
    //counstList li END

    //priceList li
    const priceList =document.createElement('li');
    ul.appendChild(priceList);
    const priceDiv=document.createElement('div');
    let productPrice=document.getElementById(`product_price`).value+"원";
    const priceText = document.createTextNode(productPrice);
    let priceId = size.value + `_amount`;
    priceDiv.setAttribute(`id`, priceId);
    
    priceList.appendChild(priceDiv);
    priceDiv.appendChild(priceText);

    mySet.add(sizevalue)

    }
    
}


function optionshow(e) {
    
    var a =document.getElementById("product_price").value;
    var price=a.split('원');
    var price2=price[0].split(',');
    var price3=price2[0]+price2[1];
    var int_price=parseInt(price3);

    
    
    if (e.value=="S"){
        paintOption(e);

        stotal=int_price
        // $("#option_ul_s").show();
        total=mtotal+ltotal+xltotal+stotal+xxltotal;
        strtotal=String(total)+"원";
        document.getElementById("total").innerHTML="TOTAL:"+strtotal;
        document.getElementById('amountIdS').value='1';
    }
    if (e.value=="M"){
        paintOption(e);
       // document.getElementById("option_ul_m").style.display="block";
        // $("#option_ul_m").show();

        mtotal=int_price
        total=mtotal+ltotal+xltotal+stotal+xxltotal;
        strtotal=String(total)+"원";
        document.getElementById("total").innerHTML="TOTAL:"+strtotal;
        document.getElementById('amountIdM').value='1';
    }
    if (e.value=="L"){
        paintOption(e);
       // document.getElementById("option_ul_l").style.display="block";
        // $("#option_ul_l").show();
        ltotal=int_price
        total=mtotal+ltotal+xltotal+stotal+xxltotal;
        strtotal=String(total)+"원";
        document.getElementById("total").innerHTML="TOTAL:"+strtotal;
        document.getElementById('amountIdL').value='1';

    }
    if (e.value=="XL"){
        paintOption(e);

        // $("#option_ul_xl").show();
        xltotal=int_price
        total=mtotal+ltotal+xltotal+stotal+xxltotal;
        strtotal=String(total)+"원";
        document.getElementById("total").innerHTML="TOTAL:"+strtotal;
        document.getElementById('amountIdXL').value='1';
    }
    if (e.value=="XXL"){
        paintOption(e);

        // $("#option_ul_xl").show();
        xxltotal=int_price
        total=mtotal+ltotal+xltotal+stotal+xxltotal;
        strtotal=String(total)+"원";
        document.getElementById("total").innerHTML="TOTAL:"+strtotal;
        document.getElementById('amountIdXXL').value='1';
    }

    const resetText = document.getElementById(`size`);
    resetText.value = `first`;

    
    // document.getElementById("option_size").innerHTML=e.value;
    // var option_result=document.getElementById("option_result");
    // var p=document.getElementById("option_ul");
    // option_result.appendChild(p);
  }

  function cancel(e){
    console.log("취소클릭")
    var a =document.getElementById("product_price").value;
    var price=a.split('원');
    var price2=price[0].split(',');
    var price3=price2[0]+price2[1];
    var int_price=parseInt(price3);
    
    // const div = document.getElementById(`adminProuctDetailDiv${cnt}`);
    // const admin = document.getElementById(`adminAppend`);
    // const input = document.getElementById(`adminProuctDetailImage${cnt}`);

    // div.remove();


        if (e=='S'){
            stotal=0
            // $("#option_ul_s").hide();
           
            //document.getElementById("total").innerHTML= document.getElementById("total").value;
            total=mtotal+ltotal+xltotal+stotal+xxltotal;
            strtotal=String(total)+"원";
            document.getElementById("total").innerHTML="TOTAL:"+strtotal;
            document.getElementById("amountIdS").value=0;
            document.getElementById("S_amount").innerHTML=String(int_price)+"원";
            var ul=document.getElementById("ulidS")
            ul.remove()
            mySet.delete('S')
        }else if (e=='M') {
            mtotal=0
            $("#option_ul_m").hide();
           
            //document.getElementById("total").innerHTML= document.getElementById("total").value;
            total=mtotal+ltotal+xltotal+stotal+xxltotal;
            strtotal=String(total)+"원";
            document.getElementById("total").innerHTML="TOTAL:"+strtotal;
            document.getElementById("amountIdM").value=0;
            document.getElementById("M_amount").innerHTML=String(int_price)+"원";
            var ul=document.getElementById("ulidM")
            ul.remove()
            mySet.delete('M')
        }else if (e=='L'){
            ltotal=0;
            //document.getElementById("total").innerHTML= document.getElementById("total").value;
            total=mtotal+ltotal+xltotal+stotal+xxltotal;
            strtotal=String(total)+"원";
            document.getElementById("total").innerHTML="TOTAL:"+strtotal;
            document.getElementById("amountIdL").value=0;
            document.getElementById("L_amount").innerHTML=String(int_price)+"원";
            var ul=document.getElementById("ulidL")
            ul.remove()
            mySet.delete('L')
            
        }else if(e=='XL'){
            xltotal=0;
           
            //document.getElementById("total").innerHTML= document.getElementById("total").value;
            total=mtotal+ltotal+xltotal+stotal+xxltotal;
            strtotal=String(total)+"원";
            document.getElementById("total").innerHTML="TOTAL:"+strtotal;
            document.getElementById("amountIdXL").value=0;
            document.getElementById("XL_amount").innerHTML=String(int_price)+"원";
            var ul=document.getElementById("ulidXL")
            ul.remove()
            mySet.delete('XL')
        }
        else if(e=='XXL'){
            xxltotal=0;
            //document.getElementById("total").innerHTML= document.getElementById("total").value;
            total=mtotal+ltotal+xltotal+stotal+xxltotal;
            strtotal=String(total)+"원";
            document.getElementById("total").innerHTML="TOTAL:"+strtotal;
            document.getElementById("amountIdXXL").value=0;
            document.getElementById("XXL_amount").innerHTML=String(int_price)+"원";
            var ul=document.getElementById("ulidXXL")
            ul.remove()
            mySet.delete('XXL')
        }
  }

  function amountprice(e,size){
    
    
    var a =document.getElementById("product_price").value;
    var price=a.split('원');
    var price2=price[0].split(',');
    var price3=price2[0]+price2[1];

    var int_price=parseInt(price3);
    int_price*=e.value;
    

   
    
    
    var str_price=String(int_price)+"원";
    if (size=='S'){
        stotal=int_price;
        document.getElementById("S_amount").innerHTML=str_price;
        //document.getElementById("S_amount").value=int_price;
        
        //document.getElementById("s_amount").value
       
    }else if (size=='M') {
        mtotal=int_price;
        document.getElementById("M_amount").innerHTML=str_price;
        //document.getElementById("M_amount").value=int_price;
    }else if (size=='L'){
        ltotal=int_price;
        document.getElementById("L_amount").innerHTML=str_price;
       // document.getElementById("L_amount").value=int_price;
    }else if(size=='XL'){
        xltotal=int_price;
        document.getElementById("XL_amount").innerHTML=str_price;
        //document.getElementById("XL_amount").value=int_price;
    }else if(size=='XXL'){
        xxltotal=int_price;
        document.getElementById("XXL_amount").innerHTML=str_price;
        //document.getElementById("XL_amount").value=int_price;
    }
    total=mtotal+ltotal+xltotal+stotal+xxltotal;
    strtotal=String(total)+"원";
    

    document.getElementById("total").innerHTML="TOTAL:"+strtotal;
    document.getElementById("total").value=total;
    // alert(String(int_price));
      //document.getElementById("s_amount").in
  }





























  function newadress(){
      document.getElementById("recipient").value=""
      document.getElementById("id").value=""
      document.getElementById("adr").value=""
      
      

  }
  function useradress(){
    document.getElementById("recipient").value=document.getElementById("username").value;
    document.getElementById("id").value=document.getElementById("userid").value;
    document.getElementById("adr").value=document.getElementById("useradr").value;
  }
  function inisispay() {
    var IMP = window.IMP;
    var code = "imp85681890";  // FIXME: 가맹점 식별코드
    IMP.init(code);
    var productname=document.getElementById('productname').value
    var recipient=document.getElementById('recipient').value
    var username=document.getElementById('username').value
    var id=document.getElementById('id').value
    var phonenumber=document.getElementById('phonenumber').value
    var adr=document.getElementById('adr').value
    var total_price=document.getElementById('total_price').value

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
        buyer_addr : adr,
        buyer_postcode : '123-456',
        m_redirect_url : 'https://www.yourdomain.com/payments/complete'
    }, function(rsp) {
        if ( rsp.success ) {
            var msg = '결제가 완료되었습니다.';
            msg += '고유ID : ' + rsp.imp_uid;
            msg += '상점 거래ID : ' + rsp.merchant_uid;
            msg += '결제 금액 : ' + rsp.paid_amount;
            msg += '카드 승인번호 : ' + rsp.apply_num;
        }
        else {
            var msg = '결제에 실패하였습니다. 에러내용 : ' + rsp.error_msg
        }
        alert(msg);
    });
}


function checkstock(e){
    totalstock=0;
    var s=document.getElementById('amountIdS').value;
    var m=document.getElementById('amountIdM').value;
    var l=document.getElementById('amountIdL').value;
    var xl=document.getElementById('amountIdXL').value;
    var xxl=document.getElementById('amountIdXXL').value;
    if (s !=''){
        totalstock+=Number(s);
    }else if (m !=''){
        totalstock+=Number(m);
    }else if (l !=''){
        totalstock+=Number(l);
    }else if(xl !=''){
        totalstock+=Number(xl);
    }
    else if(xxl !=''){
        totalstock+=Number(xxl);
    }
    if(totalstock==0){
        alert("한개이상의 수량을 선택 바랍니다");
        // history.back();
    }
 
    
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

  
  
  
