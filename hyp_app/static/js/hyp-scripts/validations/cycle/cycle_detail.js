$(function(){
	$("#id_title").prop( "disabled", true );
	$("#id_start_cycle").prop( "disabled", true );
	$("#id_end_cycle").prop( "disabled", true );
	$("#id_start_permanence_cycle").prop( "disabled", true );
	$("#id_end_permanence_cycle").prop( "disabled", true );
	$("#id_actuador_id").prop( "disabled", true );
	$("#id_is_activated").prop( "disabled", true );


    $('#id_datetimepicker_begin_cycle').datetimepicker({
        format: 'LT'
    });

    $('#id_datetimepicker_end_cycle').datetimepicker({
        format: 'LT'
    }); 
                
    $('#id_datetimepicker_begin_permanence_cycle').datetimepicker({                   
        locale: 'pt-br'
    });

    $('#id_datetimepicker_end_permanence_cycle').datetimepicker({                   
        locale: 'pt-br'
    });


	$("#id_editar_btn").click(function(){
		$( "input:disabled" ).prop( "disabled", false );
		$( "#id_actuador_id" ).prop( "disabled", false );		
		$( "#id_salvar" ).prop( "disabled", false );
	});

});