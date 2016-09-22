
$(document).ready(function(){

$(".imgmap").click(function(){

$('<div  class="dragg-able"> <img src="/static/dist/img/MapMarker_Marker_Inside_Pink.png"></div>').appendTo(".imgmap");

$( ".dragg-able" ).draggable();

})

});
