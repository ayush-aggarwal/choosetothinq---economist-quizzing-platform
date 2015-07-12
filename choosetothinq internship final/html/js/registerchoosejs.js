function abc(){
var form = document.getElementById('register');
form.submit()
alert()
}
$(document).ready(function(){
$("#register").on("keypress",function(e){
if(e.keyCode===13){
abc();
}

});
$("#reg").on("click",abc);

});
