$(function(){

	var owd = {
		'tempAtual' : '',
		'tempMax' : '',
		'tempMin' : '',
		'nebulosidade' : '',
		'pressao' : '',
		'umidade' : '',
		'velocidadeVento' : '',
		'latEstacao' : '',
		'lonEstacao' : ''
	}


	var hgbr = {
		'temp' : '',
		'nebulosidade' : '',
		'umidade' : '',
		'velocidadeVento' : '',
		'nascerSol' : '',
		'porSol' : '',
		'entrelinhar_condicao' : ''
	}


	function displayCallbackOWDData(data){

	    owd.temp = data.main.temp;
	    owd.tempMax = data.main.temp_max;
	    owd.tempMin = data.main.temp_min;
		owd.nebulosidade = data.weather[0].description;
		owd.pressao = data.main.pressure;
		owd.umidade = data.main.humidity;
		owd.velocidadeVento = data.wind.speed;
		owd.latEstacao = data.coord.lon;
		owd.lonEstacao = data.coord.lat;


	    $("#temp_atual_OWD").html(owd.temp);
	    $("#temp_max_OWD").html(owd.tempMax);
	    $("#temp_min_OWD").html(owd.tempMin);
	    $("#nebulosidade_OWD").html(owd.nebulosidade);
	    $("#pressao_OWD").html(owd.pressao);
	    $("#umidade_OWD").html(owd.umidade);
	    $("#umidade_OWD").html(owd.umidade);
	    $("#velocidade_vento_OWD").html(owd.velocidadeVento);
    	$("#lat_estacao_OWD").html(owd.latEstacao);
    	$("#lon_estacao_OWD").html(owd.lonEstacao);

	}


	function getOWMData(callback){

	    $.ajax({
	        url : "http://api.openweathermap.org/data/2.5/weather?id=3395077&APPID=1a75c08d52185cac9a9a7ba86f315e54&units=metric&lang=pt",
	        type: "GET",
	        dataType: "json"
	    }).done(function(data){
	        callback(data);
	    }).fail(function(){
	        console.log("Erro na requisição");
	    });

	}

	getOWMData(displayCallbackOWDData);


	function displayCallbackHGBrasilData(data){

		hgbr.temp = data.results.temp;
		hgbr.nebulosidade = data.results.description;
		hgbr.umidade = data.results.humidity;
		hgbr.velocidadeVento = data.results.wind_speedy;
		hgbr.nascerSol = data.results.sunrise;
		hgbr.porSol = data.results.sunset;
		hgbr.entrelinhar_condicao = data.results.condition_slug;


	    $("#temp_hgbr").html(hgbr.temp);
	    $("#nebulosidade_hgbr").html(hgbr.nebulosidade);
	    $("#umidade_hgbr").html(hgbr.umidade);
	    $("#velocidade_vento_hgbr").html(hgbr.velocidadeVento);	  
	    $("#nascer_sol_hgbr").html(hgbr.nascerSol);
	    $("#por_sol_hgbr").html(hgbr.porSol);	  	    
	    $("#entrelinhar_condicao_hgbr").html(hgbr.entrelinhar_condicao);	  
	}


	function getHGBrasilData(callback){

	    $.ajax({
	        url : "https://api.hgbrasil.com/weather?key=74fe87bd&format=json-cors&woeid=455824",
	        type: "GET",
	        dataType: "json"
	    }).done(function(data){
	        callback(data);
	    }).fail(function(xhr, status, erro){
	        console.log(status);
	    });

	}

	getHGBrasilData(displayCallbackHGBrasilData);

});