$(function(){

	$.ajax({
	    type: "GET",
	    url: "/jqueryserver/",
	   success: function(data){
	         alert(data);         
	     }
	});

});