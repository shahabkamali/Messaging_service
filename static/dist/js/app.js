// map selector

;(function($) {
	var map_data = {
		0 : {
			"marker": [
				{x: "0.5", y: "0.5", type: "tv"},
				{x: "0.322", y: "0.269", type: "led"},
				{x: "0.424", y: "0.593", type: "led"}
			],
			"image" : "/static/dist/img/test-map.png"
		},
        1 : {
			"marker": [
				{x: "0.3", y: "0.2", type: "led"},
				{x: "0.122", y: "0.169", type: "tv"},
				{x: "0.624", y: "0.393", type: "tv"}
			],
			"image" : "/static/dist/img/test-map.jpg"
		},
        2 : {
			"marker": [
				{x: "0.1", y: "0.7", type: "tv"},
				{x: "0.422", y: "0.169", type: "tv"},
				{x: "0.924", y: "0.693", type: "tv"}
			],
			"image" : "/static/dist/img/test-map2.jpg"
		},
        3 : {
			"marker": [
				{x: "0.2", y: "0.2", type: "led"},
				{x: "0.122", y: "0.869", type: "tv"},
				{x: "0.624", y: "0.393", type: "tv"}
			],
			"image" : "/static/dist/img/test-map3.jpg"
		},
        4 : {
			"marker": [
				{x: "0.3", y: "0.2", type: "led"},
				{x: "0.122", y: "0.769", type: "tv"},
				{x: "0.624", y: "0.293", type: "tv"}
			],
			"image" : "/static/dist/img/test-map5.jpg"
		},
        5 : {
			"marker": [
				{x: "0.3", y: "0.2", type: "led"},
				{x: "0.422", y: "0.169", type: "tv"},
				{x: "0.624", y: "0.393", type: "tv"}
			],
			"image" : "/static/dist/img/test-map6.jpg"
		},

	},
    map_exist = false,
    load_map = function (id) {
        // remove old map data
        var $img = $(".map img"),
            data = map_data[id];
		$img.attr("src",'/static/dist/img/boxed-bg.png');
        $img.attr("src",data['image']);
        if(map_exist){
            $img.imgNotes("destroy");
        }
        $img.imgNotes();
        $img.imgNotes("import", data['marker']);
        map_exist = true;

    }
	$(document).ready(function() {
        // load first map
        load_map(0);
        $("#change_map").change(function () {
            var id = $(this).val();
            load_map(id);
        })

        $(".send-text").on("click",function () {
            $.ajax({
                'url' : '/map',
                 method: "POST",
                 data: { text: $("#text").val(),'csrfmiddlewaretoken':$( "input[name='csrfmiddlewaretoken']" ).val() }
            })

        })
	});
})(jQuery);

