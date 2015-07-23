$( document ).ready(function() {
	$("#deploy-form").on("submit",function() {
	  var url = "path/to/post.soemthing";
	  console.log("deploy!");
	  $.ajax({
	    url: url, 
	    type: 'post',
	    data: {  
	      repo: 'github.com/artburkart/colored_pages',
	        branch: 'red',
	        subdomain: 'whatever'
	    },
	    success: function(data) {
	      alert(data);
	    }
	 });
	});
}); 