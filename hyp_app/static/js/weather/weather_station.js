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
		'entrelinhar_condicao' : '',
		'previsao' : '[]'
	}



    function plotarChart(previsao){


		var randomScalingFactor = function() {
			return Math.round(Math.random() * 100);
		};

		var config = {
			type: 'line',
			data: {
				labels: [previsao[0].date, previsao[1].date, previsao[2].date, previsao[3].date, previsao[4].date, previsao[5].date, previsao[6].date],
				datasets: [{
					label: 'Temperatura máxima',
					backgroundColor: window.chartColors.red,
					borderColor: window.chartColors.red,
					data: [
						previsao[0].max,
						previsao[1].max,
						previsao[2].max,
						previsao[3].max,
						previsao[4].max,
						previsao[5].max,
						previsao[6].max
					],
					fill: false,
				}, {
					label: 'Temperatura mínima',
					fill: false,
					backgroundColor: window.chartColors.blue,
					borderColor: window.chartColors.blue,
					data: [
						previsao[0].min,
						previsao[1].min,
						previsao[2].min,
						previsao[3].min,
						previsao[4].min,
						previsao[5].min,
						previsao[6].min
					],
				} ]
			},
			options: {
				responsive: true,
				title: {
					display: true,
					text: 'Previsão do tempo em Recife'
				},
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Dias'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Temperatura'
						},
						ticks: {
							min: 0,
							max: 40,

							// forces step size to be 5 units
							stepSize: 5
						}
					}]
				}
			}
		};

		function carregarChart() {
			var ctx = document.getElementById('canvas').getContext('2d');
			window.myLine = new Chart(ctx, config);
		};

		carregarChart();

		/*document.getElementById('randomizeData').addEventListener('click', function() {
			config.data.datasets.forEach(function(dataset) {
				dataset.data = dataset.data.map(function() {
					return randomScalingFactor();
				});
			});

			window.myLine.update();
		});

		var colorNames = Object.keys(window.chartColors);
		document.getElementById('addDataset').addEventListener('click', function() {
			var colorName = colorNames[config.data.datasets.length % colorNames.length];
			var newColor = window.chartColors[colorName];
			var newDataset = {
				label: 'Dataset ' + config.data.datasets.length,
				backgroundColor: newColor,
				borderColor: newColor,
				data: [],
				fill: false
			};

			for (var index = 0; index < config.data.labels.length; ++index) {
				newDataset.data.push(randomScalingFactor());
			}

			config.data.datasets.push(newDataset);
			window.myLine.update();
		});

		document.getElementById('addData').addEventListener('click', function() {
			if (config.data.datasets.length > 0) {
				var month = MONTHS[config.data.labels.length % MONTHS.length];
				config.data.labels.push(month);

				config.data.datasets.forEach(function(dataset) {
					dataset.data.push(randomScalingFactor());
				});

				window.myLine.update();
			}
		});

		document.getElementById('removeDataset').addEventListener('click', function() {
			config.data.datasets.splice(0, 1);
			window.myLine.update();
		});

		document.getElementById('removeData').addEventListener('click', function() {
			config.data.labels.splice(-1, 1); // remove the label first

			config.data.datasets.forEach(function(dataset) {
				dataset.data.pop();
			});

			window.myLine.update();
		});
		*/

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
		hgbr.previsao = data.results.forecast;


		plotarChart(hgbr.previsao);


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

		/*
        "date": "22/02",
        "weekday": "Sex",
        "max": "28",
        "min": "25",
        "description": "Tempestades",
        "condition": "storm"
        */





});