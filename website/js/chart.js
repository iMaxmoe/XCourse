var num_of_course = 5;
var data = {
				series: [
					{ titles: ['MGMT5500', 'ISON5100', 'ISOM5020', 'ISOM5810', 'FINA5290'], values: [97.4, 95.9, 95.7, 94.8, 94.8] },
					{ titles: ['ECON2123', 'MARK5120', 'FINA2303', 'ISOM5290', 'ISOM3370'], values: [65.1, 63.7, 61, 57.7, 56.3] },
					{ titles: ['HUI, Kai Lung', 'DIAS, Garvin Percy', 'JAISINGH, Jeevan', 'CHIU Chun Wah Andrew', 'WANG, Susheng'], values: [98.0, 98.0, 95.9, 95.0, 94.9] },
					{ titles: ['LEE, Dongwon', 'HUANG, SETH H', 'KAWAGUCHI, Kohei', 'JIA, Jia', 'HUNG Mingyi'], values: [64.5, 64.1, 62.7, 57.1, 52.3] },

					{ titles: ['MECH3640', 'COMP5331', 'COMP3721', 'COMP5711', 'CIVL5220'], values: [99.2, 95.6, 90.1, 90.0, 88.2] },
					{ titles: ['ENGG1100', 'CENG1600', 'MECH1906', 'CENG3910', 'COMP2012H'], values: [64.8, 62.1, 57.6, 57.3, 56.5] },
					{ titles: ['LI, Larry', 'WONG, Raymond C W', 'TSOI, Yau Chat, Desmond', 'MURCH, Ross', 'YI, Ke'], values: [100.0, 96.3, 95.3, 93.3, 91.7] },
					{ titles: ['ZHANG, Li Min', 'SONG, Yangqiu', 'TAI, Chiew Lan', 'KIM, Jang Kyo', 'QUAN, Long'], values: [71.3, 70.2, 61.9, 61.6, 61.1] },

					{ titles: ['MAFS5110', 'MAFS5010', 'PHYS1312', 'MAFS5140', 'CHMS5020'], values: [97.7, 95.7, 94.1, 93.8, 91.7] },
					{ titles: ['SCIE1110', 'MATH1003', 'PHYS1001', 'LIFS1901', 'MATH1012'], values: [62.3, 61.4, 58.7, 57.6, 56.4] },
					{ titles: ['JING, Bing-yi', 'CHAN, Ho Bun', 'CHEN, Kani', 'FONG, Tsz Ho', 'GRIFFITH, Stephen Miles'], values: [95.7, 95.5, 95.1, 93.3, 92.7] },
					{ titles: ['TANG, Jessica Ce Mun', 'WANG, Ke', 'CHING, Avery', 'WANG, Erxiao', 'GAO, Yuan'], values: [62.7, 62.1, 59.1, 52.7, 50.6] },

					{ titles: ['HMMA5001', 'SOSC3110', 'SOSC1150', 'SOSC2130', 'SOSC2740'], values: [92.8, 90.5, 85.8, 84.1, 83.0] },
					{ titles: ['HUMA1440', 'HUMA2621', 'HUMA1000B', 'HUMA1000A', 'SOSC2290'], values: [66.4, 63.8, 62.3, 62.2, 50.7] },
					{ titles: ['SHAW, May Yi', 'HA, Guangtian', 'WONG, Claudia', 'ZHANG, Lawrence LC', 'SHARIF, Nau Bahar'], values: [96.9, 95.4, 95.0, 93.9, 93.2] },
					{ titles:['NAM, Sai Lok', 'KWONG, Anna Yee Ngan', 'PAN, Ping', 'HO, Virgil Kit Yiu', 'CHO, Hye Jee'], values: [73.1, 71.9, 70.7, 67.9, 46.5] },
				]
			};

var chartWidth       = 75,
		barHeight        = 20,
		groupHeight      = barHeight * num_of_course,
		gapBetweenGroups = 10,
		spaceForLabels   = 125;

// Zip the series data together (first values, second values, etc.)
var zippedData = [];

for (var j=0; j<data.series.length; j++) {
	for (var i=0; i<num_of_course; i++) {
		zippedData.push(data.series[j].values[i]);
	}
}

// Color scale
//var color = d3.scale.category20();
var color = ["#a50f15", "#de2d26", "#fb6a4a", "#fcae91", "#dec5b9", "#cdd8c9", "#bae4b3", "#74c476", "#31a354", "#006d2c"];
var chartHeight = barHeight * num_of_course + gapBetweenGroups;

var x = d3.scale.linear()
		.domain([0, d3.max(zippedData)])
		.range([0, chartWidth]);

var y = d3.scale.linear()
		.range([chartHeight + gapBetweenGroups, 0]);

var yAxis = d3.svg.axis()
		.scale(y)
		.tickFormat('')
		.tickSize(0)
		.orient('left');

// Specify the chart area and dimensions
for(chart_i = 0; chart_i < 16; chart_i++)
{
	var chart_id = ('#svg'+chart_i);
	var chart = d3.select(chart_id)
			.attr('width', spaceForLabels + chartWidth)
			.attr('height', chartHeight);
	
	var chosenZippedData = zippedData.slice(chart_i*num_of_course, (chart_i+1)*num_of_course);
	
	// Create bars
	var bar = chart.selectAll('g')
			.data(chosenZippedData)
			.enter().append('g')
			.attr('transform', function(d, i) {
				return 'translate(' + spaceForLabels + ',' + (i * barHeight + gapBetweenGroups * (0.5 + Math.floor(i/num_of_course))) + ')';
			});

	// Create rectangles of the correct width
	var haha = 0;

	if (chart_i % 2 == 1)
	{
		haha = 1;
	}

	bar.append('rect')
			.attr('fill', function(d,i) { return color[5 * haha + i % num_of_course]
				; })
			.attr('class', 'bar')
			.attr('width', x)
			.attr('height', barHeight - 1);

	// Add text label in bar
	bar.append('text')
			.attr('x', function(d) { return x(d) - 3; })
			.attr('y', barHeight / 2)
			.attr('fill', 'red')
			.attr('dy', '.35em')
			.text(function(d) { return d; });

	// Draw course labels
	bar.append('text')
			.attr('class', 'label')
			.attr('x', function(d) { return - 10; })
			.attr('y', barHeight / 2)
			.attr('dy', '.35em')
			.text(function(d,i) {return data.series[chart_i].titles[i%num_of_course];});
			/*
			{
				s = Math.floor(i/data.series.length)
				return data.series[s].titles[i%data.series.length];
			});
			*/


}

