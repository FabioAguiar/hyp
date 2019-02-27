$(function(){
	
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