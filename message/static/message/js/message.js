$(document).ready(function(){

function save(){
var notes = $img.imgNotes('export');
			var jsonnotes='[';
			$.each(notes, function(index, item) {
			    jsonnotes+='{"x":"'+item.x+'","y":"'+item.y+'","note":"'+item.note+'"},'
			});
			jsonnotes = jsonnotes.substring(0, jsonnotes.length - 1);
			jsonnotes+=']'
			console.log(jsonnotes);
            var mapid= $('#mapid').val();
			var request = $.ajax({
              url: "/maps/saveMarkers/"+mapid+"/",
              method: "POST",
              data: {"json":jsonnotes},
            });
            request.done(function( msg ) {
              console.log("ok");
              });

}
    $("#mapviewer").imgViewer();
    $("#mapviewer").imgNotes({canEdit: true});

var $img = $("#mapviewer").imgNotes({
	onEdit: function(ev, elem) {
		var $elem = $(elem);
		$('#NoteDialog').remove();
	    return $('<div id="NoteDialog"></div>').dialog({
		title: "Define LED",
		resizable: false,
		modal: true,
		height: "220",
		width: "300",
		position: { my: "left bottom", at: "right top", of: elem},
			buttons: {
				"Add": function() {
				    var name=$('#name').val();
				    var mac=$('#mac').val();
					$elem.data("note",name+"</br>"+mac );
					save();
					$(this).dialog("close");
				},
				"Delete": function() {
					$elem.trigger("remove");
					save();
					$(this).dialog("close");
				},
                "Cancel": function() {
					$(this).dialog("close");
				},
				},
				open: function(event, ui) {
					$(this).css("overflow", "hidden");
					var mac=""
					var name=""
					try{
					    var note=$elem.data("note").split('</br>');
					    name=note[0];
					    mac=note[1];
					}
					catch(e)
					{
					    name="";
					    mac="";
					}

					console.log(mac);
					var inputs = '';
					    inputs+='<div class="form-group">';
                        inputs+='<input type="text" class="form-control" id="name" placeholder="Name" value='+name+'  ></div>';
                        inputs+='<div class="form-group">';
                        inputs+='<input type="text" class="form-control" id="mac" placeholder="Mac Address" value='+mac+' ></div>';
                        $(this).html(inputs);
				},

				});
				}
		});
        var mapid= $('#map_id').val();
        var mapname=$("#map_id option[value='"+mapid+"']").text();
        console.log(mapname);
        var jsonmarkers="";
        $img.imgNotes('option', 'canEdit', false);
        $("#mapviewer").imgViewer("option", "zoomable", false);
            $(window).keydown(function(e){
        if (e.altKey){console.log('down')}
            $("#mapviewer").imgViewer("option", "zoomable", true);
    });
    $(window).keyup(function(e){
        $("#mapviewer").imgViewer("option", "zoomable", false);
        if (e.altKey)
            console.log('up')
    });

    $("#show-map").click(function(){

    $img.imgNotes('clear');
    var map_id=$("#map_id").val();
    if(map_id){
      $.getJSON("/messages/getmapaddress/"+map_id+"/",function(json){
        console.log(json);
        var jsonobj = JSON.parse(json);
        console.log(jsonobj);
        var srcstr="/media/"+jsonobj[0].fields.picture;
       console.log($("#mapviewer").prop( "src", srcstr));
//        $("#mapviewer").attr("src",srcstr)
        var mapid= jsonobj[0].pk;
        var jsonmarkers="";
        $.get( "/maps/getmarkers/"+mapid+"/", function( data ) {
           var json = JSON.parse(data);
           $img.imgNotes("import",json );
        });
      });
    }
});

});

function update(picker) {
        $('#id_r').val(Math.round(picker.rgb[0]));
        $('#id_g').val(Math.round(picker.rgb[1]));
        $('#id_b').val(Math.round(picker.rgb[2]));
}

function building_change(){
    builidng_id=$('#building_select').val();
    $.getJSON("/messages/getfloors/"+builidng_id+"/",function(json){
      var jsonobj = JSON.parse(json);
      var itemlist="";
      for(var i=0;i<jsonobj.length;i++)
      {
          itemlist+="<option value='"+jsonobj[i].pk+"'>"+jsonobj[i].fields.name+"</option>";
      }
      $("#floor_id").html(itemlist);
      $("#map_id").html("");
      floor_change();
});
}

function floor_change(){
    floor_id=$('#floor_id').val();
    if(floor_id){
        $.getJSON("/messages/getmaps/"+floor_id+"/",function(json){
           var jsonobj = JSON.parse(json);
           var itemlist="";
           for(var i=0;i<jsonobj.length;i++)
           {
               itemlist+="<option value='"+jsonobj[i].pk+"'>"+jsonobj[i].fields.mapname+"</option>";
           }
          $("#map_id").html(itemlist);
        });
    }
}


