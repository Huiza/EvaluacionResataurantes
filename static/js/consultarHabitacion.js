$(document).ready(function(){
	$("#buscarHabitacion").submit(function(e){
		e.preventDefault();
		$.ajax({
			url:$(this).attr('action'),
			type:$(this).attr('method'),
			data:$(this).serialize(),

			success: function(json){
				console.log(json);
			}
		})
	})
})

$(function(){
	var $tabla = $('#tabla');
	$('#selectHabitacion').change(function(){
		var value =$(this).val();
		if(value){
			$('tbody tr.' +value,$tabla).show();
			$('tbody tr:not(.' +valu+')',$tabla).hide();

		}
		else{
			$('tbody tr.',$tabla).show();
		}
	});


});