function crawl(){
$("#adminupload").on('submit',function(event) {
var formData1={
	'password'              : $('input[name=password]').val(),
	};
$("#uploadfile").attr('disabled','disabled');
$("#pwd").attr('disabled','disabled');
$("#quizf").attr('disabled','disabled');
$('#errormsg1').html('');
$('#errormsg1').append("Please Wait !! Crawling in Progress.......")
$.ajax({
url:"/cgi-bin/crawlchoose.py",
data:formData1,
type:"POST",
beforeSend:function(){
$('#dialog').html('')
$('#dialog').attr("title","Crawling").css("background-color","#223561").css("color","yellow").append('<div class="circle"></div><div class="circle1"></div>').append("<p><b>Crawling in Progress!!</b></p>").dialog({draggable:false,resizable:false,resizable:false,show:"fade in",modal:true,});
},
success:function(data){	
$('#dialog').dialog('close');
$('#errormsg1').html('');
var json=JSON.parse(data);
	if(Object.keys(json)[0]=="invalid")
	{
		var m=json["invalid"]
		$("#errormsg1").append(""+m[0]["answer"]+"");	
	}
	if(Object.keys(json)[0]=="valid")
	{
		$('#errormsg1').html('');
		var m=json["valid"]
		$('#dialog').html('')
		$('#dialog').attr("title","Success").css("background-color","").css("color","black").append("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-_hhG8UcUyhNesQ0BCvrUOjYL-O6g7GHbgxohA7KrSlyGGgKw' style='display:block;margin-left:auto;margin-right:auto;'></img>").append('<p style="text-align:center;"><b>'+m[0]["answer"]+'</b></p>').dialog({ buttons: {'Ok':function(){
			$(this).dialog('close');  
			}},closeOnEscape:true, draggable:false,resizable:false,show:"fade",modal:true,});		
	}
}
});
event.preventDefault();
});
}
function abc(){
$("#adminupload").on('submit',function(event) {
var formData = {
		  'password'              : $('input[name=password]').val(),
          'quizfile'              : $('input[type=file]').val(),
          };
$("#crawlques").attr('disabled','disabled')
$("#pwd").attr('disabled','disabled');
$("#quizf").attr('disabled','disabled');
$.ajax({
url:"/cgi-bin/adminaccesschoose.py",
data:formData,
type:"POST",
beforeSend:function(){
$('#dialog').html('')
$('#dialog').attr("title","Uploading").css("background-color","#223561").css("color","yellow").append('<div class="circle"></div><div class="circle1"></div>').append("<p><b>Uploading in Progress!!</b></p>").dialog({draggable:false,resizable:false,resizable:false,show:"fade in",modal:true,});
},
success:function(data){	
$('#dialog').dialog('close');
$('#errormsg').html('');
var json=JSON.parse(data);
	if(Object.keys(json)[0]=="invalid")
	{
		var m=json["invalid"]
		$("#errormsg").append(""+m[0]["answer"]+"");	
	}
	if(Object.keys(json)[0]=="valid")
	{
		var m=json["valid"]
		$('#dialog').html('')
		$('#dialog').attr("title","Success").css("background-color","").css("color","black").append("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-_hhG8UcUyhNesQ0BCvrUOjYL-O6g7GHbgxohA7KrSlyGGgKw' style='display:block;margin-left:auto;margin-right:auto;'></img>").append('<p style="text-align:center;"><b>'+m[0]["answer"]+'</b></p>').dialog({ buttons: {'Ok':function(){
			$(this).dialog('close');  
			}},closeOnEscape:true, draggable:false,resizable:false,show:"fade",modal:true,});	
	}
}
});
event.preventDefault();
});
}
$(document).ready(function(){
$("#uploadfile").on("click",abc);
$("#crawlques").on("click",crawl);
});
