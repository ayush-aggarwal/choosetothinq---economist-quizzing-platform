function abc()
{
$("#validate").on('submit',function(event) {
var formData={
		  'username'              : $('input[name=username]').val(),
          'password'             : $('input[name=password]').val(),
          };
$.ajax({
url:"/cgi-bin/loginchoose.py",
data:formData,
type:"POST",

success:function(data){	
var json=JSON.parse(data);
	if(Object.keys(json)[0]=="invalid")
	{
	$("#errormsg").html("")
	$("#errormsg").append("Authentication Failed!!Try Again!!")
	}
	if(Object.keys(json)[0]=="valid")
	{
	var m=json["valid"]
	if(String(m[0]["answer"])=="Administrator")
	{
		location.href="http://localhost/adminaccesschoose.html"
	}
	if(String(m[0]["answer"])=="Authorised")
	{ 
		localStorage.setItem('token',m[0]["email"])
		location.href="http://localhost/freelancer/user.html"	
	}
	}
}
});
event.preventDefault();
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

