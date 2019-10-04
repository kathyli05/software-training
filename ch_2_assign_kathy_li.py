teams = {}
while True: 
	user_action = input("Welcome to the menu. Please select an action: add, remove, modify, view, search, or list. To quit, enter quit.")
	if user_action == "list":
		print(teams)
		continue
	#note to self: validation to do - "list" with no teams inside prints infinite teams
	elif user_action == "remove": 
		delete_team = int(input("Which team would you like to remove? Enter 0 to return to the main menu."))
		if delete_team == 0:
			continue
		elif delete_team in teams.keys():
			teams.pop(delete_team)
			print("Team " + str(delete_team) + " has been removed.")
		else: 
			print("Team " + str(delete_team) + " has not been found. Returning to main menu...")
			continue
	
	elif user_action == "modify": 
		update_team = int(input("Which team would you like to modify? To return the to the main menu, enter 0." ))
		if update_team == 0:
			continue
		if update_team in teams.keys():
			update_variable = input("Which field would you like to modify? ")
			change = input("Enter the new value. ")
			teams[update_team][update_variable] = change
		else:
			print("Team " + str(update_team) + " was not found. Returning to main menu...")
			continue
#			area_of_update_team = input("Which area of the team would you like to update?")
			
#This below chunk of code is error message debugger code that I haven't finished yet.

#		if area_of_update_team in ["new_team",  "new_team_robot_width", "new_team_robot_length", "new_team_drivetrain_motors"]:
#				update_value = input("New value: ")
#					if not area_of_update_team.isnumeric():
#						print("Input is not valid.")
#			elif area_of_update_team == "new_team_camera_vision":
#				if value != "yes" and value != "no":

#
#
#
#		else: 
#			teams[update_team_input][area_of_update_team] = value
#			print("The team has been updated.")


	elif user_action == "add": 
		new_team = input("Enter the number of the team you want to add. To return to the main menu, enter 0. ")
		if not new_team.isnumeric():
			print("Must be a number. Returning to main menu... ")
			continue
		elif new_team == 0:
			continue
		else:
			new_team = int(new_team)
			teams[new_team] = {}
			teams[new_team]["name"] = input("What is the team's name? ")
			teams[new_team]["programming language"] = input("What programming language does the team use? ")
			width = input("What is the width of the team's robot? ")
			if not width.isnumeric():
				print("Width must be a number. Returning to main menu... ")
				continue
			else: 
				width = float(width)
				teams[new_team]["width of robot"] = width
			length = input("What is the length of the team's robot? ")
			if not length.isnumeric():
				print("Length must be a number. Returning to main menu... ")
				continue
			else: 
				length = float(width)
				teams[new_team]["length of robot"] = length
			teams[new_team]["camera vision"] = input("Does the team have a camera vision system? ")
			drivetrain_motors = input("How many drivetrain motors does the robot have? ")
			if not drivetrain_motors.isnumeric(): 
				print("Drivetrain motors must be a number. Returning to main menu... ")
				continue
			else:
				teams[new_team]["number of drivetrain motors"] = drivetrain_motors
			print("Team added. Returning to main menu... ")
			continue
	
	elif user_action == "view": 
		view_input = int(input("Which team's information would you like to view? To continue to the menu, press 0. "))
		if view_input == 0:
			continue
		elif view_input in teams: 
			print(teams[view_input])
		else: 
			print("Team " + view_input + " has not been found. Returning to main menu... ")
			continue
	
	elif user_action == "search": 
		search_input = int(input("Which team would you like to search for? To return to the main menu, enter 0. "))
		if search_input == 0:
			continue
		elif search_input in teams.keys():
			print(teams[search_input])
		else:
			print("Team does not exist. Returning to main menu... ")
			break
	
	elif user_action == "quit":
		break
#To not receive an error message in the add function, could I define each variable seperately and make an if/else/elif statement?
#Can I loop the code instead of making it continue to the main menu?
#Have not tested entire code/done validation yet. 