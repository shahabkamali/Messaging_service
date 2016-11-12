
$(document).ready(function(){
    $("#mapviewer").imgViewer();
    $("#mapviewer").imgNotes({canEdit: true});

    var $img = $("#mapviewer").imgNotes({	onAdd: function() {
				this.options.vAll = "bottom";
				this.options.hAll = "middle";
				elem = $(document.createElement('div'))
				       .css({width:'27px', height:'40px','text-align':'center',color:'#fff','font-weight':'bold', 'font-size':'14px'})
				       .append($('<p>'+this.noteCount+'</p>').css({'z-index':1, position:'relative', top:'-8px'}))
				       .prepend($('<img>',{src: '/static/dist/img/MapMarker_Marker_Inside_Pink.png', width:'40px', height:'40px'}).css({position:'absolute', top:'0px', left:'0px'}));
				return elem;
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
       });
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
       });
  });
});
