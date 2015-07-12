function finishquiz(email){
	location.href="http://localhost/finishquizchoose.html"
}
function check(u,v,email){
$.ajax({
url:"/cgi-bin/quizanswerchoose.py",
data:{id:u,ans:v,email:email},
type:"POST",
success:function(data){
var json=JSON.parse(data);
if(Object.keys(json)[0]=="invalid")
{
$("#cont").css("background-color","#FF9E9E");
var o=json["invalid"]
$('#dialog').html('')
$('#dialog').attr("title","Answer").append("<img src='https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTnqGnNqxjEzPil_znpCobn8FQJKOx7itTuNv8Qo05r404Gi6Cn' style='display:block;margin-left:auto;margin-right:auto;'></img>").append('<p>Sorry!! Your answer was incorrect!!</p><p>Your answer:- <b>'+v+'</b></p><p>Correct Answer is:- <b>'+o[0]["answer"]+'</b></p>').dialog({ buttons: {'Ok':function(){
$(this).dialog('close');
}},closeOnEscape:true, draggable:false,resizable:false,show:"bounce",modal:true,});
}
if(Object.keys(json)[0]=="valid")
{
$("#cont").css("background-color","#9EFFA4");
$('#dialog').html('')
$('#dialog').attr("title","Answer").append("<img src='https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTmt2Oc1n0HpNj8o6AplubpmSp1qnTiPtl5-xkj8CgLYu8lkGlH8A' style='display:block;margin-left:auto;margin-right:auto;'></img>").append('<p><b>Congratulations!! Your Answer is correct!! You got 10 points !!</b></p>').dialog({ buttons: {'Ok':function(){
$(this).dialog('close'); 
}},closeOnEscape:true, draggable:false,resizable:false,show:"bounce",modal:true,});
}
}
});
if(u==9){
setTimeout(function() { 
  window.onbeforeunload=null;
  finishquiz(email)
}, 5000);
}
}
function abc(d)
{
var em=localStorage.getItem("token")
if(d<10){
$("#no").html("");
$("#no").append(d)
$.ajax({
url:"/cgi-bin/quizquestionchoose.py",
data:{id:d},
type:"POST",
success:function(data){
	$("#curdate").html("")
	$('#ques').html("")
	$('#opt1').html("")
	$('#opt2').html("")
	$('#opt3').html("")
	$('#opt4').html("")
	$('#submitbtn').html("")
	var json=JSON.parse(data);
	var m=json["valid"]
	$("#curdate").append("<b>"+m[0]["date"]+"</b>")
	$("#ques").append(""+m[0]["question"]+"")
	$("#opt1").append('<input type="radio" name="answer" value='+String(m[0]["opt1"]).replace(/\ /g,"_")+'> '+m[0]["opt1"]+'')
	$("#opt2").append('<input type="radio" name="answer" value='+String(m[0]["opt2"]).replace(/\ /g,"_")+'> '+m[0]["opt2"]+'')
	$("#opt3").append('<input type="radio" name="answer" value='+String(m[0]["opt3"]).replace(/\ /g,"_")+'> '+m[0]["opt3"]+'')
	$("#opt4").append('<input type="radio" name="answer" value='+String(m[0]["opt4"]).replace(/\ /g,"_")+'> '+m[0]["opt4"]+'')
	$("#submitbtn").append('<button class="btn btn-lg btn-primary" style="margin-left:auto;margin-right:auto;display:block;margin-bottom:0%" type="submit" id="checkans" disabled="true">Submit</button>')
	$("#opt1,#opt2,#opt3,#opt4").click(function(){
	$("#checkans").removeAttr("disabled");
	});
	$("#checkans").on("click",function(e){
	var ans=$('input[type="radio"][name="answer"]:checked').val();
	ans=String(ans).replace(/\_/g," ");
	if(d==9)
	{
	$("#msg").append("Saving Your Score.........");
	}
	check(d,ans,em);
	d=d+1;
	localStorage.setItem("no",d)
	abc(d);
	});
}
});
}
	event.preventDefault();
}
window.onbeforeunload = function (e) {
return "Leave the quiz. Closing/Refreshing will cause your score not to be recorded"
}
$(window).on("unload",function(){
var em=localStorage.getItem("token")
var n=localStorage.getItem("no")
if(n<10)
{
$.ajax({
url:"/cgi-bin/leavebetweenchoose.py",
data:{"email":em},
type:"POST",
async: false,
success:function(data){
console.log(data)
}
});
}
});
$(document).ready(function(){
$.ajax({
url:"/cgi-bin/top20playerchoose.py",
type:"POST",
success:function(data){
var json=JSON.parse(data);
var fd=json["top20"]
$.each(fd,function(value){
$("#contable").append('<tr style="border:2px solid #000000;"><td>'+fd[value][0]+'</td><td>'+fd[value][1]+'</td><td>'+fd[value][2]+'</td><td>'+fd[value][3]+'</td><td>'+fd[value][4]+'</td><td>'+fd[value][5]+'</td></tr>')
});
}
});
var m=1
abc(m);
});
