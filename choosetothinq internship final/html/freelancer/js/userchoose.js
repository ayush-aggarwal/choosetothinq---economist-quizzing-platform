function logoff()
{
localStorage.removeItem("token")
alert("You have been logged out !!")
location.href="http://localhost/stylishportfolio/main.html"
}
function abc(){
$("#contactForm").on('submit',function(event) {
var formData={
	'name'              : $('input[name=name]').val(),
	'email'				: $('input[name=email]').val(),
	'message'			: $('textarea[name=message]').val(),
	};
$.ajax({
url:"http://localhost/cgi-bin/feedbackchoose.py",
data:formData,
type:"POST",
success:function(data){
if(String(data)=="Fail"){
$('#success').html("<div class='alert alert-danger'>");
                    $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#success > .alert-danger').append("<strong>Sorry " + formData["name"] + ", it seems that my server is not responding. Please try again later!");
                    $('#success > .alert-danger').append('</div>');
                    //clear all fields
                    $('#contactForm').trigger("reset");
}
if(String(data)=="Success"){
$("#btnSubmit").attr("disabled", false);
                    $('#success').html("<div class='alert alert-success'>");
                    $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#success > .alert-success')
                        .append("<strong>Thank You for your Feedback!! </strong>");
                    $('#success > .alert-success')
                        .append('</div>');

                    //clear all fields
                    $('#contactForm').trigger("reset");
                    }
}
});
	
});
}
$("#name1").html("")
$("#email1").html("")
$("#name").html("")
$("#email").html("")
$("#country1").html("")
$("#totalscore1").html("")
$("#nog1").html("")
$("#avgscore1").html("")
$('#profileimg').css("background","url('https://lh3.googleusercontent.com/-IIA7k0wkU3g/AAAAAAAAAAI/AAAAAAAAADI/cwnx8R-I2Kk/photo.jpg') no-repeat")
var data1=localStorage.getItem("token")
$.ajax({
url:"http://localhost/cgi-bin/userchoose.py",
data:{"email":data1},
type:"POST",
success:function(data){
var json=JSON.parse(data);
var m=json["valid"]
$("#name1").append(""+String(m[0]["name"])+"")
$("#email1").append(""+String(m[0]["email"])+"")
$("#name").attr("value",""+String(m[0]["name"])+"").prop("disabled","disabled")
$("#email").attr("value",""+String(m[0]["email"])+"").prop("disabled","disabled")
$("#country1").append(""+String(m[0]["country"])+"")
$("#totalscore1").append(""+String(m[0]["total_score"])+"")
$("#nog1").append(""+String(m[0]["no_of_games"])+"")
$("#avgscore1").append(""+String(m[0]["average_score"])+"")
var n=json["email"]
localStorage.setItem("em",String(n))
}
});
$(document).ready(function(){
$("#submitfeed").on("click",abc);
$("#logout").on("click",logoff);
});
