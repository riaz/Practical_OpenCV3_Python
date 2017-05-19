$(function() {

  var url = "img/";

  function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.queryImg').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
  }

  // on image change
  $("#imgUpload").change(function(e) {

    console.log("searching for related images.....");

    /* use this function to render the query image, adjacent to canvas */
    //readURL(this);

    var image = $('#imgUpload').prop('files')[0];

    var fd = new FormData();

    fd.append("img", image);

    $('#results').empty();

    // ajax request
    $.ajax({
      type: "POST",
      url: "/search",
      contentType: false,
      cache: false,
      processData: false,
      data : fd,
      success: function(result) {
        /* handle success*/
        console.log("Success");

        var data = result.results

        // loop through results, append to dom
        for (i = 0; i < data.length; i++) {

            //add a new row for every 4th image
            if(i % 4 == 0) $("#results").append("<div class='row _row'></div>");

            //append the image to the last child of _row
            $("._row:last-child").append('<div class="col-md-3 res"><a href="'+(url + data[i]['image'])+'"><img src="'+("img/"+ data[i]['image'])+
            '" class="result-img" /></a></div>')
        }
      },
      error: function(error) {
        /* handle error */
        console.log(error);
      }
    });
  });
});
