$(document).ready(function(){


});

function update(picker) {


        $('#id_r').val(Math.round(picker.rgb[0]));
        $('#id_g').val(Math.round(picker.rgb[1]));
        $('#id_b').val(Math.round(picker.rgb[2]));
}