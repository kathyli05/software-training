teams = {}
while True: 
	user_action = input("Welcome to the menu. Please select an action: add, remove, modify, view, search, or list. To quit, enter quit. \n")
	
	if user_action == "list":
		print(teams)
		continue

	elif user_action == "remove": 
		delete_team = int(input("Which team would you like to remove? Enter 0 to return to the menu. \n"))
		if delete_team == 0:
			continue
		elif delete_team in teams.keys():
			teams.pop(delete_team)
			print("Team " + str(delete_team) + " has been removed. Returning to menu... ")
			continue
		else: 
			print("Team " + str(delete_team) + " has not been found. Returning to menu... ")
			continue
	
	elif user_action == "modify": 
		update_team = int(input("Which team would you like to modify? To return the to the menu, enter 0. \n "))
		if update_team == 0:
			continue
		elif update_team in teams.keys():
			update_variable = input("Which field would you like to modify: name, programming language, width, length, number of drivetrain motors, or camera vision? \n")
			if update_variable not in teams[new_team].keys():
				print("There is no such field. Returning to menu... ")
				continue
			change = input("Enter the new value. \n")
			if update_variable in ["width", "length", "number of drivetrain motors"]: 
				if not change.isnumeric():
					print("Input is invalid. Returning to menu... ")
					continue
				else:
					teams[update_team][update_variable] = change
					print("Successfully changed. Returning to menu... ")
					continue
			elif update_variable == "camera vision":
				change = bool(change)
				if not change == True or change == False:
					print("Please input True or False. Returning to menu... ")
					continue
				else: 
					teams[update_team][update_variable] = change
					print("Successfully changed. Returning to menu... ")
			else:
				teams[update_team][update_variable] = change
				print("Successfully changed. Returning to menu... ")
				continue
		else:
			print("Team " + str(update_team) + " was not found. Returning to menu... ")
			continue

	elif user_action == "add": 
		new_team = input("Enter the number of the team you want to add. To return to the menu, enter 0. \n")
		if not new_team.isnumeric():
			print("Must be a number. Returning to menu... ")
			continue
		elif new_team == 0:
			continue
		else:
			new_team = int(new_team)
			teams[new_team] = {}
			teams[new_team]["name"] = input("What is the team's name? \n")
			teams[new_team]["programming language"] = input("What programming language does the team use? \n")
			width = input("What is the width of the team's robot? \n")
			if not width.isnumeric():
				print("Width must be a number. Returning to menu... ")
				continue
			else: 
				width = float(width)
				teams[new_team]["width"] = width
			length = input("What is the length of the team's robot? \n")
			if not length.isnumeric():
				print("Length must be a number. Returning to menu... ")
				continue
			else: 
				length = float(width)
				teams[new_team]["length"] = length
			camera_vision = input("Does the team have a camera vision system? Input True or False. \n")
			camera_vision = bool(camera_vision)
			if not camera_vision == True or camera_vision == False:
				print("Please follow directions. Returning to menu... ")
				continue
			else:
				teams[new_team]["camera vision"] = camera_vision
			drivetrain_motors = input("How many drivetrain motors does the robot have? \n")
			if not drivetrain_motors.isnumeric(): 
				print("Drivetrain motors must be a number. Returning to menu... ")
				continue
			else:
				teams[new_team]["number of drivetrain motors"] = drivetrain_motors
			print("Team added. Returning to menu... ")
			continue
	
	elif user_action == "view": 
		view_input = input("Which team's information would you like to view? To return to the menu, press 0. \n")
		if not view_input.isnumeric():
			print("Team must be a number. Returning	to menu... ")
			continue
		elif view_input == int(0):
			continue
		view_input = int(view_input)
		elif view_input in teams: 
			print(teams[view_input])
			continue
		else: 
			print("Team " + view_input + " has not been found. Returning to menu... ")
			continue
	elif user_action == "search": 
		search_input = int(input("Which team would you like to search for? To return to the menu, enter 0. \n"))
		if search_input == 0:
			continue
		elif search_input in teams.keys():
			print(teams[search_input])
		else:
			print("Team does not exist. Returning to menu... ")
			continue
	elif user_action == "quit":
		break