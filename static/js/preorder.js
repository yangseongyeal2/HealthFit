
mtotal=0
stotal=0
ltotal=0
xltotal=0
xxltotal=0;
let mySet = new Set();

document.addEventListener('keydown', function(event) {
    if (event.keyCode === 13) {
       event.preventDefault();
       if( document.getElementById("amountIdS")){
        document.getElementById("amountIdS").blur()
       }
       if( document.getElementById("amountIdM")){
        document.getElementById("amountIdM").blur()
       }
       if(document.getElementById("amountIdL")) {
        document.getElementById("amountIdL").blur()
       }
       if( document.getElementById("amountIdXL")){
        document.getElementById("amountIdXL").blur()
       }
       if( document.getElementById("amountIdXXL")){
        document.getElementById("amountIdXXL").blur()
       }
    };
  },
   true);

//   $('input[type="text"]').keydown(function() {
//     if (event.keyCode === 13) {
//       //event.preventDefault();
//       alert("앤터키눌림")
//     };
//   });

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
    //let productPrice=document.getElementById(`product_price`).value+"원";
    let productPrice=comma(document.getElementById(`product_price`).value)+"원";
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
       
        //strtotal=String(total)+"원";
        strtotal=comma(total)+"원"
      
        document.getElementById("total").innerHTML="TOTAL:"+strtotal;
        document.getElementById('amountIdS').value='1';
    }
    if (e.value=="M"){
        paintOption(e);
       // document.getElementById("option_ul_m").style.display="block";
        // $("#option_ul_m").show();

        mtotal=int_price
        total=mtotal+ltotal+xltotal+stotal+xxltotal;
        //strtotal=String(total)+"원";
        strtotal=comma(total)+"원"
        document.getElementById("total").innerHTML="TOTAL:"+strtotal;
        document.getElementById('amountIdM').value='1';
    }
    if (e.value=="L"){
        paintOption(e);
       // document.getElementById("option_ul_l").style.display="block";
        // $("#option_ul_l").show();
        ltotal=int_price
        total=mtotal+ltotal+xltotal+stotal+xxltotal;
        //strtotal=String(total)+"원";
        strtotal=comma(total)+"원"
        document.getElementById("total").innerHTML="TOTAL:"+strtotal;
        document.getElementById('amountIdL').value='1';

    }
    if (e.value=="XL"){
        paintOption(e);

        // $("#option_ul_xl").show();
        xltotal=int_price
        total=mtotal+ltotal+xltotal+stotal+xxltotal;
        //strtotal=String(total)+"원";
        strtotal=comma(total)+"원"
        document.getElementById("total").innerHTML="TOTAL:"+strtotal;
        document.getElementById('amountIdXL').value='1';
    }
    if (e.value=="XXL"){
        paintOption(e);

        // $("#option_ul_xl").show();
        xxltotal=int_price
        total=mtotal+ltotal+xltotal+stotal+xxltotal;
        //strtotal=String(total)+"원";
        strtotal=comma(total)+"원"
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
            strtotal=comma(total)+"원"
            //strtotal=String(total)+"원";
            document.getElementById("total").innerHTML="TOTAL:"+strtotal;
            //document.getElementById("amountIdS").value=0;
            //document.getElementById("S_amount").innerHTML=String(int_price)+"원";
            var ul=document.getElementById("ulidS")
            ul.remove()
            mySet.delete('S')
        }else if (e=='M') {
            mtotal=0
            $("#option_ul_m").hide();
           
            //document.getElementById("total").innerHTML= document.getElementById("total").value;
            total=mtotal+ltotal+xltotal+stotal+xxltotal;
            //strtotal=String(total)+"원";
            strtotal=comma(total)+"원"
            document.getElementById("total").innerHTML="TOTAL:"+strtotal;
            //document.getElementById("amountIdM").value=0;
            //document.getElementById("M_amount").innerHTML=String(int_price)+"원";
            var ul=document.getElementById("ulidM")
            ul.remove()
            mySet.delete('M')
        }else if (e=='L'){
            ltotal=0;
            //document.getElementById("total").innerHTML= document.getElementById("total").value;
            total=mtotal+ltotal+xltotal+stotal+xxltotal;
            //strtotal=String(total)+"원";
            strtotal=comma(total)+"원"
            document.getElementById("total").innerHTML="TOTAL:"+strtotal;
            //document.getElementById("amountIdL").value=0;
            //document.getElementById("L_amount").innerHTML=String(int_price)+"원";
            var ul=document.getElementById("ulidL")
            ul.remove()
            mySet.delete('L')
            
        }else if(e=='XL'){
            xltotal=0;
           
            //document.getElementById("total").innerHTML= document.getElementById("total").value;
            total=mtotal+ltotal+xltotal+stotal+xxltotal;
            //strtotal=String(total)+"원";
            strtotal=comma(total)+"원"
            document.getElementById("total").innerHTML="TOTAL:"+strtotal;
            //document.getElementById("amountIdXL").value=0;
            //document.getElementById("XL_amount").innerHTML=String(int_price)+"원";
            var ul=document.getElementById("ulidXL")
            ul.remove()
            mySet.delete('XL')
        }
        else if(e=='XXL'){
            xxltotal=0;
            //document.getElementById("total").innerHTML= document.getElementById("total").value;
            total=mtotal+ltotal+xltotal+stotal+xxltotal;
            //strtotal=String(total)+"원";
            strtotal=comma(total)+"원"
            document.getElementById("total").innerHTML="TOTAL:"+strtotal;
            //document.getElementById("amountIdXXL").value=0;
           // document.getElementById("XXL_amount").innerHTML=String(int_price)+"원";
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
    

   
    
    
    //var str_price=String(int_price)+"원";
    var str_price=comma(int_price)+"원";
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
    //strtotal=String(total)+"원";
    strtotal=comma(total)+"원";
    

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
 


function checkstock(e){
    totalstock=0;
    let s=''
    var m=''
    var l=''
    var xl=''
    var xxl=''
    if (document.getElementById('amountIdS') ){
        s=document.getElementById('amountIdS').value;
    }
    if (document.getElementById('amountIdM') ){
        m=document.getElementById('amountIdM').value;
    }
    if (document.getElementById('amountIdL') ){
        l=document.getElementById('amountIdL').value;
    }
    if (document.getElementById('amountIdXL') ){
        xl=document.getElementById('amountIdXL').value;
    }
    if (document.getElementById('amountIdXXL') ){
        xxl=document.getElementById('amountIdXXL').value;
    }
       
    // var m=document.getElementById('amountIdM').value;
    // var l=document.getElementById('amountIdL').value;
    // var xl=document.getElementById('amountIdXL').value;
    // var xxl=document.getElementById('amountIdXXL').value;
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



function comma(num){
    var len, point, str; 
       
    num = num + ""; 
    point = num.length % 3 ;
    len = num.length; 
   
    str = num.substring(0, point); 
    while (point < len) { 
        if (str != "") str += ","; 
        str += num.substring(point, point + 3); 
        point += 3; 
    } 
     
    return str;
 
}



  
  
  
