$(function(){
	$("#id_is_activated").prop( "disabled", true );
    $("#id_name").prop( "disabled", true );
    $("#id_port").prop( "disabled", true );
    $("#id_keep_alive").prop( "disabled", true );
    $("#id_user_name").prop( "disabled", true );
    $("#id_passwd").prop( "disabled", true );


	$("#id_editar_btn").click(function(){
		$( "input:disabled" ).prop( "disabled", false );
		$( "#id_salvar" ).prop( "disabled", false );
	});

});
