## Project name: Expense Management 

# Project Issue/Problem to Be Solved: 
Managing personal finances is often a challenge for many people. This project addresses the problem by providing a digital solution to:
	- Record daily expenses easily.
	-  Categorize expenses (e.g., food, travel, bills).
	-  Generate monthly summaries to help users track spending habits.

# Current Progress (PDLC: Problem Analysis, Design, etc.)

	• Problem Analysis:
	This project addresses the challenge of managing personal finances by providing a digital solution to easily record daily expenses, categorize them (e.g., food, travel, bills), and generate monthly summaries to help users track and understand their spending habits.
	• System Design:
	Database Design: Two primary tables:
		User data: Stores user id, username and password.
		User expense: each user expense details.
	User Interface: A tabbed user interface organizes different sections or features Dashboard, Add Expense, Update Expense, Delete Expense, View Expenses, and Reports into tabs for easy navigation and efficient space use.
	• Development: 
		▫ the backend functionalities in your project handle storing, managing, and generating monthly summaries of expense records using SQLite.
		▫ ueses Tkinter to create a  GUI, enabling intuitive navigation for entering expenses and viewing summaries.
		▫ Basic error handling and validations implemented.
	• Project Functions / Features
	Core Features:
		▫ User Authentication: Login, sign up, password management.
		▫ Data Management: Add, update, delete, and view records.
		▫ Search Functionality: Search for data or items within the system.
		▫ Reporting: Generate reports based on user inputs or stored data.
	• Additional Features:
		▫ Error handling for invalid inputs:  ensures that the system can handle cases where users provide non-numeric or invalid values for expense amount. 
		▫ Unique license plate validation: checks if a license plate entered by the user is unique and not already in use.
	• Planned Enhancements:
		▫ Export or import data in various formats (e.g., CSV, PDF)
		▫ Display data-driven insights through charts or graphs
	
	
# Expected Pages

	• Homepage: login or SignUp to log in with a username and password or create an account.
	• Dashboard Page: provides navigation to other functionalities.
	• Add Expense Page: to add new expenses to the system
	• Update Expense Page: to update existing expenses.
	• Delete Expense Page: to delete an existing expense.
	• View Expenses Page: displays a list of all recorded expenses.
	• Reports Page: Generate monthly summaries in each category
	
# Database Applied (Table Plus)
Tables:
	Expense Table: expense details (username, expense name, category, amount, date, note).
	User Table:  user id, username, user password.
Records:
	Download Table Plus to see
	Dynamic entries for cars and sales based on user input.

# Project Reference / Source

Tutorials:
https://stackoverflow.com/questions/44308137/how-to-pass-credentials-through-code-instead-of-requesting-user
https://stackoverflow.com/questions/71238320/python-tkinter-simpledialog
How to Debug in Visual Studio: A Beginner's Guide 
How to install SQLite3 on Windows 10/11 [2024 Update] Create Database, Table in SQL | Complete Guide 
Sqlite 3 Python Tutorial in 5 minutes - Creating Database, Tables and Querying [2020] 
https://community.fly.io/t/connect-to-sqlite-of-app-through-db-gui-tableplus/10791
https://www.cursorup.com/blog/laws-of-ux
https://www.wisecube.ai/blog/knowledge-graphs-vs-relational-databases-everything-you-need-to-know/ 

 
# Defining System Requirements

# Functionalities:
	• User management
	• Expense management
	• Generate report
# Technical Requirements:
		▫ Python 3.8+.
		▫ VScode
		▫ SQLite for database management.
		▫ Tkinter for GUI
		▫ Download Table Plus to view the database table. 
# Required Software and Libraries
Python 3.8+
Required Python libraries:
		▫ kinter: Comes bundled with Python as part of the standard library.
		▫ sqlite3: Also included with Python in the standard library.
# Installation Instructions

		▫ Install Python 3.8+: Download Python
		▫ Install TablePlus (optional for viewing databases)
		▫ Download TablePlus

# Run the Application
Clone or download the repository.
Open a terminal/command prompt.
	- Navigate to the project directory: cd path/to/ExpenseManagement
	- Run the main application file:  python main.py

# Configuration Settings
No configuration changes required. The application automatically uses the expense.db and expense_data.json files.
	
# Dependencies
SQLite for database storage (no installation needed).
TablePlus (optional) to view and manage your SQLite database.

     
![image](https://github.com/user-attachments/assets/8fcb6acd-9063-4b6f-8ba5-69f333d0b364)


# GUI 
![Screenshot 2024-11-24 224511](https://github.com/user-attachments/assets/5ae1b4b6-1dd1-46d9-8855-53e50152b700)
![Screenshot 2024-11-24 224526](https://github.com/user-attachments/assets/511e806c-98d3-4997-ae63-2e6ecc981284)
![Screenshot 2024-11-24 224545](https://github.com/user-attachments/assets/d4be4914-c1af-482f-8fb3-1c9a679a6b9e)
![Screenshot 2024-11-24 224604](https://github.com/user-attachments/assets/3c46c823-882a-4800-99ba-afadced26bc2)
![Screenshot 2024-11-24 224949](https://github.com/user-attachments/assets/9c2194a9-6991-4dcc-8309-39ebffae7b07)
![Screenshot 2024-11-24 225003](https://github.com/user-attachments/assets/b3440e49-3755-4bac-b3d8-e0d67092a4bb)
![Screenshot 2024-11-24 225027](https://github.com/user-attachments/assets/7b90c542-298e-4fdd-90db-34d8a5d4ab71)


