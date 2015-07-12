function abc(){
$("#forgetpassverify").on('submit',function(event) {
alert()
event.preventDefault();
});
}
$(document).ready(function(){
$("#forgetpassverify").on("keypress",function(e){
if(e.keyCode===13){
abc();
}

});
$("#resetpass").on("click",abc);

});
