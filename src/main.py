import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from database import Database 
import tkinter.simpledialog as simpledialog
from collections import defaultdict


class ExpenseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Management")
        self.geometry("900x600")
        self.config(bg="#f7f7f7")

        self.db = Database()  
        self.users = self.db.load_users_data()
        self.current_user = None  
        self.expenses = []

        self.frames = {}
        self.show_frame("Login")

    def load_expense_data(self):
        if self.current_user:
            self.expenses = self.db.load_expense_data(self.current_user)

    def save_expense_data(self):
        if self.current_user:
            self.db.save_expense_data(self.current_user, self.expenses)

    def save_users_data(self):
        self.db.save_users_data(self.users)

    def show_frame(self, frame_name):
        frame = self.frames.get(frame_name)
        if frame is None:
            if frame_name == "Login":
                frame = LoginFrame(self)
            elif frame_name == "SignUp":
                frame = SignUpFrame(self)
            elif frame_name == "Dashboard":
                frame = DashboardFrame(self)
            elif frame_name == "AddExpense":
                frame = AddExpenseFrame(self)
            elif frame_name == "UpdateExpense":
                frame = UpdateExpenseFrame(self)
            elif frame_name == "DeleteExpense":
                frame = DeleteExpenseFrame(self)
            elif frame_name == "ViewExpenses":
                frame = ViewExpensesFrame(self)
            elif frame_name == "Reports":
                frame = ReportsFrame(self)

            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        frame.tkraise()

class BaseFrame(tk.Frame):
    def __init__(self, app):
        super().__init__(app)
        self.app = app

class LoginFrame(BaseFrame):
    def __init__(self, app):
        super().__init__(app)
        self.config(bg="#FBFCF8")

        title_label = tk.Label(self, text="Login", font=("Helvetica", 24, "bold"), bg="#FBFCF8")
        title_label.pack(pady=20)

        self.username = self.create_input_field("Username:")
        self.password = self.create_input_field("Password:", show="*")

        login_button = tk.Button(self, text="Login", command=self.login, font=("Helvetica", 14), bg="#728156", fg="white", relief="raised")
        login_button.pack(pady=20, padx=50, fill="x")

        signup_button = tk.Button(self, text="Don't have an account? Sign Up", command=lambda: self.app.show_frame("SignUp"),
                                  font=("Helvetica", 12), bg="#ed7061", fg="white", relief="raised")
        signup_button.pack(pady=10)

    def create_input_field(self, label, **kwargs):
        frame = tk.Frame(self, bg="#FBFCF8")
        frame.pack(pady=5, padx=50, fill="x")

        label_widget = tk.Label(frame, text=label, font=("Helvetica", 14), bg="#FBFCF8")
        label_widget.pack(side="left", padx=10)

        entry = tk.Entry(frame, font=("Helvetica", 14), bd=2, relief="solid", **kwargs)
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if username in self.app.users and self.app.users[username] == password:
            self.app.current_user = username
            self.app.load_expense_data()
            self.app.show_frame("Dashboard")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

class SignUpFrame(BaseFrame):
    def __init__(self, app):
        super().__init__(app)
        self.config(bg="#FBFCF8")

        title_label = tk.Label(self, text="Sign Up", font=("Helvetica", 24, "bold"), bg="#FBFCF8")
        title_label.pack(pady=20)

        self.username = self.create_input_field("Username:")
        self.password = self.create_input_field("Password:", show="*")

        signup_button = tk.Button(self, text="Sign Up", command=self.sign_up, font=("Helvetica", 14), bg="#ed7061", fg="white", relief="raised")
        signup_button.pack(pady=20, padx=50, fill="x")

        login_button = tk.Button(self, text="Already have an account? Login", command=lambda: self.app.show_frame("Login"),
                                 font=("Helvetica", 12), bg="#728156", fg="white", relief="raised")
        login_button.pack(pady=10)

    def create_input_field(self, label, **kwargs):
        frame = tk.Frame(self, bg="#FBFCF8")
        frame.pack(pady=5, padx=50, fill="x")

        label_widget = tk.Label(frame, text=label, font=("Helvetica", 14), bg="#FBFCF8")
        label_widget.pack(side="left", padx=10)

        entry = tk.Entry(frame, font=("Helvetica", 14), bd=2, relief="solid", **kwargs)
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def sign_up(self):
        username = self.username.get()
        password = self.password.get()

        if username in self.app.users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            self.app.users[username] = password
            self.app.save_users_data()
            messagebox.showinfo("Success", "Account created successfully!")
            self.app.show_frame("Login")

class DashboardFrame(BaseFrame):
    def __init__(self, app):
        super().__init__(app)
        self.config(bg="#FBFCF8")

        title_label = tk.Label(self, text=f"Welcome {self.app.current_user}!", font=("Helvetica", 24, "bold"), bg="#FBFCF8" )
        title_label.pack(pady=30)

        add_button = tk.Button(self, text="Add Expense", width=20, height=2, command=lambda: self.app.show_frame("AddExpense"),
                               font=("Helvetica", 14), bg="#333d29", fg="white", relief="raised")
        add_button.pack(pady=10)

        update_button = tk.Button(self, text="Update Expense", width=20, height=2, command=lambda: self.app.show_frame("UpdateExpense"),
                                  font=("Helvetica", 14), bg="#414833", fg="white", relief="raised")
        update_button.pack(pady=10)

        delete_button = tk.Button(self, text="Delete Expense", width=20, height=2, command=lambda: self.app.show_frame("DeleteExpense"),
                                  font=("Helvetica", 14), bg="#656d4a", fg="white", relief="raised")
        delete_button.pack(pady=10)

        view_button = tk.Button(self, text="View All Expenses", width=20, height=2, command=lambda: self.app.show_frame("ViewExpenses"),
                                font=("Helvetica", 14), bg="#a4ac86", fg="white", relief="raised")
        view_button.pack(pady=10)

        reports_button = tk.Button(self, text="View Reports", width=20, height=2, command=lambda: self.app.show_frame("Reports"),
                                   font=("Helvetica", 14), bg="#936639", fg="white", relief="raised")
        reports_button.pack(pady=10)

        logout_button = tk.Button(self, text="Logout", width=20, height=2, command=self.logout,
                                  font=("Helvetica", 14), bg="#dc3e41", fg="white", relief="raised")
        logout_button.pack(pady=30)

    def logout(self):
        self.app.current_user = None
        self.app.show_frame("Login")

class AddExpenseFrame(BaseFrame):
    def __init__(self, app):
        super().__init__(app)
        self.config(bg="#FBFCF8")

        title_label = tk.Label(self, text="Add Expense", font=("Helvetica", 24, "bold"), bg="#FBFCF8")
        title_label.pack(pady=20)

        self.expense_name = self.create_input_field("Expense Name:")
        self.category = self.create_input_field("Category:")
        self.amount = self.create_input_field("Amount (USD):")
        self.date = self.create_input_field("Date (YYYY-MM-DD):", datetime.now().strftime("%Y-%m-%d"))
        self.note = self.create_input_field("Note:")

        add_button = tk.Button(self, text="Add Expense", command=self.add_expense, font=("Helvetica", 14), bg="#ed7061", fg="white", relief="raised")
        add_button.pack(pady=20, padx=50, fill="x")

        back_button = tk.Button(self, text="Back to Dashboard", command=lambda: self.app.show_frame("Dashboard"),
                                font=("Helvetica", 14), bg="#728156", fg="white", relief="raised")
        back_button.pack(pady=10, padx=50, fill="x")

    def create_input_field(self, label, default_text=""):
        frame = tk.Frame(self, bg="#FBFCF8")
        frame.pack(pady=5, padx=50, fill="x")

        label_widget = tk.Label(frame, text=label, font=("Helvetica", 14), bg="#FBFCF8")
        label_widget.pack(side="left", padx=10)

        entry = tk.Entry(frame, font=("Helvetica", 14), bd=2, relief="solid")
        entry.insert(0, default_text)
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def add_expense(self):
        try:
            expense_name = self.expense_name.get()
            category = self.category.get()
            amount = self.amount.get()
            
            if not amount.replace('.', '', 1).isdigit(): 
                raise ValueError("Amount must be a valid number.")
            amount = float(amount)  
            date = self.date.get()
            note = self.note.get()
            
            if expense_name and category and amount > 0 and date:
                new_expense = {"name": expense_name, "category": category, "amount": amount, "date": date, "note": note}
                self.app.expenses.append(new_expense)
                self.app.save_expense_data()

                # Refresh the expense list in the dashboard and other relevant frames
                if 'ViewExpenses' in self.app.frames:
                    self.app.frames['ViewExpenses'].populate_expense_table()
                if 'UpdateExpense' in self.app.frames:
                    self.app.frames['UpdateExpense'].populate_expense_list()
                if 'DeleteExpense' in self.app.frames:
                    self.app.frames['DeleteExpense'].populate_expense_list()

                messagebox.showinfo("Success", f"Expense '{expense_name}' added successfully!")
                self.app.show_frame("Dashboard")
            else:
                messagebox.showerror("Error", "All fields are required, and amount must be positive.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

                
class UpdateExpenseFrame(BaseFrame):
    def __init__(self, app):
        super().__init__(app)
        self.config(bg="#FBFCF8")

        title_label = tk.Label(self, text="Update Expense", font=("Helvetica", 24, "bold"), bg="#FBFCF8")
        title_label.pack(pady=20)

        self.expense_list = ttk.Combobox(self, font=("Helvetica", 14), state="readonly")
        self.expense_list.pack(pady=10, padx=50, fill="x")
        self.populate_expense_list()

        update_button = tk.Button(self, text="Update Selected Expense", command=self.update_expense, font=("Helvetica", 14),
                                  bg="#505d7d", fg="white", relief="raised")
        update_button.pack(pady=20, padx=50, fill="x")

        back_button = tk.Button(self, text="Back to Dashboard", command=lambda: self.app.show_frame("Dashboard"),
                                font=("Helvetica", 14), bg="#728156", fg="white", relief="raised")
        back_button.pack(pady=10, padx=50, fill="x")

    def populate_expense_list(self):
        self.expense_list["values"] = [f"{i + 1}. {expense['name']} - ${expense['amount']}" for i, expense in enumerate(self.app.expenses)]

    def update_expense(self):
        selected_index = self.expense_list.current()
        if selected_index >= 0:
            expense = self.app.expenses[selected_index]
            new_amount = simpledialog.askfloat("Update Amount", f"Update amount for {expense['name']}:")
            if new_amount:
                expense["amount"] = new_amount
                self.app.save_expense_data()
                self.populate_expense_list()
                messagebox.showinfo("Success", "Expense updated successfully!")
        else:
            messagebox.showerror("Error", "No expense selected.")


class DeleteExpenseFrame(BaseFrame):
    def __init__(self, app):
        super().__init__(app)
        self.config(bg="#FBFCF8")

        title_label = tk.Label(self, text="Delete Expense", font=("Helvetica", 24, "bold"), bg="#FBFCF8")
        title_label.pack(pady=20)

        self.expense_list = ttk.Combobox(self, font=("Helvetica", 14), state="readonly")
        self.expense_list.pack(pady=10, padx=50, fill="x")
        self.populate_expense_list()

        delete_button = tk.Button(self, text="Delete Selected Expense", command=self.delete_expense, font=("Helvetica", 14),
                                  bg="#ed7061", fg="white", relief="raised")
        delete_button.pack(pady=20, padx=50, fill="x")

        back_button = tk.Button(self, text="Back to Dashboard", command=lambda: self.app.show_frame("Dashboard"),
                                font=("Helvetica", 14), bg="#728156", fg="white", relief="raised")
        back_button.pack(pady=10, padx=50, fill="x")

    def populate_expense_list(self):
        self.expense_list["values"] = [f"{i + 1}. {expense['name']} - ${expense['amount']}" for i, expense in enumerate(self.app.expenses)]

    def delete_expense(self):
        selected_index = self.expense_list.current()
        if selected_index >= 0:
            del self.app.expenses[selected_index]
            self.app.save_expense_data()
            self.populate_expense_list()
            messagebox.showinfo("Success", "Expense deleted successfully!")
        else:
            messagebox.showerror("Error", "No expense selected.")

class DeleteExpenseFrame(BaseFrame):
    def __init__(self, app):
        super().__init__(app)
        self.config(bg="#FBFCF8")

        title_label = tk.Label(self, text="Delete Expense", font=("Helvetica", 24, "bold"), bg="#FBFCF8")
        title_label.pack(pady=20)

        self.expense_list = ttk.Combobox(self, font=("Helvetica", 14), state="readonly")
        self.expense_list.pack(pady=10, padx=50, fill="x")
        self.populate_expense_list()

        delete_button = tk.Button(self, text="Delete Selected Expense", command=self.delete_expense, font=("Helvetica", 14),
                                  bg="#ed7061", fg="white", relief="raised")
        delete_button.pack(pady=20, padx=50, fill="x")

        back_button = tk.Button(self, text="Back to Dashboard", command=lambda: self.app.show_frame("Dashboard"),
                                font=("Helvetica", 14), bg="#728156", fg="white", relief="raised")
        back_button.pack(pady=10, padx=50, fill="x")

    def populate_expense_list(self):
        """Populate combobox with expense names and amounts, keeping track of indices"""
        self.expense_list["values"] = [f"{i + 1}. {expense['name']} - ${expense['amount']}" for i, expense in enumerate(self.app.expenses)]

    def delete_expense(self):
        """Delete the selected expense from the list"""
        selected_value = self.expense_list.get() 
        if selected_value:

            index = int(selected_value.split(".")[0]) - 1 
            if 0 <= index < len(self.app.expenses):  
                del self.app.expenses[index] 
                self.app.save_expense_data()  
                self.populate_expense_list()  
                messagebox.showinfo("Success", "Expense deleted successfully!")
            else:
                messagebox.showerror("Error", "Invalid expense index.")
        else:
            messagebox.showerror("Error", "No expense selected.")


class ViewExpensesFrame(BaseFrame):
    def __init__(self, app):
        super().__init__(app)
        self.config(bg="#FBFCF8")

        title_label = tk.Label(self, text="View All Expenses", font=("Helvetica", 24, "bold"), bg="#FBFCF8")
        title_label.pack(pady=20)

        self.expense_table = ttk.Treeview(self, columns=("Expense", "Category", "Amount($)", "Date", "Note"), show="headings")
        self.expense_table.pack(fill="both", padx=50, pady=20, expand=True)

        self.expense_table.heading("Expense", text="Expense")
        self.expense_table.heading("Category", text="Category")
        self.expense_table.heading("Amount($)", text="Amount($)")
        self.expense_table.heading("Date", text="Date")
        self.expense_table.heading("Note", text="Note")

        self.populate_expense_table()

        back_button = tk.Button(self, text="Back to Dashboard", command=lambda: self.app.show_frame("Dashboard"),
                                font=("Helvetica", 14), bg="#728156", fg="white", relief="raised")
        back_button.pack(pady=10)

    def populate_expense_table(self):
        for row in self.expense_table.get_children():
            self.expense_table.delete(row)

        for expense in self.app.expenses:
            self.expense_table.insert("", "end", values=(expense["name"], expense["category"], expense["amount"], expense["date"], expense["note"]))


class ReportsFrame(BaseFrame):
    def __init__(self, app):
        super().__init__(app)
        self.config(bg="#FBFCF8")

        title_label = tk.Label(self, text="Expense Reports 📊", font=("Helvetica", 24, "bold"), bg="#FBFCF8")
        title_label.pack(pady=20)

        self.report_text = tk.Text(self, font=("Helvetica", 14), wrap="word", height=10, width=50, bd=2, relief="solid")
        self.report_text.pack(pady=20, padx=50)

        self.generate_report()

        back_button = tk.Button(self, text="Back to Dashboard", command=lambda: self.app.show_frame("Dashboard"),
                                font=("Helvetica", 14), bg="#728156", fg="white", relief="raised")
        back_button.pack(pady=10, padx=50, fill="x")

    def generate_report(self):
 
        monthly_totals = self.calculate_monthly_totals()

        self.report_text.delete(1.0, tk.END)

        report_header = "Monthly Spending Summary\n" + "="*40 + "\n"
        self.report_text.insert(tk.END, report_header)

        for month, totals in monthly_totals.items():
            self.report_text.insert(tk.END, f"{month}: ${totals['total']:.2f}\n")
            for category, amount in totals['categories'].items():
                self.report_text.insert(tk.END, f"  - {category}: ${amount:.2f}\n")
            self.report_text.insert(tk.END, "-"*40 + "\n")

    def calculate_monthly_totals(self):

        monthly_totals = defaultdict(lambda: {"total": 0, "categories": defaultdict(float)})

        for expense in self.app.expenses:

            date = datetime.strptime(expense['date'], "%Y-%m-%d")
            month = date.strftime("%B %Y")  
            category = expense['category']
            amount = expense['amount']

            monthly_totals[month]["total"] += amount
            monthly_totals[month]["categories"][category] += amount

        return monthly_totals

if __name__ == "__main__":
    app = ExpenseApp()
    app.mainloop()
