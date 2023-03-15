#Software Engineering Course Project
#Group 3
#Cooper Poole
#Christian Chow Quan 
#Jason Barican
#Jian Gong

import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import *
import Important_Links as IL
import Useful_Links as UL
#import Profile_Functions as PF

#global arrays to store account information during runtime

loginUsername = ''
accEmailPrefs = 1
accSMSPrefs = 1
accTAPrefs = 1
accLangPrefs = "English"
PrevWindow = 'MainMenu'

#presents menu for user to utilize application functions
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #self.controller.geometry("800x800")
        self.controller.title('InCollege beta v0.5.3')
        
        tk.Label(self, text = "Welcome to InCollege Beta!\n\nINCOLLEGE SUCCESS STORY\nJohn used LinkedIn.\nHe could not get a job.\nJohn then started using InCollege.\nHe got a job.\n\nPlease select an option below.").pack(padx=10, pady=10)
        
        # Create a dropdown menu with the options "General", "Browse InCollege", "Business Solutions", and "Directories"
        menu_var = tk.StringVar()
        menu_var.set("Useful Links")
        options = ["General", "Browse InCollege", "Business Solutions", "Directories"]
        option_menu = tk.OptionMenu(self, menu_var, *options)
        option_menu.pack(padx=10, pady=10)
        option_menu.config(width=25, height =2)

        
        # Create buttons to navigate to different frames based on the selected option
        loginButton = tk.Button(self, text="Login", command=lambda: controller.show_frame("LoginWindow"), width = 25, height = 2)
        loginButton.pack(padx=10, pady=10)
        
        signInButton = tk.Button(self, text="Sign-Up", command=lambda: controller.show_frame("SignUpWindow"), width = 25, height = 2)
        signInButton.pack(padx=10, pady=10)
        
        videoButton = tk.Button(self, text="Play Video", command=lambda: controller.show_frame("VideoWindow"), width = 25, height = 2)
        videoButton.pack(padx=10, pady=10)
        
        findSomeoneButton = tk.Button(self, text="Find Someone", command=lambda: controller.show_frame("FindSomeoneFrame"), width = 25, height = 2)
        findSomeoneButton.pack(padx=10, pady=10)
        
        option_menu['menu'].entryconfig(0, command=lambda: controller.show_frame("GeneralWindow"))
        # Bind the "Browse InCollege", "Business Solutions", and "Directories" options to the "under_construction" function
        option_menu['menu'].entryconfig(1, command=lambda: controller.show_frame("UnderConstruction"))
        option_menu['menu'].entryconfig(2, command=lambda: controller.show_frame("UnderConstruction"))
        option_menu['menu'].entryconfig(3, command=lambda: controller.show_frame("UnderConstruction"))
        
        exitButton = tk.Button(self, text="Exit", command=self.quit, width = 25, height = 2)
        exitButton.pack(padx=10, pady=10)

        # Create the second dropdown menu with the options "Copyright Notice", "About", "Accessibility", "User Agreement", "Privacy Policy", "Cookie Policy", "Copyright Policy", "Brand Policy", "Guest Controls", and "Languages"
        menu_var2 = tk.StringVar()
        menu_var2.set("InCollege Important Links")
        options2 = ["Copyright Notice",
                    "About",
                    "Accessibility",
                    "User Agreement",
                    "Privacy Policy",
                    "Cookie Policy",
                    "Copyright Policy",
                    "Brand Policy",
                    "Languages"]
        option_menu2 = tk.OptionMenu(self, menu_var2, *options2)
        option_menu2.pack(padx=10, pady=10)
        option_menu2['menu'].entryconfig(0, command=lambda: controller.show_frame("CopyrightNoticeFrame"))
        option_menu2['menu'].entryconfig(1, command=lambda: controller.show_frame("InCollegeAboutFrame"))
        option_menu2['menu'].entryconfig(2, command=lambda: controller.show_frame("AccessibilityNoticeFrame"))
        option_menu2['menu'].entryconfig(3, command=lambda: controller.show_frame("UserAgreementFrame"))
        option_menu2['menu'].entryconfig(4, command=lambda: controller.show_frame("PrivacyPolicyFrame"))
        option_menu2['menu'].entryconfig(5, command=lambda: controller.show_frame("CookiePolicyFrame"))
        option_menu2['menu'].entryconfig(6, command=lambda: controller.show_frame("CopyrightPolicyFrame"))
        option_menu2['menu'].entryconfig(7, command=lambda: controller.show_frame("BrandPolicyFrame"))
        option_menu2['menu'].entryconfig(9, command=lambda: controller.show_frame("LanguageFrame"))
        option_menu2.config(width=25, height =2)
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):
       global PrevWindow
       PrevWindow = "MainMenu"

class GuestControlsFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.conn = sqlite3.connect('database.db')  
    self.cursor = self.conn.cursor()

    # Create a label for the frame
    label = tk.Label(self, text="Guest Controls")
    label.pack(pady=10)

    # Create the InCollege Email checkbox
    self.email_var = tk.BooleanVar()
    self.email_checkbutton = tk.Checkbutton(self, text="InCollege Email", variable=self.email_var, onvalue = 1, offvalue = 0)
    self.email_checkbutton.select()
    self.email_checkbutton.pack(pady=5)

    # Create the SMS checkbox
    self.sms_var = tk.BooleanVar()
    self.sms_checkbutton = tk.Checkbutton(self, text="SMS", variable=self.sms_var, onvalue = 1, offvalue = 0)
    self.sms_checkbutton.select()
    self.sms_checkbutton.pack(pady=5)

    # Create the Targeted Advertising checkbox
    self.targeting_var = tk.BooleanVar()
    self.targeting_checkbutton = tk.Checkbutton(self, text="Targeted Advertising", variable=self.targeting_var, onvalue = 1, offvalue = 0)
    self.targeting_checkbutton.select()
    self.targeting_checkbutton.pack(pady=5)

    # Create a button to go back to the previous frame
    back_button = tk.Button(self, text="Back", command=self.save_prefs)
    back_button.pack(pady=10)

    self.bind("<<ShowFrame>>", self.on_show_frame)

  def on_show_frame(self, event):
    get_email_pref_query = "SELECT EMAIL_PREF FROM USER_DATA WHERE USERNAME = '"+ loginUsername +"'"
    get_sms_pref_query = "SELECT SMS_PREF FROM USER_DATA WHERE USERNAME = '"+ loginUsername +"'"
    get_ta_pref_query = "SELECT TA_PREF FROM USER_DATA WHERE USERNAME = '"+ loginUsername +"'"

    self.cursor.execute(get_email_pref_query)
    selected_email = self.cursor.fetchone()
    sel_email = selected_email[0]
 
    if sel_email == 1:
      self.email_checkbutton.select()
    else:
      self.email_var.set(0)

    self.cursor.execute(get_sms_pref_query)
    selected_sms = self.cursor.fetchone()
    sel_sms = selected_sms[0]

    if sel_sms == 1:
      self.sms_checkbutton.select()
    else:
      self.sms_var.set(0)

    self.cursor.execute(get_ta_pref_query)
    selected_ta = self.cursor.fetchone()
    sel_ta = selected_ta[0]
 
    if sel_ta == 1:
      self.targeting_checkbutton.select()
    else:
      self.targeting_var.set(0)

  def save_prefs(self):
    global loginUsername
    global PrevWindow
    update_email_pref_query = "UPDATE USER_DATA SET EMAIL_PREF = 1 WHERE USERNAME = '"+ loginUsername +"'"
    if self.email_var.get() == 0:
      update_email_pref_query = "UPDATE USER_DATA SET EMAIL_PREF = 0 WHERE USERNAME = '"+ loginUsername +"'"

    update_sms_pref_query = "UPDATE USER_DATA SET SMS_PREF = 1 WHERE USERNAME = '"+ loginUsername +"'" 
    if self.sms_var.get() == 0:
      update_sms_pref_query = "UPDATE USER_DATA SET SMS_PREF = 0 WHERE USERNAME = '"+ loginUsername +"'"

    update_ta_pref_query = "UPDATE USER_DATA SET TA_PREF = 1 WHERE USERNAME = '"+ loginUsername +"'"  
    if self.targeting_var.get() == 0:
      update_ta_pref_query = "UPDATE USER_DATA SET TA_PREF = 0 WHERE USERNAME = '"+ loginUsername +"'"

    self.cursor.execute(update_email_pref_query)
    self.cursor.execute(update_sms_pref_query)
    self.cursor.execute(update_ta_pref_query)
    self.conn.commit()

    self.controller.show_frame(PrevWindow)


class LanguageFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.conn = sqlite3.connect('database.db')  
    self.cursor = self.conn.cursor()

    # Create a label
    label = tk.Label(self, text="Please select your preferred language:")
    label.pack(pady=10)

    # Create a StringVar to hold the selected language
    self.language_var = tk.StringVar()

    self.bind("<<ShowFrame>>", self.on_show_frame)
    # Create two checkboxes for English and Spanish, and make them mutually exclusive
    self.english_checkbox = tk.Checkbutton(self, text="English", variable=self.language_var, onvalue="English", offvalue="")
    self.spanish_checkbox = tk.Checkbutton(self, text="Spanish", variable=self.language_var, onvalue="Spanish", offvalue="")
    self.english_checkbox.select()
    self.english_checkbox.pack(pady=5)
    self.spanish_checkbox.pack(pady=5)
    # Create a button to save the selected language and return to the previous frame
    save_button = tk.Button(self, text="Save and Return", command=self.save_language)
    save_button.pack(pady=10)

  def on_show_frame(self, event):
    selected_language = self.language_var.get() 
    get_lang_pref_query = "SELECT LANG_PREF FROM USER_DATA WHERE USERNAME = '"+ loginUsername +"'"

    print(get_lang_pref_query)
    self.cursor.execute(get_lang_pref_query)
    selected_language = self.cursor.fetchone()
    sel_lang = selected_language[0]
 
    if sel_lang == "English":
      self.english_checkbox.select()
    elif sel_lang == "Spanish":
      self.spanish_checkbox.select()


  def save_language(self):
    global loginUsername
    global PrevWindow
    # Get the selected language from the StringVar and save it
    update_lang_pref_query = "UPDATE USER_DATA SET LANG_PREF = 'English' WHERE USERNAME = '"+ loginUsername +"'"
    if self.language_var.get() == "English":
      update_lang_pref_query = "UPDATE USER_DATA SET LANG_PREF = 'English' WHERE USERNAME = '"+ loginUsername +"'"
    elif self.language_var.get() == "Spanish":
      update_lang_pref_query = "UPDATE USER_DATA SET LANG_PREF = 'Spanish' WHERE USERNAME = '"+ loginUsername +"'"
    self.cursor.execute(update_lang_pref_query)
    self.conn.commit()

    # Return to the previous frame
    self.controller.show_frame(PrevWindow)


class GeneralWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.prevWindow = tk.StringVar()
    
    tk.Label(self, text = "General", font = ("Arial", 14)).pack(pady = 10)
    
    signUpButton = tk.Button(self, text="Sign Up", command=lambda: controller.show_frame("SignUpWindow"))
    signUpButton.pack(pady = 10)
    
    helpCenterButton = tk.Button(self, text="Help Center", command=lambda: controller.show_frame("HelpCenterFrame"))
    helpCenterButton.pack(pady = 10)
    
    aboutButton = tk.Button(self, text="About", command=lambda: controller.show_frame("AboutFrame"))
    aboutButton.pack(pady = 10)
    
    pressButton = tk.Button(self, text="Press", command=lambda: controller.show_frame("PressFrame"))
    pressButton.pack(pady = 10)
    
    blogButton = tk.Button(self, text="Blog", command=lambda: controller.show_frame("UnderConstruction"))
    blogButton.pack(pady = 10)
    
    careersButton = tk.Button(self, text="Careers", command=lambda: controller.show_frame("UnderConstruction"))
    careersButton.pack(pady = 10)
    
    developersButton = tk.Button(self, text="Developers", command=lambda: controller.show_frame("UnderConstruction"))
    developersButton.pack(pady = 10)
    
    backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame(self.prevWindow))
    backButton.pack(pady = 10)
    self.bind("<<ShowFrame>>", self.on_show_frame)

  def on_show_frame(self, event):
    global PrevWindow
    self.prevWindow = PrevWindow
    PrevWindow = "GeneralWindow"


class LoginWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text = "Please enter username and password.").pack(padx=10, pady=10)
    self.loggedIn = False

    usernameLabel = tk.Label(self, text = "Username:")
    usernameLabel.pack(padx=10, pady=10)
    self.usernameEntry = tk.Entry(self, bd = 5)
    self.usernameEntry.pack(padx=10, pady=10)

    passwordLabel = tk.Label(self, text = "Password:")
    passwordLabel.pack(padx=10, pady=10)
    self.passwordEntry = tk.Entry(self, bd = 5)
    self.passwordEntry.pack(padx=10, pady=10)

    buttonframe = tk.Frame(self)
    buttonframe.pack()
    enterButton = tk.Button(buttonframe, text = "Enter", command = lambda: self.login())
    enterButton.pack(padx = 10, pady = 10)

    global PrevWindow
    backButton = tk.Button(buttonframe, text = "Back", command = lambda: controller.show_frame(PrevWindow))
    backButton.pack(padx=10, pady=10)



  def login(self):
    global loginUsername
    loginUsername = self.usernameEntry.get()
    loginPassword = self.passwordEntry.get()

    self.database = sqlite3.connect('database.db')  
    self.databaseCursor = self.database.cursor()

    self.databaseCursor.execute("SELECT * from USER_DATA")
    accounts = self.databaseCursor.fetchall()

    print(accounts)

    for i in range(0, len(accounts)):
      if loginUsername in accounts[i]:
        if loginPassword in accounts[i]:
          
          self.loggedIn = True
          messagebox.showinfo("Logged In", "You have successfully logged in.")
          self.controller.show_frame("ApplicationWindow")

    if self.loggedIn == False:
      messagebox.showerror("Error", "Incorrect username/password. Please try again.")
              
    
class SignUpWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    #opens database
    self.conn = sqlite3.connect('database.db')  
    self.cursor = self.conn.cursor()
    
    #username entry
    tk.Label(self, text="Create Username:").pack(padx=10, pady=10)
    self.newUsernameEntry = tk.Entry(self,bd = 5)
    self.newUsernameEntry.pack(padx=10, pady=10)

    #password entry
    tk.Label(self,text= "Create Password:").pack(padx=10, pady=10)
    self.newPasswordEntry = tk.Entry(self,bd = 5)
    self.newPasswordEntry.pack(padx=10, pady=10)

    #full name entry
    tk.Label(self,text= "Enter your first and last name:").pack(padx=10, pady=10)
    self.fullNameEntry = tk.Entry(self,bd = 5)
    self.fullNameEntry.pack(padx=10, pady=10)

    self.enterButton = tk.Button(self, text = "Enter", command = lambda: self.checkIfValid())
    self.enterButton.pack(padx = 10, pady = 10)
    global PrevWindow
    self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame(PrevWindow))
    self.backButton.pack(padx=10, pady=10)
        

  def checkIfValid(self):

    count = 0
    self.cursor.execute('''SELECT * from USER_DATA''')
    database = self.cursor.fetchall()
    
    usernameValid = False
    passwordValid = False
    fullNameValid = False

    count += len(database)
    
    if count >= 5:
      tk.Label(self, text="All permitted accounts have been created. Please come back later.").pack(padx=10, pady=10)
    else:
      self.newUsername = self.newUsernameEntry.get().replace(" ","")
      
      if len(database) != 0:
        self.cursor.execute("SELECT USERNAME from USER_DATA")
        usernames = self.cursor.fetchall()

        for i in range(0, len(usernames)):

          #ensuring username is unique
          if self.newUsername in usernames[i] or self.newUsername == "":
            messagebox.showerror("Error", "Invalid Entry/Account username already in use. Please try again.")
            self.newUsernameEntry.delete(0, 'end')
          else:
             usernameValid = True

      elif self.newUsername == "":
        messagebox.showerror("Error", "Invalid Entry/Account username already in use. Please try again.")
      
      elif len(database) == 0:
         usernameValid = True
  
    
    hasDigit = False
    hasNonAlphaNumeric = False
    
    self.newPassword = self.newPasswordEntry.get().replace(" ","")

    #validation check for length and presence of upercase, special, and numeric character.
    if len(self.newPassword) >= 8 and len(self.newPassword) <= 12 and self.newPassword.lower() != self.newPassword:
      for char in self.newPassword:
        if char.isdigit():
          hasDigit = True
        if not char.isalpha():
          hasNonAlphaNumeric = True
    if hasDigit is not True and hasNonAlphaNumeric is not True:
      messagebox.showerror("Error", "Invalid Password. Try a better password.")
      self.newPasswordEntry.delete(0, 'end')
    else:
      passwordValid = True

 
    self.name = self.fullNameEntry.get()
    nameCount = self.name.split()

    if len(nameCount) != 2:
      messagebox.showerror("Error", "Invalid format, Two names not found. Please try again.")
      self.fullNameEntry.delete(0, 'end')

    else:
      fullNameValid = True
      self.firstName = nameCount[0]
      self.lastName = nameCount[1]

    if usernameValid is True and passwordValid is True and fullNameValid is True:
      data_insert_query = ('''INSERT INTO USER_DATA(
                          USER_ID, USERNAME, PASSWORD, FIRSTNAME, LASTNAME, EMAIL_PREF, SMS_PREF, TA_PREF, LANG_PREF) VALUES
                          (?, ?, ?, ?, ?, ?, ?, ?, ?)
                          ''')
      
      count += 1
      #executed through tuples since insert query cant read from variable
      data_insert_tuple = (count, self.newUsername, self.newPassword, self.firstName, self.lastName, accEmailPrefs, accSMSPrefs, accTAPrefs, accLangPrefs)

      self.cursor.execute(data_insert_query, data_insert_tuple)
      self.conn.commit()
      
      messagebox.showinfo("Account Created", "You have successfully created a new account.")

      self.newUsernameEntry.delete(0, 'end')
      self.newPasswordEntry.delete(0, 'end')
      self.fullNameEntry.delete(0, 'end')
      self.controller.show_frame("MainMenu")

      usernameValid = False
      passwordValid = False
      fullNameValid = False


class VideoWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text = "Video is now playing").pack(padx=10, pady=10)
    backButton = tk.Button(self, text = "Back", 
                          command = lambda: controller.show_frame("MainMenu"))
    backButton.pack(padx=10, pady=10)


class ApplicationWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller    

    tk.Label(self, text = "You have successfully logged in!\nPlease select an option.").pack(padx=10, pady=10) 

    menu_var = tk.StringVar()
    menu_var.set("Useful Links")
    options = ["General", "Browse InCollege", "Business Solutions", "Directories"]
    option_menu = tk.OptionMenu(self, menu_var, *options)
    option_menu.pack(padx = 10, pady = 10)
    self.bind("<<ShowFrame>>", self.on_show_frame)

    option_menu['menu'].entryconfig(0, command=lambda: controller.show_frame("GeneralWindow"))
    # Bind the "Browse InCollege", "Business Solutions", and "Directories" options to the "under_construction" function
    option_menu['menu'].entryconfig(1, command=lambda: controller.show_frame("UnderConstruction"))
    option_menu['menu'].entryconfig(2, command=lambda: controller.show_frame("UnderConstruction"))
    option_menu['menu'].entryconfig(3, command=lambda: controller.show_frame("UnderConstruction"))

    CreateProfileButton = tk.Button(self, text = "Create Profile", command = lambda: controller.show_frame("ProfileFrame"))
    CreateProfileButton.pack(padx = 10, pady = 10)

    DisplayProfileButton = tk.Button(self, text = "Display Profile", command = lambda: controller.show_frame("DisplayProfileFrame"))
    DisplayProfileButton.pack(padx = 10, pady = 10)

    jobSearchButton = tk.Button(self, text = "Job/Internship Search", command = lambda: controller.show_frame("JobSearchFrame"))
    jobSearchButton.pack(padx = 10, pady = 10)

    findSomeoneButton = tk.Button(self, text = "Find Someone", command = lambda: controller.show_frame("FindSomeoneFrame"))
    findSomeoneButton.pack(padx = 10, pady = 10)

    learnSkillButton = tk.Button(self, text = "Learn a new skill", command = lambda: controller.show_frame("LearnSkillWindow"))
    learnSkillButton.pack(padx = 10, pady = 10)

    postJobButton = tk.Button(self, text = "Post a new job", command = lambda: controller.show_frame("AddJobFrame"))
    postJobButton.pack(padx = 10, pady = 10)

    FriendButton = tk.Button(self, text = "Add friends", command = lambda: controller.show_frame("FriendFrame"))
    FriendButton.pack(padx = 10, pady = 10)

    exitButton = tk.Button(self, text = "Exit", command = self.quit)
    exitButton.pack(padx = 10, pady = 10)

    backButton = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame("MainMenu"))
    backButton.pack(padx = 10, pady = 10)

# Create the second dropdown menu with the options "Copyright Notice", "About", "Accessibility", "User Agreement", "Privacy Policy", "Cookie Policy", "Copyright Policy", "Brand Policy", "Guest Controls", and "Languages"
    menu_var2 = tk.StringVar()
    menu_var2.set("InCollege Important Links")
    options2 = ["Copyright Notice",
                "About",
                "Accessibility",
                "User Agreement",
                "Privacy Policy",
                "Cookie Policy",
                "Copyright Policy",
                "Brand Policy",
                "Languages"]
    option_menu2 = tk.OptionMenu(self, menu_var2, *options2)
    option_menu2.pack(padx = 10, pady = 10)
    option_menu2['menu'].entryconfig(0, command=lambda: controller.show_frame("CopyrightNoticeFrame"))
    option_menu2['menu'].entryconfig(1, command=lambda: controller.show_frame("InCollegeAboutFrame"))
    option_menu2['menu'].entryconfig(2, command=lambda: controller.show_frame("AccessibilityNoticeFrame"))
    option_menu2['menu'].entryconfig(3, command=lambda: controller.show_frame("UserAgreementFrame"))
    option_menu2['menu'].entryconfig(4, command=lambda: controller.show_frame("PrivacyPolicyFrame"))
    option_menu2['menu'].entryconfig(5, command=lambda: controller.show_frame("CookiePolicyFrame"))
    option_menu2['menu'].entryconfig(6, command=lambda: controller.show_frame("CopyrightPolicyFrame"))
    option_menu2['menu'].entryconfig(7, command=lambda: controller.show_frame("BrandPolicyFrame"))
    option_menu2['menu'].entryconfig(9, command=lambda: controller.show_frame("LanguageFrame"))

  def on_show_frame(self, event):
    global PrevWindow
    PrevWindow = "ApplicationWindow"

class LearnSkillWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text = "Please select a skill to learn.").pack(padx=10, pady=10) 

    skill1Button = tk.Button(self, text = "Skill 1", command = lambda: controller.show_frame("UnderConstruction"))
    skill1Button.pack(padx = 10, pady = 10)

    skill2Button = tk.Button(self, text = "Skill 2",command = lambda: controller.show_frame("UnderConstruction"))
    skill2Button.pack(padx = 10, pady = 10)

    skill3Button = tk.Button(self, text = "Skill 3",command = lambda: controller.show_frame("UnderConstruction"))
    skill3Button.pack(padx = 10, pady = 10)

    skill4Button = tk.Button(self, text = "Skill 4",command = lambda: controller.show_frame("UnderConstruction"))
    skill4Button.pack(padx = 10, pady = 10)

    skill5Button = tk.Button(self, text = "Skill 5",command = lambda: controller.show_frame("UnderConstruction"))
    skill5Button.pack(padx = 10, pady = 10)

    backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("ApplicationWindow"))
    backButton.pack(padx = 10, pady = 10)

    exitButton = tk.Button(self, text = "Exit", command = self.quit)
    exitButton.pack(padx = 10, pady = 10)
    self.bind("<<ShowFrame>>", self.on_show_frame)

  def on_show_frame(self, event):
    global PrevWindow
    PrevWindow = "LearnSkillWindow"


    
class UnderConstruction(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller  

    tk.Label(self, text="Under Construction.").pack(padx=10, pady=10)
    global PrevWindow
    backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame(PrevWindow))
    backButton.pack(padx=10, pady=10)

          


class FindSomeoneFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller 
    self.conn = sqlite3.connect('database.db')
    self.create_widgets()
    self.bind("<<ShowFrame>>", self.on_show_frame)
    self.prevWindow = tk.StringVar()

  def create_widgets(self):
      self.name_label = tk.Label(self, text="Enter full name of person:")
      self.name_entry = tk.Entry(self)
      self.name_label.pack(padx=10, pady=10)
      self.name_entry.pack(padx=10, pady=10)

      self.search_button = tk.Button(self, text="Search", command=self.search)
      self.search_button.pack(padx=10, pady=10)

      backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame(self.prevWindow))
      backButton.pack(padx=10, pady=10)


  def on_show_frame(self, event):
    global PrevWindow
    self.prevWindow = PrevWindow
    PrevWindow = "FindSomeoneFrame"


  def search(self):
    searched_name = self.name_entry.get()
    nameCount = searched_name.split()
    displayButtons = False

    if len(nameCount) != 2:
      messagebox.showerror("Error", "Invalid format, Two names not found. Please try again.")
    else:
        firstName = nameCount[0]
        lastName = nameCount[1]
        cursor = self.conn.execute(f"SELECT * FROM USER_DATA WHERE FIRSTNAME = '{firstName}' AND LASTNAME = '{lastName}'")
        name = cursor.fetchall()
        print(name)
        if len(name) < 1:
            result_text = f"{searched_name} is not a part of the InCollege system yet."
            displayButtons = False
        else:
            result_text = f"{searched_name} is part of the InCollege system. Login or sign up to join them!"
            displayButtons = True

    result_label = tk.Label(self, text=result_text)
    result_label.pack(padx=5, pady=5)

    if displayButtons == True:
        loginButton = tk.Button(self, text = "login", command = lambda: self.controller.show_frame("LoginWindow"))
        loginButton.pack(padx=10, pady=10)
        signupButton = tk.Button(self, text = "Sign up", command = lambda: self.controller.show_frame("SignUpWindow"))
        signupButton.pack(padx=10, pady=10)


      
class JobSearchFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text="Welcome to Job/Internship Search!\nPlease select an option below.").pack(padx=10, pady=10)

    addJobButton = tk.Button(self, text = "Add Job", command = lambda: controller.show_frame("AddJobFrame"))
    addJobButton.pack(padx = 10, pady = 10)

    backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("ApplicationWindow"))
    backButton.pack(padx=10, pady=10)

class FriendFrame(tk.Frame):

  # Connect to the database

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    
    # Create Scrollbar widget and Canvas widget
    scrollbar = tk.Scrollbar(self)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    self.canvas = tk.Canvas(self, yscrollcommand=scrollbar.set)
    self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=self.canvas.yview)

    # Create a Frame widget to contain all the elements and buttons
    self.frame = tk.Frame(self.canvas)
    self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

    # Add the Pending Requests LabelFrame
    self.pending_frame = tk.LabelFrame(self.frame, text="Pending Requests")
    self.pending_frame.pack(pady=10)

    # Connect to the database
    self.conn = sqlite3.connect('database.db')
    # Retrieve the user's userid from the accounts table based on their username
    global loginUsername
    #self.main()
  
  def main(self):
    cursor = self.conn.execute(f"SELECT USER_ID FROM USER_DATA WHERE USERNAME = '{loginUsername}'")
    userid = cursor.fetchone()
    print(userid)

    # Display the elements and buttons in the Pending Requests LabelFrame
    
    cursor = self.conn.execute(f"SELECT PENDING_FIRST, PENDING_LAST FROM PENDING WHERE USER_ID = '{userid}'")
    self.pendingUsers = cursor.fetchall()
    self.add_pending_elements(self.pending_frame)

    # Add the Friends LabelFrame
    friends_frame = tk.LabelFrame(self.frame, text="Friends")
    friends_frame.pack(pady=10)

    # Display the elements and buttons in the Friends LabelFrame
    cursor = self.conn.execute(f"SELECT FRIEND_FIRST, FRIEND_LAST FROM FRIENDS WHERE USER_ID = '{userid}'")
    self.friendUsers = cursor.fetchall()
    self.add_friends_elements(friends_frame)

    self.pending_frame = self.pending_frame
    self.friends_frame = friends_frame

    # Allow the Canvas widget to automatically adjust its size
    self.frame.update_idletasks()
    self.canvas.config(scrollregion=self.canvas.bbox('all'))

  def add_pending_elements(self, frame):
    # Clear the Frame widget before adding elements
    for widget in frame.winfo_children():
        widget.destroy()

    if not self.pendingUsers:
        label = tk.Label(frame, text="No new pending requests", width=50)
        label.grid(row=0, column=0, padx=5, pady=5)
    else:
        # Add elements and buttons to the Frame widget
        for i, element in enumerate(self.pendingUsers):
            label = tk.Label(frame, text=element, width=50)
            label.grid(row=i, column=0, padx=5, pady=5)
            button1 = tk.Button(frame, text='reject', command=lambda element=element: self.delete_element(element))
            button1.grid(row=i, column=1, padx=5, pady=5)
            button2 = tk.Button(frame, text='accept', command=lambda element=element: self.move_element(element))
            button2.grid(row=i, column=2, padx=5, pady=5)

  def add_friends_elements(self, frame):
    # Clear the Frame widget before adding elements
    for widget in frame.winfo_children():
        widget.destroy()

    if not self.friendUsers:
        label = tk.Label(frame, text="Don't have any friends yet", width=50)
        label.grid(row=0, column=0, padx=5, pady=5)
    else:
        # Add elements and buttons to the Frame widget
        for i, element in enumerate(self.friendUsers):
            label = tk.Label(frame, text=element, width=50)
            label.grid(row=i, column=0, padx=5, pady=5)
            button1 = tk.Button(frame, text='disconnect', command=lambda element=element: self.disconnect_element(element))
            button1.grid(row=i, column=1, padx=5, pady=5)

    # Add back button
    backButton = tk.Button(frame, text="Back", command=lambda: self.controller.show_frame("ApplicationWindow"))
    backButton.grid(row=len(self.friendUsers)+1, column=0, padx=5, pady=5)

  #delete request from pending table
  def delete_element(self, element):
    self.conn.execute(f"DELETE FROM PENDING WHERE USER_ID = {self.userid} AND PENDING_FIRST = '{element[0]}' AND pendingLast = '{element[1]}'")
    self.conn.commit()
    self.pendingUsers.remove(element)
    self.update_frame()
  
  #move user to friends table
  def move_element(self, element):
    self.conn.execute(f"INSERT INTO FRIENDS (USER_ID, FRIEND_FIRST, FRIEND_LAST) VALUES ({self.userid}, '{element[0]}', '{element[1]}')")
    self.conn.execute(f"DELETE FROM PENDING WHERE USER_ID = {self.userid} AND pendingFirst = '{element[0]}' AND PENDING_LAST = '{element[1]}'")
    self.conn.commit()
    self.pendingUsers.remove(element)
    self.friendUsers.append((element[0], element[1]))
    cursor = self.conn.execute(f"SELECT USER_ID FROM USER_DATA WHERE FIRSTNAME = '{element[0]}' AND LASTNAME = '{element[1]}'")
    friend_userid = cursor.fetchone()[0]
    self.conn.execute(f"INSERT INTO FRIENDS (USER_ID, FRIEND_FIRST, FRIEND_LAST) VALUES (?, ?, ?)", (friend_userid, self.myfirst, self.mylast))
    self.conn.commit()
    self.update_frame()

  #remove user from friends table
  def disconnect_element(self, element):
    #delete my friend
    self.conn.execute(f"DELETE FROM FRIENDS WHERE USER_ID = {self.userid} AND FRIEND_FIRST = '{element[0]}' AND FRIEND_LAST = '{element[1]}'")
    self.conn.commit()
    #delete friend's friend(me)
    cursor = self.conn.execute(f"SELECT USER_ID FROM USER_DATA WHERE FIRSTNAME = '{element[0]}' AND LASTNAME = '{element[1]}'")
    friend_userid = cursor.fetchone()[0]
    #self.conn.execute(f"DELETE FROM friends (userid, friendFirst, friendLast) VALUES (?, ?, ?)", (friend_userid, self.myfirst, self.mylast))
    self.conn.execute(f"DELETE FROM FRIENDS WHERE USER_ID = {friend_userid} AND FRIEND_FIRST = '{self.myfirst}' AND FRIEND_LAST = '{self.mylast}'")       
    self.conn.commit()
    self.friendUsers.remove(element)
    self.update_frame()

  def update_frame(self):
    self.add_pending_elements(self.pending_frame)
    self.add_friends_elements(self.friends_frame)
    self.frame.update_idletasks()
    self.canvas.config(scrollregion=self.canvas.bbox('all'))

  def add_elements(self):
    # Clear the Frame widget before adding elements
    for widget in self.frame.winfo_children():
        widget.destroy()

    # Add pending requests label frame and elements
    pendingFrame = tk.LabelFrame(self.frame, text="Pending Requests")
    pendingFrame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5, expand=True)
    self.add_pending_elements(pendingFrame)

    # Add friends label frame and elements
    friendsFrame = tk.LabelFrame(self.frame, text="Friends")
    friendsFrame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5, expand=True)
    self.add_friends_elements(friendsFrame)

    # Allow the Canvas widget to automatically adjust its size
    self.frame.update_idletasks()
    self.canvas.config(scrollregion=self.canvas.bbox('all'))



class AddJobFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.create_widgets()

    self.conn = sqlite3.connect('database.db')  
    self.cursor = self.conn.cursor()

  def create_widgets(self):
      self.title_label = tk.Label(self, text="Enter title:")
      self.title_entry = tk.Entry(self)
      self.title_label.grid(row=0, column=0, padx=5, pady=5)
      self.title_entry.grid(row=0, column=1, padx=5, pady=5)

      self.description_label = tk.Label(self, text="Enter description:")
      self.description_entry = tk.Entry(self)
      self.description_label.grid(row=1, column=0, padx=5, pady=5)
      self.description_entry.grid(row=1, column=1, padx=5, pady=5)

      self.employer_label = tk.Label(self, text="Enter employer:")
      self.employer_entry = tk.Entry(self)
      self.employer_label.grid(row=2, column=0, padx=5, pady=5)
      self.employer_entry.grid(row=2, column=1, padx=5, pady=5)

      self.location_label = tk.Label(self, text="Enter location:")
      self.location_entry = tk.Entry(self)
      self.location_label.grid(row=3, column=0, padx=5, pady=5)
      self.location_entry.grid(row=3, column=1, padx=5, pady=5)

      self.salary_label = tk.Label(self, text="Enter salary:")
      self.salary_entry = tk.Entry(self)
      self.salary_label.grid(row=4, column=0, padx=5, pady=5)
      self.salary_entry.grid(row=4, column=1, padx=5, pady=5)

      self.post_button = tk.Button(self, text="Post job", command=self.post_job)
      self.post_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

      self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("ApplicationWindow"))
      self.back_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

  def post_job(self):
      global loginUsername
      count = 0
      jobs = self.cursor.fetchall()
      
      count += len(jobs)

      #checking if amount of accounts has exceeded maximum
      if count >= 10:
        result_text = "All permitted jobs have been created, please come back later"
      else:
        title = self.title_entry.get()
        description = self.description_entry.get()
        employer = self.employer_entry.get()
        location = self.location_entry.get()
        salary = self.salary_entry.get()

        data_insert_query = ('''INSERT INTO JOB_DATA(
                            TITLE, DESCRIPTION, EMPLOYER, LOCATION, SALARY) VALUES
                            (?, ?, ?, ?, ?)
                            ''')

        data_insert_tuple = (title, description, employer, location, salary)
        
        self.cursor.execute(data_insert_query, data_insert_tuple)
        self.conn.commit()

        
        result_text = "New job posted!"

      result_label = tk.Label(self, text=result_text)
      result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)



class ProfileFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create label for title
        title_label = Label(self, text="Title:")
        title_label.grid(row=0, column=0, padx=10, pady=10)

        # create entry for title
        title_entry = Entry(self)
        title_entry.grid(row=0, column=1, padx=10, pady=10)

        # create label for major
        major_label = Label(self, text="Major:")
        major_label.grid(row=1, column=0, padx=10, pady=10)

        # create entry for major
        major_entry = Entry(self)
        major_entry.grid(row=1, column=1, padx=10, pady=10)

        # create label for university
        university_label = Label(self, text="University:")
        university_label.grid(row=2, column=0, padx=10, pady=10)

        # create entry for university
        university_entry = Entry(self)
        university_entry.grid(row=2, column=1, padx=10, pady=10)

        # create label for about
        about_label = Label(self, text="About:")
        about_label.grid(row=3, column=0, padx=10, pady=10)

        # create text box for about
        about_text = Text(self, height=5, width=50)
        about_text.grid(row=3, column=1, padx=10, pady=10)


        # create label for experience
        experience_label = Label(self, text="Experience:")
        experience_label.grid(row=4, column=0, padx=10, pady=10)

        # create text box for experience
        experience_text = Text(self, height=5, width=50)
        experience_text.grid(row=4, column=1, padx=10, pady=10)


        # create label for education
        education_label = Label(self, text="Education:")
        education_label.grid(row=5, column=0, padx=10, pady=10)

        # create label for school name
        school_name_label = Label(self, text="School Name:")
        school_name_label.grid(row=6, column=0, padx=10, pady=10)

        # create entry for school name
        school_name_entry = Entry(self)
        school_name_entry.grid(row=6, column=1, padx=10, pady=10)

        # create label for degree
        degree_label = Label(self, text="Degree:")
        degree_label.grid(row=7, column=0, padx=10, pady=10)

        # create entry for degree
        degree_entry = Entry(self)
        degree_entry.grid(row=7, column=1, padx=10, pady=10)

        # create label for years attended
        years_attended_label = Label(self, text="Years Attended:")
        years_attended_label.grid(row=8, column=0, padx=10, pady=10)

        # create entry for years attended
        years_attended_entry = Entry(self)
        years_attended_entry.grid(row=8, column=1, padx=10, pady=10)

        saveButton = tk.Button(self, text="Save", command=lambda: controller.show_frame("ApplicationWindow"))
        saveButton.grid(row=9,column=1)

        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("ApplicationWindow"))
        backButton.grid(row=10,column=1)

    # function to handle submit button click
    def submit_profile(self):
        # get values from input fields
        title = self.title_entry.get()
        major = self.major_entry.get().lower().title()  # convert to title case
        university = self.university_entry.get().lower().title()
        about = self.about_text.get("1.0", END)
        experience = self.experience_text.get("1.0", END)
        school_name = self.school_name_entry.get()
        degree = self.degree_entry.get()
        years_attended = self.years_attended_entry.get()
        education = f"{degree} at {school_name}, {years_attended} years"

        #inserting into database
        database = sqlite3.connect('database.db')

        data_insert_query = ("INSERT INTO PROFILE_DATA (USERNAME, Title, Major, University, About, Experience, Education) \
        VALUES (?,?,?,?,?,?)")

        global loginUsername

        data_insert_tuple = (loginUsername, title, major, university, about, experience, education)

        database.execute(data_insert_query, data_insert_tuple)
        database.commit()

        database.close()
        
        # create submit button
        submit_button = Button(self.root, text="Save", command=self.submit_profile)
        submit_button.grid(row=6, column=1, padx=10, pady=10)

        self.root.mainloop()


class DisplayProfileFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # connect to the database
        database = sqlite3.connect('database.db')
        self.cursor = database.cursor()

        self.profile = {'title': '',
            'major': '',
            'university': '',
            'info': '',
            'about': '',
            'experience': '',
            'education': ''}

        self.bind("<<ShowFrame>>", self.on_show_frame)

        title_label = tk.Label(self, text=f"Title: {self.profile['title']}")
        title_label.grid(row=0, column=0, padx=10, pady=10)

        major_label = tk.Label(self, text=f"Major: {self.profile['major']}")
        major_label.grid(row=1, column=0, padx=10, pady=10)

        university_label = tk.Label(self, text=f"University: {self.profile['university']}")
        university_label.grid(row=2, column=0, padx=10, pady=10)

        info_label = tk.Label(self, text=f"Info: {self.profile['info']}")
        info_label.grid(row=3, column=0, padx=10, pady=10)

        experience_label = tk.Label(self, text="Experience:")
        experience_label.grid(row=4, column=0, padx=10, pady=10)
        for experience in self.profile['experience']:
            experience_line_label = tk.Label(self, text=f"- {experience}")
            experience_line_label.grid(row=5, column=0, padx=10, pady=10)

        education_label = tk.Label(self, text="Education:")
        education_label.grid(row=6, column=0, padx=10, pady=10)
        for education in self.profile['education']:
            education_line_label = tk.Label(self, text=f"- {education}")
            education_line_label.grid(row=7, column=0, padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("ApplicationWindow"))
        backButton.grid(row=8,column=1)
    

    def on_show_frame(self, event):
        # retrieve the profile information from the database

        global loginUsername
        profile_data_query=("SELECT * FROM PROFILE_DATA WHERE USERNAME='"+ loginUsername +"'")


        self.cursor.execute(profile_data_query)
        profile_data = self.cursor.fetchone()


        # convert the retrieved data to a dictionary
        self.profile = {
            'title': profile_data[0],
            'major': profile_data[1],
            'university': profile_data[2],
            'about': profile_data[3],
            'experience': profile_data[4].split('\n') if profile_data[4] else [],
            'education': profile_data[5].split('\n') if profile_data[5] else []
        }



class MainWindow(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    mainframe = tk.Frame()
    self.windowNum = 0
    mainframe.pack(padx = 5, pady = 5,)# fill = 'both', expand = 1)
    self.framelist = {}                 #dictionary for different pages

    for F in (MainMenu, LoginWindow, SignUpWindow,
              VideoWindow, ApplicationWindow, LearnSkillWindow,
              FindSomeoneFrame, JobSearchFrame, AddJobFrame, DisplayProfileFrame, ProfileFrame, IL.CopyrightNoticeFrame,
              IL.InCollegeAboutFrame, IL.AccessibilityNoticeFrame, IL.UserAgreementFrame,
              IL.PrivacyPolicyFrame, IL.CookiePolicyFrame, IL.CopyrightPolicyFrame,
              IL.BrandPolicyFrame, GuestControlsFrame, LanguageFrame,
              GeneralWindow, UL.HelpCenterFrame, UL.AboutFrame, 
              UL.PressFrame, UnderConstruction, FriendFrame):

      frame_name = F.__name__
      frame = F(parent = mainframe, controller = self)
      frame.grid(row = 0, column = 0, sticky = 'nsew')
      self.framelist[frame_name] = frame

    self.show_frame("MainMenu")

    #creation of sqlite database
    database = sqlite3.connect('database.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS USER_DATA(
                    USER_ID INT,
                    USERNAME TEXT, 
                    PASSWORD TEXT, 
                    FIRSTNAME TEXT, 
                    LASTNAME TEXT,
                    EMAIL_PREF INT,
                    SMS_PREF INT, 
                    TA_PREF INT,
                    LANG_PREF TEXT,
                    PRIMARY KEY (USERNAME)
    )'''

    database.execute(table_create_query)
    
    job_table_query = '''CREATE TABLE IF NOT EXISTS JOB_DATA(
                        TITLE TEXT,
                        DESCRIPTION TEXT,
                        EMPLOYER TEXT,
                        LOCATION TEXT,
                        SALARY TEXT
    )'''

    database.execute(job_table_query)
    
    
    profile_table_query = '''CREATE TABLE IF NOT EXISTS PROFILE_DATA(
                        USERNAME TEXT,
                        Title TEXT, 
                        Major TEXT, 
                        University TEXT, 
                        About TEXT,
                        Experience INT,
                        Education INT,
                        PRIMARY KEY (USERNAME),
                        FOREIGN KEY (USERNAME) REFERENCES USER_DATA(USERNAME)
    )'''
    
    database.execute(profile_table_query)



    friends_query = '''CREATE TABLE IF NOT EXISTS FRIENDS(
                    USER_ID INT,
                    FRIEND_FIRST TEXT,
                    FRIEND_LAST TEXT
    )'''

    database.execute(friends_query)



    pending_query = '''CREATE TABLE IF NOT EXISTS PENDING(
                    USER_ID INT,
                    PENDING_FIRST TEXT,
                    PENDING_LAST TEXT
    )'''

    database.execute(pending_query)


  def show_frame(self, frame_name):
    frame = self.framelist[frame_name]
    frame.event_generate("<<ShowFrame>>")
    frame.tkraise()

  
if __name__ == '__main__':
  window = MainWindow()
  window.mainloop()