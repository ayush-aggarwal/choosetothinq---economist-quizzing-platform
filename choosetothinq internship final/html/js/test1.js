function abc(){
$.ajax({
url:"/cgi-bin/test3.py",
data:{query:$("#validate").val().trim()},
type:"POST",
success:function(data){
$("#errormsg").html("");
var json=JSON.parse(data);
var m=json["msg"]
if(m=="Success")
{
}
if(m=="Error")
{
	$("#errormsg").append("Invalid EmailId or Password")
}
},
error:function(err){
console.log(err);
}
});
}
$(document).ready(function(){
$("#validate").on("keypress",function(e){
if(e.keyCode===13){
abc();
}

});
$("#login").on("click",abc);

});
