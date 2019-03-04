$(function(){
    var dateTimeStartCycleAux = $("#id_start_cycle").val();
    var dayStartCycle = dateTimeStartCycleAux.substring(8, 10);
    var monthStartCycle = dateTimeStartCycleAux.substring(5, 7);
    var yearStartCycle = dateTimeStartCycleAux.substring(0, 4);
    var hourStartCycle = dateTimeStartCycleAux.substring(11, 13);
    var minuteStartCycle = dateTimeStartCycleAux.substring(14, 16);
    var dateTimeStartCycle = dayStartCycle +'/'+monthStartCycle+'/'+yearStartCycle+' '+hourStartCycle+':'+minuteStartCycle;
    $("#id_start_cycle").val(dateTimeStartCycle)

    var dateTimeEndCycleAux = $("#id_end_cycle").val();
    var dayEndCycle = dateTimeEndCycleAux.substring(8, 10);
    var monthEndCycle = dateTimeEndCycleAux.substring(5, 7);
    var yearEndCycle = dateTimeEndCycleAux.substring(0, 4);
    var hourEndCycle = dateTimeEndCycleAux.substring(11, 13);
    var minuteEndCycle = dateTimeEndCycleAux.substring(14, 16);
    var dateTimeEndCycle = dayEndCycle +'/'+monthEndCycle+'/'+yearEndCycle+' '+hourEndCycle+':'+minuteEndCycle;
    $("#id_end_cycle").val(dateTimeEndCycle)

	$("#id_title").prop( "disabled", true );
	$("#id_start_time").prop( "disabled", true );
	$("#id_end_time").prop( "disabled", true );
	$("#id_start_cycle").prop( "disabled", true );
	$("#id_end_cycle").prop( "disabled", true );
	$("#id_actuador_id").prop( "disabled", true );
	$("#id_is_activated").prop( "disabled", true );

    $("#id_salvar").click(function(){
        var dateTimeStartCycleAux = $("#id_start_cycle").val();
        var dayStartCycle = dateTimeStartCycleAux.substring(0, 2);
        var monthStartCycle = dateTimeStartCycleAux.substring(3, 5);
        var yearStartCycle = dateTimeStartCycleAux.substring(6, 10);
        var hourStartCycle = dateTimeStartCycleAux.substring(11, 13);
        var minuteStartCycle = dateTimeStartCycleAux.substring(14, 16);
        var dateTimeStartCycle = yearStartCycle +'-'+monthStartCycle+'-'+dayStartCycle+' '+hourStartCycle+':'+minuteStartCycle;
        $("#id_start_cycle").val(dateTimeStartCycle)

        var dateTimeEndCycleAux = $("#id_end_cycle").val();
        var dayEndCycle = dateTimeEndCycleAux.substring(0, 2);
        var monthEndCycle = dateTimeEndCycleAux.substring(3, 5);
        var yearEndCycle = dateTimeEndCycleAux.substring(6, 10);
        var hourEndCycle = dateTimeEndCycleAux.substring(11, 13);
        var minuteEndCycle = dateTimeEndCycleAux.substring(14, 16);
        var dateTimeEndCycle = yearEndCycle +'-'+monthEndCycle+'-'+dayEndCycle+' '+hourEndCycle+':'+minuteEndCycle;
        $("#id_end_cycle").val(dateTimeEndCycle)
    });


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
