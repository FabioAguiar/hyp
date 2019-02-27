$(function(){
	var topic_base = $("#id_topic_base").val();
	var type_peripheral  = $("#id_type_peripheral").val();
	var topic_name = $("#id_topic_name").val();
	var specification = $("#id_specification").val();
	var mqtt_topic = $("#id_mqtt_topic").val();

	$("#id_topic_base").prop( "disabled", true );
	$("#id_type_peripheral").prop( "disabled", true );
	$("#id_topic_name").prop( "disabled", true );
	$("#id_specification").prop( "disabled", true );
	$("#id_mqtt_topic").prop( "disabled", true );
	$("#id_name").prop( "disabled", true );
	$("#id_technical_name").prop( "disabled", true );
	$("#id_description").prop( "disabled", true );
	$("#id_is_activated").prop( "disabled", true );
	$("#id_data_metric").prop( "disabled", true );

	function MQTTTopic(topic_val){
		mqtt_topic = topic_base + type_peripheral + topic_name + specification;
		$("#id_mqtt_topic").val(mqtt_topic);
	}


	$("#id_editar_btn").click(function(){
		$( "input:disabled" ).prop( "disabled", false );
		$( "#id_type_peripheral" ).prop( "disabled", false );
		$( "#id_description" ).prop( "disabled", false );	
		$( "#id_salvar" ).prop( "disabled", false );
	});


	$("#id_mqtt_topic").prop("disabled", true);

	$("#id_topic_base").keyup(function(){
		topic_base = $(this).val();
		if(topic_base.length > 0){
			topic_base += '/';
		}
		if(type_peripheral == ""){
			type_peripheral = 'sensor/';
		}

		MQTTTopic();
	});


	$("#id_type_peripheral").change(function(){
		type_peripheral = $(this).val();
		if(type_peripheral.length > 0){
			type_peripheral += '/';
		}	
		MQTTTopic();
	});


	$("#id_topic_name").keyup(function(){
		topic_name = $(this).val();
		if(topic_name.length > 0){
			topic_name += '/';
		}	
		MQTTTopic();
		
	});

	$("#id_specification").keyup(function(){
		specification = $(this).val();
		if(specification.length > 0){
			specification += '/';
		}		
		MQTTTopic();
	});


	$('#id_peripheral_form').submit(function(){
	    $("#id_peripheral_form :disabled").removeAttr('disabled');
	});



});