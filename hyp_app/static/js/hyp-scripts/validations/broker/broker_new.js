$(function(){

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


    $('#id_datetimepicker_time_test').datetimepicker({
        locale: 'pt-br'
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

});