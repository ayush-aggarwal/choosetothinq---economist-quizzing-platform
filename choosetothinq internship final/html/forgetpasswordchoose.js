function abc1()
{
$("#errormsg").html("");
var formData1={
	'username'              : $('input[name=username]').val(),
	'password'              : $('input[name=password]').val(),
	'rpassword'              : $('input[name=rpassword]').val(),
	};
if(String(formData1["password"])!=String(formData1["rpassword"])){
	$('#errormsg').append("** Passwords Do Not Match");
}
if(String(formData1["password"])==String(formData1["rpassword"])){
$.ajax({
url:"/cgi-bin/forgetpasswordchoose1.py",
data:formData1,
type:"POST",
success:function(data){
var json=JSON.parse(data);
$("#errormsg").html("");
if(Object.keys(json)[0]=="invalid"){
var m=json["invalid"]
$('#errormsg').append(""+m[0]["answer"]+"")
}
if(Object.keys(json)[0]=="valid"){
$('#errormsg').append("Your Request Has been Received.")
$('#errormsg').append("Your password will be resetted in a short time!!")
$("#rpasswd").prop("disabled",true);
$("#passwd").prop("disabled",true);
}
}
});
}
event.preventDefault();
}
function abc(){
$("#forgetpass").on('submit',function(event) {
var formData={
	'username'              : $('input[name=username]').val()
	};
$.ajax({
url:"/cgi-bin/forgetpasswordchoose.py",
data:formData,
type:"POST",
success:function(data){
$("#errormsg").html("");
$("#pass").html("");
$("#rpass").html("");
var json=JSON.parse(data);	
if(Object.keys(json)[0]=="invalid")
	{
		$("#errormsg").append("**Email-Id Not Registered");	
	}
if(Object.keys(json)[0]=="valid")
	{
		$("#submitbtn").html("");
		var m=json["valid"]
		$("#validemail").prop("disabled",true);
		$('#pass').append('<span class="input-group-addon"><i class="fa fa-lock"> New Password</i></span><input type="password" name="password" placeholder="Password" class="form-control" id="passwd" required>')
		$('#rpass').append('<span class="input-group-addon"><i class="fa fa-lock"> Confirm Password</i></span><input type="password" name="rpassword" placeholder="Password" class="form-control" id="rpasswd" required>')
		$('#submitbtn').append('<button class="btn btn-lg btn-success btn-block" type="submit" id="submitpass">Submit Password</button>')
		$('#forgetpass').attr('id','verifypass')
		$(document).ready(function(){
		$("#verifypass").on("keypress",function(e){
		if(e.keyCode===13){
		abc1();
		}

		});
		$("#submitpass").on("click",abc1);

		});
			}
		}
		});
event.preventDefault();
});
}
$(document).ready(function(){
$("#forgetpass").on("keypress",function(e){
if(e.keyCode===13){
abc();
}

});
$("#submitemail").on("click",abc);

});
