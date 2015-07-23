$( document ).ready(function() {
  $.fn.serializeObject = function()
  {
      var o = {};
      var a = this.serializeArray();
      $.each(a, function() {
          if (o[this.name] !== undefined) {
              if (!o[this.name].push) {
                  o[this.name] = [o[this.name]];
              }
              o[this.name].push(this.value || '');
          } else {
              o[this.name] = this.value || '';
          }
      });
      return o;
  };
  $("#deploy-form").on("submit",function(e) {
    e.preventDefault();
    var url = "/api";
    var form = $("#deploy-form").serializeObject();
    console.log(form);
    $.ajax({
      url: url, 
      type: 'post',
      data: JSON.stringify(form),
      contentType: "application/json",
      datatype : "json",
      success: function(data) {
        alert("You've Deployed!");
      }
   });
  });
}); 