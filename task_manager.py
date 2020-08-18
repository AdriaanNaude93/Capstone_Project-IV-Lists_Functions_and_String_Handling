# The function below was created to add a task number to the tasks.
# It counts the amount of lines in the text file and adds to it, to
# give each task a number.
# I also edited the text file, by adding numbers 1 to 3 to the existing tasks.
# This function can also be used in the generate report section of the assignment.

def num_of_tasks():
	with open("tasks.txt") as f:
		for i, l in enumerate(f):
			pass
	return i + 2

# The functions below are used to the generate report part of this program.
# The idex position of the "Yes" and "No" in the task text file is checked
# To see if a task has been completed or not.
	
def completed_tasks():
	tasks = open("tasks.txt","r+")
	amount = 0
	for line in tasks:
		completed_task = line.split(",")
		if completed_task[5] == " Yes":
			amount += 1
	return amount
	
def incomplete_tasks():
	tasks = open("tasks.txt","r+")
	amount = 0
	for line in tasks:
		completed_task = line.split(",")
		if completed_task[5] == " No":
			amount += 1
	return amount

# The overdue task function applies a value to the whole of the date. The
# dates are case sensitive and this is expressed to the used when they initially enter
# today's date. The day, month and year all have values and if they are added together,
# the user can see which dates come before others.
# If the weight of the due date is more than the current date, and the task has not
#been completed, the task will be saved as overdue.

def overdue_tasks():
	tasks = open("tasks.txt","r+")
	amount = 0
	for line in tasks:
		completed_task = line.split(",")
		did_complete = completed_task[5]
		given_date = completed_task[3]
		due_date = completed_task[4]
		given_day = int(given_date.split()[0])
		given_month = given_date.split()[1]
		given_year = int(given_date.split()[2])
		due_day = int(due_date.split()[0])
		due_month = due_date.split()[1]
		due_year = int(due_date.split()[2])
		if due_month == "January":
			due_month = int(110)
		elif due_month == "February":
			due_month = int(120)
		elif due_month == "March":
			due_month = int(130)
		elif due_month == "April":
			due_month = int(140)
		elif due_month == "May":
			due_month = int(150)
		elif due_month == "June":
			due_month = int(160)
		elif due_month == "July":
			due_month = int(170)
		elif due_month == "August":
			due_month = int(180)
		elif due_month == "September":
			due_month = int(190)
		elif due_month == "October":
			due_month = int(200)
		elif due_month == "November":
			due_month = int(210)
		elif due_month == "December":
			due_month = int(220)
		due_weight = (due_day / 100) + due_month + due_year
		
		if completed_task[5] == " No" and today_weight < due_weight:
			amount += 1
			
	return amount
	

#-----------------------------------FUNCTIONS--------------------------------------
#----------------------------------------------------------------------------------

# The initial code of assignment 20 formed the backbone of this function.
# By placing it in a function, it was easier to edit and could just be called
# when the user asks for it.

def reg_user():
	users = open("user.txt","r+")
	print("Let's register a new user.\n")
	new_user = input("Username: ")
	for line in users:
		existing_user = line.split(",")
		existing_users = existing_user[0]
	
# Here I added code to check the list of users in the user text file.
# If a username appears in the file, the user can;t use the same name when adding
# a new user.	
	
		while new_user == existing_users:
			print("User already exists, please enter another.")
			new_user = input("Username: ") 
		while new_user == "admin":
			print("User already exists, please enter another.")
			new_user = input("Username: ") 
	new_password = input("Password: ")
	confirm_password = input("Confirm Password: ")
	while new_password != confirm_password:
		print("The two passwords didn't match, try again.\n")
		print(f"Username: {new_user}")
		new_password = input("Password: ")
		confirm_password = input("Confirm Password: ")
	if new_password == confirm_password:
		users.write("\n")
		users.write(f"{new_user}, {new_password}")
	print("\nThank you, the new user has been saved.")
	users.close()
#-----------------------------------------------------------------------------------
def add_task():
	tasks = open("tasks.txt","a+")
	print("Let's add a task.\n")
	task_user = input("Username of person in charge of the task: ")
	task_title = input("Title of the task: ")
	task_description = input("Description of the task: ")
	date_assigned = current_date
	date_due = input("Date which the task is due: ")
		
# task_complete is no, because the briefing tells us to assume that the task
# is not complete.

	task_complete = "No"
	task_number = num_of_tasks()
	
# Here the \n has to be at the back of the line of code, because the tasks text file won't necessarily have
# any tasks. This means that there won't be any blank spaces before the first task.

	tasks.write(f"{task_user}, {task_title}, {task_description}, {date_assigned}, {date_due}, {task_complete}, {task_number}\n")
	print("\nThank you, the new task has been added.")
	tasks.close()
#-----------------------------------------------------------------------------------
def view_all():
	print("Here are all the tasks:")
	tasks = open("tasks.txt","r+")
	for line in tasks:
		list = line.split(",")

# Each line in the list for tasks were put into a list.
# We know that the task will have 6 parts to it, namely:
# username, due date etc. The fact that we know this allows
# us to save each part of the line to a variable and name each
# variable. This makes it easier to display in a more user friendly manner.

		view_username = list[0]
		view_taskname = list[1]
		view_description = list[2]
		view_assigned_date = list[3]
		view_due_date = list[4]
		view_completed = list[5]
		view_task_number = (list[6]).strip()
		print(f"""
Task number: {view_task_number}
Name: {view_username}
Name of task: {view_taskname}
Description: {view_description}
Date assigned: {view_assigned_date}
Due date: {view_due_date}
Completed: {view_completed}
""")
	
	tasks.close()
#----------------------------------------------------------------------------------

# I added the code for the user to edit the tasks.
# I found it very difficult to edit the line in the text file
# and would have to revisit it at a later stage.

def view_mine():
	print("Here are all your tasks:")
	tasks = open("tasks.txt","r+")
	for line in tasks:
		list = line.split(",")
		view_username = list[0]
		view_taskname = list[1]
		view_description = list[2]
		view_assigned_date = list[3]
		view_due_date = list[4]
		view_completed = list[5]
		view_task_number = (list[6]).strip()
		if username == view_username:
			print(f"""
Task number: {view_task_number}
Name: {view_username}
Name of task: {view_taskname}
Description: {view_description}
Date assigned: {view_assigned_date}
Due date: {view_due_date}
Completed: {view_completed}
""")


		user_choice = int(input("Enter a task number to edit it or enter -1 to return to the menu: "))
		if user_choice == view_task_number:
			edit = input("Please type 'edit' to edit the task, 'comp' to mark as complete and '-1' to return to the menu: ")
			if edit == "edit" and view_completed != " Yes":
				new_user = input("Enter the new name of the new user in charge of the task: ")
				new_due_date = input("Enter the new due date of the task: ")
				new_user = view_username
				new_due_date = view_due_date
							
			elif edit == "comp":
				view_completed == " Yes"
	
		else:
			print()
	
	tasks.close()	
		
#-------------------------------------LOGIN----------------------------------------

users = open("user.txt","r+")
login = False

# This login code was from the video in dropbox, but there was one mistake.
# The code only reads the last line in the text file, which means that only
# the final name and password will be True when entered.
# This meant that the lines had to be stripped to strip the end-line break.
# I also added the variable current_date, because when a new task is added,
# the date assigned should be today's date.

#It is very important that the date be entered in the correct format, because ot influences 
# the checking of tasks that are overdue.
# Because of this, the program will close if not entered correctly.

print("""
Please make sure that when entering the date, you use the same format as the example (it is case sensitive).
Eg: 01 January 2001
""")
current_date = input("Please enter today's date: ")
current_date_list = current_date.split()
today_day = int(current_date_list[0])
today_month = current_date_list[1]
today_year = int(current_date_list[2])
if today_month == "January":
    today_month = int(110)
elif today_month == "February":
    today_month = int(120)
elif today_month == "March":
    today_month = int(130)
elif today_month == "April":
    today_month = int(140)
elif today_month == "May":
    today_month = int(150)
elif today_month == "June":
    today_month = int(160)
elif today_month == "July":
    today_month = int(170)
elif today_month == "August":
    today_month = int(180)
elif today_month == "September":
    today_month = int(190)
elif today_month == "October":
    today_month = int(200)
elif today_month == "November":
    today_month = int(210)
elif today_month == "December":
    today_month = int(220)
today_weight = (today_day / 100) + today_month + today_year
print("\n")

while login == False:
	username = input("Enter your username (it is case sensitive): ")
	password = input("Enter your password (it is case sensitive): ")
	
	for line in users:
		stripped_line = line.strip()
		valid_user, valid_password = stripped_line.split(", ")
		line += (line + "\n")
		
		if username == valid_user and password == valid_password:
			login = True
		
	if login == False:
		print("Incorrect details, please enter a valid username and password:")
	users.seek(0)
	
print(f"\nWelcome {username}!")

users.close()

#---------------------------TASK MANAGER---------------------------------------------
	
# I placed everyhting in a while loop, like the game assignment.
# This means that after a user completes doing one of the options below, they can do another without having to
# restart the program. They can quit when they want.

while 1:

# Depending on the username, they will receive a different menu.
# admin will receive a menu that includes the option to type 's'.

	if login == True and username == "admin":
		choice = input("""
-------------------------------------------------------------------------------
Please select one of the following options by typing the corresponding letter:
-------------------------------------------------------------------------------
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
-------------------------------------------------------------------------------
""")

	if login == True and username != "admin":
		choice = input("""
-------------------------------------------------------------------------------
Please select one of the following options by typing the corresponding letter:
-------------------------------------------------------------------------------
r - register user
a - add task
va - view all tasks
vm - view my tasks
e - exit
-------------------------------------------------------------------------------
""")

# I like to open and close the text files during every option.
# It feels more coherent that way.


#-------------------------------CREATE USER------------------------------------

	if choice == "r" and username == "admin":
		reg_user()
		
	if choice == "r" and username != "admin":
		print("You do not have authorisation to register users.")

#----------------------------CREATE TASK-----------------------------------------

	if choice == "a":
		add_task()

#-------------------------------VIEW ALL TASKS--------------------------------------
		
	if choice == "va":
		view_all()
	
#------------------------------VIEW MY TASKS----------------------------------------
	
	if choice == "vm":
		view_mine()
#------------------------------GENERATE REPORTS---------------------------------

	if choice == "gr":
		task_overview = open("task_overview.txt","w+")
		task_overview = open("task_overview.txt","r+")
		tasks = open("tasks.txt","r+")
		user_overview = open("user_overview.txt","w+")
		user_overview = open("user_overview.txt","r+")
		users = open("user.txt","r+")
		
# The task and user amount carried over from the previous task_manager assignment and was easy to reuse.
		
		task_amount = 0
		for line in tasks:
			if line[0] != "":
				task_amount += 1
		task_overview.write(f"Task amount = {task_amount}\n")
		user_overview.write(f"Task amount = {task_amount}\n")
		
		user_amount = 0
		for line in users:
			if line[0] != "":
				user_amount += 1
		user_overview.write(f"User amount = {user_amount}\n")
		
		incomplete_percentage = ((incomplete_tasks()) / (task_amount))*100
		overdue_percentage = ((overdue_tasks()) / (task_amount)) * 100
		
# The task_overview file is easier to work with, because the text file for tasks can be read
# as a whole, instead of having to focuse on specific indexes.
		
		task_overview.write(f"Completed tasks = {completed_tasks()}\n")
		task_overview.write(f"Incomplete tasks = {incomplete_tasks()}\n")
		task_overview.write(f"{incomplete_percentage}% of tasks are incomplete.\n")
		task_overview.write(f"Overdue tasks = {overdue_tasks()}\n")
		task_overview.write(f"{overdue_percentage}% of tasks are overdue.\n")
	
# In order to get the weight of the due date, I used the same method
# to calculate it, as I did with today's date.
# Later months carry more weight, which makes it easier,
# to find out if the user is past the due date.
# If the due date has more weigth than today's date
# the task is overdue.
	
		tasks = open("tasks.txt","r+")
		user_tasks = 0
		finished_task = 0
		not_and_overdue = 0
		name_of_user = input("Please choose the user to generate reports for: ")
		for line in tasks:
			completed_task = line.split(", ")
			did_complete = completed_task[5]
			given_date = completed_task[3]
			due_date = completed_task[4]
			given_day = int(given_date.split()[0])
			given_month = given_date.split()[1]
			given_year = int(given_date.split()[2])
			due_day = int(due_date.split()[0])
			due_month = due_date.split()[1]
			due_year = int(due_date.split()[2])
			if due_month == "January":
				due_month = int(110)
			elif due_month == "February":
				due_month = int(120)
			elif due_month == "March":
				due_month = int(130)
			elif due_month == "April":
				due_month = int(140)
			elif due_month == "May":
				due_month = int(150)
			elif due_month == "June":
				due_month = int(160)
			elif due_month == "July":
				due_month = int(170)
			elif due_month == "August":
				due_month = int(180)
			elif due_month == "September":
				due_month = int(190)
			elif due_month == "October":
				due_month = int(200)
			elif due_month == "November":
				due_month = int(210)
			elif due_month == "December":
				due_month = int(220)
			due_weight = (due_day / 100) + due_month + due_year
			
			if completed_task[0] == (name_of_user):
				user_tasks += 1			
				
			if completed_task[0] == name_of_user and completed_task[5] == " Yes":
				finished_task += 1				
					
			if completed_task[0] == name_of_user and due_weight > today_weight and completed_task[5] == " No":
				not_and_overdue += 1
		
# The calculations below takes the name of any user and displays the statistics
# of this user as the briefing asks.
# This makes it easier to pinpoint a specific person in the company,
# for his/her performance review.
		
		completed_task_percentage = (finished_task / user_tasks) * 100
		incomplete_task_percentage = 100 - completed_task_percentage
		task_percentage = (user_tasks / task_amount) * 100
		not_completed = user_tasks - finished_task	
		full_not_and_overdue = (not_and_overdue / user_tasks) * 100
			
		user_overview.write(f"{name_of_user} has {user_tasks} tasks assigned.\n")
		user_overview.write(f"{task_percentage}% of tasks has been assigned to {name_of_user}.\n")
		user_overview.write(f"{name_of_user} has completed {completed_task_percentage}% of his/her tasks.\n")
		user_overview.write(f"{name_of_user} still needs to complete {incomplete_task_percentage}% of his/her tasks.\n")
		user_overview.write(f"{full_not_and_overdue}% of {name_of_user}'s tasks are incomplete and overdue.\n")
		
				
		tasks.close()
		users.close()
		task_overview.close()
		user_overview.close()
		
		print("Thank you, the reports have been generated.")

#--------------------------------STATISTICS-----------------------------------------

# The code below displays the two text files, user_overview and task_overview.
# When writing to the files, I wrote it in a very user friendly way,
# This means that the code doesn't need to be edited further to be easily read
# and can only be printed as is.	
	
	if choice == "ds" and username == "admin":
		print("-------------------------------------")
		print("Here are the current task statistics:")
		print("-------------------------------------")
		task_overview = open("task_overview.txt","r")
		for line in task_overview:
			print(line)
		print("-------------------------------------")
		print("Here are the current user statistics:")
		print("-------------------------------------")
		user_overview = open("user_overview.txt","r")
		for line in user_overview:
			print(line)
				
		task_overview.close()
		user_overview.close()
		
#---------------------------------EXIT---------------------------------------------------
	
	if choice == "e":
		input('\nPress ENTER to exit')
		exit(0)

#----------------------------------END---------------------------------------------------

# Overall I am not very happy with this assignment, but I believe that it is good enough to
# move on to level two of the course.
# I will return to this assignment, to finetune any redundant code,
# before I consider adding it to my portfolio.
