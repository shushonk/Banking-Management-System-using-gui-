from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk


class BankSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank Management System")
        self.master.geometry("800x450")  # Reduced window size for shorter output
        self.master.config(bg="white")
        self.master.bind('<q>', self.exit_program)  # Bind Q key to exit program

        self.users = {}  # Dictionary to store user data

        # Create Account Frame (Visible initially)
        self.create_account_frame = Frame(self.master, bg="white", bd=2, relief="solid")
        self.create_account_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=350)

        self.login_frame = Frame(self.master, bg="white", bd=2, relief="solid")
        self.name = ""
        self.age = ""
        self.salary = ""
        self.pin = ""
        self.current_balance = 0
        self.transaction_log = []

        self.create_account_widgets()

    def create_account_widgets(self):
        self.title_label = Label(self.create_account_frame, text="Create Account", font=("Helvetica", 18, "bold"), fg="#333", bg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=15)

        self.name_label = Label(self.create_account_frame, text="Name:", font=("Helvetica", 12), bg="white")
        self.name_label.grid(row=1, column=0, padx=15, pady=8, sticky="w")
        self.name_entry = Entry(self.create_account_frame, font=("Helvetica", 12), bg="#f7f7f7", relief="solid", borderwidth=1)
        self.name_entry.grid(row=1, column=1, padx=15, pady=8)

        self.age_label = Label(self.create_account_frame, text="Age:", font=("Helvetica", 12), bg="white")
        self.age_label.grid(row=2, column=0, padx=15, pady=8, sticky="w")
        self.age_entry = Entry(self.create_account_frame, font=("Helvetica", 12), bg="#f7f7f7", relief="solid", borderwidth=1)
        self.age_entry.grid(row=2, column=1, padx=15, pady=8)

        self.salary_label = Label(self.create_account_frame, text="Salary:", font=("Helvetica", 12), bg="white")
        self.salary_label.grid(row=3, column=0, padx=15, pady=8, sticky="w")
        self.salary_entry = Entry(self.create_account_frame, font=("Helvetica", 12), bg="#f7f7f7", relief="solid", borderwidth=1)
        self.salary_entry.grid(row=3, column=1, padx=15, pady=8)

        self.pin_label = Label(self.create_account_frame, text="PIN:", font=("Helvetica", 12), bg="white")
        self.pin_label.grid(row=4, column=0, padx=15, pady=8, sticky="w")
        self.pin_entry = Entry(self.create_account_frame, show="*", font=("Helvetica", 12), bg="#f7f7f7", relief="solid", borderwidth=1)
        self.pin_entry.grid(row=4, column=1, padx=15, pady=8)

        self.create_account_button = Button(self.create_account_frame, text="Create Account", command=self.create_account, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff", relief="solid", width=20, height=2, bd=2)
        self.create_account_button.grid(row=5, column=0, columnspan=2, pady=15)

        self.switch_to_login_button = Button(self.create_account_frame, text="Already have an account? Login", command=self.show_login_frame, font=("Helvetica", 10), fg="#1a73e8", bg="white", relief="flat", width=25)
        self.switch_to_login_button.grid(row=6, column=0, columnspan=2, pady=8)

    def show_login_frame(self):
        self.create_account_frame.place_forget()
        self.login_frame = Frame(self.master, bg="white", bd=2, relief="solid")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=300)

        self.title_label = Label(self.login_frame, text="Login", font=("Helvetica", 18, "bold"), fg="#333", bg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=15)

        self.login_name_label = Label(self.login_frame, text="Name:", font=("Helvetica", 12), bg="white")
        self.login_name_label.grid(row=1, column=0, padx=15, pady=8, sticky="w")
        self.login_name_entry = Entry(self.login_frame, font=("Helvetica", 12), bg="#f7f7f7", relief="solid", borderwidth=1)
        self.login_name_entry.grid(row=1, column=1, padx=15, pady=8)

        self.login_pin_label = Label(self.login_frame, text="PIN:", font=("Helvetica", 12), bg="white")
        self.login_pin_label.grid(row=2, column=0, padx=15, pady=8, sticky="w")
        self.login_pin_entry = Entry(self.login_frame, show="*", font=("Helvetica", 12), bg="#f7f7f7", relief="solid", borderwidth=1)
        self.login_pin_entry.grid(row=2, column=1, padx=15, pady=8)

        self.login_button = Button(self.login_frame, text="Login", command=self.login, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff", relief="solid", width=20, height=2, bd=2)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=15)

        self.switch_to_create_account_button = Button(self.login_frame, text="Don't have an account? Create one", command=self.show_create_account_frame, font=("Helvetica", 10), fg="#1a73e8", bg="white", relief="flat", width=25)
        self.switch_to_create_account_button.grid(row=4, column=0, columnspan=2, pady=8)

    def show_create_account_frame(self):
        self.login_frame.place_forget()
        self.create_account_frame = Frame(self.master, bg="white", bd=2, relief="solid")
        self.create_account_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=350)
        self.create_account_widgets()

    def create_account(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        salary = self.salary_entry.get()
        pin = self.pin_entry.get()

        # Validate input
        if not name or not age or not salary or not pin:
            messagebox.showerror("Error", "All fields are required!")
            return
        if not age.isdigit():
            messagebox.showerror("Error", "Age must be a number!")
            return
        if not salary.isdigit():
            messagebox.showerror("Error", "Salary must be a number!")
            return
        if not pin.isdigit() or len(pin) != 4:
            messagebox.showerror("Error", "PIN must be a 4-digit number!")
            return

        user_data = {'name': name, 'age': age, 'salary': salary, 'pin': pin, 'balance': 0, 'transaction_log': []}
        self.users[pin] = user_data

        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.salary_entry.delete(0, END)
        self.pin_entry.delete(0, END)

        messagebox.showinfo("Success", "Account created successfully!")

    def login(self):
        name = self.login_name_entry.get()
        pin = self.login_pin_entry.get()

        if pin in self.users and self.users[pin]['name'] == name:
            self.current_user_data = self.users[pin]
            self.create_user_dashboard()  # Create the user dashboard

            # Hide login screen and show user dashboard
            self.login_frame.place_forget()
            self.update_user_details()  # Update user details on the dashboard

        else:
            messagebox.showerror("Error", "Invalid PIN or UserName")

    def update_user_details(self):
        self.name_label2 = Label(self.user_dashboard, text="Name: " + self.current_user_data['name'], font=('Arial', 12), bg="white")
        self.name_label2.grid(row=0, column=0, padx=10, pady=8)
        self.age_label2 = Label(self.user_dashboard, text="Age: " + self.current_user_data['age'], font=('Arial', 12), bg="white")
        self.age_label2.grid(row=1, column=0, padx=10, pady=8)
        self.salary_label2 = Label(self.user_dashboard, text="Salary: " + self.current_user_data['salary'], font=('Arial', 12), bg="white")
        self.salary_label2.grid(row=2, column=0, padx=10, pady=8)
        self.current_balance_label = Label(self.user_dashboard, text="Current Balance: " + str(self.current_user_data['balance']), font=('Arial', 12), bg="white")
        self.current_balance_label.grid(row=3, column=0, padx=10, pady=8)

    def create_user_dashboard(self):
        self.user_dashboard = Frame(self.master, bg="white", bd=2, relief="solid")
        self.user_dashboard.place(relx=0.5, rely=0.5, anchor="center", width=450, height=350)

        self.deposit_button = Button(self.user_dashboard, text="Deposit", command=self.deposit, font=('Arial', 12), bg='#4CAF50', fg='#ffffff', relief="solid", width=20, height=2, bd=2)
        self.deposit_button.grid(row=4, column=0, padx=10, pady=10)

        self.withdraw_button = Button(self.user_dashboard, text="Withdraw", command=self.withdraw, font=('Arial', 12), bg='#FF5733', fg='#ffffff', relief="solid", width=20, height=2, bd=2)
        self.withdraw_button.grid(row=5, column=0, padx=10, pady=10)

        self.transaction_log_button = Button(self.user_dashboard, text="View Transaction Log", command=self.view_transaction_log, font=('Arial', 12), bg='#337AB7', fg='#ffffff', relief="solid", width=20, height=2, bd=2)
        self.transaction_log_button.grid(row=6, column=0, padx=10, pady=10)

        self.logout_button = Button(self.user_dashboard, text="Logout", command=self.logout, font=('Arial', 12), bg='#D9534F', fg='#ffffff', relief="solid", width=20, height=2, bd=2)
        self.logout_button.grid(row=7, column=0, padx=10, pady=10)

    def deposit(self):
        amount = simpledialog.askstring("Deposit", "Enter amount:")
        if not amount or not amount.isdigit() or int(amount) <= 0:
            messagebox.showerror("Error", "Invalid input!")
            return
        
        amount = int(amount)
        self.current_user_data['balance'] += amount
        self.update_user_details()

        transaction = f"Deposit: +{amount}, New Balance: {self.current_user_data['balance']}"
        self.current_user_data['transaction_log'].append(transaction)

    def withdraw(self):
        amount = simpledialog.askstring("Withdraw", "Enter amount:")
        if not amount or not amount.isdigit() or int(amount) <= 0:
            messagebox.showerror("Error", "Invalid amount!")
            return

        amount = int(amount)
        if amount > self.current_user_data['balance']:
            messagebox.showerror("Error", "Insufficient balance!")
            return

        self.current_user_data['balance'] -= amount
        self.update_user_details()

        transaction = f"Withdraw: -{amount}, New Balance: {self.current_user_data['balance']}"
        self.current_user_data['transaction_log'].append(transaction)

    def view_transaction_log(self):
        transaction_log_window = Toplevel(self.master)
        transaction_log_window.title("Transaction Log")

        transaction_log_frame = Frame(transaction_log_window)
        transaction_log_frame.pack(padx=10, pady=10)

        transaction_log_label = Label(transaction_log_frame, text="Transaction Log:", font=('Arial', 12))
        transaction_log_label.grid(row=0, column=0, padx=10, pady=10)

        transaction_log_listbox = Listbox(transaction_log_frame, width=50, height=8)
        transaction_log_listbox.grid(row=1, column=0, padx=10, pady=10)

        for transaction in self.current_user_data['transaction_log']:
            transaction_log_listbox.insert(END, transaction)

        # Move the listbox a little higher
        transaction_log_listbox.grid(row=0, column=0, padx=10, pady=(5, 0))  # Adjusted padding

    def logout(self):
        self.current_user_data = None
        self.user_dashboard.place_forget()
        self.show_login_frame()

    def exit_program(self, event=None):
        self.master.quit()


def main():
    root = Tk()
    bank_system = BankSystem(root)
    root.mainloop()


if __name__ == '__main__':
    main()
