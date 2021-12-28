
function changeActive(id){
    var body = document.body.id;
    var itemId = "item-" + body;
    var element = document.getElementById(itemId);
    // window.alert(element.textContent);
    element.classList.add("active");
}

function searchrecords(){
    var input,tr,td,filter,table,j,txtdata;
    input=document.getElementById("company-search").value;
    // window.alert(String(input))
   
    filter=input.value.toUpperCase();
    table=document.getElementsByClassName("content-row");
    tr=table.getElementsByTagName("tr");
    document.write(table);
    for(j=0;j<tr.length;j++)
    {
    td=tr[j].getElementsByTagName("td")[1];
    if(td)
    {
    txtdata=td.innerText;
    if(txtdata.toUpperCase().indexOf(filter)>-1){
        tr[j].style.display="";
    }
    else{
        tr[j].style.display="none";
    }
    }
    }
    }

var url = window.location.href;
var a = url.split('/');
const startingMinutes = a[7];

let time = startingMinutes * 60;

setInterval(updateCountdown,1000);

function updateCountdown(){
    const minutes = Math.floor(time/60);
    let seconds = time % 60;
    document.getElementById("time-lefts").innerHTML = `${minutes}: ${seconds}`;
    time--;
    if (time == 0){
        document.getElementById("quiz-submit").click();
    }
 }

// var queryString = window.location.href;
// console.log(queryString);
// var a = queryString.split('/')
// console.log(a[6])
// var timeleft = a[7]*60;
// var downloadTimer = setInterval(function(){
//   if(timeleft <= 0){
//     clearInterval(downloadTimer);
//     document.getElementById("time-lefts").innerHTML = "Finished";
//   } else {
//     document.getElementById("time-lefts").innerHTML = timeleft;
//   }
//   timeleft -= 1;
// }, 1000);





var popup;

var url = window.location.href;

function openPopup(a)

{
console.log(a)
popup = window.open(a,"quiz", "height=2160,width=1980")
}

function closePopup()

{

popup.close();

}

