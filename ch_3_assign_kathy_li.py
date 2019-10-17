teams = {}

def master_action(): 
	while True:
		user_action = input("Welcome to the menu. Please select an action: add, remove, modify, view, search, or list. To quit, enter quit. \n")
		if user_action == "list":
			list_teams()
		elif user_action == "remove":
			remove_team()
		elif user_action == "search":
			search_team()
		elif user_action == "add":
			add_team()
		elif user_action == "modify":
			modify_team()
		elif user_action == "view":
			view_team()
		elif user_action == "quit":
			quit_program()

def list_teams():
    print(teams)

def remove_team():
	delete_team = int(input("Which team would you like to remove? \n"))
	if delete_team in teams.keys():
		teams.pop(delete_team)
		print("Team " + str(delete_team) + " has been removed. Returning to menu... ")
	else: 
		print("Team " + str(delete_team) + " has not been found. Returning to menu... ")

def search_team():
	search_input = int(input("Which team would you like to search for? \n"))
	if search_input in teams.keys():
		print(teams[search_input])
	else:
		print("Team does not exist. Returning to menu... ")

def add_team():
	new_team = input("Enter the number of the team you want to add. \n")
	if new_team.isnumeric() == False:
		print("Must be a number. Returning to menu... ")
	else:
		new_team = int(new_team)
		teams[new_team] = {}
		teams[new_team]["name"] = input("What is the team's name? \n")
		
		teams[new_team]["location"] = input("Where is the team located? \n")
		
		rookie_year = input("What is the team's rookie year? \n")
		if not rookie_year.isnumeric():
			print("Rookie year must be a number. Returning to menu... ")
		else: 
			rookie_year = int(rookie_year)
			teams[new_team]["rookie year"] = rookie_year
	
			competed_in_2019 = input("Did they compete in 2019? Input True or False. \n")
			competed_in_2019 = bool(competed_in_2019)
			if not competed_in_2019 == True or competed_in_2019 == False:
				print("Please follow directions. Returning to menu... ")
				master_action()
			elif competed_in_2019 == False:
				print("Information added, returning to menu.")
			else:
				teams[new_team]["competed in 2019"] = competed_in_2019
			
			teams[new_team]["2019 competitions"] = input("What were their 2019 competitions? \n")
			teams[new_team]["2019 awards"] = input("What awards did they receive in 2019? \n")
			print("Team added. Returning to menu... ")

def view_team():
	view_input = input("Which team's information would you like to view? \n")
	if not view_input.isnumeric():
		print("Team must be a number. Returning	to menu... ")
	view_input = int(view_input)
	if view_input in teams: 
		print(teams[view_input])
	else: 
		print("Team " + view_input + " has not been found. Returning to menu... ")

def modify_team(): 
	update_team = int(input("Which team would you like to modify? To return the to the menu, enter 0. \n "))
	if update_team in teams.keys():
		update_variable = input("Which field would you like to modify: name, location, rookie year, compteted in 2019, 2019 competitions, or 2019 awards? \n")
		if update_variable not in teams[update_team].keys():
			print("There is no such field. Returning to menu... ")

		change = input("Enter the new value. \n")
		if update_variable == "rookie year": 
			if not change.isnumeric():
				print("Input is invalid. Returning to menu... ")
	
			else:
				teams[update_team][update_variable] = change
				print("Successfully changed. Returning to menu... ")
	
		elif update_variable == "competed in 2019":
			change = bool(change)
			if not change == True or change == False:
				print("Please input True or False. Returning to menu... ")
	
			else: 
				teams[update_team][update_variable] = change
				print("Successfully changed. Returning to menu... ")
		else:
			teams[update_team][update_variable] = change
			print("Successfully changed. Returning to menu... ")

	else:
		print("Team " + str(update_team) + " was not found. Returning to menu... ")

def quit_program():
	##break
	print("Use Ctrl-C to exit the program.")

master_action()