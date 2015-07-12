function abc(){
$("#register").on('submit',function(event) {
$('#passworderr').html('');
$('#rpassworderr').html('');
$('#countryerr').html('');
$('#errormsg').html('');
var flag=0;
var formData = {
		  'fullname'              : $('input[name=fullname]').val(),
          'username'              : $('input[name=username]').val(),
          'password'             : $('input[name=password]').val(),
          'rpassword'             : $('input[name=rpassword]').val(),
          'country_id'             : $('select[name=country_id]').val(),
        };
        var m=String(formData["password"]).length;
        if(m<=7){
        	flag=1
        	$("#passworderr").append("**Password must be 8 or more characters")
        }
        if(String(formData["password"])!=String(formData["rpassword"])){
        	flag=1
        	$("#rpassworderr").append("**Passwords do not match")
       }
       if(String(formData["country_id"])=="invalid"){
       		flag=1
       		$("#countryerr").append("**Please select your country")
       	}
       	if(flag==0){
$.ajax({
url:"/cgi-bin/registrationchoose.py",
data:formData,
type:"POST",

success:function(data){	
$('#errormsg').html('');
$("#errormsg").append(data)
$("#errormsg").append('Please <a href="http://localhost/loginchoose.html">Click Here</a> to Log in into your account.<br />')
$("#errormsg").append('Please <a href="http://localhost/forgetpasswordchoose.html">Click Here</a> to reset your password.<br />')
}});
}
  event.preventDefault();
});
}
$(document).ready(function(){
$("#register").on("keypress",function(e){
if(e.keyCode===13){
abc();
}

});
$("#reg").on("click",abc);

});
