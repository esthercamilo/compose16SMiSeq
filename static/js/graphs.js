var modalDiv = $("#modal-div-report");

$(".open-modal-report").on("click", function() {
  $.ajax({
    url: $(this).attr("data-url"),
    success: function(data) {
      modalDiv.html(data);
      $("#myEdit").modal();
    }
  });
});