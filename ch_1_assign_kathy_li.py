#This is the dictionary that stores all the information about the teams.
teams_info = {
	1678: {
		'location': 'Davis, California, USA', 
		'rookie year': 2005,
		'competed in 2019?': True,
		'2019 competitions': [
			'Central Valley Regional (Fresno, California, USA)',
			'Sacramento Regional (Davis, California, USA)',
			'Aerospace Valley (Lancaster, California, USA)',
			'Carver Division - Houston Championship (Houston, Texas, USA)', 
			'Einstein Field - Houston Championship (Houston, Texas, USA)', 
			'RCC Qianjiang International Robotics Invitational (Hangzhou, Zhejiang, China)', 
			'Chezy Champs (San Jose, California, USA)',
		],
		'2019 season awards': [
			'Chairman\'s Award, Central Valley Regional',
			'Winner, 2019 Central Valley Regional',
			'FIRST Dean\'s List Finalist Award, Sacramento Regional (Katie Stachowicz)',
			'Industrial Design Award (sponsored by General Motors), Sacramento Regional',
			'Winner, 2019 Sacramento Regional',
			'Excellence in Engineering Award (sponsored by Delphi), Aerospace Valley Regional',
			'Winner, 2019 Aerospace Valley Regional',
			'Entrepreneurship Award (sponsored by Kleiner Perkins Caufield and Byers)',
			'Winner, 2019 Carver Division - Houston Championship',
		]
	},
	1868: {
		'location': 'Mountain View, California, USA',
		'rookie year': 2006,
		'competed in 2019?': True,
		'2019 competitions': [
			'Los Angeles North Regional (Valencia, California, USA)',
			'Silicon Valley Regional (San Jose, California, USA)',
			'Turing Division - Houston Championship (Houston, TX)',
			'Chezy Champs (San Jose, California, USA)',
		],
		'2019 season awards': [
			'Chairman\'s Award, Los Angeles North Regional',
			'Winner, 2019 Los Angeles North Regional',
			'Entrepreneurship Award (sponsored by Kleiner Perkins Caufield and Byers), Silicon Valley Regional',
		]
	},
	1323: {
		'location': 'Madera, California, USA',
		'rookie year': 2004,
		'competed in 2019?': True,
		'2019 competitions': [
			'Central Valley Regional (Fresno, California, USA)',
			'Sacramento Regional (Davis, California, USA)',
			'Newton Division - Houston Championship (Houston, Texas, USA)',
			'Einstein Field (Houston, Texas, USA)',
		],
		'2019 season awards': [
			'Autonomous Award (sponsored by Ford), Central Valley Regional',
			'Winner, 2019 Central Valley Regional',
			'Quality Award sponsored by Motorola Solutions Foundation',
			'Winner, 2019 Sacramento Regional',
			'Industrial Design Award (sponsored by General Motors), Houston Championship '
			'Winner, 2019 Newton Division - Houston Championship',
			'Winner, 2019 Houston Championship',
		]
	},
	3132: {
		'location': 'Sydney, Australia',
		'rookie year': 2010,
		'competed in 2019?': True,
		'2019 competitions': [
			'Southern Cross Regional (Sydney, Australia)',
			'South Pacific Regional (Sydney, Australia)',
			'Carver Division - Houston Championship (Houston, Texas, USA)',
			'Einstein Field - Houston Championship (Houston, Texas, USA)',
			'Duel Down Under (Sydney, Australia)',
		],
		'2019 season awards': [
			'Woodie Flowers Finalist Award, Southern Cross Regional (Sarah Heimlich)',
			'Gracious Professionalism Award (sponsored by Johnson & Johnson), Southern Cross Regional',
			'Regional Engineering Inspiration Award, South Pacific Regional',
			'FIRST Dean\'s List Finalist Award, South Pacific Regional (Jaye Heimlich)',
			'Safety Award (sponsored by Underwriters Laboratories), South Pacific Regional',
			'Winner, 2019 Carver Division - Houston Championship',
		]
	},
	254: {
		'location': 'San Jose, California, USA',
		'rookie	year': 1999,
		'competed in 2019?': True,
		'2019 competitions': [ 
			'San Francisco Regional (San Francisco, California, USA)',
			'Silicon Valley Regional (San Jose, California, USA)',
			'Turing Division - Houston Championship (Houston, Texas, USA)',
			'Einstein Field - Houston Championship (Houston, Texas, USA)',
			'Chezy Champs (San Jose, California, USA)'
		],
		'2019 season awards': [
			'Innovation in Control Award (sponsored by Rockwell Automation), San Francisco Regional',
			'Winner, 2019 San Francisco Regional',
			'Excellence in Engineering Award (sponsored by Delphi), Silicon Valley Regional',
			'Winner, 2019 Silicon Valley Regional',
			'Industrial Design Award (sponsored by General Motors), Turing Divions'
			'Winner, 2019 Turing Division - Houston Championship',
			'Championship Finalist, Einstein Field - Houston Championship',

		]
	},
}
team_input = int(input('Choose an FRC team: 1678, 1868, 1323, 3132, or 254.\n'))
team_attribute = input('Enter an attribute: "Location", "Rookie Year", "Competed in 2019?", "2019 Competitions", and "2019 Season Awards".\n').lower()
#without .lower(), user input is case-sensitive.
print(teams_info[team_input][team_attribute])