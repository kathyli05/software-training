teams = {}
user_action = input("Welcome to the Menu. Please select an action: add, remove, modify, view team information, search, or list. To quit, enter quit.")
while True: 
	
	if user_action == "list":
		print(teams)
		return
	
	elif user_action == "remove": 
		delete_team_input = int(input("Which team would you like to remove? Enter 0 to return to the main menu."))
		if delete_team_input == "0":
			return
		elif delete_team_input in teams.keys():
			teams.pop(delete_team_input)
			print("Team " + delete_team_input + " has been removed.")
		else: 
			print("Team " + delete_team_input " has not been found. Returning to main menu...")
			return
	
#	elif user_action == "modify": 
#		update_team_input = input("which team would you like to modify?")
#		if update_team_input in teams.keys():
#			print(teams[update_team_input])
#			area_of_update_team = input("Which area of the team would you like to update?")
			
#This below chunk of code is error message debugger code that I haven't finished yet.

#		if area_of_update_team in ["new_team",  "new_team_robot_width", "new_team_robot_length", "new_team_drivetrain_motors"]:
#				update_value = input("New value: ")
#					if not area_of_update_team.isnumeric():
#						print("Input is not valid.")
#			elif area_of_update_team == "new_team_camera_vision":
#				if value.lower() != "yes" and value.lower() != "no":
#
#
#
#		else: 
#			teams[update_team_input][area_of_update_team] = value
#			print("The team has been updated.")


	elif user_action == "add": 
		new_team = int(input("Enter the number of the team you want to add."))
		teams[new_team] = {}
		new_team_name = input("What is the team's name?")
		teams[new_team]["name"] = new_team_name
		new_team_programming_language = input("What programming language does the team use?")
		teams[new_team]["programming language"] = new_team_programming_language
		new_team_robot_width = input("What is the width of the team's robot?")
		teams[new_team_name]["width of robot"] = new_team_robot_width
		new_team_robot_length = int(input("What is the length of the team's robot?"))
		teams[new_team_name]["length of robot"] = new_team_robot_length
		new_team_camera_vision = int(input("Does the team have a camera vision system?"))
		teams[new_team_name]["camera vision"] = new_team_camera_vision
		new_team_number_of_drivetrain_motors = input("How many drivetrain motors does the robot have?")
		teams[new_team]["number of drivetrain motors"] = new_team_number_of_drivetrain_motors
		print("Returning to main menu...")
		return 
	
	elif user_action == "view team information": 
		view_team_input = input("Which team's information would you like to view? To return to the menu, press 0.")
		if view_team_input == "0":
			return
		elif view_team_input in teams(): 
			print(teams[view_team_input])
		else: 
			print("Team" + view_team_input + " has not been found. Returning to main menu...")
			return
	
	elif user_action == "search": 
		search_team_input = input("Which team would you like to search for? To return to the main menu, enter 0.")
		if search_team_input in teams.keys():
			print(teams[search_team_input])
		else
			print("Team does not exist. Returning to main menu...")
			break
	
	elif user_action == "quit":
		break
#To not receive an error message in the add function, could I define each variable seperately and make an if/else/elif statement?
#Can I loop the code instead of making it return to the main menu?
#Have not tested entire code/done validation yet. 	