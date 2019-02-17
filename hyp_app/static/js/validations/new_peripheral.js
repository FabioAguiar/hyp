$(function(){
	var topic_base = "";
	var type_peripheral  = "";
	var topic_name = "";
	var specification = "";
	var mqtt_topic = "";


	$("#id_last_record_state").val(0);
	$("#id_last_record").val(new Date());


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

	function MQTTTopic(topic_val){
		mqtt_topic = topic_base + type_peripheral + topic_name + specification;
		$("#id_mqtt_topic").val(mqtt_topic);
		//console.log(mqtt_topic);
	}

});