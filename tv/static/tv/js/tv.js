

$(document).ready(function(){
    var mapviewer="<img id='mapviewer' width='100%' height='100%' alt='map'>";
    $(".image-container").append(mapviewer);
    $("#mapviewer").imgViewer();
    $("#mapviewer").imgNotes({canEdit: true});
var $img = $("#mapviewer").imgNotes({
	onEdit: function(ev, elem) {
		var $elem = $(elem);
		$('#NoteDialog').remove();
	    return $('<div id="NoteDialog"></div>').dialog({
		title: "select speakers",
		resizable: false,
		modal: true,
		height: "220",
		width: "300",
		position: { my: "left bottom", at: "right top", of: elem},
			buttons: {
				"Add": function() {
				    var name=$('#name').val();
				    var building=$('#building_select option:selected').text();
				    var floor=$('#floor_id option:selected').text();
				    var map=$('#map_id option:selected').text();
				    var mac=$('#mac').val();
				    $('#markerlist tr:last').after('<tr><td class="name">'+building+'_'+floor+'_'+map+'_'+name+'</td><td class="mac">'+mac+'</td><td><button id="delete-row"  class="btn btn-danger delete-row">Delete</button></td></tr>');

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
					    $elem.trigger("remove");
					    $(this).dialog("close");
					    name="";
					    mac="";
					}
					var inputs = '';
					    inputs+='<div class="form-group">';
                        inputs+='<input type="text" class="form-control" id="name" placeholder="Name" readonly value='+name+'  ></div>';
                        inputs+='<div class="form-group">';
                        inputs+='<input type="text" class="form-control" id="mac" placeholder="Mac Address" readonly value='+mac+' ></div>';
                        $(this).html(inputs);
				},

				});
				}
		});
        var mapid= $('#map_id').val();
        var mapname=$("#map_id option[value='"+mapid+"']").text();
        var jsonmarkers="";
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
        var jsonobj = JSON.parse(json);
        console.log(jsonobj);
        var srcstr="/media/"+jsonobj[0].fields.picture;
       $("#mapviewer").prop( "src", srcstr);
        var mapid= jsonobj[0].pk;
        var jsonmarkers="";
        $.get( "/maps/getmarkers/"+mapid+"/", function( data ) {
           var json = JSON.parse(data);
           var markerjson=[];
           console.log(json);
           jQuery.each(json, function() {
              var type = this.note.split("</br>")[2];
              console.log(type);
              if (type == "TV"){
                  markerjson.push(this);
              }
           });
           $img.imgNotes("import",markerjson );
        });
      });
    }
    else{
        $("#mapviewer").removeAttr( "src");
    }
});

  ///clear image from markers
  $("#floor_id").change(function(){
      $img.imgNotes('clear');
  });
  $("#building_select").change(function(){
      $img.imgNotes('clear');
  });
  $("#map_id").change(function(){
      $img.imgNotes('clear');
      $("#mapviewer").removeAttr( "src");
  });
  $('#save-list').click(function(){
    var list_name=$('#list-name').val();
    $('#list-name').val("");
    if (!list_name){
      alert("please set name");
      return;
    }
    var list=get_list();
    console.log(list);
    $.ajax({
    method: "POST",
    url: "/tvs/savelist/",
    data: { "jsonlist" : list,"listname":list_name },
    dataType: "json",
    success: function(result){
      console.log(result);
  }})
    $('#save-modal').modal('hide');
  });
       ///delete selected list
  $('#delete-selected-list').click(function(){
      var list_name=$('#select_saved_message option:selected').text();
      $.ajax({
      method: "POST",
      url: "/speakers/deletelist/",
      data: { "listname":list_name },
      success: function(result){
        $("#select_saved_message option:selected").remove();
      }});
  });
  //load list
  $('#loadmessage').click(function(){
      $("#markerlist").find("tr:gt(0)").remove();
      var list=$('#select_saved_message').val();
      var jsonlist=JSON.parse(list);
      console.log(jsonlist);
      jQuery.each(jsonlist, function(i,val) {
         $('#markerlist tr:last').after('<tr><td class="name">'+val.name+'</td><td class="mac">'+val.mac+'</td><td><button id="delete-row"  class="btn btn-danger delete-row">Delete</button></td></tr>');
      });
  });
  //save button
  $('.addtv #save-btn,.edittv #save-btn').click(function(){
      var context=tinyMCE.activeEditor.getContent();
      $('#id_context').val(context);
      console.log(context);
  });
  ///send message
    $('#send-message').click(function(){
      var messageid=$('#select-message').val();
      console.log(messageid);
      var list=get_mac_list();
      $.ajax({
      method: "POST",
      url: "/tvs/sendmessage/",
      data: { "messageid" : messageid,"maclist":list },
      dataType: "json",
      success: function(result){
        console.log(result);
    }})
  });
});

$( "body" ).on( "click", "#delete-row", function() {
  var whichtr = $(this).closest("tr");
    whichtr.remove();
});
function update(picker) {
        $('#id_r').val(Math.round(picker.rgb[0]));
        $('#id_g').val(Math.round(picker.rgb[1]));
        $('#id_b').val(Math.round(picker.rgb[2]));
}

function building_change(){
    $("#mapviewer").removeAttr( "src");
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
    $("#mapviewer").removeAttr( "src");
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

function get_list(){
    var jsonArr = [];
    $('#markerlist tr').each(function() {
       var mac = $(this).find(".mac").html();
       var name = $(this).find(".name").html();
       if(mac){
           jsonArr.push({
            mac:mac,
            name:name
            });
       }
 });
 return  JSON.stringify(jsonArr);
}

function get_mac_list(){
    var jsonArr = [];
    $('#markerlist tr').each(function() {
       var mac = $(this).find(".mac").html();
       if(mac){
           jsonArr.push({
            mac
            });
       }
 });
 return  JSON.stringify(jsonArr);
}


