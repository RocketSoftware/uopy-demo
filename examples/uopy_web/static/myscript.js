function getData() {
    var user = user
    $.post( "/postmethod", {
      user: JSON.stringify(user)
    }, function(err, req, resp){
      window.location.href = "/simple_chart/"+resp["responseJSON"]["user"];  
    });
  }

  $( "#clearButton" ).click(function(){
    clearCanvas();
  });

  $( "#sendButton" ).click(function(){
    getData();
  });
