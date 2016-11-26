
$(document).ready(function(){

function macAdd(val){
if (/[^\w-]|_/.test(val))
{alert("invalid form only alpanumeric and -")
return val}


val=val.replace(/[^\w-]|_/g,'')
val=val.replace(/(\w{2})([^-])/g,'$1'+'-'+'$2')
val=val.replace(/-$/,'')
return val
}

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
		title: "Mac Address",
		resizable: false,
		modal: true,
		height: "180",
		width: "300",
		position: { my: "left bottom", at: "right top", of: elem},
			buttons: {
				"Add": function() {
				    var mac=$('#mac').val();
					$elem.data("note",mac );
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
					mac=$elem.data("note");
					if (!mac){
					    mac ="00:00:00:00:00:00"
					}
					console.log(mac);
					var inputs = '';
                                 inputs+='<div class="form-group">';
                                 inputs+='  <input type="text" class="form-control" id="mac"  value='+mac+' ></div>';
                                $(this).html(inputs);
				},

				});
				}
		});
        var mapid= $('#mapid').val();
        var jsonmarkers="";
        $.get( "/maps/getmarkers/"+mapid+"/", function( data ) {
           var json = JSON.parse(data);
           $img.imgNotes("import",json );
        });

        //$img.imgNotes("import",jsonmarkers);
        //console.log(jsonmarkers);
//		$img.imgNotes("import", [	{x: "0.5", y:"0.5", note:"AFL Grand Final Trophy"},
//									{x: "0.322", y:"0.269", note: "Brisbane Lions Flag"},
//									{x: "0.824", y: "0.593", note: "Fluffy microphone"}]);
		var $toggle = $("#toggleEdit");

		if ($img.imgNotes("option","canEdit")) {
			$toggle.text("View");
		} else {
			$toggle.text("Edit");
		}
		$toggle.on("click", function() {
									var $this = $(this);
									if ($this.text()=="Edit") {
										$this.text("View");
										$img.imgNotes("option", "canEdit", true);
									} else {
										$this.text('Edit');
										$img.imgNotes('option', 'canEdit', false);
									}
		});
		var $export = $("#save");
		$export.on("click", function() {
		    save();
		});
		var $clear = $("#clear");
		$clear.on("click", function() {
									$img.imgNotes('clear');
		});
		var $print = $("#print");
		$print.on("click", function() {
									$(".viewport").printThis();
		});

    $('#showBuldingModal').click(function(){
       $('#addBuilingModal').modal('show');
    });
  $('#building-save-btn').click(function(){
       var bname = $('.addmap #building-name').val();
       $.ajax({
       url: "/maps/addbuilding/",
       method: "POST",
       data: { name : bname },
       }).done(function() {
           $('#addBuilingModal').modal('hide');
           location.reload();
       });
       //
  });
   ///floor
   $('#showfloorModal').click(function(){
       $('#addFloorModal').modal('show');
    });

    $('#floor-save-btn').click(function(){
       var fname = $('.addmap #id_name').val();
       var building_id=$('.addmap #id_building').val();
       $.ajax({
       url: "/maps/addfloor/",
       method: "POST",
       data: { name : fname, building:building_id },
       }).done(function() {
           $('#addFloorModal').modal('hide');
           location.reload();
       });

  });

  var length = 1;
$("#mac").focusin(function (evt) {

    $(this).keypress(function () {
        var content = $(this).val();
        var content1 = content.replace(/\:/g, '');
        length = content1.length;
        if(((length % 2) == 0) && length < 10 && length > 1){
            $('#mac').val($('#mac').val() + ':');
        }
    });
});
});
