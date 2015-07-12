function abc()
{
	location.href="http://localhost/freelancer/user.html"
}
function bcd()
{
	localStorage.removeItem("token");
	alert("You have been successfully logged out!!")
	location.href="http://localhost/stylishportfolio/main.html"
}
var em=localStorage.getItem("token")
$.ajax({
url:"/cgi-bin/finishquizchoose.py",
data:{email:em},
type:"POST",
success:function(data){
$("#score").append("<b>"+data+"</b>")
}
});
$(document).ready(function(){
 $("#back").on("click",abc);
 $("#logout").on("click",bcd);
});
