function back(){
	location.href="http://localhost/freelancer/user.html"
}
function abc(){
var m=localStorage.getItem("token")
$.ajax({
url:"/cgi-bin/startquizchoose.py",
data:{username:m},
type:"POST",
success:function(data){
	$("#errormsg").html("");
	var json=JSON.parse(data);
	if(Object.keys(json)[0]=="invalid")
	{
		$("#errormsg").append("Sorry !! Server Problem !! Will get back soon....");	
	}
	if(Object.keys(json)[0]=="valid")
	{
		location.href='http://localhost/quizchoose.html'
	}
},
error:function(err){
console.log(err);
}
});
}
var em=localStorage.getItem("em")
localStorage.removeItem("em")
$("#validemail").attr("value",String(em)).attr("disabled","disabled")
$(document).ready(function(){
$("#back").on("click",back)
$("#validemail").on("keypress",function(e){
if(e.keyCode===13){
abc();
}

});
$("#startquiz").on("click",abc);

});
