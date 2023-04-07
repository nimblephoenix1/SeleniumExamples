#import for webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# Import library for creating GUIs
import tkinter as tk

# Define the GUI class
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Login System")

        # Create widgets
        self.title_label = tk.Label(master, text="Enter your Login Credentials for https://www.github.com/login")
        self.title_label.pack(pady=10)

        self.user_id_label = tk.Label(master, text="User ID:")
        self.user_id_label.pack(pady=5)

        self.user_id_entry = tk.Entry(master)
        self.user_id_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack(pady=5)

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    # Define the login function
    def login(self):
        user_id = self.user_id_entry.get()
        password = self.password_entry.get()

        # Add your user_id and password validation logic here
        # For example, you can use a list of allowed user IDs and passwords

	  # assigne variables for webdriver
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        DRIVER_PATH = 'C:\Program Files\Google\Chrome\Application\chromedriver'
        driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        driver.get("https://www.github.com/login")
        #print(driver.page_source)

        #Send the user name to the user name login field
        username = user_id
        uname = driver.find_element("id", "login_field") 
        uname.send_keys( username )

        #Send the password to the password field
        psswrd 	= password
        pw = driver.find_element("id", "password") 
        pw.send_keys( psswrd )

        #Find and click the 'sign in' button
        driver.find_element("name", "commit").click()

        # Wait for login process to complete.
        WebDriverWait(driver=driver, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))

        error_message = "Incorrect username or password."
        # Retrieve any errors found. 
        errors = driver.find_elements(By.CLASS_NAME, "flash-error")

        # When errors are found, the login will fail. 
        if any(error_message in e.text for e in errors):
            print("[!] Login failed")
        else:
            print("[+] Login successful")

        driver.close()

        # Clear the entry fields once the login button is clicked
        self.user_id_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()

# Create an instance of the GUI class
gui = GUI(root)

# Run the main loop
root.mainloop()