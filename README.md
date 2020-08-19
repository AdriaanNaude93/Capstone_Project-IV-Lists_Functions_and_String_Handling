# Capstone_Project-IV-Lists_Functions_and_String_Handling
This program is a task manager aimed at allowing a company to easily set tasks for users and keep track of their progress. It deals heavily with the use of lists and saving user inputted information to text files and recalling this information as needed.

The program comes with at least one user already saved in the text file called admin. This user has more functionality over the program as it can view statistics and register new users.

## How it works
Once the user open the program, they will be greeted with a question that asks for the date. This date is used to see if tasks are overdue, as well as the date assigned when creating a new task.

After this, the user is prompted to input their login details. All the details for each user are stored in a text file and the program scans this file to see if the correct information has been entered. If the user inputs incorrect information, they are prompted to try again until the correct username and password compination is reached.

Once logged in, the user has the option to initiate certain commands. As stated in the intro, the admin user has more power. If the user is not admin, they can do the following:
1. Add a task
2. View all tasks
3. View my tasks

Depending on the choice of the user, they can either add tasks, which will prompt the user to enter information relating to the task, such as due date etc. The input from the user will then be saved in a text file that is used to view tasks.

If the user chooses view all tasks, or view my tasks, they will either be given all the information regarding all the tasks in the text file, or only the ones that have their username in it.

If the user logs in with the admin information, they will have more options to choose from. They will be able to do the following:
1. Register a user
2. Add a task
3. View all tasks
4. View my tasks
5. Generate reports
6. Display statistics

The admin user is able to register more users which will be added to the relevant text file. Tasks can also be added and viewed, but one of the cooler aspects of the admin's abilities is that they can generate and display statictics. If the user chooses the generate reports, they can choose which user to do it for. The admin can then choose to view the statistics after which they will be greeted with statistics relating to the tasks and users.

As stated previously, there are text files for users and tasks in which information is stored. The statistics is stored in two other text files called task_overview and user_overview. As the names suggest, each text file stores information regarding tasks and users.

The task_overview file stores and will display, if asked:
1. Task amount
2. Completed tasks
3. Incomplete tasks
4. Percentage of incomplete tasks
5. Overdue tasks
6. Percentage of tasks overdue

The user_overview file stores and will display, if asked:
1. Task amount 
2. User amount

### The program aims to streamline the process of task management by supplying the user with a way to easily monitor user tasks and keep track of how effective an operation is functioning.

## What I learned
1. How to store user input in lists
2. How to save to and display text files
3. The importance of loops, especially during login
4. Keeping programs simple and easy to use
5. Comfortability with lists, functions and string handling.
